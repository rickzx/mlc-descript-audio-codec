import logging

import torch
import tvm
from tvm.runtime import Device, NDArray
from tvm.contrib import tvmjs
from tvm.runtime.ndarray import array as as_ndarray

from mlc_dac.dac import DAC

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


class DACLoader:
    def __init__(self, path="weights.pth"):
        self.path = path

    def bold(self, text):
        return f"\033[1m{text}\033[0m"
    
    def covert_weight(self, device: Device):
        tvmjs.dump_ndarray_cache(
            self.load(device),
            "weights",
            encode_format="raw",
        )

    def load(self, device: Device):
        model = DAC()
        _, _named_params, _ = model.export_tvm(  # type: ignore[misc]
            spec=model.get_default_spec(),
            allow_extern=True,
        )
        named_parameters = dict(_named_params)

        state_dict = torch.load(self.path, map_location=torch.device("cpu"))[
            "state_dict"
        ]

        for mlc_name, param in named_parameters.items():
            if mlc_name not in state_dict:
                raise KeyError(f"Missing key {mlc_name} in state_dict")

            logger.info(
                'Parameter: "%s", shape: %s, dtype: %s',
                self.bold(mlc_name),
                param.shape,
                param.dtype,
            )

            torch_param = state_dict[mlc_name]
            if list(torch_param.shape) != param.shape:
                raise ValueError(
                    f"Shape mismatch: {list(torch_param.shape)} (PyTorch) != {param.shape} (MLC)"
                )
            mlc_param = as_ndarray(torch_param.data.numpy(), device)
            yield mlc_name, mlc_param


if __name__ == "__main__":
    loader = DACLoader()
    loader.covert_weight(device=tvm.metal())
