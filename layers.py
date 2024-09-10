from typing import Optional

from tvm import te
from tvm.relax import op as _op
from tvm.relax.frontend import nn


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
    Module for weight norm conv1d layer.
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


class WNConvTranspose1d(nn.Module):
    """
    Module for weight norm convtranspose1d layer.
    """

    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        kernel_size: int,
        stride: int = 1,
        padding: int = 0,
        output_padding: int = 0,
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
        self.output_padding = output_padding
        self.dilation = dilation
        self.groups = groups
        self.dtype = dtype

        self.weight_g = nn.Parameter(
            (
                self.in_channels,
                1,
                1,
            ),
            dtype,
        )

        self.weight_v = nn.Parameter(
            (
                self.in_channels,
                int(self.out_channels // self.groups),
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
            self.weight_g._expr * (self.weight_v._expr / norm_v),
            name="wnconvtranspose1d",
        )
        return nn.op.conv1d_transpose(
            x, weight, self.bias, self.stride, self.padding, self.output_padding, self.dilation, self.groups
        )


class Tanh(nn.Module):
    def forward(self, x: nn.Tensor) -> nn.Tensor:
        return nn.op.tanh(x)
