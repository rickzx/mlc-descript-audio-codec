import json
import random
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import tvm
from tvm import dlight as dl
from tvm import relax
from tvm.relax.frontend.nn import Parameter
from tvm.contrib import tvmjs
from tvm.runtime import Device
from tvm.target import Target

from mlc_dac.dac import DAC


def load_params(
    model_weight_path: str, device: Device, named_params: List[Tuple[str, Parameter]]
) -> List[tvm.nd.NDArray]:
    params, _ = tvmjs.load_ndarray_cache(model_weight_path, device)
    param_names = [name for name, _ in named_params]

    plist = []
    for param_name in param_names:
        param_name = param_name.replace(".layers.", ".")
        param_name = param_name.replace(".branches.0.", ".")
        plist.append(params[param_name])
    return plist


def get_tvm_module(device: Device):
    model = DAC(input_chunk_size=512)
    mod, named_params, _ = model.export_tvm(
        spec=model.get_default_spec(),
        allow_extern=True,
        debug=True,
    )
    seq = tvm.transform.Sequential(
        [
            tvm.relax.transform.LegalizeOps(),
            tvm.relax.transform.AnnotateTIROpPattern(),
            tvm.relax.transform.FoldConstant(),
            tvm.relax.transform.FuseOps(),
            tvm.relax.transform.FuseTIR(),
            dl.ApplyDefaultSchedule(
                dl.gpu.Matmul(),
                dl.gpu.GEMV(),
                dl.gpu.Reduction(),
                dl.gpu.GeneralReduction(),
                dl.gpu.Fallback(),
            ),
        ]
    )
    target = Target.from_device(device)
    with target:
        mod = seq(mod)

    with open("mod.txt", "w", encoding="utf-8") as f:
        f.write(mod.script())

    ex = relax.build(mod, target)

    vm = relax.VirtualMachine(ex, device, profile=True)
    return vm, named_params


def start_profile(device: Device, model_weight_path: str = "weights"):
    vm, named_params = get_tvm_module(device)
    params = load_params(model_weight_path, device, named_params)
    np.random.seed(0)
    audio_data = np.random.randn(1, 1, 512).astype("float32")
    print(audio_data)
    audio_data = tvm.nd.array(audio_data, device=device)
    
    mod = vm.module
    effects = mod["_initialize_effect"]()

    report = vm.profile("encode", audio_data, *effects, params)
    time_eval = vm.time_evaluator("encode", device, 10, 5)(audio_data, *effects, params)
    print(time_eval)

    csv = report.csv()

    with open("profile_stream.csv", "w", encoding="utf-8") as f:
        f.write(csv)
        print("Profile saved to profile.csv")


if __name__ == "__main__":
    device = tvm.metal()
    start_profile(device)
