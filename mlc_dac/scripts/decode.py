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
from tvm.runtime import Device, Module, Object, ShapeTuple
from tvm.runtime.relax_vm import VirtualMachine
from tvm.target import Target

from mlc_dac.dac import DAC
import time


def load_params(
    model_weight_path: str, device: Device, named_params: List[Tuple[str, Parameter]]
) -> List[tvm.nd.NDArray]:
    params, _ = tvmjs.load_ndarray_cache(model_weight_path, device)
    param_names = [name for name, _ in named_params]

    plist = []
    for param_name in param_names:
        plist.append(params[param_name])
    return plist


def get_tvm_module(device: Device):
    model = DAC()
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
                # dl.gpu.Matmul(),
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
    ex = relax.build(mod, target)

    vm = relax.VirtualMachine(ex, device)
    return vm.module, named_params


def decode(device: Device, model_weight_path: str = "weights"):
    mod, named_params = get_tvm_module(device)
    params = load_params(model_weight_path, device, named_params)
    forward_fn = mod["decode"]
    np.random.seed(0)
    codes = np.random.randn(1, 1024, 891).astype("float32")
    print(codes)
    codes = tvm.nd.array(codes, device=device)
    effects = mod["_initialize_effect"]()

    begin = time.time()
    z = forward_fn(codes, *effects, params)[0]
    end = time.time()
    print("Time elapsed: ", end - begin)
    return z

if __name__ == "__main__":
    device = tvm.metal()
    z = decode(device)
    print(z.shape)
    print(z)
