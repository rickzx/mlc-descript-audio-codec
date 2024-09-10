from typing import Optional, Union

from tvm.relax.frontend import nn

from .layers import WNConv1d


def normalize(x: nn.Tensor, axis: Optional[int] = 1, eps: float = 1e-12):
    denom = nn.op.sum(nn.op.square(x), axis=axis, keepdims=True)
    denom = nn.op.sqrt(
        nn.op.maximum(nn.op.broadcast_to(denom, x.shape), nn.Tensor.from_const(eps))
    )
    return x / denom


class VectorQuantize(nn.Module):
    def __init__(self, input_dim: int, codebook_size: int, codebook_dim: int):
        self.codebook_size = codebook_size
        self.codebook_dim = codebook_dim

        self.in_proj = WNConv1d(input_dim, codebook_dim, kernel_size=1)
        self.out_proj = WNConv1d(codebook_dim, input_dim, kernel_size=1)
        self.codebook = nn.Embedding(codebook_size, codebook_dim)

    def forward(self, z: nn.Tensor):
        z_e = self.in_proj(z)
        z_q, indices = self.decode_latents(z_e)
        z_q = self.out_proj(z_q)
        return z_q, indices

    def decode_latents(self, latents: nn.Tensor):
        encodings = nn.op.permute_dims(latents, [0, 2, 1])  # (b, t, d)
        encodings = nn.op.reshape(encodings, [-1, encodings.shape[2]])  # (b*t, d)
        codebook = self.codebook.weight

        encodings = normalize(encodings)  # (b*t, d)
        codebook = normalize(codebook)  # (N, d)

        dist = (
            nn.op.sum(nn.op.square(encodings), axis=1, keepdims=True)  # (b*t, 1)
            - 2
            * nn.op.matmul(encodings, nn.op.permute_dims(codebook, [1, 0]))  # (b*t, N)
            + nn.op.permute_dims(
                nn.op.sum(nn.op.square(codebook), axis=1, keepdims=True), [1, 0]
            )  # (1, N)
        )  # (b*t, N)

        indices = nn.op.argsort(dist, axis=1)  # (b*t, N)
        indices = nn.op.take(indices, nn.Tensor.from_const([0]), axis=1)  # (b*t, 1)
        indices = nn.op.reshape(indices, [latents.shape[0], latents.shape[2]])  # (b, t)

        z_q = self.codebook(indices)  # (b, t, d)
        z_q = nn.op.permute_dims(z_q, [0, 2, 1])  # (b, d, t)
        return z_q, indices


class ResidualVectorQuantize(nn.Module):
    def __init__(
        self,
        input_dim: int = 512,
        n_codebooks: int = 9,
        codebook_size: int = 1024,
        codebook_dim: Union[int, list] = 8,
        quantizer_dropout: float = 0.0,
    ):
        if isinstance(codebook_dim, int):
            codebook_dim = [codebook_dim for _ in range(n_codebooks)]

        self.n_codebooks = n_codebooks
        self.codebook_dim = codebook_dim
        self.codebook_size = codebook_size

        self.quantizers = nn.ModuleList(
            [
                VectorQuantize(input_dim, codebook_size, codebook_dim[i])
                for i in range(n_codebooks)
            ]
        )
        self.quantizer_dropout = quantizer_dropout

    def forward(self, z: nn.Tensor):
        z_q = nn.zeros(z.shape, dtype=z.dtype)
        residual = z
        codebook_indices = []

        for quantizer in self.quantizers:
            z_q_i, indices = quantizer(residual)
            z_q = z_q + z_q_i
            residual = residual - z_q_i
            codebook_indices.append(indices)

        return z_q, codebook_indices
