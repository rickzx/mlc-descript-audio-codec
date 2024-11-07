from typing import List, Optional
import tvm
from tvm import relax as rx
from tvm.relax.frontend import nn
from tvm.relax.frontend.nn import Tensor, Effect
from tvm.script import tir as T


@T.prim_func
def cached_padding_1d_init(
    var_cache: T.handle,
):
    b = T.int32()
    c = T.int32()
    p = T.int32()

    cache = T.match_buffer(var_cache, (b, c, p), "float32")
    for bb, cc, pp in T.grid(b, c, p):
        with T.block("cache_init"):
            vb, vc, vp = T.axis.remap("SSS", [bb, cc, pp])
            cache[vb, vc, vp] = 0.0


@T.prim_func
def cached_padding_1d_update(
    var_cache: T.handle,
    var_data: T.handle,
    var_res: T.handle,
):
    B = T.int32()
    c = T.int32()
    p = T.int32()

    b = T.int32()
    n = T.int32()
    out = T.int32()

    cache = T.match_buffer(var_cache, (B, c, p), "float32")
    data = T.match_buffer(var_data, (b, c, n), "float32")
    res = T.match_buffer(var_res, (b, c, out), "float32")

    for bb, cc, oo in T.grid(b, c, out):
        with T.block("res_update"):
            vb, vc, vo = T.axis.remap("SSS", [bb, cc, oo])
            res[vb, vc, vo] = T.if_then_else(
                vo < p, cache[vb, vc, vo], data[vb, vc, vo - p]
            )

    for bb, cc, pp in T.grid(b, c, p):
        with T.block("cache_update"):
            vb, vc, vp = T.axis.remap("SSS", [bb, cc, pp])
            cache[vb, vc, vp] = res[vb, vc, out - p + vp]


@T.prim_func
def cached_padding_transpose_1d_update(
    var_cache: T.handle,
    var_data: T.handle,
    var_res: T.handle,
):
    B = T.int32()
    c = T.int32()
    p = T.int32()

    b = T.int32()
    n = T.int32()
    out = T.int32()

    cache = T.match_buffer(var_cache, (B, c, p), "float32")
    data = T.match_buffer(var_data, (b, c, n), "float32")
    res = T.match_buffer(var_res, (b, c, out), "float32")

    for bb, cc, oo in T.grid(b, c, out):
        with T.block("res_update"):
            vb, vc, vo = T.axis.remap("SSS", [bb, cc, oo])
            res[vb, vc, vo] = T.if_then_else(
                vo < p, cache[vb, vc, vo] + data[vb, vc, vo], data[vb, vc, vo]
            )

    for bb, cc, pp in T.grid(b, c, p):
        with T.block("cache_update"):
            vb, vc, vp = T.axis.remap("SSS", [bb, cc, pp])
            cache[vb, vc, vp] = res[vb, vc, out - p + vp]


@T.prim_func
def cached_padding_1d_crop(
    var_x: T.handle,
    var_res: T.handle,
):
    b = T.int32()
    c = T.int32()
    out = T.int32()
    n = T.int32()

    x = T.match_buffer(var_x, (b, c, out), "float32")
    res = T.match_buffer(var_res, (b, c, n), "float32")

    for bb, cc, nn in T.grid(b, c, n):
        with T.block("res_crop"):
            vb, vc, vn = T.axis.remap("SSS", [bb, cc, nn])
            res[vb, vc, vn] = x[vb, vc, vn]


class CachedPadding1dEffect(Effect):

    padding: int
    crop: bool
    max_batch_size: int
    cache: Optional[rx.Var]
    is_transposed: bool

    def __init__(
        self,
        padding: int,
        crop: bool = False,
        max_batch_size: int = 32,
        is_transposed: bool = False,
    ):
        self.padding = padding
        self.crop = crop
        self.max_batch_size = max_batch_size
        self.is_transposed = is_transposed

    def emit_init(self, name_hint, bb: rx.BlockBuilder):
        if self.is_transposed:
            fupdate = cached_padding_transpose_1d_update
        else:
            fupdate = cached_padding_1d_update

        args = [
            rx.PrimValue(self.padding),
            rx.PrimValue(self.crop),
            rx.PrimValue(self.max_batch_size),
            rx.PrimValue(self.is_transposed),
            bb.add_func(cached_padding_1d_init, "cached_padding_1d_init"),
            bb.add_func(fupdate, "cached_padding_1d_update"),
            bb.add_func(cached_padding_1d_crop, "cached_padding_1d_crop"),
        ]

        return [
            bb.emit(
                rx.call_pure_packed(
                    "vm.builtin.cached_padding_1d_create",
                    *args,
                    sinfo_args=rx.ObjectStructInfo(),
                ),
                name_hint,
            )
        ]

    def create(self, name_hint: str) -> List[rx.Var]:
        cache = rx.Var(name_hint, struct_info=rx.ObjectStructInfo())
        return [cache]

    def set_state(self, state_vars: List[rx.Var]) -> None:
        (self.cache,) = state_vars

    def finalize(self) -> List[rx.Var]:
        result = self.cache
        self.cache = None
        return [result]

    def to(self, dtype: Optional[str] = None) -> None:
        pass

    def forward(self, x: Tensor):
        b, c, n = x.shape

        if self.is_transposed:
            out = n
        else:
            out = n + self.padding

        if self.crop:
            out_shape = (b, c, out - self.padding)
        else:
            out_shape = (b, c, out)

        return Tensor(
            _expr=rx.BlockBuilder.current().emit(
                rx.call_pure_packed(
                    "vm.builtin.cached_padding_1d_update",
                    self.cache,
                    x._expr,
                    sinfo_args=rx.TensorStructInfo(out_shape, x.dtype),
                )
            )
        )

    def view(self, channels):
        return Tensor(
            _expr=rx.BlockBuilder.current().emit(
                rx.call_pure_packed(
                    "vm.builtin.cached_padding_1d_view",
                    self.cache,
                    sinfo_args=rx.TensorStructInfo(
                        (self.max_batch_size, channels, self.padding), "float32"
                    ),
                )
            )
        )


class CachedPadding1d(nn.Module):
    def __init__(self, padding: int, crop: bool = False, max_batch_size: int = 32):
        self.cache = CachedPadding1dEffect(padding, crop, max_batch_size)

    def forward(self, x: Tensor):
        return self.cache.forward(x)

    def view(self, channels):
        return self.cache.view(channels)


class CachedPadding1dTranspose(nn.Module):
    def __init__(self, padding: int, max_batch_size: int = 32):
        self.cache = CachedPadding1dEffect(
            padding, True, max_batch_size, is_transposed=True
        )

    def forward(self, x: Tensor):
        return self.cache.forward(x)

    def view(self, channels):
        return self.cache.view(channels)
