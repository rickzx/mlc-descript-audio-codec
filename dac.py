import math
from typing import List, Optional, Union

import numpy as np
import tvm
from tvm import dlight as dl
from tvm import relax, te
from tvm.relax import op as _op
from tvm.relax.frontend import nn
from tvm.target import Target


class Snake1d(nn.Module):
    def __init__(self, channels, dtype: Optional[str] = None):
        self.alpha = nn.Parameter((1, channels, 1), dtype)

    def forward(self, x: nn.Tensor):
        shape_x = x.shape
        x = nn.op.reshape(x, (shape_x[0], shape_x[1], -1))

        b, c, w = x.shape

        x = nn.op.tensor_expr_op(
            lambda x, alpha: te.compute(
                (b, c, w),
                lambda i, j, k: x[i, j, k]
                + 1
                / (alpha[0, j, 0] + 1e-9)
                * te.power(te.sin(alpha[0, j, 0] * x[i, j, k]), 2),
                name="snake_compute",
            ),
            "snake",
            args=[x, self.alpha],
        )

        x = nn.op.reshape(x, shape_x)
        return x


class WNConv1d(nn.Module):
    """
    Module for conv1d layer.
    """

    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        kernel_size: int,
        stride: int = 1,
        padding: int = 0,
        dilation: int = 1,
        groups: int = 1,
        bias: bool = True,
        dtype: Optional[str] = None,
    ) -> None:
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.dilation = dilation
        self.groups = groups
        self.dtype = dtype

        self.weight_g = nn.Parameter(
            (
                self.out_channels,
                1,
                1,
            ),
            dtype,
        )

        self.weight_v = nn.Parameter(
            (
                self.out_channels,
                self.in_channels // self.groups,
                self.kernel_size,
            ),
            dtype,
        )
        if bias:
            self.bias = nn.Parameter((self.out_channels,), dtype)
        else:
            self.bias = None

    def forward(self, x: nn.Tensor) -> nn.Tensor:
        dim = [i for i in range(1, x.ndim)]
        norm_v = _op.sqrt(
            _op.sum(_op.square(self.weight_v._expr), axis=dim, keepdims=True),
        )
        weight = nn.wrap_nested(
            self.weight_g._expr * (self.weight_v._expr / norm_v), name="wnconv1d"
        )
        return nn.op.conv1d(
            x, weight, self.bias, self.stride, self.padding, self.dilation, self.groups
        )


class ResidualUnit(nn.Module):
    def __init__(self, dim: int = 16, dilation: int = 1):
        pad = ((7 - 1) * dilation) // 2
        self.block = nn.ModuleList(
            [
                Snake1d(dim),
                WNConv1d(dim, dim, kernel_size=7, dilation=dilation, padding=pad),
                Snake1d(dim),
                WNConv1d(dim, dim, kernel_size=1),
            ]
        )

    def forward(self, x: nn.Tensor):
        residual = x
        for layer in self.block:
            x = layer(x)
        return x + residual


class EncoderBlock(nn.Module):
    def __init__(self, dim: int = 16, stride: int = 1):
        self.block = nn.ModuleList(
            [
                ResidualUnit(dim // 2, dilation=1),
                ResidualUnit(dim // 2, dilation=3),
                ResidualUnit(dim // 2, dilation=9),
                Snake1d(dim // 2),
                WNConv1d(
                    dim // 2,
                    dim,
                    kernel_size=2 * stride,
                    stride=stride,
                    padding=math.ceil(stride / 2),
                ),
            ]
        )

    def forward(self, x):
        for layer in self.block:
            x = layer(x)
        return x


class Encoder(nn.Module):
    def __init__(
        self,
        d_model: int = 64,
        strides: list = [2, 4, 8, 8],
        d_latent: int = 64,
    ):

        self.block = [WNConv1d(1, d_model, kernel_size=7, padding=3)]

        for stride in strides:
            d_model *= 2
            self.block += [EncoderBlock(d_model, stride=stride)]

        # Create last convolution
        self.block += [
            Snake1d(d_model),
            WNConv1d(d_model, d_latent, kernel_size=3, padding=1),
        ]

        # Wrap black into nn.Sequential
        self.block = nn.ModuleList(self.block)

    def forward(self, x):
        for layer in self.block:
            x = layer(x)
        return x


class DAC(nn.Module):
    def __init__(
        self,
        encoder_dim: int = 64,
        encoder_rates: List[int] = [2, 4, 8, 8],
        latent_dim: int = None,
        decoder_dim: int = 1536,
        decoder_rates: List[int] = [8, 8, 4, 2],
        n_codebooks: int = 9,
        codebook_size: int = 1024,
        codebook_dim: Union[int, list] = 8,
        quantizer_dropout: bool = False,
        sample_rate: int = 44100,
    ):
        pass

    def forward(self, x):
        pass
