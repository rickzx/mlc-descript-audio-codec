import math
from typing import List, Union

from tvm.relax.frontend import nn

from mlc_dac.layers import (
    AlignBranches,
    CachedSequential,
    CachedWNConv1d,
    CachedWNConvTranspose1d,
    Identity,
    Snake1d,
    Tanh,
)
from mlc_dac.quantize import ResidualVectorQuantize


class ResidualUnit(nn.Module):
    def __init__(self, dim: int = 16, dilation: int = 1, cumulative_delay: int = 0):
        pad = ((7 - 1) * dilation) // 2

        block = []
        block.append(Snake1d(dim))
        block.append(
            CachedWNConv1d(
                dim,
                dim,
                kernel_size=7,
                dilation=dilation,
                padding=pad,
                cumulative_delay=cumulative_delay,
            )
        )
        block.append(Snake1d(dim))
        block.append(
            CachedWNConv1d(
                dim, dim, kernel_size=1, cumulative_delay=block[-2].cumulative_delay
            )
        )
        block = CachedSequential(*block)
        self.block = AlignBranches(
            block,
            Identity(),
            delays=[block.cumulative_delay, cumulative_delay],
        )
        self.cumulative_delay = self.block.cumulative_delay

    def forward(self, x: nn.Tensor):
        return sum(self.block(x))


class EncoderBlock(nn.Module):
    def __init__(self, dim: int = 16, stride: int = 1, cumulative_delay: int = 0):
        block = []
        block.append(
            ResidualUnit(dim // 2, dilation=1, cumulative_delay=cumulative_delay)
        )
        block.append(
            ResidualUnit(
                dim // 2, dilation=3, cumulative_delay=block[-1].cumulative_delay
            )
        )
        block.append(
            ResidualUnit(
                dim // 2, dilation=9, cumulative_delay=block[-1].cumulative_delay
            )
        )
        block.append(Snake1d(dim // 2))
        block.append(
            CachedWNConv1d(
                dim // 2,
                dim,
                kernel_size=2 * stride,
                stride=stride,
                padding=math.ceil(stride / 2),
                cumulative_delay=block[-2].cumulative_delay,
            )
        )
        self.block = CachedSequential(*block)
        self.cumulative_delay = self.block.cumulative_delay

    def forward(self, x):
        return self.block(x)


class Encoder(nn.Module):
    def __init__(
        self,
        d_model: int = 64,
        strides: list = [2, 4, 8, 8],
        d_latent: int = 64,
    ):

        self.block = [CachedWNConv1d(1, d_model, kernel_size=7, padding=3)]

        for stride in strides:
            d_model *= 2
            self.block += [
                EncoderBlock(
                    d_model,
                    stride=stride,
                    cumulative_delay=self.block[-1].cumulative_delay,
                )
            ]

        # Create last convolution
        self.block += [
            Snake1d(d_model),
            CachedWNConv1d(
                d_model,
                d_latent,
                kernel_size=3,
                padding=1,
                cumulative_delay=self.block[-1].cumulative_delay,
            ),
        ]

        # Wrap black into nn.Sequential
        self.block = CachedSequential(*self.block)
        self.cumulative_delay = self.block.cumulative_delay

    def forward(self, x):
        return self.block(x)


class DecoderBlock(nn.Module):
    def __init__(
        self,
        input_dim: int = 16,
        output_dim: int = 8,
        stride: int = 1,
        cumulative_delay: int = 0,
    ):
        block = []
        block.append(Snake1d(input_dim))
        block.append(
            CachedWNConvTranspose1d(
                input_dim,
                output_dim,
                kernel_size=2 * stride,
                stride=stride,
                padding=math.ceil(stride / 2),
                cumulative_delay=cumulative_delay,
            )
        )
        block.append(
            ResidualUnit(
                output_dim, dilation=1, cumulative_delay=block[-1].cumulative_delay
            )
        )
        block.append(
            ResidualUnit(
                output_dim, dilation=3, cumulative_delay=block[-1].cumulative_delay
            )
        )
        block.append(
            ResidualUnit(
                output_dim, dilation=9, cumulative_delay=block[-1].cumulative_delay
            )
        )
        self.block = CachedSequential(*block)
        self.cumulative_delay = self.block.cumulative_delay

    def forward(self, x):
        return self.block(x)


class Decoder(nn.Module):
    def __init__(
        self,
        input_channel,
        channels,
        rates,
        d_out: int = 1,
    ):
        layers = [CachedWNConv1d(input_channel, channels, kernel_size=7, padding=3)]

        # Add upsampling + MRF blocks
        for i, stride in enumerate(rates):
            input_dim = channels // 2**i
            output_dim = channels // 2 ** (i + 1)
            layers += [
                DecoderBlock(
                    input_dim,
                    output_dim,
                    stride,
                    cumulative_delay=layers[-1].cumulative_delay,
                )
            ]

        # Add final conv layer
        layers += [
            Snake1d(output_dim),
            CachedWNConv1d(
                output_dim,
                d_out,
                kernel_size=7,
                padding=3,
                cumulative_delay=layers[-1].cumulative_delay,
            ),
            Tanh(),
        ]

        self.model = CachedSequential(*layers)
        self.cumulative_delay = self.model.cumulative_delay

    def forward(self, x):
        return self.model(x)


class DAC(nn.Module):
    def __init__(
        self,
        input_chunk_size,
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
        self.input_chunk_size = input_chunk_size
        self.hop_length = math.prod(encoder_rates)
        self.output_length = input_chunk_size // self.hop_length

        self.encoder_dim = encoder_dim
        self.encoder_rates = encoder_rates
        self.decoder_dim = decoder_dim
        self.decoder_rates = decoder_rates
        self.sample_rate = sample_rate
        self.effect_mode = "plain"

        if latent_dim is None:
            latent_dim = encoder_dim * (2 ** len(encoder_rates))

        self.latent_dim = latent_dim

        self.encoder = Encoder(encoder_dim, encoder_rates, latent_dim)
        self.encoder_cumulative_delay = self.encoder.cumulative_delay

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

        self.decoder = Decoder(
            latent_dim,
            decoder_dim,
            decoder_rates,
        )
        self.decoder_cumulative_delay = self.decoder.cumulative_delay

    def encode(self, audio_data):
        z = self.encoder(audio_data)
        z, codes = self.quantizer(z)
        return z, codes

    def decode(self, z):
        return self.decoder(z)

    def forward(self, audio_data):
        z, codes = self.encode(audio_data)
        x = self.decode(z)
        return x, z, codes

    def get_default_spec(self):
        mod_spec = {
            "encode": {
                "audio_data": nn.spec.Tensor(
                    ["batch_size", 1, self.input_chunk_size], "float32"
                ),
                "$": {
                    "param_mode": "packed",
                    "effect_mode": self.effect_mode,
                },
            },
            "decode": {
                "z": nn.spec.Tensor(
                    ["batch_size", self.latent_dim, self.output_length], "float32"
                ),
                "$": {
                    "param_mode": "packed",
                    "effect_mode": self.effect_mode,
                },
            },
        }

        return nn.spec.ModuleSpec.from_raw(mod_spec, self)
