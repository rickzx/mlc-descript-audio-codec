import math
from typing import List, Union

from tvm.relax.frontend import nn

from layers import Snake1d, WNConv1d


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
