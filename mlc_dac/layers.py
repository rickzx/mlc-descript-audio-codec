from typing import List, Optional

from mlc_dac.streaming import CachedPadding1d, CachedPadding1dTranspose
from tvm import te
from tvm.relax import op as _op
from tvm.relax.frontend import nn


class CachedConv1d(nn.Conv1D):
    def __init__(self, *args, **kwargs):
        padding = kwargs.get("padding", 0)
        cumulative_delay = kwargs.pop("cumulative_delay", 0)

        kwargs["padding"] = 0

        super().__init__(*args, **kwargs)

        if isinstance(padding, int):
            r_pad = padding
            padding = 2 * padding
        elif isinstance(padding, list) or isinstance(padding, tuple):
            r_pad = padding[1]
            padding = padding[0] + padding[1]

        s = self.stride
        cd = cumulative_delay

        stride_delay = (s - ((r_pad + cd) % s)) % s

        self.cumulative_delay = (r_pad + stride_delay + cd) // s

        self.cache = CachedPadding1d(padding)
        self.downsampling_delay = CachedPadding1d(stride_delay, crop=True)

    def forward(self, x: nn.Tensor) -> nn.Tensor:
        x = self.downsampling_delay(x)
        x = self.cache(x)
        return super().forward(x)


class CachedConvTranspose1d(nn.ConvTranspose1D):
    def __init__(self, *args, **kwargs):
        padding = kwargs.get("padding", 0)
        cumulative_delay = kwargs.pop("cumulative_delay", 0)

        kwargs["padding"] = 0

        super().__init__(*args, **kwargs)

        if isinstance(padding, int):
            l_pad = padding
            padding = 2 * padding
        elif isinstance(padding, list) or isinstance(padding, tuple):
            l_pad = padding[0]
            padding = padding[0] + padding[1]

        stride = self.stride
        self.cumulative_delay = l_pad + cumulative_delay * stride

        self.cache = CachedPadding1dTranspose(padding)

    def forward(self, x: nn.Tensor) -> nn.Tensor:
        x = nn.op.conv1d_transpose(
            x,
            self.weight,
            None,
            self.stride,
            0,
            self.output_padding,
            self.dilation,
            self.groups,
        )
        x = self.cache(x)
        bias = self.bias
        if bias is not None:
            x = x + nn.op.unsqueeze(bias, -1)
        return x


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


class CachedWNConv1d(WNConv1d):
    def __init__(self, *args, **kwargs):
        padding = kwargs.get("padding", 0)
        cumulative_delay = kwargs.pop("cumulative_delay", 0)

        kwargs["padding"] = 0

        super().__init__(*args, **kwargs)

        if isinstance(padding, int):
            r_pad = padding
            padding = 2 * padding
        elif isinstance(padding, list) or isinstance(padding, tuple):
            r_pad = padding[1]
            padding = padding[0] + padding[1]

        s = self.stride
        cd = cumulative_delay

        stride_delay = (s - ((r_pad + cd) % s)) % s

        self.cumulative_delay = (r_pad + stride_delay + cd) // s

        self.cache = CachedPadding1d(padding)
        self.downsampling_delay = CachedPadding1d(stride_delay, crop=True)

    def forward(self, x: nn.Tensor) -> nn.Tensor:
        x = self.downsampling_delay(x)
        x = self.cache(x)
        return super().forward(x)


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
            x,
            weight,
            self.bias,
            self.stride,
            self.padding,
            self.output_padding,
            self.dilation,
            self.groups,
        )


class CachedWNConvTranspose1d(WNConvTranspose1d):
    def __init__(self, *args, **kwargs):
        padding = kwargs.get("padding", 0)
        cumulative_delay = kwargs.pop("cumulative_delay", 0)

        kwargs["padding"] = 0

        super().__init__(*args, **kwargs)

        if isinstance(padding, int):
            l_pad = padding
            padding = 2 * padding
        elif isinstance(padding, list) or isinstance(padding, tuple):
            l_pad = padding[0]
            padding = padding[0] + padding[1]

        stride = self.stride
        self.cumulative_delay = l_pad + cumulative_delay * stride

        self.cache = CachedPadding1dTranspose(padding)

    def forward(self, x: nn.Tensor) -> nn.Tensor:
        dim = [i for i in range(1, x.ndim)]
        norm_v = _op.sqrt(
            _op.sum(_op.square(self.weight_v._expr), axis=dim, keepdims=True),
        )
        weight = nn.wrap_nested(
            self.weight_g._expr * (self.weight_v._expr / norm_v),
            name="wnconvtranspose1d",
        )
        x = nn.op.conv1d_transpose(
            x,
            weight,
            None,
            self.stride,
            0,
            self.output_padding,
            self.dilation,
            self.groups,
        )
        x = self.cache(x)
        bias = self.bias
        if bias is not None:
            x = x + nn.op.unsqueeze(bias, -1)
        return x


class Tanh(nn.Module):
    def forward(self, x: nn.Tensor) -> nn.Tensor:
        return nn.op.tanh(x)


class CachedSequential(nn.Module):
    def __init__(self, *layers, cumulative_delay: int = 0, stride: int = 1):
        self.layers = nn.ModuleList(layers)

        self.cumulative_delay = int(cumulative_delay) * stride
        last_delay = 0
        for i in range(1, len(self.layers) + 1):
            try:
                last_delay = self.layers[-i].cumulative_delay
                break
            except AttributeError:
                pass

        self.cumulative_delay += last_delay

    def forward(self, x: nn.Tensor) -> nn.Tensor:
        for layer in self.layers:
            x = layer(x)
        return x


class AlignBranches(nn.Module):
    def __init__(self, *branches, delays=None, cumulative_delay=0, stride=1):
        self.branches = nn.ModuleList(branches)

        if delays is None:
            delays = list(map(lambda x: x.cumulative_delay, self.branches))

        max_delay = max(delays)

        self.paddings = nn.ModuleList(
            [
                CachedPadding1d(p, crop=True)
                for p in map(lambda f: max_delay - f, delays)
            ]
        )

        self.cumulative_delay = int(cumulative_delay * stride) + max_delay

    def forward(self, x: nn.Tensor) -> List[nn.Tensor]:
        outs = []
        for branch, padding in zip(self.branches, self.paddings):
            delayed_x = padding(x)
            outs.append(branch(delayed_x))

        return outs


class Identity(nn.Module):
    def forward(self, x: nn.Tensor) -> nn.Tensor:
        return x
