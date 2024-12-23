import time
import warnings
from typing import List, Tuple, Dict

import dac
import numpy as np
import torch
import tvm
from tvm import relax
from torch.nn import Module
from tvm.contrib import tvmjs
from tvm.relax.frontend.nn import Parameter
from tvm.runtime import Device

import mlc_dac
import mlc_dac.dac

warnings.filterwarnings("ignore")


def benchmark_torch(
    model: Module,
    input_shape: Tuple[int, ...],
    num_repeats: int = 10,
    warmup_rounds: int = 2,
    device: str = "cpu",
    streaming: bool = False,
) -> float:
    if device not in ["cpu", "mps"]:
        raise ValueError("Device must be either 'cpu' or 'mps'")

    if device == "mps" and not torch.backends.mps.is_available():
        raise RuntimeError("MPS device requested but not available")

    model = model.to(device)
    model.eval()

    dummy_input = torch.randn(input_shape, device=device)

    print("Performing warmup...")
    with torch.no_grad():
        for _ in range(warmup_rounds):
            if streaming:
                for i in range(0, dummy_input.shape[-1], 512):
                    model.encode(dummy_input[..., i : i + 512])[1]
            else:
               model.encode(dummy_input)
            if device == "mps":
                torch.mps.synchronize()

    print(f"Running {num_repeats} iterations...")
    total_time = 0
    with torch.no_grad():
        for _ in range(num_repeats):
            start = time.perf_counter()
            if streaming:
                for i in range(0, dummy_input.shape[-1], 512):
                    model.encode(dummy_input[..., i : i + 512])[1]
            else:
               model.encode(dummy_input)
            if device == "mps":
                torch.mps.synchronize()
            total_time += time.perf_counter() - start

    mean_time = (total_time / num_repeats) * 1000
    return mean_time


def benchmark_tvm(
    forward_fn,
    effects,
    params,
    audio_data: np.ndarray,
    device: tvm.runtime.Device,
    num_repeats: int = 5,
    warmup_rounds: int = 2,
    packed_params: bool = False,
) -> float:
    # Split audio data into chunks of 512 samples
    chunks = np.array_split(audio_data, audio_data.shape[-1] // 512, axis=-1)
    chunks = [tvm.nd.array(chunk, device=device) for chunk in chunks]

    # Warmup phase
    print("Performing warmup...")
    for _ in range(warmup_rounds):
        effects_warm = effects
        for audio_data_chunk in chunks:
            if packed_params:
                _, effects_warm = forward_fn(audio_data_chunk, *effects_warm, *params)
            else:
                _, effects_warm = forward_fn(audio_data_chunk, *effects_warm, params)

    # Timing
    print(f"Running {num_repeats} iterations...")
    total_time = 0

    for _ in range(num_repeats):
        effects_run = effects
        start = time.perf_counter()
        for audio_data_chunk in chunks:
            if packed_params:
                _, effects_run = forward_fn(audio_data_chunk, *effects_run, *params)
            else:
                _, effects_run = forward_fn(audio_data_chunk, *effects_run, params)
        total_time += time.perf_counter() - start

    mean_time = (total_time / num_repeats) * 1000
    return mean_time


def profile_torch(model_path, device, streaming):
    print(f"Configuration - Backend: Torch, Device: {device}, Streaming: {streaming}")
    dac.DAC.enable_streaming(streaming)
    model = dac.DAC.load(model_path)
    input_shape = (1, 1, 512000)
    time = benchmark_torch(model, input_shape, device=device, streaming=streaming)
    print(f"Time taken: {time:.2f} ms")


def load_params_tvm(
    model_weight_path: str, device: Device, named_params: List[Tuple[str, Parameter]]
):
    params, _ = tvmjs.load_ndarray_cache(model_weight_path, device)
    param_names = [name for name, _ in named_params]

    plist = []
    for param_name in param_names:
        param_name = param_name.replace(".layers.", ".")
        param_name = param_name.replace(".branches.0.", ".")
        plist.append(params[param_name])
    return plist


def profile_tvm_untuned():
    print(f"Configuration - Backend: TVM (Untuned), Device: CPU, Streaming: True")
    ex = tvm.runtime.load_module("../dist/deploy-untuned-metal.so")
    model = mlc_dac.dac.DAC(input_chunk_size=512)
    _, named_params = model.export_tvm(
        spec=model.get_default_spec(),
        debug=True,
    )

    device = tvm.metal()
    params = load_params_tvm("../weights", device, named_params)

    vm = relax.VirtualMachine(ex, device)
    effects = vm["_initialize_effect"]()
    forward_fn = vm["encode"]

    audio_data = np.random.randn(1, 1, 512000).astype("float32")
    time = benchmark_tvm(forward_fn, effects, params, audio_data, device)
    print(f"Time taken: {time:.2f} ms")


def load_transformed_params(
    artifact_path: str, device
) -> Dict[str, List[tvm.nd.NDArray]]:
    from tvm.contrib import tvmjs

    pdict = {}
    params, meta = tvmjs.load_ndarray_cache(f"{artifact_path}/params", device)
    for model in ["encode", "decode"]:
        plist = []
        size = meta[f"{model}ParamSize"]
        for i in range(size):
            plist.append(params[f"{model}_{i}"])
        pdict[model] = plist
    return pdict


def profile_tvm_tuned():
    print(f"Configuration - Backend: TVM (Tuned), Device: CPU, Streaming: True")
    ex = tvm.runtime.load_module("../dist/deploy-metal.so")

    device = tvm.metal()
    const_params_dict = load_transformed_params("../dist", device)
    vm = relax.vm.VirtualMachine(ex, device)
    forward_fn = vm["encode"]
    effects = vm["_initialize_effect"]()

    audio_data = np.random.randn(1, 1, 512000).astype("float32")
    time = benchmark_tvm(
        forward_fn, effects, const_params_dict["encode"], audio_data, device, packed_params=True
    )
    print(f"Time taken: {time:.2f} ms")


if __name__ == "__main__":
    model_path = dac.utils.download(model_type="44khz")
    profile_torch(model_path, "cpu", streaming=False)
    profile_torch(model_path, "mps", streaming=False)
    profile_torch(model_path, "cpu", streaming=True)
    profile_torch(model_path, "mps", streaming=True)
    profile_tvm_untuned()
    profile_tvm_tuned()
