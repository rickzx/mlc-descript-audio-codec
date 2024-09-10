import math
from typing import List, Union

from tvm.relax.frontend import nn

from layers import Snake1d, WNConv1d
from quantize import ResidualVectorQuantize


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
        self.encoder_dim = encoder_dim
        self.encoder_rates = encoder_rates
        self.decoder_dim = decoder_dim
        self.decoder_rates = decoder_rates
        self.sample_rate = sample_rate

        if latent_dim is None:
            latent_dim = encoder_dim * (2 ** len(encoder_rates))

        self.latent_dim = latent_dim

        self.encoder = Encoder(encoder_dim, encoder_rates, latent_dim)

        self.n_codebooks = n_codebooks
        self.codebook_size = codebook_size
        self.codebook_dim = codebook_dim
        self.quantizer = ResidualVectorQuantize(
            input_dim=latent_dim,
            n_codebooks=n_codebooks,
            codebook_size=codebook_size,
            codebook_dim=codebook_dim,
            quantizer_dropout=quantizer_dropout,
        )

    def forward(self, audio_data):
        z = self.encoder(audio_data)
        z, codes = self.quantizer(z)
        return z, codes

    def get_default_spec(self):
        mod_spec = {
            "forward": {
                "audio_data": nn.spec.Tensor(["batch_size", 1, "seq_len"], "float32"),
                "$": {
                    "param_mode": "packed",
                    "effect_mode": "plain",
                },
            }
        }

        return nn.spec.ModuleSpec.from_raw(mod_spec, self)
