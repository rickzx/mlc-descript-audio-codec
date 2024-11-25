metadata = tvm.ir.load_json("""{
  \"root\": 1, 
  \"nodes\": [
    {
      \"type_key\": \"\"
    }, 
    {
      \"type_key\": \"Map\", 
      \"keys\": [
        \"relax.expr.Constant\"
      ], 
      \"data\": [2]
    }, 
    {
      \"type_key\": \"Array\", 
      \"data\": [3, 11, 19, 27, 35, 43, 51, 59, 67]
    }, 
    {
      \"type_key\": \"relax.expr.Constant\", 
      \"attrs\": {
        \"_checked_type_\": \"10\", 
        \"data\": \"0\", 
        \"span\": \"0\", 
        \"struct_info_\": \"4\"
      }
    }, 
    {
      \"type_key\": \"relax.TensorStructInfo\", 
      \"attrs\": {
        \"dtype\": \"int32\", 
        \"ndim\": \"1\", 
        \"shape\": \"5\", 
        \"span\": \"0\", 
        \"vdevice\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.expr.ShapeExpr\", 
      \"attrs\": {
        \"_checked_type_\": \"9\", 
        \"span\": \"0\", 
        \"struct_info_\": \"8\", 
        \"values\": \"6\"
      }
    }, 
    {
      \"type_key\": \"Array\", 
      \"data\": [7]
    }, 
    {
      \"type_key\": \"IntImm\", 
      \"attrs\": {
        \"dtype\": \"int64\", 
        \"span\": \"0\", 
        \"value\": \"1\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeStructInfo\", 
      \"attrs\": {
        \"ndim\": \"1\", 
        \"span\": \"0\", 
        \"values\": \"6\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeType\", 
      \"attrs\": {
        \"ndim\": \"1\", 
        \"span\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.DynTensorType\", 
      \"attrs\": {
        \"dtype\": \"int32\", 
        \"ndim\": \"1\", 
        \"span\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.expr.Constant\", 
      \"attrs\": {
        \"_checked_type_\": \"18\", 
        \"data\": \"1\", 
        \"span\": \"0\", 
        \"struct_info_\": \"12\"
      }
    }, 
    {
      \"type_key\": \"relax.TensorStructInfo\", 
      \"attrs\": {
        \"dtype\": \"int32\", 
        \"ndim\": \"1\", 
        \"shape\": \"13\", 
        \"span\": \"0\", 
        \"vdevice\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.expr.ShapeExpr\", 
      \"attrs\": {
        \"_checked_type_\": \"17\", 
        \"span\": \"0\", 
        \"struct_info_\": \"16\", 
        \"values\": \"14\"
      }
    }, 
    {
      \"type_key\": \"Array\", 
      \"data\": [15]
    }, 
    {
      \"type_key\": \"IntImm\", 
      \"attrs\": {
        \"dtype\": \"int64\", 
        \"span\": \"0\", 
        \"value\": \"1\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeStructInfo\", 
      \"attrs\": {
        \"ndim\": \"1\", 
        \"span\": \"0\", 
        \"values\": \"14\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeType\", 
      \"attrs\": {
        \"ndim\": \"1\", 
        \"span\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.DynTensorType\", 
      \"attrs\": {
        \"dtype\": \"int32\", 
        \"ndim\": \"1\", 
        \"span\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.expr.Constant\", 
      \"attrs\": {
        \"_checked_type_\": \"26\", 
        \"data\": \"2\", 
        \"span\": \"0\", 
        \"struct_info_\": \"20\"
      }
    }, 
    {
      \"type_key\": \"relax.TensorStructInfo\", 
      \"attrs\": {
        \"dtype\": \"int32\", 
        \"ndim\": \"1\", 
        \"shape\": \"21\", 
        \"span\": \"0\", 
        \"vdevice\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.expr.ShapeExpr\", 
      \"attrs\": {
        \"_checked_type_\": \"25\", 
        \"span\": \"0\", 
        \"struct_info_\": \"24\", 
        \"values\": \"22\"
      }
    }, 
    {
      \"type_key\": \"Array\", 
      \"data\": [23]
    }, 
    {
      \"type_key\": \"IntImm\", 
      \"attrs\": {
        \"dtype\": \"int64\", 
        \"span\": \"0\", 
        \"value\": \"1\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeStructInfo\", 
      \"attrs\": {
        \"ndim\": \"1\", 
        \"span\": \"0\", 
        \"values\": \"22\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeType\", 
      \"attrs\": {
        \"ndim\": \"1\", 
        \"span\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.DynTensorType\", 
      \"attrs\": {
        \"dtype\": \"int32\", 
        \"ndim\": \"1\", 
        \"span\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.expr.Constant\", 
      \"attrs\": {
        \"_checked_type_\": \"34\", 
        \"data\": \"3\", 
        \"span\": \"0\", 
        \"struct_info_\": \"28\"
      }
    }, 
    {
      \"type_key\": \"relax.TensorStructInfo\", 
      \"attrs\": {
        \"dtype\": \"int32\", 
        \"ndim\": \"1\", 
        \"shape\": \"29\", 
        \"span\": \"0\", 
        \"vdevice\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.expr.ShapeExpr\", 
      \"attrs\": {
        \"_checked_type_\": \"33\", 
        \"span\": \"0\", 
        \"struct_info_\": \"32\", 
        \"values\": \"30\"
      }
    }, 
    {
      \"type_key\": \"Array\", 
      \"data\": [31]
    }, 
    {
      \"type_key\": \"IntImm\", 
      \"attrs\": {
        \"dtype\": \"int64\", 
        \"span\": \"0\", 
        \"value\": \"1\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeStructInfo\", 
      \"attrs\": {
        \"ndim\": \"1\", 
        \"span\": \"0\", 
        \"values\": \"30\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeType\", 
      \"attrs\": {
        \"ndim\": \"1\", 
        \"span\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.DynTensorType\", 
      \"attrs\": {
        \"dtype\": \"int32\", 
        \"ndim\": \"1\", 
        \"span\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.expr.Constant\", 
      \"attrs\": {
        \"_checked_type_\": \"42\", 
        \"data\": \"4\", 
        \"span\": \"0\", 
        \"struct_info_\": \"36\"
      }
    }, 
    {
      \"type_key\": \"relax.TensorStructInfo\", 
      \"attrs\": {
        \"dtype\": \"int32\", 
        \"ndim\": \"1\", 
        \"shape\": \"37\", 
        \"span\": \"0\", 
        \"vdevice\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.expr.ShapeExpr\", 
      \"attrs\": {
        \"_checked_type_\": \"41\", 
        \"span\": \"0\", 
        \"struct_info_\": \"40\", 
        \"values\": \"38\"
      }
    }, 
    {
      \"type_key\": \"Array\", 
      \"data\": [39]
    }, 
    {
      \"type_key\": \"IntImm\", 
      \"attrs\": {
        \"dtype\": \"int64\", 
        \"span\": \"0\", 
        \"value\": \"1\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeStructInfo\", 
      \"attrs\": {
        \"ndim\": \"1\", 
        \"span\": \"0\", 
        \"values\": \"38\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeType\", 
      \"attrs\": {
        \"ndim\": \"1\", 
        \"span\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.DynTensorType\", 
      \"attrs\": {
        \"dtype\": \"int32\", 
        \"ndim\": \"1\", 
        \"span\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.expr.Constant\", 
      \"attrs\": {
        \"_checked_type_\": \"50\", 
        \"data\": \"5\", 
        \"span\": \"0\", 
        \"struct_info_\": \"44\"
      }
    }, 
    {
      \"type_key\": \"relax.TensorStructInfo\", 
      \"attrs\": {
        \"dtype\": \"int32\", 
        \"ndim\": \"1\", 
        \"shape\": \"45\", 
        \"span\": \"0\", 
        \"vdevice\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.expr.ShapeExpr\", 
      \"attrs\": {
        \"_checked_type_\": \"49\", 
        \"span\": \"0\", 
        \"struct_info_\": \"48\", 
        \"values\": \"46\"
      }
    }, 
    {
      \"type_key\": \"Array\", 
      \"data\": [47]
    }, 
    {
      \"type_key\": \"IntImm\", 
      \"attrs\": {
        \"dtype\": \"int64\", 
        \"span\": \"0\", 
        \"value\": \"1\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeStructInfo\", 
      \"attrs\": {
        \"ndim\": \"1\", 
        \"span\": \"0\", 
        \"values\": \"46\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeType\", 
      \"attrs\": {
        \"ndim\": \"1\", 
        \"span\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.DynTensorType\", 
      \"attrs\": {
        \"dtype\": \"int32\", 
        \"ndim\": \"1\", 
        \"span\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.expr.Constant\", 
      \"attrs\": {
        \"_checked_type_\": \"58\", 
        \"data\": \"6\", 
        \"span\": \"0\", 
        \"struct_info_\": \"52\"
      }
    }, 
    {
      \"type_key\": \"relax.TensorStructInfo\", 
      \"attrs\": {
        \"dtype\": \"int32\", 
        \"ndim\": \"1\", 
        \"shape\": \"53\", 
        \"span\": \"0\", 
        \"vdevice\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.expr.ShapeExpr\", 
      \"attrs\": {
        \"_checked_type_\": \"57\", 
        \"span\": \"0\", 
        \"struct_info_\": \"56\", 
        \"values\": \"54\"
      }
    }, 
    {
      \"type_key\": \"Array\", 
      \"data\": [55]
    }, 
    {
      \"type_key\": \"IntImm\", 
      \"attrs\": {
        \"dtype\": \"int64\", 
        \"span\": \"0\", 
        \"value\": \"1\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeStructInfo\", 
      \"attrs\": {
        \"ndim\": \"1\", 
        \"span\": \"0\", 
        \"values\": \"54\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeType\", 
      \"attrs\": {
        \"ndim\": \"1\", 
        \"span\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.DynTensorType\", 
      \"attrs\": {
        \"dtype\": \"int32\", 
        \"ndim\": \"1\", 
        \"span\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.expr.Constant\", 
      \"attrs\": {
        \"_checked_type_\": \"66\", 
        \"data\": \"7\", 
        \"span\": \"0\", 
        \"struct_info_\": \"60\"
      }
    }, 
    {
      \"type_key\": \"relax.TensorStructInfo\", 
      \"attrs\": {
        \"dtype\": \"int32\", 
        \"ndim\": \"1\", 
        \"shape\": \"61\", 
        \"span\": \"0\", 
        \"vdevice\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.expr.ShapeExpr\", 
      \"attrs\": {
        \"_checked_type_\": \"65\", 
        \"span\": \"0\", 
        \"struct_info_\": \"64\", 
        \"values\": \"62\"
      }
    }, 
    {
      \"type_key\": \"Array\", 
      \"data\": [63]
    }, 
    {
      \"type_key\": \"IntImm\", 
      \"attrs\": {
        \"dtype\": \"int64\", 
        \"span\": \"0\", 
        \"value\": \"1\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeStructInfo\", 
      \"attrs\": {
        \"ndim\": \"1\", 
        \"span\": \"0\", 
        \"values\": \"62\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeType\", 
      \"attrs\": {
        \"ndim\": \"1\", 
        \"span\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.DynTensorType\", 
      \"attrs\": {
        \"dtype\": \"int32\", 
        \"ndim\": \"1\", 
        \"span\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.expr.Constant\", 
      \"attrs\": {
        \"_checked_type_\": \"74\", 
        \"data\": \"8\", 
        \"span\": \"0\", 
        \"struct_info_\": \"68\"
      }
    }, 
    {
      \"type_key\": \"relax.TensorStructInfo\", 
      \"attrs\": {
        \"dtype\": \"int32\", 
        \"ndim\": \"1\", 
        \"shape\": \"69\", 
        \"span\": \"0\", 
        \"vdevice\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.expr.ShapeExpr\", 
      \"attrs\": {
        \"_checked_type_\": \"73\", 
        \"span\": \"0\", 
        \"struct_info_\": \"72\", 
        \"values\": \"70\"
      }
    }, 
    {
      \"type_key\": \"Array\", 
      \"data\": [71]
    }, 
    {
      \"type_key\": \"IntImm\", 
      \"attrs\": {
        \"dtype\": \"int64\", 
        \"span\": \"0\", 
        \"value\": \"1\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeStructInfo\", 
      \"attrs\": {
        \"ndim\": \"1\", 
        \"span\": \"0\", 
        \"values\": \"70\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeType\", 
      \"attrs\": {
        \"ndim\": \"1\", 
        \"span\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.DynTensorType\", 
      \"attrs\": {
        \"dtype\": \"int32\", 
        \"ndim\": \"1\", 
        \"span\": \"0\"
      }
    }
  ], 
  \"b64ndarrays\": [
    \"P6G0lvBAXt0AAAAAAAAAAAEAAAAAAAAAAQAAAAAgAQABAAAAAAAAAAQAAAAAAAAAAAAAAA==\", 
    \"P6G0lvBAXt0AAAAAAAAAAAEAAAAAAAAAAQAAAAAgAQABAAAAAAAAAAQAAAAAAAAAAAAAAA==\", 
    \"P6G0lvBAXt0AAAAAAAAAAAEAAAAAAAAAAQAAAAAgAQABAAAAAAAAAAQAAAAAAAAAAAAAAA==\", 
    \"P6G0lvBAXt0AAAAAAAAAAAEAAAAAAAAAAQAAAAAgAQABAAAAAAAAAAQAAAAAAAAAAAAAAA==\", 
    \"P6G0lvBAXt0AAAAAAAAAAAEAAAAAAAAAAQAAAAAgAQABAAAAAAAAAAQAAAAAAAAAAAAAAA==\", 
    \"P6G0lvBAXt0AAAAAAAAAAAEAAAAAAAAAAQAAAAAgAQABAAAAAAAAAAQAAAAAAAAAAAAAAA==\", 
    \"P6G0lvBAXt0AAAAAAAAAAAEAAAAAAAAAAQAAAAAgAQABAAAAAAAAAAQAAAAAAAAAAAAAAA==\", 
    \"P6G0lvBAXt0AAAAAAAAAAAEAAAAAAAAAAQAAAAAgAQABAAAAAAAAAAQAAAAAAAAAAAAAAA==\", 
    \"P6G0lvBAXt0AAAAAAAAAAAEAAAAAAAAAAQAAAAAgAQABAAAAAAAAAAQAAAAAAAAAAAAAAA==\"
  ], 
  \"attrs\": {\"tvm_version\": \"0.19.dev0\"}
}""")
# from tvm.script import ir as I
# from tvm.script import tir as T
# from tvm.script import relax as R

@I.ir_module
class Module:
    @T.prim_func
    def cached_padding_1d_crop(var_x: T.handle, var_res: T.handle):
        b, c, out = T.int32(), T.int32(), T.int32()
        x = T.match_buffer(var_x, (b, c, out))
        n = T.int32()
        res = T.match_buffer(var_res, (b, c, n))
        # with T.block("root"):
        for bb, cc, nn in T.grid(b, c, n):
            with T.block("res_crop"):
                vb, vc, vn = T.axis.remap("SSS", [bb, cc, nn])
                T.reads(x[vb, vc, vn])
                T.writes(res[vb, vc, vn])
                res[vb, vc, vn] = x[vb, vc, vn]

    @T.prim_func
    def cached_padding_1d_init(var_cache: T.handle):
        b, c, p = T.int32(), T.int32(), T.int32()
        cache = T.match_buffer(var_cache, (b, c, p))
        # with T.block("root"):
        for bb, cc, pp in T.grid(b, c, p):
            with T.block("cache_init"):
                vb, vc, vp = T.axis.remap("SSS", [bb, cc, pp])
                T.reads()
                T.writes(cache[vb, vc, vp])
                cache[vb, vc, vp] = T.float32(0.0)

    @T.prim_func
    def cached_padding_1d_update(var_cache: T.handle, var_data: T.handle, var_res: T.handle):
        B, c, p = T.int32(), T.int32(), T.int32()
        cache = T.match_buffer(var_cache, (B, c, p))
        b, n = T.int32(), T.int32()
        data = T.match_buffer(var_data, (b, c, n))
        out = T.int32()
        res = T.match_buffer(var_res, (b, c, out))
        # with T.block("root"):
        for bb, cc, oo in T.grid(b, c, out):
            with T.block("res_update"):
                vb, vc, vo = T.axis.remap("SSS", [bb, cc, oo])
                T.reads(cache[vb, vc, vo], data[vb, vc, vo - p])
                T.writes(res[vb, vc, vo])
                res[vb, vc, vo] = T.if_then_else(vo < p, cache[vb, vc, vo], data[vb, vc, vo - p])
        for bb, cc, pp in T.grid(b, c, p):
            with T.block("cache_update"):
                vb, vc, vp = T.axis.remap("SSS", [bb, cc, pp])
                T.reads(res[vb, vc, out - p + vp])
                T.writes(cache[vb, vc, vp])
                cache[vb, vc, vp] = res[vb, vc, out - p + vp]

    @T.prim_func
    def cached_padding_transpose_1d_update(var_cache: T.handle, var_data: T.handle, var_res: T.handle):
        B, c, p = T.int32(), T.int32(), T.int32()
        cache = T.match_buffer(var_cache, (B, c, p))
        b, n = T.int32(), T.int32()
        data = T.match_buffer(var_data, (b, c, n))
        out = T.int32()
        res = T.match_buffer(var_res, (b, c, out))
        # with T.block("root"):
        for bb, cc, oo in T.grid(b, c, out):
            with T.block("res_update"):
                vb, vc, vo = T.axis.remap("SSS", [bb, cc, oo])
                T.reads(cache[vb, vc, vo], data[vb, vc, vo])
                T.writes(res[vb, vc, vo])
                res[vb, vc, vo] = T.if_then_else(vo < p, cache[vb, vc, vo] + data[vb, vc, vo], data[vb, vc, vo])
        for bb, cc, pp in T.grid(b, c, p):
            with T.block("cache_update"):
                vb, vc, vp = T.axis.remap("SSS", [bb, cc, pp])
                T.reads(res[vb, vc, out - p + vp])
                T.writes(cache[vb, vc, vp])
                cache[vb, vc, vp] = res[vb, vc, out - p + vp]

    @T.prim_func(private=True)
    def snake(reshape: T.Buffer((T.int64(1), T.int64(64), T.int64(512)), "float32"), encoder_block_layers_1_block_layers_0_block_branches_0_layers_0_alpha: T.Buffer((T.int64(1), T.int64(64), T.int64(1)), "float32"), snake_compute: T.Buffer((T.int64(1), T.int64(64), T.int64(512)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i, j, k in T.grid(T.int64(1), T.int64(64), T.int64(512)):
            with T.block("snake_compute"):
                v_i, v_j, v_k = T.axis.remap("SSS", [i, j, k])
                T.reads(reshape[v_i, v_j, v_k], encoder_block_layers_1_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_j, T.int64(0)])
                T.writes(snake_compute[v_i, v_j, v_k])
                snake_compute[v_i, v_j, v_k] = reshape[v_i, v_j, v_k] + T.float32(1.0) / (encoder_block_layers_1_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_j, T.int64(0)] + T.float32(1.0000000000000001e-09)) * T.pow(T.sin(encoder_block_layers_1_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_j, T.int64(0)] * reshape[v_i, v_j, v_k]), T.float32(2.0))

    @T.prim_func(private=True)
    def snake1(reshape14: T.Buffer((T.int64(1), T.int64(128), T.int64(256)), "float32"), encoder_block_layers_2_block_layers_0_block_branches_0_layers_0_alpha: T.Buffer((T.int64(1), T.int64(128), T.int64(1)), "float32"), snake_compute: T.Buffer((T.int64(1), T.int64(128), T.int64(256)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i, j, k in T.grid(T.int64(1), T.int64(128), T.int64(256)):
            with T.block("snake_compute"):
                v_i, v_j, v_k = T.axis.remap("SSS", [i, j, k])
                T.reads(reshape14[v_i, v_j, v_k], encoder_block_layers_2_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_j, T.int64(0)])
                T.writes(snake_compute[v_i, v_j, v_k])
                snake_compute[v_i, v_j, v_k] = reshape14[v_i, v_j, v_k] + T.float32(1.0) / (encoder_block_layers_2_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_j, T.int64(0)] + T.float32(1.0000000000000001e-09)) * T.pow(T.sin(encoder_block_layers_2_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_j, T.int64(0)] * reshape14[v_i, v_j, v_k]), T.float32(2.0))

    @T.prim_func(private=True)
    def snake2(reshape28: T.Buffer((T.int64(1), T.int64(256), T.int64(64)), "float32"), encoder_block_layers_3_block_layers_0_block_branches_0_layers_0_alpha: T.Buffer((T.int64(1), T.int64(256), T.int64(1)), "float32"), snake_compute: T.Buffer((T.int64(1), T.int64(256), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i, j, k in T.grid(T.int64(1), T.int64(256), T.int64(64)):
            with T.block("snake_compute"):
                v_i, v_j, v_k = T.axis.remap("SSS", [i, j, k])
                T.reads(reshape28[v_i, v_j, v_k], encoder_block_layers_3_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_j, T.int64(0)])
                T.writes(snake_compute[v_i, v_j, v_k])
                snake_compute[v_i, v_j, v_k] = reshape28[v_i, v_j, v_k] + T.float32(1.0) / (encoder_block_layers_3_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_j, T.int64(0)] + T.float32(1.0000000000000001e-09)) * T.pow(T.sin(encoder_block_layers_3_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_j, T.int64(0)] * reshape28[v_i, v_j, v_k]), T.float32(2.0))

    @T.prim_func(private=True)
    def snake3(reshape42: T.Buffer((T.int64(1), T.int64(512), T.int64(8)), "float32"), encoder_block_layers_4_block_layers_0_block_branches_0_layers_0_alpha: T.Buffer((T.int64(1), T.int64(512), T.int64(1)), "float32"), snake_compute: T.Buffer((T.int64(1), T.int64(512), T.int64(8)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i, j, k in T.grid(T.int64(1), T.int64(512), T.int64(8)):
            with T.block("snake_compute"):
                v_i, v_j, v_k = T.axis.remap("SSS", [i, j, k])
                T.reads(reshape42[v_i, v_j, v_k], encoder_block_layers_4_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_j, T.int64(0)])
                T.writes(snake_compute[v_i, v_j, v_k])
                snake_compute[v_i, v_j, v_k] = reshape42[v_i, v_j, v_k] + T.float32(1.0) / (encoder_block_layers_4_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_j, T.int64(0)] + T.float32(1.0000000000000001e-09)) * T.pow(T.sin(encoder_block_layers_4_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_j, T.int64(0)] * reshape42[v_i, v_j, v_k]), T.float32(2.0))

    @T.prim_func(private=True)
    def snake4(reshape56: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32"), encoder_block_layers_5_alpha: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32"), snake_compute: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i, j, k in T.grid(T.int64(1), T.int64(1024), T.int64(1)):
            with T.block("snake_compute"):
                v_i, v_j, v_k = T.axis.remap("SSS", [i, j, k])
                T.reads(reshape56[v_i, v_j, v_k], encoder_block_layers_5_alpha[T.int64(0), v_j, T.int64(0)])
                T.writes(snake_compute[v_i, v_j, v_k])
                snake_compute[v_i, v_j, v_k] = reshape56[v_i, v_j, v_k] + T.float32(1.0) / (encoder_block_layers_5_alpha[T.int64(0), v_j, T.int64(0)] + T.float32(1.0000000000000001e-09)) * T.pow(T.sin(encoder_block_layers_5_alpha[T.int64(0), v_j, T.int64(0)] * reshape56[v_i, v_j, v_k]), T.float32(2.0))

    @T.prim_func(private=True)
    def snake5(reshape94: T.Buffer((T.int64(1), T.int64(1536), T.int64(1)), "float32"), decoder_model_layers_1_block_layers_0_alpha1: T.Buffer((T.int64(1), T.int64(1536), T.int64(1)), "float32"), snake_compute: T.Buffer((T.int64(1), T.int64(1536), T.int64(1)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i, j, k in T.grid(T.int64(1), T.int64(1536), T.int64(1)):
            with T.block("snake_compute"):
                v_i, v_j, v_k = T.axis.remap("SSS", [i, j, k])
                T.reads(reshape94[v_i, v_j, v_k], decoder_model_layers_1_block_layers_0_alpha1[T.int64(0), v_j, T.int64(0)])
                T.writes(snake_compute[v_i, v_j, v_k])
                snake_compute[v_i, v_j, v_k] = reshape94[v_i, v_j, v_k] + T.float32(1.0) / (decoder_model_layers_1_block_layers_0_alpha1[T.int64(0), v_j, T.int64(0)] + T.float32(1.0000000000000001e-09)) * T.pow(T.sin(decoder_model_layers_1_block_layers_0_alpha1[T.int64(0), v_j, T.int64(0)] * reshape94[v_i, v_j, v_k]), T.float32(2.0))

    @T.prim_func(private=True)
    def snake6(reshape96: T.Buffer((T.int64(1), T.int64(768), T.int64(8)), "float32"), decoder_model_layers_1_block_layers_2_block_branches_0_layers_0_alpha1: T.Buffer((T.int64(1), T.int64(768), T.int64(1)), "float32"), snake_compute: T.Buffer((T.int64(1), T.int64(768), T.int64(8)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i, j, k in T.grid(T.int64(1), T.int64(768), T.int64(8)):
            with T.block("snake_compute"):
                v_i, v_j, v_k = T.axis.remap("SSS", [i, j, k])
                T.reads(reshape96[v_i, v_j, v_k], decoder_model_layers_1_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_j, T.int64(0)])
                T.writes(snake_compute[v_i, v_j, v_k])
                snake_compute[v_i, v_j, v_k] = reshape96[v_i, v_j, v_k] + T.float32(1.0) / (decoder_model_layers_1_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_j, T.int64(0)] + T.float32(1.0000000000000001e-09)) * T.pow(T.sin(decoder_model_layers_1_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_j, T.int64(0)] * reshape96[v_i, v_j, v_k]), T.float32(2.0))

    @T.prim_func(private=True)
    def snake7(reshape110: T.Buffer((T.int64(1), T.int64(384), T.int64(64)), "float32"), decoder_model_layers_2_block_layers_2_block_branches_0_layers_0_alpha1: T.Buffer((T.int64(1), T.int64(384), T.int64(1)), "float32"), snake_compute: T.Buffer((T.int64(1), T.int64(384), T.int64(64)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i, j, k in T.grid(T.int64(1), T.int64(384), T.int64(64)):
            with T.block("snake_compute"):
                v_i, v_j, v_k = T.axis.remap("SSS", [i, j, k])
                T.reads(reshape110[v_i, v_j, v_k], decoder_model_layers_2_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_j, T.int64(0)])
                T.writes(snake_compute[v_i, v_j, v_k])
                snake_compute[v_i, v_j, v_k] = reshape110[v_i, v_j, v_k] + T.float32(1.0) / (decoder_model_layers_2_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_j, T.int64(0)] + T.float32(1.0000000000000001e-09)) * T.pow(T.sin(decoder_model_layers_2_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_j, T.int64(0)] * reshape110[v_i, v_j, v_k]), T.float32(2.0))

    @T.prim_func(private=True)
    def snake8(reshape124: T.Buffer((T.int64(1), T.int64(192), T.int64(256)), "float32"), decoder_model_layers_3_block_layers_2_block_branches_0_layers_0_alpha1: T.Buffer((T.int64(1), T.int64(192), T.int64(1)), "float32"), snake_compute: T.Buffer((T.int64(1), T.int64(192), T.int64(256)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i, j, k in T.grid(T.int64(1), T.int64(192), T.int64(256)):
            with T.block("snake_compute"):
                v_i, v_j, v_k = T.axis.remap("SSS", [i, j, k])
                T.reads(reshape124[v_i, v_j, v_k], decoder_model_layers_3_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_j, T.int64(0)])
                T.writes(snake_compute[v_i, v_j, v_k])
                snake_compute[v_i, v_j, v_k] = reshape124[v_i, v_j, v_k] + T.float32(1.0) / (decoder_model_layers_3_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_j, T.int64(0)] + T.float32(1.0000000000000001e-09)) * T.pow(T.sin(decoder_model_layers_3_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_j, T.int64(0)] * reshape124[v_i, v_j, v_k]), T.float32(2.0))

    @T.prim_func(private=True)
    def snake9(reshape138: T.Buffer((T.int64(1), T.int64(96), T.int64(512)), "float32"), decoder_model_layers_4_block_layers_2_block_branches_0_layers_0_alpha1: T.Buffer((T.int64(1), T.int64(96), T.int64(1)), "float32"), snake_compute: T.Buffer((T.int64(1), T.int64(96), T.int64(512)), "float32")):
        T.func_attr({"tir.noalias": T.bool(True)})
        # with T.block("root"):
        for i, j, k in T.grid(T.int64(1), T.int64(96), T.int64(512)):
            with T.block("snake_compute"):
                v_i, v_j, v_k = T.axis.remap("SSS", [i, j, k])
                T.reads(reshape138[v_i, v_j, v_k], decoder_model_layers_4_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_j, T.int64(0)])
                T.writes(snake_compute[v_i, v_j, v_k])
                snake_compute[v_i, v_j, v_k] = reshape138[v_i, v_j, v_k] + T.float32(1.0) / (decoder_model_layers_4_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_j, T.int64(0)] + T.float32(1.0000000000000001e-09)) * T.pow(T.sin(decoder_model_layers_4_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_j, T.int64(0)] * reshape138[v_i, v_j, v_k]), T.float32(2.0))

    @R.function
    def _initialize_effect() -> R.Tuple(R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object):
        cls = Module
        with R.dataflow():
            _io: R.Object = R.null_value()
            encoder_block_layers_0_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(6), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_0_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(6), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_1_block_layers_0_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_1_block_layers_0_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(3), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(18), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_1_block_layers_1_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_1_block_layers_1_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(9), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(54), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_1_block_layers_2_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_1_block_layers_2_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(27), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_1_block_layers_4_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(2), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_1_block_layers_4_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(1), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(6), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_2_block_layers_0_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_2_block_layers_0_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(3), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(18), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_2_block_layers_1_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_2_block_layers_1_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(9), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(54), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_2_block_layers_2_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_2_block_layers_2_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(27), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_2_block_layers_4_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(4), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_2_block_layers_4_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(1), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(6), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_3_block_layers_0_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_3_block_layers_0_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(3), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(18), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_3_block_layers_1_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_3_block_layers_1_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(9), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(54), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_3_block_layers_2_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_3_block_layers_2_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(27), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_3_block_layers_4_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(8), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_3_block_layers_4_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(5), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(6), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_4_block_layers_0_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_4_block_layers_0_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(3), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(18), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_4_block_layers_1_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_4_block_layers_1_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(9), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(54), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_4_block_layers_2_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_4_block_layers_2_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(27), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_4_block_layers_4_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(8), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_4_block_layers_4_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(5), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_6_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(2), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            encoder_block_layers_6_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_0_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(6), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_0_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_1_block_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(8), R.prim_value(1), R.prim_value(32), R.prim_value(1), cls.cached_padding_1d_init, cls.cached_padding_transpose_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(6), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_1_block_layers_2_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_1_block_layers_2_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(3), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(18), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_1_block_layers_3_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_1_block_layers_3_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(9), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(54), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_1_block_layers_4_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_1_block_layers_4_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(27), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_2_block_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(8), R.prim_value(1), R.prim_value(32), R.prim_value(1), cls.cached_padding_1d_init, cls.cached_padding_transpose_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(6), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_2_block_layers_2_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_2_block_layers_2_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(3), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(18), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_2_block_layers_3_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_2_block_layers_3_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(9), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(54), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_2_block_layers_4_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_2_block_layers_4_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(27), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_3_block_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(4), R.prim_value(1), R.prim_value(32), R.prim_value(1), cls.cached_padding_1d_init, cls.cached_padding_transpose_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(6), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_3_block_layers_2_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_3_block_layers_2_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(3), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(18), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_3_block_layers_3_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_3_block_layers_3_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(9), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(54), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_3_block_layers_4_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_3_block_layers_4_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(27), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_4_block_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(2), R.prim_value(1), R.prim_value(32), R.prim_value(1), cls.cached_padding_1d_init, cls.cached_padding_transpose_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(6), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_4_block_layers_2_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_4_block_layers_2_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(3), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(18), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_4_block_layers_3_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_4_block_layers_3_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(9), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(54), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_4_block_layers_4_block_paddings_0_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_4_block_layers_4_block_paddings_1_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(27), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_6_cache_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(6), R.prim_value(0), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            decoder_model_layers_6_downsampling_delay_cache: R.Object = R.call_pure_packed("vm.builtin.cached_padding_1d_create", R.prim_value(0), R.prim_value(1), R.prim_value(32), R.prim_value(0), cls.cached_padding_1d_init, cls.cached_padding_1d_update, cls.cached_padding_1d_crop, sinfo_args=(R.Object,))
            lv: R.Tuple(R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object) = _io, encoder_block_layers_0_cache_cache, encoder_block_layers_0_downsampling_delay_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_1_block_layers_0_block_paddings_0_cache, encoder_block_layers_1_block_layers_0_block_paddings_1_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_1_block_layers_1_block_paddings_0_cache, encoder_block_layers_1_block_layers_1_block_paddings_1_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_1_block_layers_2_block_paddings_0_cache, encoder_block_layers_1_block_layers_2_block_paddings_1_cache, encoder_block_layers_1_block_layers_4_cache_cache, encoder_block_layers_1_block_layers_4_downsampling_delay_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_2_block_layers_0_block_paddings_0_cache, encoder_block_layers_2_block_layers_0_block_paddings_1_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_2_block_layers_1_block_paddings_0_cache, encoder_block_layers_2_block_layers_1_block_paddings_1_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_2_block_layers_2_block_paddings_0_cache, encoder_block_layers_2_block_layers_2_block_paddings_1_cache, encoder_block_layers_2_block_layers_4_cache_cache, encoder_block_layers_2_block_layers_4_downsampling_delay_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_3_block_layers_0_block_paddings_0_cache, encoder_block_layers_3_block_layers_0_block_paddings_1_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_3_block_layers_1_block_paddings_0_cache, encoder_block_layers_3_block_layers_1_block_paddings_1_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_3_block_layers_2_block_paddings_0_cache, encoder_block_layers_3_block_layers_2_block_paddings_1_cache, encoder_block_layers_3_block_layers_4_cache_cache, encoder_block_layers_3_block_layers_4_downsampling_delay_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_4_block_layers_0_block_paddings_0_cache, encoder_block_layers_4_block_layers_0_block_paddings_1_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_4_block_layers_1_block_paddings_0_cache, encoder_block_layers_4_block_layers_1_block_paddings_1_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_4_block_layers_2_block_paddings_0_cache, encoder_block_layers_4_block_layers_2_block_paddings_1_cache, encoder_block_layers_4_block_layers_4_cache_cache, encoder_block_layers_4_block_layers_4_downsampling_delay_cache, encoder_block_layers_6_cache_cache, encoder_block_layers_6_downsampling_delay_cache, decoder_model_layers_0_cache_cache, decoder_model_layers_0_downsampling_delay_cache, decoder_model_layers_1_block_layers_1_cache_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_1_block_layers_2_block_paddings_0_cache, decoder_model_layers_1_block_layers_2_block_paddings_1_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_1_block_layers_3_block_paddings_0_cache, decoder_model_layers_1_block_layers_3_block_paddings_1_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_1_block_layers_4_block_paddings_0_cache, decoder_model_layers_1_block_layers_4_block_paddings_1_cache, decoder_model_layers_2_block_layers_1_cache_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_2_block_layers_2_block_paddings_0_cache, decoder_model_layers_2_block_layers_2_block_paddings_1_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_2_block_layers_3_block_paddings_0_cache, decoder_model_layers_2_block_layers_3_block_paddings_1_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_2_block_layers_4_block_paddings_0_cache, decoder_model_layers_2_block_layers_4_block_paddings_1_cache, decoder_model_layers_3_block_layers_1_cache_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_3_block_layers_2_block_paddings_0_cache, decoder_model_layers_3_block_layers_2_block_paddings_1_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_3_block_layers_3_block_paddings_0_cache, decoder_model_layers_3_block_layers_3_block_paddings_1_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_3_block_layers_4_block_paddings_0_cache, decoder_model_layers_3_block_layers_4_block_paddings_1_cache, decoder_model_layers_4_block_layers_1_cache_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_4_block_layers_2_block_paddings_0_cache, decoder_model_layers_4_block_layers_2_block_paddings_1_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_4_block_layers_3_block_paddings_0_cache, decoder_model_layers_4_block_layers_3_block_paddings_1_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_4_block_layers_4_block_paddings_0_cache, decoder_model_layers_4_block_layers_4_block_paddings_1_cache, decoder_model_layers_6_cache_cache, decoder_model_layers_6_downsampling_delay_cache
            gv: R.Tuple(R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object) = lv
            R.output(gv)
        return gv

    @R.function
    def decode(z: R.Tensor((1, 1024, 1), dtype="float32"), _io: R.Object, encoder_block_layers_0_cache_cache: R.Object, encoder_block_layers_0_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_0_block_paddings_0_cache: R.Object, encoder_block_layers_1_block_layers_0_block_paddings_1_cache: R.Object, encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_1_block_paddings_0_cache: R.Object, encoder_block_layers_1_block_layers_1_block_paddings_1_cache: R.Object, encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_2_block_paddings_0_cache: R.Object, encoder_block_layers_1_block_layers_2_block_paddings_1_cache: R.Object, encoder_block_layers_1_block_layers_4_cache_cache: R.Object, encoder_block_layers_1_block_layers_4_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_0_block_paddings_0_cache: R.Object, encoder_block_layers_2_block_layers_0_block_paddings_1_cache: R.Object, encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_1_block_paddings_0_cache: R.Object, encoder_block_layers_2_block_layers_1_block_paddings_1_cache: R.Object, encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_2_block_paddings_0_cache: R.Object, encoder_block_layers_2_block_layers_2_block_paddings_1_cache: R.Object, encoder_block_layers_2_block_layers_4_cache_cache: R.Object, encoder_block_layers_2_block_layers_4_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_0_block_paddings_0_cache: R.Object, encoder_block_layers_3_block_layers_0_block_paddings_1_cache: R.Object, encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_1_block_paddings_0_cache: R.Object, encoder_block_layers_3_block_layers_1_block_paddings_1_cache: R.Object, encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_2_block_paddings_0_cache: R.Object, encoder_block_layers_3_block_layers_2_block_paddings_1_cache: R.Object, encoder_block_layers_3_block_layers_4_cache_cache: R.Object, encoder_block_layers_3_block_layers_4_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_0_block_paddings_0_cache: R.Object, encoder_block_layers_4_block_layers_0_block_paddings_1_cache: R.Object, encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_1_block_paddings_0_cache: R.Object, encoder_block_layers_4_block_layers_1_block_paddings_1_cache: R.Object, encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_2_block_paddings_0_cache: R.Object, encoder_block_layers_4_block_layers_2_block_paddings_1_cache: R.Object, encoder_block_layers_4_block_layers_4_cache_cache: R.Object, encoder_block_layers_4_block_layers_4_downsampling_delay_cache: R.Object, encoder_block_layers_6_cache_cache: R.Object, encoder_block_layers_6_downsampling_delay_cache: R.Object, decoder_model_layers_0_cache_cache: R.Object, decoder_model_layers_0_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_1_cache_cache: R.Object, decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_2_block_paddings_0_cache: R.Object, decoder_model_layers_1_block_layers_2_block_paddings_1_cache: R.Object, decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_3_block_paddings_0_cache: R.Object, decoder_model_layers_1_block_layers_3_block_paddings_1_cache: R.Object, decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_4_block_paddings_0_cache: R.Object, decoder_model_layers_1_block_layers_4_block_paddings_1_cache: R.Object, decoder_model_layers_2_block_layers_1_cache_cache: R.Object, decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_2_block_paddings_0_cache: R.Object, decoder_model_layers_2_block_layers_2_block_paddings_1_cache: R.Object, decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_3_block_paddings_0_cache: R.Object, decoder_model_layers_2_block_layers_3_block_paddings_1_cache: R.Object, decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_4_block_paddings_0_cache: R.Object, decoder_model_layers_2_block_layers_4_block_paddings_1_cache: R.Object, decoder_model_layers_3_block_layers_1_cache_cache: R.Object, decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_2_block_paddings_0_cache: R.Object, decoder_model_layers_3_block_layers_2_block_paddings_1_cache: R.Object, decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_3_block_paddings_0_cache: R.Object, decoder_model_layers_3_block_layers_3_block_paddings_1_cache: R.Object, decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_4_block_paddings_0_cache: R.Object, decoder_model_layers_3_block_layers_4_block_paddings_1_cache: R.Object, decoder_model_layers_4_block_layers_1_cache_cache: R.Object, decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_2_block_paddings_0_cache: R.Object, decoder_model_layers_4_block_layers_2_block_paddings_1_cache: R.Object, decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_3_block_paddings_0_cache: R.Object, decoder_model_layers_4_block_layers_3_block_paddings_1_cache: R.Object, decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_4_block_paddings_0_cache: R.Object, decoder_model_layers_4_block_layers_4_block_paddings_1_cache: R.Object, decoder_model_layers_6_cache_cache: R.Object, decoder_model_layers_6_downsampling_delay_cache: R.Object, packed_params: R.Tuple(R.Tensor((64, 1, 1), dtype="float32"), R.Tensor((64, 1, 7), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((1, 64, 1), dtype="float32"), R.Tensor((64, 1, 1), dtype="float32"), R.Tensor((64, 64, 7), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((1, 64, 1), dtype="float32"), R.Tensor((64, 1, 1), dtype="float32"), R.Tensor((64, 64, 1), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((1, 64, 1), dtype="float32"), R.Tensor((64, 1, 1), dtype="float32"), R.Tensor((64, 64, 7), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((1, 64, 1), dtype="float32"), R.Tensor((64, 1, 1), dtype="float32"), R.Tensor((64, 64, 1), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((1, 64, 1), dtype="float32"), R.Tensor((64, 1, 1), dtype="float32"), R.Tensor((64, 64, 7), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((1, 64, 1), dtype="float32"), R.Tensor((64, 1, 1), dtype="float32"), R.Tensor((64, 64, 1), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((1, 64, 1), dtype="float32"), R.Tensor((128, 1, 1), dtype="float32"), R.Tensor((128, 64, 4), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((1, 128, 1), dtype="float32"), R.Tensor((128, 1, 1), dtype="float32"), R.Tensor((128, 128, 7), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((1, 128, 1), dtype="float32"), R.Tensor((128, 1, 1), dtype="float32"), R.Tensor((128, 128, 1), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((1, 128, 1), dtype="float32"), R.Tensor((128, 1, 1), dtype="float32"), R.Tensor((128, 128, 7), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((1, 128, 1), dtype="float32"), R.Tensor((128, 1, 1), dtype="float32"), R.Tensor((128, 128, 1), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((1, 128, 1), dtype="float32"), R.Tensor((128, 1, 1), dtype="float32"), R.Tensor((128, 128, 7), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((1, 128, 1), dtype="float32"), R.Tensor((128, 1, 1), dtype="float32"), R.Tensor((128, 128, 1), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((1, 128, 1), dtype="float32"), R.Tensor((256, 1, 1), dtype="float32"), R.Tensor((256, 128, 8), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((1, 256, 1), dtype="float32"), R.Tensor((256, 1, 1), dtype="float32"), R.Tensor((256, 256, 7), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((1, 256, 1), dtype="float32"), R.Tensor((256, 1, 1), dtype="float32"), R.Tensor((256, 256, 1), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((1, 256, 1), dtype="float32"), R.Tensor((256, 1, 1), dtype="float32"), R.Tensor((256, 256, 7), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((1, 256, 1), dtype="float32"), R.Tensor((256, 1, 1), dtype="float32"), R.Tensor((256, 256, 1), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((1, 256, 1), dtype="float32"), R.Tensor((256, 1, 1), dtype="float32"), R.Tensor((256, 256, 7), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((1, 256, 1), dtype="float32"), R.Tensor((256, 1, 1), dtype="float32"), R.Tensor((256, 256, 1), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((1, 256, 1), dtype="float32"), R.Tensor((512, 1, 1), dtype="float32"), R.Tensor((512, 256, 16), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((1, 512, 1), dtype="float32"), R.Tensor((512, 1, 1), dtype="float32"), R.Tensor((512, 512, 7), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((1, 512, 1), dtype="float32"), R.Tensor((512, 1, 1), dtype="float32"), R.Tensor((512, 512, 1), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((1, 512, 1), dtype="float32"), R.Tensor((512, 1, 1), dtype="float32"), R.Tensor((512, 512, 7), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((1, 512, 1), dtype="float32"), R.Tensor((512, 1, 1), dtype="float32"), R.Tensor((512, 512, 1), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((1, 512, 1), dtype="float32"), R.Tensor((512, 1, 1), dtype="float32"), R.Tensor((512, 512, 7), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((1, 512, 1), dtype="float32"), R.Tensor((512, 1, 1), dtype="float32"), R.Tensor((512, 512, 1), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((1, 512, 1), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 512, 16), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1, 1024, 1), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 1024, 3), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((8, 1, 1), dtype="float32"), R.Tensor((8, 1024, 1), dtype="float32"), R.Tensor((8,), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 8, 1), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024, 8), dtype="float32"), R.Tensor((8, 1, 1), dtype="float32"), R.Tensor((8, 1024, 1), dtype="float32"), R.Tensor((8,), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 8, 1), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024, 8), dtype="float32"), R.Tensor((8, 1, 1), dtype="float32"), R.Tensor((8, 1024, 1), dtype="float32"), R.Tensor((8,), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 8, 1), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024, 8), dtype="float32"), R.Tensor((8, 1, 1), dtype="float32"), R.Tensor((8, 1024, 1), dtype="float32"), R.Tensor((8,), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 8, 1), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024, 8), dtype="float32"), R.Tensor((8, 1, 1), dtype="float32"), R.Tensor((8, 1024, 1), dtype="float32"), R.Tensor((8,), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 8, 1), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024, 8), dtype="float32"), R.Tensor((8, 1, 1), dtype="float32"), R.Tensor((8, 1024, 1), dtype="float32"), R.Tensor((8,), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 8, 1), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024, 8), dtype="float32"), R.Tensor((8, 1, 1), dtype="float32"), R.Tensor((8, 1024, 1), dtype="float32"), R.Tensor((8,), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 8, 1), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024, 8), dtype="float32"), R.Tensor((8, 1, 1), dtype="float32"), R.Tensor((8, 1024, 1), dtype="float32"), R.Tensor((8,), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 8, 1), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024, 8), dtype="float32"), R.Tensor((8, 1, 1), dtype="float32"), R.Tensor((8, 1024, 1), dtype="float32"), R.Tensor((8,), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 8, 1), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024, 8), dtype="float32"), R.Tensor((1536, 1, 1), dtype="float32"), R.Tensor((1536, 1024, 7), dtype="float32"), R.Tensor((1536,), dtype="float32"), R.Tensor((1, 1536, 1), dtype="float32"), R.Tensor((1536, 1, 1), dtype="float32"), R.Tensor((1536, 768, 16), dtype="float32"), R.Tensor((768,), dtype="float32"), R.Tensor((1, 768, 1), dtype="float32"), R.Tensor((768, 1, 1), dtype="float32"), R.Tensor((768, 768, 7), dtype="float32"), R.Tensor((768,), dtype="float32"), R.Tensor((1, 768, 1), dtype="float32"), R.Tensor((768, 1, 1), dtype="float32"), R.Tensor((768, 768, 1), dtype="float32"), R.Tensor((768,), dtype="float32"), R.Tensor((1, 768, 1), dtype="float32"), R.Tensor((768, 1, 1), dtype="float32"), R.Tensor((768, 768, 7), dtype="float32"), R.Tensor((768,), dtype="float32"), R.Tensor((1, 768, 1), dtype="float32"), R.Tensor((768, 1, 1), dtype="float32"), R.Tensor((768, 768, 1), dtype="float32"), R.Tensor((768,), dtype="float32"), R.Tensor((1, 768, 1), dtype="float32"), R.Tensor((768, 1, 1), dtype="float32"), R.Tensor((768, 768, 7), dtype="float32"), R.Tensor((768,), dtype="float32"), R.Tensor((1, 768, 1), dtype="float32"), R.Tensor((768, 1, 1), dtype="float32"), R.Tensor((768, 768, 1), dtype="float32"), R.Tensor((768,), dtype="float32"), R.Tensor((1, 768, 1), dtype="float32"), R.Tensor((768, 1, 1), dtype="float32"), R.Tensor((768, 384, 16), dtype="float32"), R.Tensor((384,), dtype="float32"), R.Tensor((1, 384, 1), dtype="float32"), R.Tensor((384, 1, 1), dtype="float32"), R.Tensor((384, 384, 7), dtype="float32"), R.Tensor((384,), dtype="float32"), R.Tensor((1, 384, 1), dtype="float32"), R.Tensor((384, 1, 1), dtype="float32"), R.Tensor((384, 384, 1), dtype="float32"), R.Tensor((384,), dtype="float32"), R.Tensor((1, 384, 1), dtype="float32"), R.Tensor((384, 1, 1), dtype="float32"), R.Tensor((384, 384, 7), dtype="float32"), R.Tensor((384,), dtype="float32"), R.Tensor((1, 384, 1), dtype="float32"), R.Tensor((384, 1, 1), dtype="float32"), R.Tensor((384, 384, 1), dtype="float32"), R.Tensor((384,), dtype="float32"), R.Tensor((1, 384, 1), dtype="float32"), R.Tensor((384, 1, 1), dtype="float32"), R.Tensor((384, 384, 7), dtype="float32"), R.Tensor((384,), dtype="float32"), R.Tensor((1, 384, 1), dtype="float32"), R.Tensor((384, 1, 1), dtype="float32"), R.Tensor((384, 384, 1), dtype="float32"), R.Tensor((384,), dtype="float32"), R.Tensor((1, 384, 1), dtype="float32"), R.Tensor((384, 1, 1), dtype="float32"), R.Tensor((384, 192, 8), dtype="float32"), R.Tensor((192,), dtype="float32"), R.Tensor((1, 192, 1), dtype="float32"), R.Tensor((192, 1, 1), dtype="float32"), R.Tensor((192, 192, 7), dtype="float32"), R.Tensor((192,), dtype="float32"), R.Tensor((1, 192, 1), dtype="float32"), R.Tensor((192, 1, 1), dtype="float32"), R.Tensor((192, 192, 1), dtype="float32"), R.Tensor((192,), dtype="float32"), R.Tensor((1, 192, 1), dtype="float32"), R.Tensor((192, 1, 1), dtype="float32"), R.Tensor((192, 192, 7), dtype="float32"), R.Tensor((192,), dtype="float32"), R.Tensor((1, 192, 1), dtype="float32"), R.Tensor((192, 1, 1), dtype="float32"), R.Tensor((192, 192, 1), dtype="float32"), R.Tensor((192,), dtype="float32"), R.Tensor((1, 192, 1), dtype="float32"), R.Tensor((192, 1, 1), dtype="float32"), R.Tensor((192, 192, 7), dtype="float32"), R.Tensor((192,), dtype="float32"), R.Tensor((1, 192, 1), dtype="float32"), R.Tensor((192, 1, 1), dtype="float32"), R.Tensor((192, 192, 1), dtype="float32"), R.Tensor((192,), dtype="float32"), R.Tensor((1, 192, 1), dtype="float32"), R.Tensor((192, 1, 1), dtype="float32"), R.Tensor((192, 96, 4), dtype="float32"), R.Tensor((96,), dtype="float32"), R.Tensor((1, 96, 1), dtype="float32"), R.Tensor((96, 1, 1), dtype="float32"), R.Tensor((96, 96, 7), dtype="float32"), R.Tensor((96,), dtype="float32"), R.Tensor((1, 96, 1), dtype="float32"), R.Tensor((96, 1, 1), dtype="float32"), R.Tensor((96, 96, 1), dtype="float32"), R.Tensor((96,), dtype="float32"), R.Tensor((1, 96, 1), dtype="float32"), R.Tensor((96, 1, 1), dtype="float32"), R.Tensor((96, 96, 7), dtype="float32"), R.Tensor((96,), dtype="float32"), R.Tensor((1, 96, 1), dtype="float32"), R.Tensor((96, 1, 1), dtype="float32"), R.Tensor((96, 96, 1), dtype="float32"), R.Tensor((96,), dtype="float32"), R.Tensor((1, 96, 1), dtype="float32"), R.Tensor((96, 1, 1), dtype="float32"), R.Tensor((96, 96, 7), dtype="float32"), R.Tensor((96,), dtype="float32"), R.Tensor((1, 96, 1), dtype="float32"), R.Tensor((96, 1, 1), dtype="float32"), R.Tensor((96, 96, 1), dtype="float32"), R.Tensor((96,), dtype="float32"), R.Tensor((1, 96, 1), dtype="float32"), R.Tensor((1, 1, 1), dtype="float32"), R.Tensor((1, 96, 7), dtype="float32"), R.Tensor((1,), dtype="float32"))) -> R.Tuple(R.Tensor((1, 1, 512), dtype="float32"), R.Tuple(R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object)):
        R.func_attr({"num_input": 166})
        cls = Module
        with R.dataflow():
            encoder_block_layers_0_weight_g1: R.Tensor((64, 1, 1), dtype="float32") = packed_params[0]
            encoder_block_layers_0_weight_v1: R.Tensor((64, 1, 7), dtype="float32") = packed_params[1]
            encoder_block_layers_0_bias1: R.Tensor((64,), dtype="float32") = packed_params[2]
            encoder_block_layers_1_block_layers_0_block_branches_0_layers_0_alpha1: R.Tensor((1, 64, 1), dtype="float32") = packed_params[3]
            encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_weight_g1: R.Tensor((64, 1, 1), dtype="float32") = packed_params[4]
            encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_weight_v1: R.Tensor((64, 64, 7), dtype="float32") = packed_params[5]
            encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_bias1: R.Tensor((64,), dtype="float32") = packed_params[6]
            encoder_block_layers_1_block_layers_0_block_branches_0_layers_2_alpha1: R.Tensor((1, 64, 1), dtype="float32") = packed_params[7]
            encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_weight_g1: R.Tensor((64, 1, 1), dtype="float32") = packed_params[8]
            encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_weight_v1: R.Tensor((64, 64, 1), dtype="float32") = packed_params[9]
            encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_bias1: R.Tensor((64,), dtype="float32") = packed_params[10]
            encoder_block_layers_1_block_layers_1_block_branches_0_layers_0_alpha1: R.Tensor((1, 64, 1), dtype="float32") = packed_params[11]
            encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_weight_g1: R.Tensor((64, 1, 1), dtype="float32") = packed_params[12]
            encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_weight_v1: R.Tensor((64, 64, 7), dtype="float32") = packed_params[13]
            encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_bias1: R.Tensor((64,), dtype="float32") = packed_params[14]
            encoder_block_layers_1_block_layers_1_block_branches_0_layers_2_alpha1: R.Tensor((1, 64, 1), dtype="float32") = packed_params[15]
            encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_weight_g1: R.Tensor((64, 1, 1), dtype="float32") = packed_params[16]
            encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_weight_v1: R.Tensor((64, 64, 1), dtype="float32") = packed_params[17]
            encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_bias1: R.Tensor((64,), dtype="float32") = packed_params[18]
            encoder_block_layers_1_block_layers_2_block_branches_0_layers_0_alpha1: R.Tensor((1, 64, 1), dtype="float32") = packed_params[19]
            encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_weight_g1: R.Tensor((64, 1, 1), dtype="float32") = packed_params[20]
            encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_weight_v1: R.Tensor((64, 64, 7), dtype="float32") = packed_params[21]
            encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_bias1: R.Tensor((64,), dtype="float32") = packed_params[22]
            encoder_block_layers_1_block_layers_2_block_branches_0_layers_2_alpha1: R.Tensor((1, 64, 1), dtype="float32") = packed_params[23]
            encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_weight_g1: R.Tensor((64, 1, 1), dtype="float32") = packed_params[24]
            encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_weight_v1: R.Tensor((64, 64, 1), dtype="float32") = packed_params[25]
            encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_bias1: R.Tensor((64,), dtype="float32") = packed_params[26]
            encoder_block_layers_1_block_layers_3_alpha1: R.Tensor((1, 64, 1), dtype="float32") = packed_params[27]
            encoder_block_layers_1_block_layers_4_weight_g1: R.Tensor((128, 1, 1), dtype="float32") = packed_params[28]
            encoder_block_layers_1_block_layers_4_weight_v1: R.Tensor((128, 64, 4), dtype="float32") = packed_params[29]
            encoder_block_layers_1_block_layers_4_bias1: R.Tensor((128,), dtype="float32") = packed_params[30]
            encoder_block_layers_2_block_layers_0_block_branches_0_layers_0_alpha1: R.Tensor((1, 128, 1), dtype="float32") = packed_params[31]
            encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_weight_g1: R.Tensor((128, 1, 1), dtype="float32") = packed_params[32]
            encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_weight_v1: R.Tensor((128, 128, 7), dtype="float32") = packed_params[33]
            encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_bias1: R.Tensor((128,), dtype="float32") = packed_params[34]
            encoder_block_layers_2_block_layers_0_block_branches_0_layers_2_alpha1: R.Tensor((1, 128, 1), dtype="float32") = packed_params[35]
            encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_weight_g1: R.Tensor((128, 1, 1), dtype="float32") = packed_params[36]
            encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_weight_v1: R.Tensor((128, 128, 1), dtype="float32") = packed_params[37]
            encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_bias1: R.Tensor((128,), dtype="float32") = packed_params[38]
            encoder_block_layers_2_block_layers_1_block_branches_0_layers_0_alpha1: R.Tensor((1, 128, 1), dtype="float32") = packed_params[39]
            encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_weight_g1: R.Tensor((128, 1, 1), dtype="float32") = packed_params[40]
            encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_weight_v1: R.Tensor((128, 128, 7), dtype="float32") = packed_params[41]
            encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_bias1: R.Tensor((128,), dtype="float32") = packed_params[42]
            encoder_block_layers_2_block_layers_1_block_branches_0_layers_2_alpha1: R.Tensor((1, 128, 1), dtype="float32") = packed_params[43]
            encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_weight_g1: R.Tensor((128, 1, 1), dtype="float32") = packed_params[44]
            encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_weight_v1: R.Tensor((128, 128, 1), dtype="float32") = packed_params[45]
            encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_bias1: R.Tensor((128,), dtype="float32") = packed_params[46]
            encoder_block_layers_2_block_layers_2_block_branches_0_layers_0_alpha1: R.Tensor((1, 128, 1), dtype="float32") = packed_params[47]
            encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_weight_g1: R.Tensor((128, 1, 1), dtype="float32") = packed_params[48]
            encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_weight_v1: R.Tensor((128, 128, 7), dtype="float32") = packed_params[49]
            encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_bias1: R.Tensor((128,), dtype="float32") = packed_params[50]
            encoder_block_layers_2_block_layers_2_block_branches_0_layers_2_alpha1: R.Tensor((1, 128, 1), dtype="float32") = packed_params[51]
            encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_weight_g1: R.Tensor((128, 1, 1), dtype="float32") = packed_params[52]
            encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_weight_v1: R.Tensor((128, 128, 1), dtype="float32") = packed_params[53]
            encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_bias1: R.Tensor((128,), dtype="float32") = packed_params[54]
            encoder_block_layers_2_block_layers_3_alpha1: R.Tensor((1, 128, 1), dtype="float32") = packed_params[55]
            encoder_block_layers_2_block_layers_4_weight_g1: R.Tensor((256, 1, 1), dtype="float32") = packed_params[56]
            encoder_block_layers_2_block_layers_4_weight_v1: R.Tensor((256, 128, 8), dtype="float32") = packed_params[57]
            encoder_block_layers_2_block_layers_4_bias1: R.Tensor((256,), dtype="float32") = packed_params[58]
            encoder_block_layers_3_block_layers_0_block_branches_0_layers_0_alpha1: R.Tensor((1, 256, 1), dtype="float32") = packed_params[59]
            encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_weight_g1: R.Tensor((256, 1, 1), dtype="float32") = packed_params[60]
            encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_weight_v1: R.Tensor((256, 256, 7), dtype="float32") = packed_params[61]
            encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_bias1: R.Tensor((256,), dtype="float32") = packed_params[62]
            encoder_block_layers_3_block_layers_0_block_branches_0_layers_2_alpha1: R.Tensor((1, 256, 1), dtype="float32") = packed_params[63]
            encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_weight_g1: R.Tensor((256, 1, 1), dtype="float32") = packed_params[64]
            encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_weight_v1: R.Tensor((256, 256, 1), dtype="float32") = packed_params[65]
            encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_bias1: R.Tensor((256,), dtype="float32") = packed_params[66]
            encoder_block_layers_3_block_layers_1_block_branches_0_layers_0_alpha1: R.Tensor((1, 256, 1), dtype="float32") = packed_params[67]
            encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_weight_g1: R.Tensor((256, 1, 1), dtype="float32") = packed_params[68]
            encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_weight_v1: R.Tensor((256, 256, 7), dtype="float32") = packed_params[69]
            encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_bias1: R.Tensor((256,), dtype="float32") = packed_params[70]
            encoder_block_layers_3_block_layers_1_block_branches_0_layers_2_alpha1: R.Tensor((1, 256, 1), dtype="float32") = packed_params[71]
            encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_weight_g1: R.Tensor((256, 1, 1), dtype="float32") = packed_params[72]
            encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_weight_v1: R.Tensor((256, 256, 1), dtype="float32") = packed_params[73]
            encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_bias1: R.Tensor((256,), dtype="float32") = packed_params[74]
            encoder_block_layers_3_block_layers_2_block_branches_0_layers_0_alpha1: R.Tensor((1, 256, 1), dtype="float32") = packed_params[75]
            encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_weight_g1: R.Tensor((256, 1, 1), dtype="float32") = packed_params[76]
            encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_weight_v1: R.Tensor((256, 256, 7), dtype="float32") = packed_params[77]
            encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_bias1: R.Tensor((256,), dtype="float32") = packed_params[78]
            encoder_block_layers_3_block_layers_2_block_branches_0_layers_2_alpha1: R.Tensor((1, 256, 1), dtype="float32") = packed_params[79]
            encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_weight_g1: R.Tensor((256, 1, 1), dtype="float32") = packed_params[80]
            encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_weight_v1: R.Tensor((256, 256, 1), dtype="float32") = packed_params[81]
            encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_bias1: R.Tensor((256,), dtype="float32") = packed_params[82]
            encoder_block_layers_3_block_layers_3_alpha1: R.Tensor((1, 256, 1), dtype="float32") = packed_params[83]
            encoder_block_layers_3_block_layers_4_weight_g1: R.Tensor((512, 1, 1), dtype="float32") = packed_params[84]
            encoder_block_layers_3_block_layers_4_weight_v1: R.Tensor((512, 256, 16), dtype="float32") = packed_params[85]
            encoder_block_layers_3_block_layers_4_bias1: R.Tensor((512,), dtype="float32") = packed_params[86]
            encoder_block_layers_4_block_layers_0_block_branches_0_layers_0_alpha1: R.Tensor((1, 512, 1), dtype="float32") = packed_params[87]
            encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_weight_g1: R.Tensor((512, 1, 1), dtype="float32") = packed_params[88]
            encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_weight_v1: R.Tensor((512, 512, 7), dtype="float32") = packed_params[89]
            encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_bias1: R.Tensor((512,), dtype="float32") = packed_params[90]
            encoder_block_layers_4_block_layers_0_block_branches_0_layers_2_alpha1: R.Tensor((1, 512, 1), dtype="float32") = packed_params[91]
            encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_weight_g1: R.Tensor((512, 1, 1), dtype="float32") = packed_params[92]
            encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_weight_v1: R.Tensor((512, 512, 1), dtype="float32") = packed_params[93]
            encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_bias1: R.Tensor((512,), dtype="float32") = packed_params[94]
            encoder_block_layers_4_block_layers_1_block_branches_0_layers_0_alpha1: R.Tensor((1, 512, 1), dtype="float32") = packed_params[95]
            encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_weight_g1: R.Tensor((512, 1, 1), dtype="float32") = packed_params[96]
            encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_weight_v1: R.Tensor((512, 512, 7), dtype="float32") = packed_params[97]
            encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_bias1: R.Tensor((512,), dtype="float32") = packed_params[98]
            encoder_block_layers_4_block_layers_1_block_branches_0_layers_2_alpha1: R.Tensor((1, 512, 1), dtype="float32") = packed_params[99]
            encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_weight_g1: R.Tensor((512, 1, 1), dtype="float32") = packed_params[100]
            encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_weight_v1: R.Tensor((512, 512, 1), dtype="float32") = packed_params[101]
            encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_bias1: R.Tensor((512,), dtype="float32") = packed_params[102]
            encoder_block_layers_4_block_layers_2_block_branches_0_layers_0_alpha1: R.Tensor((1, 512, 1), dtype="float32") = packed_params[103]
            encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_weight_g1: R.Tensor((512, 1, 1), dtype="float32") = packed_params[104]
            encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_weight_v1: R.Tensor((512, 512, 7), dtype="float32") = packed_params[105]
            encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_bias1: R.Tensor((512,), dtype="float32") = packed_params[106]
            encoder_block_layers_4_block_layers_2_block_branches_0_layers_2_alpha1: R.Tensor((1, 512, 1), dtype="float32") = packed_params[107]
            encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_weight_g1: R.Tensor((512, 1, 1), dtype="float32") = packed_params[108]
            encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_weight_v1: R.Tensor((512, 512, 1), dtype="float32") = packed_params[109]
            encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_bias1: R.Tensor((512,), dtype="float32") = packed_params[110]
            encoder_block_layers_4_block_layers_3_alpha1: R.Tensor((1, 512, 1), dtype="float32") = packed_params[111]
            encoder_block_layers_4_block_layers_4_weight_g1: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[112]
            encoder_block_layers_4_block_layers_4_weight_v1: R.Tensor((1024, 512, 16), dtype="float32") = packed_params[113]
            encoder_block_layers_4_block_layers_4_bias1: R.Tensor((1024,), dtype="float32") = packed_params[114]
            encoder_block_layers_5_alpha1: R.Tensor((1, 1024, 1), dtype="float32") = packed_params[115]
            encoder_block_layers_6_weight_g1: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[116]
            encoder_block_layers_6_weight_v1: R.Tensor((1024, 1024, 3), dtype="float32") = packed_params[117]
            encoder_block_layers_6_bias1: R.Tensor((1024,), dtype="float32") = packed_params[118]
            quantizer_quantizers_0_in_proj_weight_g1: R.Tensor((8, 1, 1), dtype="float32") = packed_params[119]
            quantizer_quantizers_0_in_proj_weight_v1: R.Tensor((8, 1024, 1), dtype="float32") = packed_params[120]
            quantizer_quantizers_0_in_proj_bias1: R.Tensor((8,), dtype="float32") = packed_params[121]
            quantizer_quantizers_0_out_proj_weight_g1: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[122]
            quantizer_quantizers_0_out_proj_weight_v1: R.Tensor((1024, 8, 1), dtype="float32") = packed_params[123]
            quantizer_quantizers_0_out_proj_bias1: R.Tensor((1024,), dtype="float32") = packed_params[124]
            quantizer_quantizers_0_codebook_weight1: R.Tensor((1024, 8), dtype="float32") = packed_params[125]
            quantizer_quantizers_1_in_proj_weight_g1: R.Tensor((8, 1, 1), dtype="float32") = packed_params[126]
            quantizer_quantizers_1_in_proj_weight_v1: R.Tensor((8, 1024, 1), dtype="float32") = packed_params[127]
            quantizer_quantizers_1_in_proj_bias1: R.Tensor((8,), dtype="float32") = packed_params[128]
            quantizer_quantizers_1_out_proj_weight_g1: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[129]
            quantizer_quantizers_1_out_proj_weight_v1: R.Tensor((1024, 8, 1), dtype="float32") = packed_params[130]
            quantizer_quantizers_1_out_proj_bias1: R.Tensor((1024,), dtype="float32") = packed_params[131]
            quantizer_quantizers_1_codebook_weight1: R.Tensor((1024, 8), dtype="float32") = packed_params[132]
            quantizer_quantizers_2_in_proj_weight_g1: R.Tensor((8, 1, 1), dtype="float32") = packed_params[133]
            quantizer_quantizers_2_in_proj_weight_v1: R.Tensor((8, 1024, 1), dtype="float32") = packed_params[134]
            quantizer_quantizers_2_in_proj_bias1: R.Tensor((8,), dtype="float32") = packed_params[135]
            quantizer_quantizers_2_out_proj_weight_g1: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[136]
            quantizer_quantizers_2_out_proj_weight_v1: R.Tensor((1024, 8, 1), dtype="float32") = packed_params[137]
            quantizer_quantizers_2_out_proj_bias1: R.Tensor((1024,), dtype="float32") = packed_params[138]
            quantizer_quantizers_2_codebook_weight1: R.Tensor((1024, 8), dtype="float32") = packed_params[139]
            quantizer_quantizers_3_in_proj_weight_g1: R.Tensor((8, 1, 1), dtype="float32") = packed_params[140]
            quantizer_quantizers_3_in_proj_weight_v1: R.Tensor((8, 1024, 1), dtype="float32") = packed_params[141]
            quantizer_quantizers_3_in_proj_bias1: R.Tensor((8,), dtype="float32") = packed_params[142]
            quantizer_quantizers_3_out_proj_weight_g1: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[143]
            quantizer_quantizers_3_out_proj_weight_v1: R.Tensor((1024, 8, 1), dtype="float32") = packed_params[144]
            quantizer_quantizers_3_out_proj_bias1: R.Tensor((1024,), dtype="float32") = packed_params[145]
            quantizer_quantizers_3_codebook_weight1: R.Tensor((1024, 8), dtype="float32") = packed_params[146]
            quantizer_quantizers_4_in_proj_weight_g1: R.Tensor((8, 1, 1), dtype="float32") = packed_params[147]
            quantizer_quantizers_4_in_proj_weight_v1: R.Tensor((8, 1024, 1), dtype="float32") = packed_params[148]
            quantizer_quantizers_4_in_proj_bias1: R.Tensor((8,), dtype="float32") = packed_params[149]
            quantizer_quantizers_4_out_proj_weight_g1: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[150]
            quantizer_quantizers_4_out_proj_weight_v1: R.Tensor((1024, 8, 1), dtype="float32") = packed_params[151]
            quantizer_quantizers_4_out_proj_bias1: R.Tensor((1024,), dtype="float32") = packed_params[152]
            quantizer_quantizers_4_codebook_weight1: R.Tensor((1024, 8), dtype="float32") = packed_params[153]
            quantizer_quantizers_5_in_proj_weight_g1: R.Tensor((8, 1, 1), dtype="float32") = packed_params[154]
            quantizer_quantizers_5_in_proj_weight_v1: R.Tensor((8, 1024, 1), dtype="float32") = packed_params[155]
            quantizer_quantizers_5_in_proj_bias1: R.Tensor((8,), dtype="float32") = packed_params[156]
            quantizer_quantizers_5_out_proj_weight_g1: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[157]
            quantizer_quantizers_5_out_proj_weight_v1: R.Tensor((1024, 8, 1), dtype="float32") = packed_params[158]
            quantizer_quantizers_5_out_proj_bias1: R.Tensor((1024,), dtype="float32") = packed_params[159]
            quantizer_quantizers_5_codebook_weight1: R.Tensor((1024, 8), dtype="float32") = packed_params[160]
            quantizer_quantizers_6_in_proj_weight_g1: R.Tensor((8, 1, 1), dtype="float32") = packed_params[161]
            quantizer_quantizers_6_in_proj_weight_v1: R.Tensor((8, 1024, 1), dtype="float32") = packed_params[162]
            quantizer_quantizers_6_in_proj_bias1: R.Tensor((8,), dtype="float32") = packed_params[163]
            quantizer_quantizers_6_out_proj_weight_g1: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[164]
            quantizer_quantizers_6_out_proj_weight_v1: R.Tensor((1024, 8, 1), dtype="float32") = packed_params[165]
            quantizer_quantizers_6_out_proj_bias1: R.Tensor((1024,), dtype="float32") = packed_params[166]
            quantizer_quantizers_6_codebook_weight1: R.Tensor((1024, 8), dtype="float32") = packed_params[167]
            quantizer_quantizers_7_in_proj_weight_g1: R.Tensor((8, 1, 1), dtype="float32") = packed_params[168]
            quantizer_quantizers_7_in_proj_weight_v1: R.Tensor((8, 1024, 1), dtype="float32") = packed_params[169]
            quantizer_quantizers_7_in_proj_bias1: R.Tensor((8,), dtype="float32") = packed_params[170]
            quantizer_quantizers_7_out_proj_weight_g1: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[171]
            quantizer_quantizers_7_out_proj_weight_v1: R.Tensor((1024, 8, 1), dtype="float32") = packed_params[172]
            quantizer_quantizers_7_out_proj_bias1: R.Tensor((1024,), dtype="float32") = packed_params[173]
            quantizer_quantizers_7_codebook_weight1: R.Tensor((1024, 8), dtype="float32") = packed_params[174]
            quantizer_quantizers_8_in_proj_weight_g1: R.Tensor((8, 1, 1), dtype="float32") = packed_params[175]
            quantizer_quantizers_8_in_proj_weight_v1: R.Tensor((8, 1024, 1), dtype="float32") = packed_params[176]
            quantizer_quantizers_8_in_proj_bias1: R.Tensor((8,), dtype="float32") = packed_params[177]
            quantizer_quantizers_8_out_proj_weight_g1: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[178]
            quantizer_quantizers_8_out_proj_weight_v1: R.Tensor((1024, 8, 1), dtype="float32") = packed_params[179]
            quantizer_quantizers_8_out_proj_bias1: R.Tensor((1024,), dtype="float32") = packed_params[180]
            quantizer_quantizers_8_codebook_weight1: R.Tensor((1024, 8), dtype="float32") = packed_params[181]
            decoder_model_layers_0_weight_g1: R.Tensor((1536, 1, 1), dtype="float32") = packed_params[182]
            decoder_model_layers_0_weight_v1: R.Tensor((1536, 1024, 7), dtype="float32") = packed_params[183]
            decoder_model_layers_0_bias1: R.Tensor((1536,), dtype="float32") = packed_params[184]
            decoder_model_layers_1_block_layers_0_alpha1: R.Tensor((1, 1536, 1), dtype="float32") = packed_params[185]
            decoder_model_layers_1_block_layers_1_weight_g1: R.Tensor((1536, 1, 1), dtype="float32") = packed_params[186]
            decoder_model_layers_1_block_layers_1_weight_v1: R.Tensor((1536, 768, 16), dtype="float32") = packed_params[187]
            decoder_model_layers_1_block_layers_1_bias1: R.Tensor((768,), dtype="float32") = packed_params[188]
            decoder_model_layers_1_block_layers_2_block_branches_0_layers_0_alpha1: R.Tensor((1, 768, 1), dtype="float32") = packed_params[189]
            decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_weight_g1: R.Tensor((768, 1, 1), dtype="float32") = packed_params[190]
            decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_weight_v1: R.Tensor((768, 768, 7), dtype="float32") = packed_params[191]
            decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_bias1: R.Tensor((768,), dtype="float32") = packed_params[192]
            decoder_model_layers_1_block_layers_2_block_branches_0_layers_2_alpha1: R.Tensor((1, 768, 1), dtype="float32") = packed_params[193]
            decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_weight_g1: R.Tensor((768, 1, 1), dtype="float32") = packed_params[194]
            decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_weight_v1: R.Tensor((768, 768, 1), dtype="float32") = packed_params[195]
            decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_bias1: R.Tensor((768,), dtype="float32") = packed_params[196]
            decoder_model_layers_1_block_layers_3_block_branches_0_layers_0_alpha1: R.Tensor((1, 768, 1), dtype="float32") = packed_params[197]
            decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_weight_g1: R.Tensor((768, 1, 1), dtype="float32") = packed_params[198]
            decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_weight_v1: R.Tensor((768, 768, 7), dtype="float32") = packed_params[199]
            decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_bias1: R.Tensor((768,), dtype="float32") = packed_params[200]
            decoder_model_layers_1_block_layers_3_block_branches_0_layers_2_alpha1: R.Tensor((1, 768, 1), dtype="float32") = packed_params[201]
            decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_weight_g1: R.Tensor((768, 1, 1), dtype="float32") = packed_params[202]
            decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_weight_v1: R.Tensor((768, 768, 1), dtype="float32") = packed_params[203]
            decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_bias1: R.Tensor((768,), dtype="float32") = packed_params[204]
            decoder_model_layers_1_block_layers_4_block_branches_0_layers_0_alpha1: R.Tensor((1, 768, 1), dtype="float32") = packed_params[205]
            decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_weight_g1: R.Tensor((768, 1, 1), dtype="float32") = packed_params[206]
            decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_weight_v1: R.Tensor((768, 768, 7), dtype="float32") = packed_params[207]
            decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_bias1: R.Tensor((768,), dtype="float32") = packed_params[208]
            decoder_model_layers_1_block_layers_4_block_branches_0_layers_2_alpha1: R.Tensor((1, 768, 1), dtype="float32") = packed_params[209]
            decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_weight_g1: R.Tensor((768, 1, 1), dtype="float32") = packed_params[210]
            decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_weight_v1: R.Tensor((768, 768, 1), dtype="float32") = packed_params[211]
            decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_bias1: R.Tensor((768,), dtype="float32") = packed_params[212]
            decoder_model_layers_2_block_layers_0_alpha1: R.Tensor((1, 768, 1), dtype="float32") = packed_params[213]
            decoder_model_layers_2_block_layers_1_weight_g1: R.Tensor((768, 1, 1), dtype="float32") = packed_params[214]
            decoder_model_layers_2_block_layers_1_weight_v1: R.Tensor((768, 384, 16), dtype="float32") = packed_params[215]
            decoder_model_layers_2_block_layers_1_bias1: R.Tensor((384,), dtype="float32") = packed_params[216]
            decoder_model_layers_2_block_layers_2_block_branches_0_layers_0_alpha1: R.Tensor((1, 384, 1), dtype="float32") = packed_params[217]
            decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_weight_g1: R.Tensor((384, 1, 1), dtype="float32") = packed_params[218]
            decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_weight_v1: R.Tensor((384, 384, 7), dtype="float32") = packed_params[219]
            decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_bias1: R.Tensor((384,), dtype="float32") = packed_params[220]
            decoder_model_layers_2_block_layers_2_block_branches_0_layers_2_alpha1: R.Tensor((1, 384, 1), dtype="float32") = packed_params[221]
            decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_weight_g1: R.Tensor((384, 1, 1), dtype="float32") = packed_params[222]
            decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_weight_v1: R.Tensor((384, 384, 1), dtype="float32") = packed_params[223]
            decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_bias1: R.Tensor((384,), dtype="float32") = packed_params[224]
            decoder_model_layers_2_block_layers_3_block_branches_0_layers_0_alpha1: R.Tensor((1, 384, 1), dtype="float32") = packed_params[225]
            decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_weight_g1: R.Tensor((384, 1, 1), dtype="float32") = packed_params[226]
            decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_weight_v1: R.Tensor((384, 384, 7), dtype="float32") = packed_params[227]
            decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_bias1: R.Tensor((384,), dtype="float32") = packed_params[228]
            decoder_model_layers_2_block_layers_3_block_branches_0_layers_2_alpha1: R.Tensor((1, 384, 1), dtype="float32") = packed_params[229]
            decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_weight_g1: R.Tensor((384, 1, 1), dtype="float32") = packed_params[230]
            decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_weight_v1: R.Tensor((384, 384, 1), dtype="float32") = packed_params[231]
            decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_bias1: R.Tensor((384,), dtype="float32") = packed_params[232]
            decoder_model_layers_2_block_layers_4_block_branches_0_layers_0_alpha1: R.Tensor((1, 384, 1), dtype="float32") = packed_params[233]
            decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_weight_g1: R.Tensor((384, 1, 1), dtype="float32") = packed_params[234]
            decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_weight_v1: R.Tensor((384, 384, 7), dtype="float32") = packed_params[235]
            decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_bias1: R.Tensor((384,), dtype="float32") = packed_params[236]
            decoder_model_layers_2_block_layers_4_block_branches_0_layers_2_alpha1: R.Tensor((1, 384, 1), dtype="float32") = packed_params[237]
            decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_weight_g1: R.Tensor((384, 1, 1), dtype="float32") = packed_params[238]
            decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_weight_v1: R.Tensor((384, 384, 1), dtype="float32") = packed_params[239]
            decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_bias1: R.Tensor((384,), dtype="float32") = packed_params[240]
            decoder_model_layers_3_block_layers_0_alpha1: R.Tensor((1, 384, 1), dtype="float32") = packed_params[241]
            decoder_model_layers_3_block_layers_1_weight_g1: R.Tensor((384, 1, 1), dtype="float32") = packed_params[242]
            decoder_model_layers_3_block_layers_1_weight_v1: R.Tensor((384, 192, 8), dtype="float32") = packed_params[243]
            decoder_model_layers_3_block_layers_1_bias1: R.Tensor((192,), dtype="float32") = packed_params[244]
            decoder_model_layers_3_block_layers_2_block_branches_0_layers_0_alpha1: R.Tensor((1, 192, 1), dtype="float32") = packed_params[245]
            decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_weight_g1: R.Tensor((192, 1, 1), dtype="float32") = packed_params[246]
            decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_weight_v1: R.Tensor((192, 192, 7), dtype="float32") = packed_params[247]
            decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_bias1: R.Tensor((192,), dtype="float32") = packed_params[248]
            decoder_model_layers_3_block_layers_2_block_branches_0_layers_2_alpha1: R.Tensor((1, 192, 1), dtype="float32") = packed_params[249]
            decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_weight_g1: R.Tensor((192, 1, 1), dtype="float32") = packed_params[250]
            decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_weight_v1: R.Tensor((192, 192, 1), dtype="float32") = packed_params[251]
            decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_bias1: R.Tensor((192,), dtype="float32") = packed_params[252]
            decoder_model_layers_3_block_layers_3_block_branches_0_layers_0_alpha1: R.Tensor((1, 192, 1), dtype="float32") = packed_params[253]
            decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_weight_g1: R.Tensor((192, 1, 1), dtype="float32") = packed_params[254]
            decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_weight_v1: R.Tensor((192, 192, 7), dtype="float32") = packed_params[255]
            decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_bias1: R.Tensor((192,), dtype="float32") = packed_params[256]
            decoder_model_layers_3_block_layers_3_block_branches_0_layers_2_alpha1: R.Tensor((1, 192, 1), dtype="float32") = packed_params[257]
            decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_weight_g1: R.Tensor((192, 1, 1), dtype="float32") = packed_params[258]
            decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_weight_v1: R.Tensor((192, 192, 1), dtype="float32") = packed_params[259]
            decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_bias1: R.Tensor((192,), dtype="float32") = packed_params[260]
            decoder_model_layers_3_block_layers_4_block_branches_0_layers_0_alpha1: R.Tensor((1, 192, 1), dtype="float32") = packed_params[261]
            decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_weight_g1: R.Tensor((192, 1, 1), dtype="float32") = packed_params[262]
            decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_weight_v1: R.Tensor((192, 192, 7), dtype="float32") = packed_params[263]
            decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_bias1: R.Tensor((192,), dtype="float32") = packed_params[264]
            decoder_model_layers_3_block_layers_4_block_branches_0_layers_2_alpha1: R.Tensor((1, 192, 1), dtype="float32") = packed_params[265]
            decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_weight_g1: R.Tensor((192, 1, 1), dtype="float32") = packed_params[266]
            decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_weight_v1: R.Tensor((192, 192, 1), dtype="float32") = packed_params[267]
            decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_bias1: R.Tensor((192,), dtype="float32") = packed_params[268]
            decoder_model_layers_4_block_layers_0_alpha1: R.Tensor((1, 192, 1), dtype="float32") = packed_params[269]
            decoder_model_layers_4_block_layers_1_weight_g1: R.Tensor((192, 1, 1), dtype="float32") = packed_params[270]
            decoder_model_layers_4_block_layers_1_weight_v1: R.Tensor((192, 96, 4), dtype="float32") = packed_params[271]
            decoder_model_layers_4_block_layers_1_bias1: R.Tensor((96,), dtype="float32") = packed_params[272]
            decoder_model_layers_4_block_layers_2_block_branches_0_layers_0_alpha1: R.Tensor((1, 96, 1), dtype="float32") = packed_params[273]
            decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_weight_g1: R.Tensor((96, 1, 1), dtype="float32") = packed_params[274]
            decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_weight_v1: R.Tensor((96, 96, 7), dtype="float32") = packed_params[275]
            decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_bias1: R.Tensor((96,), dtype="float32") = packed_params[276]
            decoder_model_layers_4_block_layers_2_block_branches_0_layers_2_alpha1: R.Tensor((1, 96, 1), dtype="float32") = packed_params[277]
            decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_weight_g1: R.Tensor((96, 1, 1), dtype="float32") = packed_params[278]
            decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_weight_v1: R.Tensor((96, 96, 1), dtype="float32") = packed_params[279]
            decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_bias1: R.Tensor((96,), dtype="float32") = packed_params[280]
            decoder_model_layers_4_block_layers_3_block_branches_0_layers_0_alpha1: R.Tensor((1, 96, 1), dtype="float32") = packed_params[281]
            decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_weight_g1: R.Tensor((96, 1, 1), dtype="float32") = packed_params[282]
            decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_weight_v1: R.Tensor((96, 96, 7), dtype="float32") = packed_params[283]
            decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_bias1: R.Tensor((96,), dtype="float32") = packed_params[284]
            decoder_model_layers_4_block_layers_3_block_branches_0_layers_2_alpha1: R.Tensor((1, 96, 1), dtype="float32") = packed_params[285]
            decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_weight_g1: R.Tensor((96, 1, 1), dtype="float32") = packed_params[286]
            decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_weight_v1: R.Tensor((96, 96, 1), dtype="float32") = packed_params[287]
            decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_bias1: R.Tensor((96,), dtype="float32") = packed_params[288]
            decoder_model_layers_4_block_layers_4_block_branches_0_layers_0_alpha1: R.Tensor((1, 96, 1), dtype="float32") = packed_params[289]
            decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_weight_g1: R.Tensor((96, 1, 1), dtype="float32") = packed_params[290]
            decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_weight_v1: R.Tensor((96, 96, 7), dtype="float32") = packed_params[291]
            decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_bias1: R.Tensor((96,), dtype="float32") = packed_params[292]
            decoder_model_layers_4_block_layers_4_block_branches_0_layers_2_alpha1: R.Tensor((1, 96, 1), dtype="float32") = packed_params[293]
            decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_weight_g1: R.Tensor((96, 1, 1), dtype="float32") = packed_params[294]
            decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_weight_v1: R.Tensor((96, 96, 1), dtype="float32") = packed_params[295]
            decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_bias1: R.Tensor((96,), dtype="float32") = packed_params[296]
            decoder_model_layers_5_alpha1: R.Tensor((1, 96, 1), dtype="float32") = packed_params[297]
            decoder_model_layers_6_weight_g1: R.Tensor((1, 1, 1), dtype="float32") = packed_params[298]
            decoder_model_layers_6_weight_v1: R.Tensor((1, 96, 7), dtype="float32") = packed_params[299]
            decoder_model_layers_6_bias1: R.Tensor((1,), dtype="float32") = packed_params[300]
            lv402: R.Tensor((1, 1024, 1), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_0_downsampling_delay_cache, z, sinfo_args=(R.Tensor((1, 1024, 1), dtype="float32"),))
            lv403: R.Tensor((1, 1024, 7), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_0_cache_cache, lv402, sinfo_args=(R.Tensor((1, 1024, 7), dtype="float32"),))
            lv404: R.Tensor((1536, 1024, 7), dtype="float32") = R.square(decoder_model_layers_0_weight_v1)
            lv405: R.Tensor((1536, 1, 1), dtype="float32") = R.sum(lv404, axis=[1, 2], keepdims=True)
            lv406: R.Tensor((1536, 1, 1), dtype="float32") = R.sqrt(lv405)
            lv407: R.Tensor((1536, 1024, 7), dtype="float32") = R.divide(decoder_model_layers_0_weight_v1, lv406)
            wnconv1d48: R.Tensor((1536, 1024, 7), dtype="float32") = R.multiply(decoder_model_layers_0_weight_g1, lv407)
            lv408: R.Tensor((1, 1536, 1), dtype="float32") = R.nn.conv1d(lv403, wnconv1d48, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv409: R.Tensor((1, 1536, 1), dtype="float32") = R.reshape(decoder_model_layers_0_bias1, R.shape([1, 1536, 1]))
            conv1d48: R.Tensor((1, 1536, 1), dtype="float32") = R.add(lv408, lv409)
            reshape94: R.Tensor((1, 1536, 1), dtype="float32") = R.reshape(conv1d48, R.shape([1, 1536, 1]))
            lv410 = R.call_tir(cls.snake5, (reshape94, decoder_model_layers_1_block_layers_0_alpha1), out_sinfo=R.Tensor((1, 1536, 1), dtype="float32"))
            reshape95: R.Tensor((1, 1536, 1), dtype="float32") = R.reshape(lv410, R.shape([1, 1536, 1]))
            lv411: R.Tensor((1536, 768, 16), dtype="float32") = R.square(decoder_model_layers_1_block_layers_1_weight_v1)
            lv412: R.Tensor((1536, 1, 1), dtype="float32") = R.sum(lv411, axis=[1, 2], keepdims=True)
            lv413: R.Tensor((1536, 1, 1), dtype="float32") = R.sqrt(lv412)
            lv414: R.Tensor((1536, 768, 16), dtype="float32") = R.divide(decoder_model_layers_1_block_layers_1_weight_v1, lv413)
            wnconvtranspose1d: R.Tensor((1536, 768, 16), dtype="float32") = R.multiply(decoder_model_layers_1_block_layers_1_weight_g1, lv414)
            conv1d_transpose: R.Tensor((1, 768, 16), dtype="float32") = R.nn.conv1d_transpose(reshape95, wnconvtranspose1d, strides=[8], padding=[0, 0], output_padding=[0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="IOW", out_layout="NCW", out_dtype="void")
            lv415: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_1_cache_cache, conv1d_transpose, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            unsqueeze: R.Tensor((768, 1), dtype="float32") = R.expand_dims(decoder_model_layers_1_block_layers_1_bias1, axis=[-1])
            add42: R.Tensor((1, 768, 8), dtype="float32") = R.add(lv415, unsqueeze)
            lv416: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_2_block_paddings_0_cache, add42, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            reshape96: R.Tensor((1, 768, 8), dtype="float32") = R.reshape(lv416, R.shape([1, 768, 8]))
            lv417 = R.call_tir(cls.snake6, (reshape96, decoder_model_layers_1_block_layers_2_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 768, 8), dtype="float32"))
            reshape97: R.Tensor((1, 768, 8), dtype="float32") = R.reshape(lv417, R.shape([1, 768, 8]))
            lv418: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, reshape97, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv419: R.Tensor((1, 768, 14), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache, lv418, sinfo_args=(R.Tensor((1, 768, 14), dtype="float32"),))
            lv420: R.Tensor((768, 768, 7), dtype="float32") = R.square(decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_weight_v1)
            lv421: R.Tensor((768, 1, 1), dtype="float32") = R.sum(lv420, axis=[1, 2], keepdims=True)
            lv422: R.Tensor((768, 1, 1), dtype="float32") = R.sqrt(lv421)
            lv423: R.Tensor((768, 768, 7), dtype="float32") = R.divide(decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_weight_v1, lv422)
            wnconv1d49: R.Tensor((768, 768, 7), dtype="float32") = R.multiply(decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_weight_g1, lv423)
            lv424: R.Tensor((1, 768, 8), dtype="float32") = R.nn.conv1d(lv419, wnconv1d49, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv425: R.Tensor((1, 768, 1), dtype="float32") = R.reshape(decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_bias1, R.shape([1, 768, 1]))
            conv1d49: R.Tensor((1, 768, 8), dtype="float32") = R.add(lv424, lv425)
            reshape98: R.Tensor((1, 768, 8), dtype="float32") = R.reshape(conv1d49, R.shape([1, 768, 8]))
            lv426 = R.call_tir(cls.snake6, (reshape98, decoder_model_layers_1_block_layers_2_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 768, 8), dtype="float32"))
            reshape99: R.Tensor((1, 768, 8), dtype="float32") = R.reshape(lv426, R.shape([1, 768, 8]))
            lv427: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, reshape99, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv428: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache, lv427, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv429: R.Tensor((768, 768, 1), dtype="float32") = R.square(decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_weight_v1)
            lv430: R.Tensor((768, 1, 1), dtype="float32") = R.sum(lv429, axis=[1, 2], keepdims=True)
            lv431: R.Tensor((768, 1, 1), dtype="float32") = R.sqrt(lv430)
            lv432: R.Tensor((768, 768, 1), dtype="float32") = R.divide(decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_weight_v1, lv431)
            wnconv1d50: R.Tensor((768, 768, 1), dtype="float32") = R.multiply(decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_weight_g1, lv432)
            lv433: R.Tensor((1, 768, 8), dtype="float32") = R.nn.conv1d(lv428, wnconv1d50, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv434: R.Tensor((1, 768, 1), dtype="float32") = R.reshape(decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_bias1, R.shape([1, 768, 1]))
            conv1d50: R.Tensor((1, 768, 8), dtype="float32") = R.add(lv433, lv434)
            lv435: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_2_block_paddings_1_cache, add42, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            add43: R.Tensor((1, 768, 8), dtype="float32") = R.add(conv1d50, R.const(0.0, "float32"))
            add44: R.Tensor((1, 768, 8), dtype="float32") = R.add(add43, lv435)
            lv436: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_3_block_paddings_0_cache, add44, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            reshape100: R.Tensor((1, 768, 8), dtype="float32") = R.reshape(lv436, R.shape([1, 768, 8]))
            lv437 = R.call_tir(cls.snake6, (reshape100, decoder_model_layers_1_block_layers_3_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 768, 8), dtype="float32"))
            reshape101: R.Tensor((1, 768, 8), dtype="float32") = R.reshape(lv437, R.shape([1, 768, 8]))
            lv438: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, reshape101, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv439: R.Tensor((1, 768, 26), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_cache_cache, lv438, sinfo_args=(R.Tensor((1, 768, 26), dtype="float32"),))
            lv440: R.Tensor((768, 768, 7), dtype="float32") = R.square(decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_weight_v1)
            lv441: R.Tensor((768, 1, 1), dtype="float32") = R.sum(lv440, axis=[1, 2], keepdims=True)
            lv442: R.Tensor((768, 1, 1), dtype="float32") = R.sqrt(lv441)
            lv443: R.Tensor((768, 768, 7), dtype="float32") = R.divide(decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_weight_v1, lv442)
            wnconv1d51: R.Tensor((768, 768, 7), dtype="float32") = R.multiply(decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_weight_g1, lv443)
            lv444: R.Tensor((1, 768, 8), dtype="float32") = R.nn.conv1d(lv439, wnconv1d51, strides=[1], padding=[0, 0], dilation=[3], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv445: R.Tensor((1, 768, 1), dtype="float32") = R.reshape(decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_bias1, R.shape([1, 768, 1]))
            conv1d51: R.Tensor((1, 768, 8), dtype="float32") = R.add(lv444, lv445)
            reshape102: R.Tensor((1, 768, 8), dtype="float32") = R.reshape(conv1d51, R.shape([1, 768, 8]))
            lv446 = R.call_tir(cls.snake6, (reshape102, decoder_model_layers_1_block_layers_3_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 768, 8), dtype="float32"))
            reshape103: R.Tensor((1, 768, 8), dtype="float32") = R.reshape(lv446, R.shape([1, 768, 8]))
            lv447: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, reshape103, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv448: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_cache_cache, lv447, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv449: R.Tensor((768, 768, 1), dtype="float32") = R.square(decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_weight_v1)
            lv450: R.Tensor((768, 1, 1), dtype="float32") = R.sum(lv449, axis=[1, 2], keepdims=True)
            lv451: R.Tensor((768, 1, 1), dtype="float32") = R.sqrt(lv450)
            lv452: R.Tensor((768, 768, 1), dtype="float32") = R.divide(decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_weight_v1, lv451)
            wnconv1d52: R.Tensor((768, 768, 1), dtype="float32") = R.multiply(decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_weight_g1, lv452)
            lv453: R.Tensor((1, 768, 8), dtype="float32") = R.nn.conv1d(lv448, wnconv1d52, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv454: R.Tensor((1, 768, 1), dtype="float32") = R.reshape(decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_bias1, R.shape([1, 768, 1]))
            conv1d52: R.Tensor((1, 768, 8), dtype="float32") = R.add(lv453, lv454)
            lv455: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_3_block_paddings_1_cache, add44, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            add45: R.Tensor((1, 768, 8), dtype="float32") = R.add(conv1d52, R.const(0.0, "float32"))
            add46: R.Tensor((1, 768, 8), dtype="float32") = R.add(add45, lv455)
            lv456: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_4_block_paddings_0_cache, add46, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            reshape104: R.Tensor((1, 768, 8), dtype="float32") = R.reshape(lv456, R.shape([1, 768, 8]))
            lv457 = R.call_tir(cls.snake6, (reshape104, decoder_model_layers_1_block_layers_4_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 768, 8), dtype="float32"))
            reshape105: R.Tensor((1, 768, 8), dtype="float32") = R.reshape(lv457, R.shape([1, 768, 8]))
            lv458: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, reshape105, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv459: R.Tensor((1, 768, 62), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_cache_cache, lv458, sinfo_args=(R.Tensor((1, 768, 62), dtype="float32"),))
            lv460: R.Tensor((768, 768, 7), dtype="float32") = R.square(decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_weight_v1)
            lv461: R.Tensor((768, 1, 1), dtype="float32") = R.sum(lv460, axis=[1, 2], keepdims=True)
            lv462: R.Tensor((768, 1, 1), dtype="float32") = R.sqrt(lv461)
            lv463: R.Tensor((768, 768, 7), dtype="float32") = R.divide(decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_weight_v1, lv462)
            wnconv1d53: R.Tensor((768, 768, 7), dtype="float32") = R.multiply(decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_weight_g1, lv463)
            lv464: R.Tensor((1, 768, 8), dtype="float32") = R.nn.conv1d(lv459, wnconv1d53, strides=[1], padding=[0, 0], dilation=[9], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv465: R.Tensor((1, 768, 1), dtype="float32") = R.reshape(decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_bias1, R.shape([1, 768, 1]))
            conv1d53: R.Tensor((1, 768, 8), dtype="float32") = R.add(lv464, lv465)
            reshape106: R.Tensor((1, 768, 8), dtype="float32") = R.reshape(conv1d53, R.shape([1, 768, 8]))
            lv466 = R.call_tir(cls.snake6, (reshape106, decoder_model_layers_1_block_layers_4_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 768, 8), dtype="float32"))
            reshape107: R.Tensor((1, 768, 8), dtype="float32") = R.reshape(lv466, R.shape([1, 768, 8]))
            lv467: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, reshape107, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv468: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_cache_cache, lv467, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv469: R.Tensor((768, 768, 1), dtype="float32") = R.square(decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_weight_v1)
            lv470: R.Tensor((768, 1, 1), dtype="float32") = R.sum(lv469, axis=[1, 2], keepdims=True)
            lv471: R.Tensor((768, 1, 1), dtype="float32") = R.sqrt(lv470)
            lv472: R.Tensor((768, 768, 1), dtype="float32") = R.divide(decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_weight_v1, lv471)
            wnconv1d54: R.Tensor((768, 768, 1), dtype="float32") = R.multiply(decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_weight_g1, lv472)
            lv473: R.Tensor((1, 768, 8), dtype="float32") = R.nn.conv1d(lv468, wnconv1d54, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv474: R.Tensor((1, 768, 1), dtype="float32") = R.reshape(decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_bias1, R.shape([1, 768, 1]))
            conv1d54: R.Tensor((1, 768, 8), dtype="float32") = R.add(lv473, lv474)
            lv475: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_4_block_paddings_1_cache, add46, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            add47: R.Tensor((1, 768, 8), dtype="float32") = R.add(conv1d54, R.const(0.0, "float32"))
            add48: R.Tensor((1, 768, 8), dtype="float32") = R.add(add47, lv475)
            reshape108: R.Tensor((1, 768, 8), dtype="float32") = R.reshape(add48, R.shape([1, 768, 8]))
            lv476 = R.call_tir(cls.snake6, (reshape108, decoder_model_layers_2_block_layers_0_alpha1), out_sinfo=R.Tensor((1, 768, 8), dtype="float32"))
            reshape109: R.Tensor((1, 768, 8), dtype="float32") = R.reshape(lv476, R.shape([1, 768, 8]))
            lv477: R.Tensor((768, 384, 16), dtype="float32") = R.square(decoder_model_layers_2_block_layers_1_weight_v1)
            lv478: R.Tensor((768, 1, 1), dtype="float32") = R.sum(lv477, axis=[1, 2], keepdims=True)
            lv479: R.Tensor((768, 1, 1), dtype="float32") = R.sqrt(lv478)
            lv480: R.Tensor((768, 384, 16), dtype="float32") = R.divide(decoder_model_layers_2_block_layers_1_weight_v1, lv479)
            wnconvtranspose1d1: R.Tensor((768, 384, 16), dtype="float32") = R.multiply(decoder_model_layers_2_block_layers_1_weight_g1, lv480)
            conv1d_transpose1: R.Tensor((1, 384, 72), dtype="float32") = R.nn.conv1d_transpose(reshape109, wnconvtranspose1d1, strides=[8], padding=[0, 0], output_padding=[0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="IOW", out_layout="NCW", out_dtype="void")
            lv481: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_1_cache_cache, conv1d_transpose1, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            unsqueeze1: R.Tensor((384, 1), dtype="float32") = R.expand_dims(decoder_model_layers_2_block_layers_1_bias1, axis=[-1])
            add49: R.Tensor((1, 384, 64), dtype="float32") = R.add(lv481, unsqueeze1)
            lv482: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_2_block_paddings_0_cache, add49, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            reshape110: R.Tensor((1, 384, 64), dtype="float32") = R.reshape(lv482, R.shape([1, 384, 64]))
            lv483 = R.call_tir(cls.snake7, (reshape110, decoder_model_layers_2_block_layers_2_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 384, 64), dtype="float32"))
            reshape111: R.Tensor((1, 384, 64), dtype="float32") = R.reshape(lv483, R.shape([1, 384, 64]))
            lv484: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, reshape111, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv485: R.Tensor((1, 384, 70), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache, lv484, sinfo_args=(R.Tensor((1, 384, 70), dtype="float32"),))
            lv486: R.Tensor((384, 384, 7), dtype="float32") = R.square(decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_weight_v1)
            lv487: R.Tensor((384, 1, 1), dtype="float32") = R.sum(lv486, axis=[1, 2], keepdims=True)
            lv488: R.Tensor((384, 1, 1), dtype="float32") = R.sqrt(lv487)
            lv489: R.Tensor((384, 384, 7), dtype="float32") = R.divide(decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_weight_v1, lv488)
            wnconv1d55: R.Tensor((384, 384, 7), dtype="float32") = R.multiply(decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_weight_g1, lv489)
            lv490: R.Tensor((1, 384, 64), dtype="float32") = R.nn.conv1d(lv485, wnconv1d55, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv491: R.Tensor((1, 384, 1), dtype="float32") = R.reshape(decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_bias1, R.shape([1, 384, 1]))
            conv1d55: R.Tensor((1, 384, 64), dtype="float32") = R.add(lv490, lv491)
            reshape112: R.Tensor((1, 384, 64), dtype="float32") = R.reshape(conv1d55, R.shape([1, 384, 64]))
            lv492 = R.call_tir(cls.snake7, (reshape112, decoder_model_layers_2_block_layers_2_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 384, 64), dtype="float32"))
            reshape113: R.Tensor((1, 384, 64), dtype="float32") = R.reshape(lv492, R.shape([1, 384, 64]))
            lv493: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, reshape113, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv494: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache, lv493, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv495: R.Tensor((384, 384, 1), dtype="float32") = R.square(decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_weight_v1)
            lv496: R.Tensor((384, 1, 1), dtype="float32") = R.sum(lv495, axis=[1, 2], keepdims=True)
            lv497: R.Tensor((384, 1, 1), dtype="float32") = R.sqrt(lv496)
            lv498: R.Tensor((384, 384, 1), dtype="float32") = R.divide(decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_weight_v1, lv497)
            wnconv1d56: R.Tensor((384, 384, 1), dtype="float32") = R.multiply(decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_weight_g1, lv498)
            lv499: R.Tensor((1, 384, 64), dtype="float32") = R.nn.conv1d(lv494, wnconv1d56, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv500: R.Tensor((1, 384, 1), dtype="float32") = R.reshape(decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_bias1, R.shape([1, 384, 1]))
            conv1d56: R.Tensor((1, 384, 64), dtype="float32") = R.add(lv499, lv500)
            lv501: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_2_block_paddings_1_cache, add49, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            add50: R.Tensor((1, 384, 64), dtype="float32") = R.add(conv1d56, R.const(0.0, "float32"))
            add51: R.Tensor((1, 384, 64), dtype="float32") = R.add(add50, lv501)
            lv502: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_3_block_paddings_0_cache, add51, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            reshape114: R.Tensor((1, 384, 64), dtype="float32") = R.reshape(lv502, R.shape([1, 384, 64]))
            lv503 = R.call_tir(cls.snake7, (reshape114, decoder_model_layers_2_block_layers_3_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 384, 64), dtype="float32"))
            reshape115: R.Tensor((1, 384, 64), dtype="float32") = R.reshape(lv503, R.shape([1, 384, 64]))
            lv504: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, reshape115, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv505: R.Tensor((1, 384, 82), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_cache_cache, lv504, sinfo_args=(R.Tensor((1, 384, 82), dtype="float32"),))
            lv506: R.Tensor((384, 384, 7), dtype="float32") = R.square(decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_weight_v1)
            lv507: R.Tensor((384, 1, 1), dtype="float32") = R.sum(lv506, axis=[1, 2], keepdims=True)
            lv508: R.Tensor((384, 1, 1), dtype="float32") = R.sqrt(lv507)
            lv509: R.Tensor((384, 384, 7), dtype="float32") = R.divide(decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_weight_v1, lv508)
            wnconv1d57: R.Tensor((384, 384, 7), dtype="float32") = R.multiply(decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_weight_g1, lv509)
            lv510: R.Tensor((1, 384, 64), dtype="float32") = R.nn.conv1d(lv505, wnconv1d57, strides=[1], padding=[0, 0], dilation=[3], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv511: R.Tensor((1, 384, 1), dtype="float32") = R.reshape(decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_bias1, R.shape([1, 384, 1]))
            conv1d57: R.Tensor((1, 384, 64), dtype="float32") = R.add(lv510, lv511)
            reshape116: R.Tensor((1, 384, 64), dtype="float32") = R.reshape(conv1d57, R.shape([1, 384, 64]))
            lv512 = R.call_tir(cls.snake7, (reshape116, decoder_model_layers_2_block_layers_3_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 384, 64), dtype="float32"))
            reshape117: R.Tensor((1, 384, 64), dtype="float32") = R.reshape(lv512, R.shape([1, 384, 64]))
            lv513: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, reshape117, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv514: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_cache_cache, lv513, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv515: R.Tensor((384, 384, 1), dtype="float32") = R.square(decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_weight_v1)
            lv516: R.Tensor((384, 1, 1), dtype="float32") = R.sum(lv515, axis=[1, 2], keepdims=True)
            lv517: R.Tensor((384, 1, 1), dtype="float32") = R.sqrt(lv516)
            lv518: R.Tensor((384, 384, 1), dtype="float32") = R.divide(decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_weight_v1, lv517)
            wnconv1d58: R.Tensor((384, 384, 1), dtype="float32") = R.multiply(decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_weight_g1, lv518)
            lv519: R.Tensor((1, 384, 64), dtype="float32") = R.nn.conv1d(lv514, wnconv1d58, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv520: R.Tensor((1, 384, 1), dtype="float32") = R.reshape(decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_bias1, R.shape([1, 384, 1]))
            conv1d58: R.Tensor((1, 384, 64), dtype="float32") = R.add(lv519, lv520)
            lv521: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_3_block_paddings_1_cache, add51, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            add52: R.Tensor((1, 384, 64), dtype="float32") = R.add(conv1d58, R.const(0.0, "float32"))
            add53: R.Tensor((1, 384, 64), dtype="float32") = R.add(add52, lv521)
            lv522: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_4_block_paddings_0_cache, add53, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            reshape118: R.Tensor((1, 384, 64), dtype="float32") = R.reshape(lv522, R.shape([1, 384, 64]))
            lv523 = R.call_tir(cls.snake7, (reshape118, decoder_model_layers_2_block_layers_4_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 384, 64), dtype="float32"))
            reshape119: R.Tensor((1, 384, 64), dtype="float32") = R.reshape(lv523, R.shape([1, 384, 64]))
            lv524: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, reshape119, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv525: R.Tensor((1, 384, 118), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_cache_cache, lv524, sinfo_args=(R.Tensor((1, 384, 118), dtype="float32"),))
            lv526: R.Tensor((384, 384, 7), dtype="float32") = R.square(decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_weight_v1)
            lv527: R.Tensor((384, 1, 1), dtype="float32") = R.sum(lv526, axis=[1, 2], keepdims=True)
            lv528: R.Tensor((384, 1, 1), dtype="float32") = R.sqrt(lv527)
            lv529: R.Tensor((384, 384, 7), dtype="float32") = R.divide(decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_weight_v1, lv528)
            wnconv1d59: R.Tensor((384, 384, 7), dtype="float32") = R.multiply(decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_weight_g1, lv529)
            lv530: R.Tensor((1, 384, 64), dtype="float32") = R.nn.conv1d(lv525, wnconv1d59, strides=[1], padding=[0, 0], dilation=[9], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv531: R.Tensor((1, 384, 1), dtype="float32") = R.reshape(decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_bias1, R.shape([1, 384, 1]))
            conv1d59: R.Tensor((1, 384, 64), dtype="float32") = R.add(lv530, lv531)
            reshape120: R.Tensor((1, 384, 64), dtype="float32") = R.reshape(conv1d59, R.shape([1, 384, 64]))
            lv532 = R.call_tir(cls.snake7, (reshape120, decoder_model_layers_2_block_layers_4_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 384, 64), dtype="float32"))
            reshape121: R.Tensor((1, 384, 64), dtype="float32") = R.reshape(lv532, R.shape([1, 384, 64]))
            lv533: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, reshape121, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv534: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_cache_cache, lv533, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv535: R.Tensor((384, 384, 1), dtype="float32") = R.square(decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_weight_v1)
            lv536: R.Tensor((384, 1, 1), dtype="float32") = R.sum(lv535, axis=[1, 2], keepdims=True)
            lv537: R.Tensor((384, 1, 1), dtype="float32") = R.sqrt(lv536)
            lv538: R.Tensor((384, 384, 1), dtype="float32") = R.divide(decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_weight_v1, lv537)
            wnconv1d60: R.Tensor((384, 384, 1), dtype="float32") = R.multiply(decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_weight_g1, lv538)
            lv539: R.Tensor((1, 384, 64), dtype="float32") = R.nn.conv1d(lv534, wnconv1d60, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv540: R.Tensor((1, 384, 1), dtype="float32") = R.reshape(decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_bias1, R.shape([1, 384, 1]))
            conv1d60: R.Tensor((1, 384, 64), dtype="float32") = R.add(lv539, lv540)
            lv541: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_4_block_paddings_1_cache, add53, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            add54: R.Tensor((1, 384, 64), dtype="float32") = R.add(conv1d60, R.const(0.0, "float32"))
            add55: R.Tensor((1, 384, 64), dtype="float32") = R.add(add54, lv541)
            reshape122: R.Tensor((1, 384, 64), dtype="float32") = R.reshape(add55, R.shape([1, 384, 64]))
            lv542 = R.call_tir(cls.snake7, (reshape122, decoder_model_layers_3_block_layers_0_alpha1), out_sinfo=R.Tensor((1, 384, 64), dtype="float32"))
            reshape123: R.Tensor((1, 384, 64), dtype="float32") = R.reshape(lv542, R.shape([1, 384, 64]))
            lv543: R.Tensor((384, 192, 8), dtype="float32") = R.square(decoder_model_layers_3_block_layers_1_weight_v1)
            lv544: R.Tensor((384, 1, 1), dtype="float32") = R.sum(lv543, axis=[1, 2], keepdims=True)
            lv545: R.Tensor((384, 1, 1), dtype="float32") = R.sqrt(lv544)
            lv546: R.Tensor((384, 192, 8), dtype="float32") = R.divide(decoder_model_layers_3_block_layers_1_weight_v1, lv545)
            wnconvtranspose1d2: R.Tensor((384, 192, 8), dtype="float32") = R.multiply(decoder_model_layers_3_block_layers_1_weight_g1, lv546)
            conv1d_transpose2: R.Tensor((1, 192, 260), dtype="float32") = R.nn.conv1d_transpose(reshape123, wnconvtranspose1d2, strides=[4], padding=[0, 0], output_padding=[0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="IOW", out_layout="NCW", out_dtype="void")
            lv547: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_1_cache_cache, conv1d_transpose2, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            unsqueeze2: R.Tensor((192, 1), dtype="float32") = R.expand_dims(decoder_model_layers_3_block_layers_1_bias1, axis=[-1])
            add56: R.Tensor((1, 192, 256), dtype="float32") = R.add(lv547, unsqueeze2)
            lv548: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_2_block_paddings_0_cache, add56, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            reshape124: R.Tensor((1, 192, 256), dtype="float32") = R.reshape(lv548, R.shape([1, 192, 256]))
            lv549 = R.call_tir(cls.snake8, (reshape124, decoder_model_layers_3_block_layers_2_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 192, 256), dtype="float32"))
            reshape125: R.Tensor((1, 192, 256), dtype="float32") = R.reshape(lv549, R.shape([1, 192, 256]))
            lv550: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, reshape125, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv551: R.Tensor((1, 192, 262), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache, lv550, sinfo_args=(R.Tensor((1, 192, 262), dtype="float32"),))
            lv552: R.Tensor((192, 192, 7), dtype="float32") = R.square(decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_weight_v1)
            lv553: R.Tensor((192, 1, 1), dtype="float32") = R.sum(lv552, axis=[1, 2], keepdims=True)
            lv554: R.Tensor((192, 1, 1), dtype="float32") = R.sqrt(lv553)
            lv555: R.Tensor((192, 192, 7), dtype="float32") = R.divide(decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_weight_v1, lv554)
            wnconv1d61: R.Tensor((192, 192, 7), dtype="float32") = R.multiply(decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_weight_g1, lv555)
            lv556: R.Tensor((1, 192, 256), dtype="float32") = R.nn.conv1d(lv551, wnconv1d61, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv557: R.Tensor((1, 192, 1), dtype="float32") = R.reshape(decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_bias1, R.shape([1, 192, 1]))
            conv1d61: R.Tensor((1, 192, 256), dtype="float32") = R.add(lv556, lv557)
            reshape126: R.Tensor((1, 192, 256), dtype="float32") = R.reshape(conv1d61, R.shape([1, 192, 256]))
            lv558 = R.call_tir(cls.snake8, (reshape126, decoder_model_layers_3_block_layers_2_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 192, 256), dtype="float32"))
            reshape127: R.Tensor((1, 192, 256), dtype="float32") = R.reshape(lv558, R.shape([1, 192, 256]))
            lv559: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, reshape127, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv560: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache, lv559, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv561: R.Tensor((192, 192, 1), dtype="float32") = R.square(decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_weight_v1)
            lv562: R.Tensor((192, 1, 1), dtype="float32") = R.sum(lv561, axis=[1, 2], keepdims=True)
            lv563: R.Tensor((192, 1, 1), dtype="float32") = R.sqrt(lv562)
            lv564: R.Tensor((192, 192, 1), dtype="float32") = R.divide(decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_weight_v1, lv563)
            wnconv1d62: R.Tensor((192, 192, 1), dtype="float32") = R.multiply(decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_weight_g1, lv564)
            lv565: R.Tensor((1, 192, 256), dtype="float32") = R.nn.conv1d(lv560, wnconv1d62, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv566: R.Tensor((1, 192, 1), dtype="float32") = R.reshape(decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_bias1, R.shape([1, 192, 1]))
            conv1d62: R.Tensor((1, 192, 256), dtype="float32") = R.add(lv565, lv566)
            lv567: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_2_block_paddings_1_cache, add56, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            add57: R.Tensor((1, 192, 256), dtype="float32") = R.add(conv1d62, R.const(0.0, "float32"))
            add58: R.Tensor((1, 192, 256), dtype="float32") = R.add(add57, lv567)
            lv568: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_3_block_paddings_0_cache, add58, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            reshape128: R.Tensor((1, 192, 256), dtype="float32") = R.reshape(lv568, R.shape([1, 192, 256]))
            lv569 = R.call_tir(cls.snake8, (reshape128, decoder_model_layers_3_block_layers_3_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 192, 256), dtype="float32"))
            reshape129: R.Tensor((1, 192, 256), dtype="float32") = R.reshape(lv569, R.shape([1, 192, 256]))
            lv570: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, reshape129, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv571: R.Tensor((1, 192, 274), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_cache_cache, lv570, sinfo_args=(R.Tensor((1, 192, 274), dtype="float32"),))
            lv572: R.Tensor((192, 192, 7), dtype="float32") = R.square(decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_weight_v1)
            lv573: R.Tensor((192, 1, 1), dtype="float32") = R.sum(lv572, axis=[1, 2], keepdims=True)
            lv574: R.Tensor((192, 1, 1), dtype="float32") = R.sqrt(lv573)
            lv575: R.Tensor((192, 192, 7), dtype="float32") = R.divide(decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_weight_v1, lv574)
            wnconv1d63: R.Tensor((192, 192, 7), dtype="float32") = R.multiply(decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_weight_g1, lv575)
            lv576: R.Tensor((1, 192, 256), dtype="float32") = R.nn.conv1d(lv571, wnconv1d63, strides=[1], padding=[0, 0], dilation=[3], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv577: R.Tensor((1, 192, 1), dtype="float32") = R.reshape(decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_bias1, R.shape([1, 192, 1]))
            conv1d63: R.Tensor((1, 192, 256), dtype="float32") = R.add(lv576, lv577)
            reshape130: R.Tensor((1, 192, 256), dtype="float32") = R.reshape(conv1d63, R.shape([1, 192, 256]))
            lv578 = R.call_tir(cls.snake8, (reshape130, decoder_model_layers_3_block_layers_3_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 192, 256), dtype="float32"))
            reshape131: R.Tensor((1, 192, 256), dtype="float32") = R.reshape(lv578, R.shape([1, 192, 256]))
            lv579: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, reshape131, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv580: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_cache_cache, lv579, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv581: R.Tensor((192, 192, 1), dtype="float32") = R.square(decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_weight_v1)
            lv582: R.Tensor((192, 1, 1), dtype="float32") = R.sum(lv581, axis=[1, 2], keepdims=True)
            lv583: R.Tensor((192, 1, 1), dtype="float32") = R.sqrt(lv582)
            lv584: R.Tensor((192, 192, 1), dtype="float32") = R.divide(decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_weight_v1, lv583)
            wnconv1d64: R.Tensor((192, 192, 1), dtype="float32") = R.multiply(decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_weight_g1, lv584)
            lv585: R.Tensor((1, 192, 256), dtype="float32") = R.nn.conv1d(lv580, wnconv1d64, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv586: R.Tensor((1, 192, 1), dtype="float32") = R.reshape(decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_bias1, R.shape([1, 192, 1]))
            conv1d64: R.Tensor((1, 192, 256), dtype="float32") = R.add(lv585, lv586)
            lv587: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_3_block_paddings_1_cache, add58, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            add59: R.Tensor((1, 192, 256), dtype="float32") = R.add(conv1d64, R.const(0.0, "float32"))
            add60: R.Tensor((1, 192, 256), dtype="float32") = R.add(add59, lv587)
            lv588: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_4_block_paddings_0_cache, add60, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            reshape132: R.Tensor((1, 192, 256), dtype="float32") = R.reshape(lv588, R.shape([1, 192, 256]))
            lv589 = R.call_tir(cls.snake8, (reshape132, decoder_model_layers_3_block_layers_4_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 192, 256), dtype="float32"))
            reshape133: R.Tensor((1, 192, 256), dtype="float32") = R.reshape(lv589, R.shape([1, 192, 256]))
            lv590: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, reshape133, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv591: R.Tensor((1, 192, 310), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_cache_cache, lv590, sinfo_args=(R.Tensor((1, 192, 310), dtype="float32"),))
            lv592: R.Tensor((192, 192, 7), dtype="float32") = R.square(decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_weight_v1)
            lv593: R.Tensor((192, 1, 1), dtype="float32") = R.sum(lv592, axis=[1, 2], keepdims=True)
            lv594: R.Tensor((192, 1, 1), dtype="float32") = R.sqrt(lv593)
            lv595: R.Tensor((192, 192, 7), dtype="float32") = R.divide(decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_weight_v1, lv594)
            wnconv1d65: R.Tensor((192, 192, 7), dtype="float32") = R.multiply(decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_weight_g1, lv595)
            lv596: R.Tensor((1, 192, 256), dtype="float32") = R.nn.conv1d(lv591, wnconv1d65, strides=[1], padding=[0, 0], dilation=[9], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv597: R.Tensor((1, 192, 1), dtype="float32") = R.reshape(decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_bias1, R.shape([1, 192, 1]))
            conv1d65: R.Tensor((1, 192, 256), dtype="float32") = R.add(lv596, lv597)
            reshape134: R.Tensor((1, 192, 256), dtype="float32") = R.reshape(conv1d65, R.shape([1, 192, 256]))
            lv598 = R.call_tir(cls.snake8, (reshape134, decoder_model_layers_3_block_layers_4_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 192, 256), dtype="float32"))
            reshape135: R.Tensor((1, 192, 256), dtype="float32") = R.reshape(lv598, R.shape([1, 192, 256]))
            lv599: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, reshape135, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv600: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_cache_cache, lv599, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv601: R.Tensor((192, 192, 1), dtype="float32") = R.square(decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_weight_v1)
            lv602: R.Tensor((192, 1, 1), dtype="float32") = R.sum(lv601, axis=[1, 2], keepdims=True)
            lv603: R.Tensor((192, 1, 1), dtype="float32") = R.sqrt(lv602)
            lv604: R.Tensor((192, 192, 1), dtype="float32") = R.divide(decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_weight_v1, lv603)
            wnconv1d66: R.Tensor((192, 192, 1), dtype="float32") = R.multiply(decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_weight_g1, lv604)
            lv605: R.Tensor((1, 192, 256), dtype="float32") = R.nn.conv1d(lv600, wnconv1d66, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv606: R.Tensor((1, 192, 1), dtype="float32") = R.reshape(decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_bias1, R.shape([1, 192, 1]))
            conv1d66: R.Tensor((1, 192, 256), dtype="float32") = R.add(lv605, lv606)
            lv607: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_4_block_paddings_1_cache, add60, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            add61: R.Tensor((1, 192, 256), dtype="float32") = R.add(conv1d66, R.const(0.0, "float32"))
            add62: R.Tensor((1, 192, 256), dtype="float32") = R.add(add61, lv607)
            reshape136: R.Tensor((1, 192, 256), dtype="float32") = R.reshape(add62, R.shape([1, 192, 256]))
            lv608 = R.call_tir(cls.snake8, (reshape136, decoder_model_layers_4_block_layers_0_alpha1), out_sinfo=R.Tensor((1, 192, 256), dtype="float32"))
            reshape137: R.Tensor((1, 192, 256), dtype="float32") = R.reshape(lv608, R.shape([1, 192, 256]))
            lv609: R.Tensor((192, 96, 4), dtype="float32") = R.square(decoder_model_layers_4_block_layers_1_weight_v1)
            lv610: R.Tensor((192, 1, 1), dtype="float32") = R.sum(lv609, axis=[1, 2], keepdims=True)
            lv611: R.Tensor((192, 1, 1), dtype="float32") = R.sqrt(lv610)
            lv612: R.Tensor((192, 96, 4), dtype="float32") = R.divide(decoder_model_layers_4_block_layers_1_weight_v1, lv611)
            wnconvtranspose1d3: R.Tensor((192, 96, 4), dtype="float32") = R.multiply(decoder_model_layers_4_block_layers_1_weight_g1, lv612)
            conv1d_transpose3: R.Tensor((1, 96, 514), dtype="float32") = R.nn.conv1d_transpose(reshape137, wnconvtranspose1d3, strides=[2], padding=[0, 0], output_padding=[0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="IOW", out_layout="NCW", out_dtype="void")
            lv613: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_1_cache_cache, conv1d_transpose3, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            unsqueeze3: R.Tensor((96, 1), dtype="float32") = R.expand_dims(decoder_model_layers_4_block_layers_1_bias1, axis=[-1])
            add63: R.Tensor((1, 96, 512), dtype="float32") = R.add(lv613, unsqueeze3)
            lv614: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_2_block_paddings_0_cache, add63, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            reshape138: R.Tensor((1, 96, 512), dtype="float32") = R.reshape(lv614, R.shape([1, 96, 512]))
            lv615 = R.call_tir(cls.snake9, (reshape138, decoder_model_layers_4_block_layers_2_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 96, 512), dtype="float32"))
            reshape139: R.Tensor((1, 96, 512), dtype="float32") = R.reshape(lv615, R.shape([1, 96, 512]))
            lv616: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, reshape139, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv617: R.Tensor((1, 96, 518), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache, lv616, sinfo_args=(R.Tensor((1, 96, 518), dtype="float32"),))
            lv618: R.Tensor((96, 96, 7), dtype="float32") = R.square(decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_weight_v1)
            lv619: R.Tensor((96, 1, 1), dtype="float32") = R.sum(lv618, axis=[1, 2], keepdims=True)
            lv620: R.Tensor((96, 1, 1), dtype="float32") = R.sqrt(lv619)
            lv621: R.Tensor((96, 96, 7), dtype="float32") = R.divide(decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_weight_v1, lv620)
            wnconv1d67: R.Tensor((96, 96, 7), dtype="float32") = R.multiply(decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_weight_g1, lv621)
            lv622: R.Tensor((1, 96, 512), dtype="float32") = R.nn.conv1d(lv617, wnconv1d67, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv623: R.Tensor((1, 96, 1), dtype="float32") = R.reshape(decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_bias1, R.shape([1, 96, 1]))
            conv1d67: R.Tensor((1, 96, 512), dtype="float32") = R.add(lv622, lv623)
            reshape140: R.Tensor((1, 96, 512), dtype="float32") = R.reshape(conv1d67, R.shape([1, 96, 512]))
            lv624 = R.call_tir(cls.snake9, (reshape140, decoder_model_layers_4_block_layers_2_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 96, 512), dtype="float32"))
            reshape141: R.Tensor((1, 96, 512), dtype="float32") = R.reshape(lv624, R.shape([1, 96, 512]))
            lv625: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, reshape141, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv626: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache, lv625, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv627: R.Tensor((96, 96, 1), dtype="float32") = R.square(decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_weight_v1)
            lv628: R.Tensor((96, 1, 1), dtype="float32") = R.sum(lv627, axis=[1, 2], keepdims=True)
            lv629: R.Tensor((96, 1, 1), dtype="float32") = R.sqrt(lv628)
            lv630: R.Tensor((96, 96, 1), dtype="float32") = R.divide(decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_weight_v1, lv629)
            wnconv1d68: R.Tensor((96, 96, 1), dtype="float32") = R.multiply(decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_weight_g1, lv630)
            lv631: R.Tensor((1, 96, 512), dtype="float32") = R.nn.conv1d(lv626, wnconv1d68, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv632: R.Tensor((1, 96, 1), dtype="float32") = R.reshape(decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_bias1, R.shape([1, 96, 1]))
            conv1d68: R.Tensor((1, 96, 512), dtype="float32") = R.add(lv631, lv632)
            lv633: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_2_block_paddings_1_cache, add63, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            add64: R.Tensor((1, 96, 512), dtype="float32") = R.add(conv1d68, R.const(0.0, "float32"))
            add65: R.Tensor((1, 96, 512), dtype="float32") = R.add(add64, lv633)
            lv634: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_3_block_paddings_0_cache, add65, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            reshape142: R.Tensor((1, 96, 512), dtype="float32") = R.reshape(lv634, R.shape([1, 96, 512]))
            lv635 = R.call_tir(cls.snake9, (reshape142, decoder_model_layers_4_block_layers_3_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 96, 512), dtype="float32"))
            reshape143: R.Tensor((1, 96, 512), dtype="float32") = R.reshape(lv635, R.shape([1, 96, 512]))
            lv636: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, reshape143, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv637: R.Tensor((1, 96, 530), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_cache_cache, lv636, sinfo_args=(R.Tensor((1, 96, 530), dtype="float32"),))
            lv638: R.Tensor((96, 96, 7), dtype="float32") = R.square(decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_weight_v1)
            lv639: R.Tensor((96, 1, 1), dtype="float32") = R.sum(lv638, axis=[1, 2], keepdims=True)
            lv640: R.Tensor((96, 1, 1), dtype="float32") = R.sqrt(lv639)
            lv641: R.Tensor((96, 96, 7), dtype="float32") = R.divide(decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_weight_v1, lv640)
            wnconv1d69: R.Tensor((96, 96, 7), dtype="float32") = R.multiply(decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_weight_g1, lv641)
            lv642: R.Tensor((1, 96, 512), dtype="float32") = R.nn.conv1d(lv637, wnconv1d69, strides=[1], padding=[0, 0], dilation=[3], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv643: R.Tensor((1, 96, 1), dtype="float32") = R.reshape(decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_bias1, R.shape([1, 96, 1]))
            conv1d69: R.Tensor((1, 96, 512), dtype="float32") = R.add(lv642, lv643)
            reshape144: R.Tensor((1, 96, 512), dtype="float32") = R.reshape(conv1d69, R.shape([1, 96, 512]))
            lv644 = R.call_tir(cls.snake9, (reshape144, decoder_model_layers_4_block_layers_3_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 96, 512), dtype="float32"))
            reshape145: R.Tensor((1, 96, 512), dtype="float32") = R.reshape(lv644, R.shape([1, 96, 512]))
            lv645: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, reshape145, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv646: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_cache_cache, lv645, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv647: R.Tensor((96, 96, 1), dtype="float32") = R.square(decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_weight_v1)
            lv648: R.Tensor((96, 1, 1), dtype="float32") = R.sum(lv647, axis=[1, 2], keepdims=True)
            lv649: R.Tensor((96, 1, 1), dtype="float32") = R.sqrt(lv648)
            lv650: R.Tensor((96, 96, 1), dtype="float32") = R.divide(decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_weight_v1, lv649)
            wnconv1d70: R.Tensor((96, 96, 1), dtype="float32") = R.multiply(decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_weight_g1, lv650)
            lv651: R.Tensor((1, 96, 512), dtype="float32") = R.nn.conv1d(lv646, wnconv1d70, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv652: R.Tensor((1, 96, 1), dtype="float32") = R.reshape(decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_bias1, R.shape([1, 96, 1]))
            conv1d70: R.Tensor((1, 96, 512), dtype="float32") = R.add(lv651, lv652)
            lv653: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_3_block_paddings_1_cache, add65, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            add66: R.Tensor((1, 96, 512), dtype="float32") = R.add(conv1d70, R.const(0.0, "float32"))
            add67: R.Tensor((1, 96, 512), dtype="float32") = R.add(add66, lv653)
            lv654: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_4_block_paddings_0_cache, add67, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            reshape146: R.Tensor((1, 96, 512), dtype="float32") = R.reshape(lv654, R.shape([1, 96, 512]))
            lv655 = R.call_tir(cls.snake9, (reshape146, decoder_model_layers_4_block_layers_4_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 96, 512), dtype="float32"))
            reshape147: R.Tensor((1, 96, 512), dtype="float32") = R.reshape(lv655, R.shape([1, 96, 512]))
            lv656: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, reshape147, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv657: R.Tensor((1, 96, 566), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_cache_cache, lv656, sinfo_args=(R.Tensor((1, 96, 566), dtype="float32"),))
            lv658: R.Tensor((96, 96, 7), dtype="float32") = R.square(decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_weight_v1)
            lv659: R.Tensor((96, 1, 1), dtype="float32") = R.sum(lv658, axis=[1, 2], keepdims=True)
            lv660: R.Tensor((96, 1, 1), dtype="float32") = R.sqrt(lv659)
            lv661: R.Tensor((96, 96, 7), dtype="float32") = R.divide(decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_weight_v1, lv660)
            wnconv1d71: R.Tensor((96, 96, 7), dtype="float32") = R.multiply(decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_weight_g1, lv661)
            lv662: R.Tensor((1, 96, 512), dtype="float32") = R.nn.conv1d(lv657, wnconv1d71, strides=[1], padding=[0, 0], dilation=[9], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv663: R.Tensor((1, 96, 1), dtype="float32") = R.reshape(decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_bias1, R.shape([1, 96, 1]))
            conv1d71: R.Tensor((1, 96, 512), dtype="float32") = R.add(lv662, lv663)
            reshape148: R.Tensor((1, 96, 512), dtype="float32") = R.reshape(conv1d71, R.shape([1, 96, 512]))
            lv664 = R.call_tir(cls.snake9, (reshape148, decoder_model_layers_4_block_layers_4_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 96, 512), dtype="float32"))
            reshape149: R.Tensor((1, 96, 512), dtype="float32") = R.reshape(lv664, R.shape([1, 96, 512]))
            lv665: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, reshape149, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv666: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_cache_cache, lv665, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv667: R.Tensor((96, 96, 1), dtype="float32") = R.square(decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_weight_v1)
            lv668: R.Tensor((96, 1, 1), dtype="float32") = R.sum(lv667, axis=[1, 2], keepdims=True)
            lv669: R.Tensor((96, 1, 1), dtype="float32") = R.sqrt(lv668)
            lv670: R.Tensor((96, 96, 1), dtype="float32") = R.divide(decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_weight_v1, lv669)
            wnconv1d72: R.Tensor((96, 96, 1), dtype="float32") = R.multiply(decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_weight_g1, lv670)
            lv671: R.Tensor((1, 96, 512), dtype="float32") = R.nn.conv1d(lv666, wnconv1d72, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv672: R.Tensor((1, 96, 1), dtype="float32") = R.reshape(decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_bias1, R.shape([1, 96, 1]))
            conv1d72: R.Tensor((1, 96, 512), dtype="float32") = R.add(lv671, lv672)
            lv673: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_4_block_paddings_1_cache, add67, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            add68: R.Tensor((1, 96, 512), dtype="float32") = R.add(conv1d72, R.const(0.0, "float32"))
            add69: R.Tensor((1, 96, 512), dtype="float32") = R.add(add68, lv673)
            reshape150: R.Tensor((1, 96, 512), dtype="float32") = R.reshape(add69, R.shape([1, 96, 512]))
            lv674 = R.call_tir(cls.snake9, (reshape150, decoder_model_layers_5_alpha1), out_sinfo=R.Tensor((1, 96, 512), dtype="float32"))
            reshape151: R.Tensor((1, 96, 512), dtype="float32") = R.reshape(lv674, R.shape([1, 96, 512]))
            lv675: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_6_downsampling_delay_cache, reshape151, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv676: R.Tensor((1, 96, 518), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_6_cache_cache, lv675, sinfo_args=(R.Tensor((1, 96, 518), dtype="float32"),))
            lv677: R.Tensor((1, 96, 7), dtype="float32") = R.square(decoder_model_layers_6_weight_v1)
            lv678: R.Tensor((1, 1, 1), dtype="float32") = R.sum(lv677, axis=[1, 2], keepdims=True)
            lv679: R.Tensor((1, 1, 1), dtype="float32") = R.sqrt(lv678)
            lv680: R.Tensor((1, 96, 7), dtype="float32") = R.divide(decoder_model_layers_6_weight_v1, lv679)
            wnconv1d73: R.Tensor((1, 96, 7), dtype="float32") = R.multiply(decoder_model_layers_6_weight_g1, lv680)
            lv681: R.Tensor((1, 1, 512), dtype="float32") = R.nn.conv1d(lv676, wnconv1d73, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv682: R.Tensor((1, 1, 1), dtype="float32") = R.reshape(decoder_model_layers_6_bias1, R.shape([1, 1, 1]))
            conv1d73: R.Tensor((1, 1, 512), dtype="float32") = R.add(lv681, lv682)
            tanh: R.Tensor((1, 1, 512), dtype="float32") = R.tanh(conv1d73)
            gv2: R.Tuple(R.Tensor((1, 1, 512), dtype="float32"), R.Tuple(R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object)) = tanh, (_io, encoder_block_layers_0_cache_cache, encoder_block_layers_0_downsampling_delay_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_1_block_layers_0_block_paddings_0_cache, encoder_block_layers_1_block_layers_0_block_paddings_1_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_1_block_layers_1_block_paddings_0_cache, encoder_block_layers_1_block_layers_1_block_paddings_1_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_1_block_layers_2_block_paddings_0_cache, encoder_block_layers_1_block_layers_2_block_paddings_1_cache, encoder_block_layers_1_block_layers_4_cache_cache, encoder_block_layers_1_block_layers_4_downsampling_delay_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_2_block_layers_0_block_paddings_0_cache, encoder_block_layers_2_block_layers_0_block_paddings_1_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_2_block_layers_1_block_paddings_0_cache, encoder_block_layers_2_block_layers_1_block_paddings_1_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_2_block_layers_2_block_paddings_0_cache, encoder_block_layers_2_block_layers_2_block_paddings_1_cache, encoder_block_layers_2_block_layers_4_cache_cache, encoder_block_layers_2_block_layers_4_downsampling_delay_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_3_block_layers_0_block_paddings_0_cache, encoder_block_layers_3_block_layers_0_block_paddings_1_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_3_block_layers_1_block_paddings_0_cache, encoder_block_layers_3_block_layers_1_block_paddings_1_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_3_block_layers_2_block_paddings_0_cache, encoder_block_layers_3_block_layers_2_block_paddings_1_cache, encoder_block_layers_3_block_layers_4_cache_cache, encoder_block_layers_3_block_layers_4_downsampling_delay_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_4_block_layers_0_block_paddings_0_cache, encoder_block_layers_4_block_layers_0_block_paddings_1_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_4_block_layers_1_block_paddings_0_cache, encoder_block_layers_4_block_layers_1_block_paddings_1_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_4_block_layers_2_block_paddings_0_cache, encoder_block_layers_4_block_layers_2_block_paddings_1_cache, encoder_block_layers_4_block_layers_4_cache_cache, encoder_block_layers_4_block_layers_4_downsampling_delay_cache, encoder_block_layers_6_cache_cache, encoder_block_layers_6_downsampling_delay_cache, decoder_model_layers_0_cache_cache, decoder_model_layers_0_downsampling_delay_cache, decoder_model_layers_1_block_layers_1_cache_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_1_block_layers_2_block_paddings_0_cache, decoder_model_layers_1_block_layers_2_block_paddings_1_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_1_block_layers_3_block_paddings_0_cache, decoder_model_layers_1_block_layers_3_block_paddings_1_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_1_block_layers_4_block_paddings_0_cache, decoder_model_layers_1_block_layers_4_block_paddings_1_cache, decoder_model_layers_2_block_layers_1_cache_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_2_block_layers_2_block_paddings_0_cache, decoder_model_layers_2_block_layers_2_block_paddings_1_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_2_block_layers_3_block_paddings_0_cache, decoder_model_layers_2_block_layers_3_block_paddings_1_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_2_block_layers_4_block_paddings_0_cache, decoder_model_layers_2_block_layers_4_block_paddings_1_cache, decoder_model_layers_3_block_layers_1_cache_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_3_block_layers_2_block_paddings_0_cache, decoder_model_layers_3_block_layers_2_block_paddings_1_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_3_block_layers_3_block_paddings_0_cache, decoder_model_layers_3_block_layers_3_block_paddings_1_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_3_block_layers_4_block_paddings_0_cache, decoder_model_layers_3_block_layers_4_block_paddings_1_cache, decoder_model_layers_4_block_layers_1_cache_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_4_block_layers_2_block_paddings_0_cache, decoder_model_layers_4_block_layers_2_block_paddings_1_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_4_block_layers_3_block_paddings_0_cache, decoder_model_layers_4_block_layers_3_block_paddings_1_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_4_block_layers_4_block_paddings_0_cache, decoder_model_layers_4_block_layers_4_block_paddings_1_cache, decoder_model_layers_6_cache_cache, decoder_model_layers_6_downsampling_delay_cache)
            R.output(gv2)
        return gv2

    @R.function
    def encode(audio_data: R.Tensor((1, 1, 512), dtype="float32"), _io: R.Object, encoder_block_layers_0_cache_cache: R.Object, encoder_block_layers_0_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_0_block_paddings_0_cache: R.Object, encoder_block_layers_1_block_layers_0_block_paddings_1_cache: R.Object, encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_1_block_paddings_0_cache: R.Object, encoder_block_layers_1_block_layers_1_block_paddings_1_cache: R.Object, encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_2_block_paddings_0_cache: R.Object, encoder_block_layers_1_block_layers_2_block_paddings_1_cache: R.Object, encoder_block_layers_1_block_layers_4_cache_cache: R.Object, encoder_block_layers_1_block_layers_4_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_0_block_paddings_0_cache: R.Object, encoder_block_layers_2_block_layers_0_block_paddings_1_cache: R.Object, encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_1_block_paddings_0_cache: R.Object, encoder_block_layers_2_block_layers_1_block_paddings_1_cache: R.Object, encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_2_block_paddings_0_cache: R.Object, encoder_block_layers_2_block_layers_2_block_paddings_1_cache: R.Object, encoder_block_layers_2_block_layers_4_cache_cache: R.Object, encoder_block_layers_2_block_layers_4_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_0_block_paddings_0_cache: R.Object, encoder_block_layers_3_block_layers_0_block_paddings_1_cache: R.Object, encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_1_block_paddings_0_cache: R.Object, encoder_block_layers_3_block_layers_1_block_paddings_1_cache: R.Object, encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_2_block_paddings_0_cache: R.Object, encoder_block_layers_3_block_layers_2_block_paddings_1_cache: R.Object, encoder_block_layers_3_block_layers_4_cache_cache: R.Object, encoder_block_layers_3_block_layers_4_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_0_block_paddings_0_cache: R.Object, encoder_block_layers_4_block_layers_0_block_paddings_1_cache: R.Object, encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_1_block_paddings_0_cache: R.Object, encoder_block_layers_4_block_layers_1_block_paddings_1_cache: R.Object, encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_2_block_paddings_0_cache: R.Object, encoder_block_layers_4_block_layers_2_block_paddings_1_cache: R.Object, encoder_block_layers_4_block_layers_4_cache_cache: R.Object, encoder_block_layers_4_block_layers_4_downsampling_delay_cache: R.Object, encoder_block_layers_6_cache_cache: R.Object, encoder_block_layers_6_downsampling_delay_cache: R.Object, decoder_model_layers_0_cache_cache: R.Object, decoder_model_layers_0_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_1_cache_cache: R.Object, decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_2_block_paddings_0_cache: R.Object, decoder_model_layers_1_block_layers_2_block_paddings_1_cache: R.Object, decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_3_block_paddings_0_cache: R.Object, decoder_model_layers_1_block_layers_3_block_paddings_1_cache: R.Object, decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_4_block_paddings_0_cache: R.Object, decoder_model_layers_1_block_layers_4_block_paddings_1_cache: R.Object, decoder_model_layers_2_block_layers_1_cache_cache: R.Object, decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_2_block_paddings_0_cache: R.Object, decoder_model_layers_2_block_layers_2_block_paddings_1_cache: R.Object, decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_3_block_paddings_0_cache: R.Object, decoder_model_layers_2_block_layers_3_block_paddings_1_cache: R.Object, decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_4_block_paddings_0_cache: R.Object, decoder_model_layers_2_block_layers_4_block_paddings_1_cache: R.Object, decoder_model_layers_3_block_layers_1_cache_cache: R.Object, decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_2_block_paddings_0_cache: R.Object, decoder_model_layers_3_block_layers_2_block_paddings_1_cache: R.Object, decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_3_block_paddings_0_cache: R.Object, decoder_model_layers_3_block_layers_3_block_paddings_1_cache: R.Object, decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_4_block_paddings_0_cache: R.Object, decoder_model_layers_3_block_layers_4_block_paddings_1_cache: R.Object, decoder_model_layers_4_block_layers_1_cache_cache: R.Object, decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_2_block_paddings_0_cache: R.Object, decoder_model_layers_4_block_layers_2_block_paddings_1_cache: R.Object, decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_3_block_paddings_0_cache: R.Object, decoder_model_layers_4_block_layers_3_block_paddings_1_cache: R.Object, decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_4_block_paddings_0_cache: R.Object, decoder_model_layers_4_block_layers_4_block_paddings_1_cache: R.Object, decoder_model_layers_6_cache_cache: R.Object, decoder_model_layers_6_downsampling_delay_cache: R.Object, packed_params: R.Tuple(R.Tensor((64, 1, 1), dtype="float32"), R.Tensor((64, 1, 7), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((1, 64, 1), dtype="float32"), R.Tensor((64, 1, 1), dtype="float32"), R.Tensor((64, 64, 7), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((1, 64, 1), dtype="float32"), R.Tensor((64, 1, 1), dtype="float32"), R.Tensor((64, 64, 1), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((1, 64, 1), dtype="float32"), R.Tensor((64, 1, 1), dtype="float32"), R.Tensor((64, 64, 7), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((1, 64, 1), dtype="float32"), R.Tensor((64, 1, 1), dtype="float32"), R.Tensor((64, 64, 1), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((1, 64, 1), dtype="float32"), R.Tensor((64, 1, 1), dtype="float32"), R.Tensor((64, 64, 7), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((1, 64, 1), dtype="float32"), R.Tensor((64, 1, 1), dtype="float32"), R.Tensor((64, 64, 1), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((1, 64, 1), dtype="float32"), R.Tensor((128, 1, 1), dtype="float32"), R.Tensor((128, 64, 4), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((1, 128, 1), dtype="float32"), R.Tensor((128, 1, 1), dtype="float32"), R.Tensor((128, 128, 7), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((1, 128, 1), dtype="float32"), R.Tensor((128, 1, 1), dtype="float32"), R.Tensor((128, 128, 1), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((1, 128, 1), dtype="float32"), R.Tensor((128, 1, 1), dtype="float32"), R.Tensor((128, 128, 7), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((1, 128, 1), dtype="float32"), R.Tensor((128, 1, 1), dtype="float32"), R.Tensor((128, 128, 1), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((1, 128, 1), dtype="float32"), R.Tensor((128, 1, 1), dtype="float32"), R.Tensor((128, 128, 7), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((1, 128, 1), dtype="float32"), R.Tensor((128, 1, 1), dtype="float32"), R.Tensor((128, 128, 1), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((1, 128, 1), dtype="float32"), R.Tensor((256, 1, 1), dtype="float32"), R.Tensor((256, 128, 8), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((1, 256, 1), dtype="float32"), R.Tensor((256, 1, 1), dtype="float32"), R.Tensor((256, 256, 7), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((1, 256, 1), dtype="float32"), R.Tensor((256, 1, 1), dtype="float32"), R.Tensor((256, 256, 1), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((1, 256, 1), dtype="float32"), R.Tensor((256, 1, 1), dtype="float32"), R.Tensor((256, 256, 7), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((1, 256, 1), dtype="float32"), R.Tensor((256, 1, 1), dtype="float32"), R.Tensor((256, 256, 1), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((1, 256, 1), dtype="float32"), R.Tensor((256, 1, 1), dtype="float32"), R.Tensor((256, 256, 7), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((1, 256, 1), dtype="float32"), R.Tensor((256, 1, 1), dtype="float32"), R.Tensor((256, 256, 1), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((1, 256, 1), dtype="float32"), R.Tensor((512, 1, 1), dtype="float32"), R.Tensor((512, 256, 16), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((1, 512, 1), dtype="float32"), R.Tensor((512, 1, 1), dtype="float32"), R.Tensor((512, 512, 7), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((1, 512, 1), dtype="float32"), R.Tensor((512, 1, 1), dtype="float32"), R.Tensor((512, 512, 1), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((1, 512, 1), dtype="float32"), R.Tensor((512, 1, 1), dtype="float32"), R.Tensor((512, 512, 7), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((1, 512, 1), dtype="float32"), R.Tensor((512, 1, 1), dtype="float32"), R.Tensor((512, 512, 1), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((1, 512, 1), dtype="float32"), R.Tensor((512, 1, 1), dtype="float32"), R.Tensor((512, 512, 7), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((1, 512, 1), dtype="float32"), R.Tensor((512, 1, 1), dtype="float32"), R.Tensor((512, 512, 1), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((1, 512, 1), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 512, 16), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1, 1024, 1), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 1024, 3), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((8, 1, 1), dtype="float32"), R.Tensor((8, 1024, 1), dtype="float32"), R.Tensor((8,), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 8, 1), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024, 8), dtype="float32"), R.Tensor((8, 1, 1), dtype="float32"), R.Tensor((8, 1024, 1), dtype="float32"), R.Tensor((8,), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 8, 1), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024, 8), dtype="float32"), R.Tensor((8, 1, 1), dtype="float32"), R.Tensor((8, 1024, 1), dtype="float32"), R.Tensor((8,), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 8, 1), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024, 8), dtype="float32"), R.Tensor((8, 1, 1), dtype="float32"), R.Tensor((8, 1024, 1), dtype="float32"), R.Tensor((8,), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 8, 1), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024, 8), dtype="float32"), R.Tensor((8, 1, 1), dtype="float32"), R.Tensor((8, 1024, 1), dtype="float32"), R.Tensor((8,), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 8, 1), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024, 8), dtype="float32"), R.Tensor((8, 1, 1), dtype="float32"), R.Tensor((8, 1024, 1), dtype="float32"), R.Tensor((8,), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 8, 1), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024, 8), dtype="float32"), R.Tensor((8, 1, 1), dtype="float32"), R.Tensor((8, 1024, 1), dtype="float32"), R.Tensor((8,), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 8, 1), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024, 8), dtype="float32"), R.Tensor((8, 1, 1), dtype="float32"), R.Tensor((8, 1024, 1), dtype="float32"), R.Tensor((8,), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 8, 1), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024, 8), dtype="float32"), R.Tensor((8, 1, 1), dtype="float32"), R.Tensor((8, 1024, 1), dtype="float32"), R.Tensor((8,), dtype="float32"), R.Tensor((1024, 1, 1), dtype="float32"), R.Tensor((1024, 8, 1), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024, 8), dtype="float32"), R.Tensor((1536, 1, 1), dtype="float32"), R.Tensor((1536, 1024, 7), dtype="float32"), R.Tensor((1536,), dtype="float32"), R.Tensor((1, 1536, 1), dtype="float32"), R.Tensor((1536, 1, 1), dtype="float32"), R.Tensor((1536, 768, 16), dtype="float32"), R.Tensor((768,), dtype="float32"), R.Tensor((1, 768, 1), dtype="float32"), R.Tensor((768, 1, 1), dtype="float32"), R.Tensor((768, 768, 7), dtype="float32"), R.Tensor((768,), dtype="float32"), R.Tensor((1, 768, 1), dtype="float32"), R.Tensor((768, 1, 1), dtype="float32"), R.Tensor((768, 768, 1), dtype="float32"), R.Tensor((768,), dtype="float32"), R.Tensor((1, 768, 1), dtype="float32"), R.Tensor((768, 1, 1), dtype="float32"), R.Tensor((768, 768, 7), dtype="float32"), R.Tensor((768,), dtype="float32"), R.Tensor((1, 768, 1), dtype="float32"), R.Tensor((768, 1, 1), dtype="float32"), R.Tensor((768, 768, 1), dtype="float32"), R.Tensor((768,), dtype="float32"), R.Tensor((1, 768, 1), dtype="float32"), R.Tensor((768, 1, 1), dtype="float32"), R.Tensor((768, 768, 7), dtype="float32"), R.Tensor((768,), dtype="float32"), R.Tensor((1, 768, 1), dtype="float32"), R.Tensor((768, 1, 1), dtype="float32"), R.Tensor((768, 768, 1), dtype="float32"), R.Tensor((768,), dtype="float32"), R.Tensor((1, 768, 1), dtype="float32"), R.Tensor((768, 1, 1), dtype="float32"), R.Tensor((768, 384, 16), dtype="float32"), R.Tensor((384,), dtype="float32"), R.Tensor((1, 384, 1), dtype="float32"), R.Tensor((384, 1, 1), dtype="float32"), R.Tensor((384, 384, 7), dtype="float32"), R.Tensor((384,), dtype="float32"), R.Tensor((1, 384, 1), dtype="float32"), R.Tensor((384, 1, 1), dtype="float32"), R.Tensor((384, 384, 1), dtype="float32"), R.Tensor((384,), dtype="float32"), R.Tensor((1, 384, 1), dtype="float32"), R.Tensor((384, 1, 1), dtype="float32"), R.Tensor((384, 384, 7), dtype="float32"), R.Tensor((384,), dtype="float32"), R.Tensor((1, 384, 1), dtype="float32"), R.Tensor((384, 1, 1), dtype="float32"), R.Tensor((384, 384, 1), dtype="float32"), R.Tensor((384,), dtype="float32"), R.Tensor((1, 384, 1), dtype="float32"), R.Tensor((384, 1, 1), dtype="float32"), R.Tensor((384, 384, 7), dtype="float32"), R.Tensor((384,), dtype="float32"), R.Tensor((1, 384, 1), dtype="float32"), R.Tensor((384, 1, 1), dtype="float32"), R.Tensor((384, 384, 1), dtype="float32"), R.Tensor((384,), dtype="float32"), R.Tensor((1, 384, 1), dtype="float32"), R.Tensor((384, 1, 1), dtype="float32"), R.Tensor((384, 192, 8), dtype="float32"), R.Tensor((192,), dtype="float32"), R.Tensor((1, 192, 1), dtype="float32"), R.Tensor((192, 1, 1), dtype="float32"), R.Tensor((192, 192, 7), dtype="float32"), R.Tensor((192,), dtype="float32"), R.Tensor((1, 192, 1), dtype="float32"), R.Tensor((192, 1, 1), dtype="float32"), R.Tensor((192, 192, 1), dtype="float32"), R.Tensor((192,), dtype="float32"), R.Tensor((1, 192, 1), dtype="float32"), R.Tensor((192, 1, 1), dtype="float32"), R.Tensor((192, 192, 7), dtype="float32"), R.Tensor((192,), dtype="float32"), R.Tensor((1, 192, 1), dtype="float32"), R.Tensor((192, 1, 1), dtype="float32"), R.Tensor((192, 192, 1), dtype="float32"), R.Tensor((192,), dtype="float32"), R.Tensor((1, 192, 1), dtype="float32"), R.Tensor((192, 1, 1), dtype="float32"), R.Tensor((192, 192, 7), dtype="float32"), R.Tensor((192,), dtype="float32"), R.Tensor((1, 192, 1), dtype="float32"), R.Tensor((192, 1, 1), dtype="float32"), R.Tensor((192, 192, 1), dtype="float32"), R.Tensor((192,), dtype="float32"), R.Tensor((1, 192, 1), dtype="float32"), R.Tensor((192, 1, 1), dtype="float32"), R.Tensor((192, 96, 4), dtype="float32"), R.Tensor((96,), dtype="float32"), R.Tensor((1, 96, 1), dtype="float32"), R.Tensor((96, 1, 1), dtype="float32"), R.Tensor((96, 96, 7), dtype="float32"), R.Tensor((96,), dtype="float32"), R.Tensor((1, 96, 1), dtype="float32"), R.Tensor((96, 1, 1), dtype="float32"), R.Tensor((96, 96, 1), dtype="float32"), R.Tensor((96,), dtype="float32"), R.Tensor((1, 96, 1), dtype="float32"), R.Tensor((96, 1, 1), dtype="float32"), R.Tensor((96, 96, 7), dtype="float32"), R.Tensor((96,), dtype="float32"), R.Tensor((1, 96, 1), dtype="float32"), R.Tensor((96, 1, 1), dtype="float32"), R.Tensor((96, 96, 1), dtype="float32"), R.Tensor((96,), dtype="float32"), R.Tensor((1, 96, 1), dtype="float32"), R.Tensor((96, 1, 1), dtype="float32"), R.Tensor((96, 96, 7), dtype="float32"), R.Tensor((96,), dtype="float32"), R.Tensor((1, 96, 1), dtype="float32"), R.Tensor((96, 1, 1), dtype="float32"), R.Tensor((96, 96, 1), dtype="float32"), R.Tensor((96,), dtype="float32"), R.Tensor((1, 96, 1), dtype="float32"), R.Tensor((1, 1, 1), dtype="float32"), R.Tensor((1, 96, 7), dtype="float32"), R.Tensor((1,), dtype="float32"))) -> R.Tuple(R.Tuple(R.Tensor((1, 1024, 1), dtype="float32"), R.Tuple(R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"))), R.Tuple(R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object)):
        R.func_attr({"num_input": 166})
        cls = Module
        with R.dataflow():
            encoder_block_layers_0_weight_g: R.Tensor((64, 1, 1), dtype="float32") = packed_params[0]
            encoder_block_layers_0_weight_v: R.Tensor((64, 1, 7), dtype="float32") = packed_params[1]
            encoder_block_layers_0_bias: R.Tensor((64,), dtype="float32") = packed_params[2]
            encoder_block_layers_1_block_layers_0_block_branches_0_layers_0_alpha: R.Tensor((1, 64, 1), dtype="float32") = packed_params[3]
            encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_weight_g: R.Tensor((64, 1, 1), dtype="float32") = packed_params[4]
            encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_weight_v: R.Tensor((64, 64, 7), dtype="float32") = packed_params[5]
            encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_bias: R.Tensor((64,), dtype="float32") = packed_params[6]
            encoder_block_layers_1_block_layers_0_block_branches_0_layers_2_alpha: R.Tensor((1, 64, 1), dtype="float32") = packed_params[7]
            encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_weight_g: R.Tensor((64, 1, 1), dtype="float32") = packed_params[8]
            encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_weight_v: R.Tensor((64, 64, 1), dtype="float32") = packed_params[9]
            encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_bias: R.Tensor((64,), dtype="float32") = packed_params[10]
            encoder_block_layers_1_block_layers_1_block_branches_0_layers_0_alpha: R.Tensor((1, 64, 1), dtype="float32") = packed_params[11]
            encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_weight_g: R.Tensor((64, 1, 1), dtype="float32") = packed_params[12]
            encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_weight_v: R.Tensor((64, 64, 7), dtype="float32") = packed_params[13]
            encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_bias: R.Tensor((64,), dtype="float32") = packed_params[14]
            encoder_block_layers_1_block_layers_1_block_branches_0_layers_2_alpha: R.Tensor((1, 64, 1), dtype="float32") = packed_params[15]
            encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_weight_g: R.Tensor((64, 1, 1), dtype="float32") = packed_params[16]
            encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_weight_v: R.Tensor((64, 64, 1), dtype="float32") = packed_params[17]
            encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_bias: R.Tensor((64,), dtype="float32") = packed_params[18]
            encoder_block_layers_1_block_layers_2_block_branches_0_layers_0_alpha: R.Tensor((1, 64, 1), dtype="float32") = packed_params[19]
            encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_weight_g: R.Tensor((64, 1, 1), dtype="float32") = packed_params[20]
            encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_weight_v: R.Tensor((64, 64, 7), dtype="float32") = packed_params[21]
            encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_bias: R.Tensor((64,), dtype="float32") = packed_params[22]
            encoder_block_layers_1_block_layers_2_block_branches_0_layers_2_alpha: R.Tensor((1, 64, 1), dtype="float32") = packed_params[23]
            encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_weight_g: R.Tensor((64, 1, 1), dtype="float32") = packed_params[24]
            encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_weight_v: R.Tensor((64, 64, 1), dtype="float32") = packed_params[25]
            encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_bias: R.Tensor((64,), dtype="float32") = packed_params[26]
            encoder_block_layers_1_block_layers_3_alpha: R.Tensor((1, 64, 1), dtype="float32") = packed_params[27]
            encoder_block_layers_1_block_layers_4_weight_g: R.Tensor((128, 1, 1), dtype="float32") = packed_params[28]
            encoder_block_layers_1_block_layers_4_weight_v: R.Tensor((128, 64, 4), dtype="float32") = packed_params[29]
            encoder_block_layers_1_block_layers_4_bias: R.Tensor((128,), dtype="float32") = packed_params[30]
            encoder_block_layers_2_block_layers_0_block_branches_0_layers_0_alpha: R.Tensor((1, 128, 1), dtype="float32") = packed_params[31]
            encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_weight_g: R.Tensor((128, 1, 1), dtype="float32") = packed_params[32]
            encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_weight_v: R.Tensor((128, 128, 7), dtype="float32") = packed_params[33]
            encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_bias: R.Tensor((128,), dtype="float32") = packed_params[34]
            encoder_block_layers_2_block_layers_0_block_branches_0_layers_2_alpha: R.Tensor((1, 128, 1), dtype="float32") = packed_params[35]
            encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_weight_g: R.Tensor((128, 1, 1), dtype="float32") = packed_params[36]
            encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_weight_v: R.Tensor((128, 128, 1), dtype="float32") = packed_params[37]
            encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_bias: R.Tensor((128,), dtype="float32") = packed_params[38]
            encoder_block_layers_2_block_layers_1_block_branches_0_layers_0_alpha: R.Tensor((1, 128, 1), dtype="float32") = packed_params[39]
            encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_weight_g: R.Tensor((128, 1, 1), dtype="float32") = packed_params[40]
            encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_weight_v: R.Tensor((128, 128, 7), dtype="float32") = packed_params[41]
            encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_bias: R.Tensor((128,), dtype="float32") = packed_params[42]
            encoder_block_layers_2_block_layers_1_block_branches_0_layers_2_alpha: R.Tensor((1, 128, 1), dtype="float32") = packed_params[43]
            encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_weight_g: R.Tensor((128, 1, 1), dtype="float32") = packed_params[44]
            encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_weight_v: R.Tensor((128, 128, 1), dtype="float32") = packed_params[45]
            encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_bias: R.Tensor((128,), dtype="float32") = packed_params[46]
            encoder_block_layers_2_block_layers_2_block_branches_0_layers_0_alpha: R.Tensor((1, 128, 1), dtype="float32") = packed_params[47]
            encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_weight_g: R.Tensor((128, 1, 1), dtype="float32") = packed_params[48]
            encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_weight_v: R.Tensor((128, 128, 7), dtype="float32") = packed_params[49]
            encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_bias: R.Tensor((128,), dtype="float32") = packed_params[50]
            encoder_block_layers_2_block_layers_2_block_branches_0_layers_2_alpha: R.Tensor((1, 128, 1), dtype="float32") = packed_params[51]
            encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_weight_g: R.Tensor((128, 1, 1), dtype="float32") = packed_params[52]
            encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_weight_v: R.Tensor((128, 128, 1), dtype="float32") = packed_params[53]
            encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_bias: R.Tensor((128,), dtype="float32") = packed_params[54]
            encoder_block_layers_2_block_layers_3_alpha: R.Tensor((1, 128, 1), dtype="float32") = packed_params[55]
            encoder_block_layers_2_block_layers_4_weight_g: R.Tensor((256, 1, 1), dtype="float32") = packed_params[56]
            encoder_block_layers_2_block_layers_4_weight_v: R.Tensor((256, 128, 8), dtype="float32") = packed_params[57]
            encoder_block_layers_2_block_layers_4_bias: R.Tensor((256,), dtype="float32") = packed_params[58]
            encoder_block_layers_3_block_layers_0_block_branches_0_layers_0_alpha: R.Tensor((1, 256, 1), dtype="float32") = packed_params[59]
            encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_weight_g: R.Tensor((256, 1, 1), dtype="float32") = packed_params[60]
            encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_weight_v: R.Tensor((256, 256, 7), dtype="float32") = packed_params[61]
            encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_bias: R.Tensor((256,), dtype="float32") = packed_params[62]
            encoder_block_layers_3_block_layers_0_block_branches_0_layers_2_alpha: R.Tensor((1, 256, 1), dtype="float32") = packed_params[63]
            encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_weight_g: R.Tensor((256, 1, 1), dtype="float32") = packed_params[64]
            encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_weight_v: R.Tensor((256, 256, 1), dtype="float32") = packed_params[65]
            encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_bias: R.Tensor((256,), dtype="float32") = packed_params[66]
            encoder_block_layers_3_block_layers_1_block_branches_0_layers_0_alpha: R.Tensor((1, 256, 1), dtype="float32") = packed_params[67]
            encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_weight_g: R.Tensor((256, 1, 1), dtype="float32") = packed_params[68]
            encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_weight_v: R.Tensor((256, 256, 7), dtype="float32") = packed_params[69]
            encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_bias: R.Tensor((256,), dtype="float32") = packed_params[70]
            encoder_block_layers_3_block_layers_1_block_branches_0_layers_2_alpha: R.Tensor((1, 256, 1), dtype="float32") = packed_params[71]
            encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_weight_g: R.Tensor((256, 1, 1), dtype="float32") = packed_params[72]
            encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_weight_v: R.Tensor((256, 256, 1), dtype="float32") = packed_params[73]
            encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_bias: R.Tensor((256,), dtype="float32") = packed_params[74]
            encoder_block_layers_3_block_layers_2_block_branches_0_layers_0_alpha: R.Tensor((1, 256, 1), dtype="float32") = packed_params[75]
            encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_weight_g: R.Tensor((256, 1, 1), dtype="float32") = packed_params[76]
            encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_weight_v: R.Tensor((256, 256, 7), dtype="float32") = packed_params[77]
            encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_bias: R.Tensor((256,), dtype="float32") = packed_params[78]
            encoder_block_layers_3_block_layers_2_block_branches_0_layers_2_alpha: R.Tensor((1, 256, 1), dtype="float32") = packed_params[79]
            encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_weight_g: R.Tensor((256, 1, 1), dtype="float32") = packed_params[80]
            encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_weight_v: R.Tensor((256, 256, 1), dtype="float32") = packed_params[81]
            encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_bias: R.Tensor((256,), dtype="float32") = packed_params[82]
            encoder_block_layers_3_block_layers_3_alpha: R.Tensor((1, 256, 1), dtype="float32") = packed_params[83]
            encoder_block_layers_3_block_layers_4_weight_g: R.Tensor((512, 1, 1), dtype="float32") = packed_params[84]
            encoder_block_layers_3_block_layers_4_weight_v: R.Tensor((512, 256, 16), dtype="float32") = packed_params[85]
            encoder_block_layers_3_block_layers_4_bias: R.Tensor((512,), dtype="float32") = packed_params[86]
            encoder_block_layers_4_block_layers_0_block_branches_0_layers_0_alpha: R.Tensor((1, 512, 1), dtype="float32") = packed_params[87]
            encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_weight_g: R.Tensor((512, 1, 1), dtype="float32") = packed_params[88]
            encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_weight_v: R.Tensor((512, 512, 7), dtype="float32") = packed_params[89]
            encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_bias: R.Tensor((512,), dtype="float32") = packed_params[90]
            encoder_block_layers_4_block_layers_0_block_branches_0_layers_2_alpha: R.Tensor((1, 512, 1), dtype="float32") = packed_params[91]
            encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_weight_g: R.Tensor((512, 1, 1), dtype="float32") = packed_params[92]
            encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_weight_v: R.Tensor((512, 512, 1), dtype="float32") = packed_params[93]
            encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_bias: R.Tensor((512,), dtype="float32") = packed_params[94]
            encoder_block_layers_4_block_layers_1_block_branches_0_layers_0_alpha: R.Tensor((1, 512, 1), dtype="float32") = packed_params[95]
            encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_weight_g: R.Tensor((512, 1, 1), dtype="float32") = packed_params[96]
            encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_weight_v: R.Tensor((512, 512, 7), dtype="float32") = packed_params[97]
            encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_bias: R.Tensor((512,), dtype="float32") = packed_params[98]
            encoder_block_layers_4_block_layers_1_block_branches_0_layers_2_alpha: R.Tensor((1, 512, 1), dtype="float32") = packed_params[99]
            encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_weight_g: R.Tensor((512, 1, 1), dtype="float32") = packed_params[100]
            encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_weight_v: R.Tensor((512, 512, 1), dtype="float32") = packed_params[101]
            encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_bias: R.Tensor((512,), dtype="float32") = packed_params[102]
            encoder_block_layers_4_block_layers_2_block_branches_0_layers_0_alpha: R.Tensor((1, 512, 1), dtype="float32") = packed_params[103]
            encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_weight_g: R.Tensor((512, 1, 1), dtype="float32") = packed_params[104]
            encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_weight_v: R.Tensor((512, 512, 7), dtype="float32") = packed_params[105]
            encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_bias: R.Tensor((512,), dtype="float32") = packed_params[106]
            encoder_block_layers_4_block_layers_2_block_branches_0_layers_2_alpha: R.Tensor((1, 512, 1), dtype="float32") = packed_params[107]
            encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_weight_g: R.Tensor((512, 1, 1), dtype="float32") = packed_params[108]
            encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_weight_v: R.Tensor((512, 512, 1), dtype="float32") = packed_params[109]
            encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_bias: R.Tensor((512,), dtype="float32") = packed_params[110]
            encoder_block_layers_4_block_layers_3_alpha: R.Tensor((1, 512, 1), dtype="float32") = packed_params[111]
            encoder_block_layers_4_block_layers_4_weight_g: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[112]
            encoder_block_layers_4_block_layers_4_weight_v: R.Tensor((1024, 512, 16), dtype="float32") = packed_params[113]
            encoder_block_layers_4_block_layers_4_bias: R.Tensor((1024,), dtype="float32") = packed_params[114]
            encoder_block_layers_5_alpha: R.Tensor((1, 1024, 1), dtype="float32") = packed_params[115]
            encoder_block_layers_6_weight_g: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[116]
            encoder_block_layers_6_weight_v: R.Tensor((1024, 1024, 3), dtype="float32") = packed_params[117]
            encoder_block_layers_6_bias: R.Tensor((1024,), dtype="float32") = packed_params[118]
            quantizer_quantizers_0_in_proj_weight_g: R.Tensor((8, 1, 1), dtype="float32") = packed_params[119]
            quantizer_quantizers_0_in_proj_weight_v: R.Tensor((8, 1024, 1), dtype="float32") = packed_params[120]
            quantizer_quantizers_0_in_proj_bias: R.Tensor((8,), dtype="float32") = packed_params[121]
            quantizer_quantizers_0_out_proj_weight_g: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[122]
            quantizer_quantizers_0_out_proj_weight_v: R.Tensor((1024, 8, 1), dtype="float32") = packed_params[123]
            quantizer_quantizers_0_out_proj_bias: R.Tensor((1024,), dtype="float32") = packed_params[124]
            quantizer_quantizers_0_codebook_weight: R.Tensor((1024, 8), dtype="float32") = packed_params[125]
            quantizer_quantizers_1_in_proj_weight_g: R.Tensor((8, 1, 1), dtype="float32") = packed_params[126]
            quantizer_quantizers_1_in_proj_weight_v: R.Tensor((8, 1024, 1), dtype="float32") = packed_params[127]
            quantizer_quantizers_1_in_proj_bias: R.Tensor((8,), dtype="float32") = packed_params[128]
            quantizer_quantizers_1_out_proj_weight_g: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[129]
            quantizer_quantizers_1_out_proj_weight_v: R.Tensor((1024, 8, 1), dtype="float32") = packed_params[130]
            quantizer_quantizers_1_out_proj_bias: R.Tensor((1024,), dtype="float32") = packed_params[131]
            quantizer_quantizers_1_codebook_weight: R.Tensor((1024, 8), dtype="float32") = packed_params[132]
            quantizer_quantizers_2_in_proj_weight_g: R.Tensor((8, 1, 1), dtype="float32") = packed_params[133]
            quantizer_quantizers_2_in_proj_weight_v: R.Tensor((8, 1024, 1), dtype="float32") = packed_params[134]
            quantizer_quantizers_2_in_proj_bias: R.Tensor((8,), dtype="float32") = packed_params[135]
            quantizer_quantizers_2_out_proj_weight_g: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[136]
            quantizer_quantizers_2_out_proj_weight_v: R.Tensor((1024, 8, 1), dtype="float32") = packed_params[137]
            quantizer_quantizers_2_out_proj_bias: R.Tensor((1024,), dtype="float32") = packed_params[138]
            quantizer_quantizers_2_codebook_weight: R.Tensor((1024, 8), dtype="float32") = packed_params[139]
            quantizer_quantizers_3_in_proj_weight_g: R.Tensor((8, 1, 1), dtype="float32") = packed_params[140]
            quantizer_quantizers_3_in_proj_weight_v: R.Tensor((8, 1024, 1), dtype="float32") = packed_params[141]
            quantizer_quantizers_3_in_proj_bias: R.Tensor((8,), dtype="float32") = packed_params[142]
            quantizer_quantizers_3_out_proj_weight_g: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[143]
            quantizer_quantizers_3_out_proj_weight_v: R.Tensor((1024, 8, 1), dtype="float32") = packed_params[144]
            quantizer_quantizers_3_out_proj_bias: R.Tensor((1024,), dtype="float32") = packed_params[145]
            quantizer_quantizers_3_codebook_weight: R.Tensor((1024, 8), dtype="float32") = packed_params[146]
            quantizer_quantizers_4_in_proj_weight_g: R.Tensor((8, 1, 1), dtype="float32") = packed_params[147]
            quantizer_quantizers_4_in_proj_weight_v: R.Tensor((8, 1024, 1), dtype="float32") = packed_params[148]
            quantizer_quantizers_4_in_proj_bias: R.Tensor((8,), dtype="float32") = packed_params[149]
            quantizer_quantizers_4_out_proj_weight_g: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[150]
            quantizer_quantizers_4_out_proj_weight_v: R.Tensor((1024, 8, 1), dtype="float32") = packed_params[151]
            quantizer_quantizers_4_out_proj_bias: R.Tensor((1024,), dtype="float32") = packed_params[152]
            quantizer_quantizers_4_codebook_weight: R.Tensor((1024, 8), dtype="float32") = packed_params[153]
            quantizer_quantizers_5_in_proj_weight_g: R.Tensor((8, 1, 1), dtype="float32") = packed_params[154]
            quantizer_quantizers_5_in_proj_weight_v: R.Tensor((8, 1024, 1), dtype="float32") = packed_params[155]
            quantizer_quantizers_5_in_proj_bias: R.Tensor((8,), dtype="float32") = packed_params[156]
            quantizer_quantizers_5_out_proj_weight_g: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[157]
            quantizer_quantizers_5_out_proj_weight_v: R.Tensor((1024, 8, 1), dtype="float32") = packed_params[158]
            quantizer_quantizers_5_out_proj_bias: R.Tensor((1024,), dtype="float32") = packed_params[159]
            quantizer_quantizers_5_codebook_weight: R.Tensor((1024, 8), dtype="float32") = packed_params[160]
            quantizer_quantizers_6_in_proj_weight_g: R.Tensor((8, 1, 1), dtype="float32") = packed_params[161]
            quantizer_quantizers_6_in_proj_weight_v: R.Tensor((8, 1024, 1), dtype="float32") = packed_params[162]
            quantizer_quantizers_6_in_proj_bias: R.Tensor((8,), dtype="float32") = packed_params[163]
            quantizer_quantizers_6_out_proj_weight_g: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[164]
            quantizer_quantizers_6_out_proj_weight_v: R.Tensor((1024, 8, 1), dtype="float32") = packed_params[165]
            quantizer_quantizers_6_out_proj_bias: R.Tensor((1024,), dtype="float32") = packed_params[166]
            quantizer_quantizers_6_codebook_weight: R.Tensor((1024, 8), dtype="float32") = packed_params[167]
            quantizer_quantizers_7_in_proj_weight_g: R.Tensor((8, 1, 1), dtype="float32") = packed_params[168]
            quantizer_quantizers_7_in_proj_weight_v: R.Tensor((8, 1024, 1), dtype="float32") = packed_params[169]
            quantizer_quantizers_7_in_proj_bias: R.Tensor((8,), dtype="float32") = packed_params[170]
            quantizer_quantizers_7_out_proj_weight_g: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[171]
            quantizer_quantizers_7_out_proj_weight_v: R.Tensor((1024, 8, 1), dtype="float32") = packed_params[172]
            quantizer_quantizers_7_out_proj_bias: R.Tensor((1024,), dtype="float32") = packed_params[173]
            quantizer_quantizers_7_codebook_weight: R.Tensor((1024, 8), dtype="float32") = packed_params[174]
            quantizer_quantizers_8_in_proj_weight_g: R.Tensor((8, 1, 1), dtype="float32") = packed_params[175]
            quantizer_quantizers_8_in_proj_weight_v: R.Tensor((8, 1024, 1), dtype="float32") = packed_params[176]
            quantizer_quantizers_8_in_proj_bias: R.Tensor((8,), dtype="float32") = packed_params[177]
            quantizer_quantizers_8_out_proj_weight_g: R.Tensor((1024, 1, 1), dtype="float32") = packed_params[178]
            quantizer_quantizers_8_out_proj_weight_v: R.Tensor((1024, 8, 1), dtype="float32") = packed_params[179]
            quantizer_quantizers_8_out_proj_bias: R.Tensor((1024,), dtype="float32") = packed_params[180]
            quantizer_quantizers_8_codebook_weight: R.Tensor((1024, 8), dtype="float32") = packed_params[181]
            decoder_model_layers_0_weight_g: R.Tensor((1536, 1, 1), dtype="float32") = packed_params[182]
            decoder_model_layers_0_weight_v: R.Tensor((1536, 1024, 7), dtype="float32") = packed_params[183]
            decoder_model_layers_0_bias: R.Tensor((1536,), dtype="float32") = packed_params[184]
            decoder_model_layers_1_block_layers_0_alpha: R.Tensor((1, 1536, 1), dtype="float32") = packed_params[185]
            decoder_model_layers_1_block_layers_1_weight_g: R.Tensor((1536, 1, 1), dtype="float32") = packed_params[186]
            decoder_model_layers_1_block_layers_1_weight_v: R.Tensor((1536, 768, 16), dtype="float32") = packed_params[187]
            decoder_model_layers_1_block_layers_1_bias: R.Tensor((768,), dtype="float32") = packed_params[188]
            decoder_model_layers_1_block_layers_2_block_branches_0_layers_0_alpha: R.Tensor((1, 768, 1), dtype="float32") = packed_params[189]
            decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_weight_g: R.Tensor((768, 1, 1), dtype="float32") = packed_params[190]
            decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_weight_v: R.Tensor((768, 768, 7), dtype="float32") = packed_params[191]
            decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_bias: R.Tensor((768,), dtype="float32") = packed_params[192]
            decoder_model_layers_1_block_layers_2_block_branches_0_layers_2_alpha: R.Tensor((1, 768, 1), dtype="float32") = packed_params[193]
            decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_weight_g: R.Tensor((768, 1, 1), dtype="float32") = packed_params[194]
            decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_weight_v: R.Tensor((768, 768, 1), dtype="float32") = packed_params[195]
            decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_bias: R.Tensor((768,), dtype="float32") = packed_params[196]
            decoder_model_layers_1_block_layers_3_block_branches_0_layers_0_alpha: R.Tensor((1, 768, 1), dtype="float32") = packed_params[197]
            decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_weight_g: R.Tensor((768, 1, 1), dtype="float32") = packed_params[198]
            decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_weight_v: R.Tensor((768, 768, 7), dtype="float32") = packed_params[199]
            decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_bias: R.Tensor((768,), dtype="float32") = packed_params[200]
            decoder_model_layers_1_block_layers_3_block_branches_0_layers_2_alpha: R.Tensor((1, 768, 1), dtype="float32") = packed_params[201]
            decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_weight_g: R.Tensor((768, 1, 1), dtype="float32") = packed_params[202]
            decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_weight_v: R.Tensor((768, 768, 1), dtype="float32") = packed_params[203]
            decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_bias: R.Tensor((768,), dtype="float32") = packed_params[204]
            decoder_model_layers_1_block_layers_4_block_branches_0_layers_0_alpha: R.Tensor((1, 768, 1), dtype="float32") = packed_params[205]
            decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_weight_g: R.Tensor((768, 1, 1), dtype="float32") = packed_params[206]
            decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_weight_v: R.Tensor((768, 768, 7), dtype="float32") = packed_params[207]
            decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_bias: R.Tensor((768,), dtype="float32") = packed_params[208]
            decoder_model_layers_1_block_layers_4_block_branches_0_layers_2_alpha: R.Tensor((1, 768, 1), dtype="float32") = packed_params[209]
            decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_weight_g: R.Tensor((768, 1, 1), dtype="float32") = packed_params[210]
            decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_weight_v: R.Tensor((768, 768, 1), dtype="float32") = packed_params[211]
            decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_bias: R.Tensor((768,), dtype="float32") = packed_params[212]
            decoder_model_layers_2_block_layers_0_alpha: R.Tensor((1, 768, 1), dtype="float32") = packed_params[213]
            decoder_model_layers_2_block_layers_1_weight_g: R.Tensor((768, 1, 1), dtype="float32") = packed_params[214]
            decoder_model_layers_2_block_layers_1_weight_v: R.Tensor((768, 384, 16), dtype="float32") = packed_params[215]
            decoder_model_layers_2_block_layers_1_bias: R.Tensor((384,), dtype="float32") = packed_params[216]
            decoder_model_layers_2_block_layers_2_block_branches_0_layers_0_alpha: R.Tensor((1, 384, 1), dtype="float32") = packed_params[217]
            decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_weight_g: R.Tensor((384, 1, 1), dtype="float32") = packed_params[218]
            decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_weight_v: R.Tensor((384, 384, 7), dtype="float32") = packed_params[219]
            decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_bias: R.Tensor((384,), dtype="float32") = packed_params[220]
            decoder_model_layers_2_block_layers_2_block_branches_0_layers_2_alpha: R.Tensor((1, 384, 1), dtype="float32") = packed_params[221]
            decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_weight_g: R.Tensor((384, 1, 1), dtype="float32") = packed_params[222]
            decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_weight_v: R.Tensor((384, 384, 1), dtype="float32") = packed_params[223]
            decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_bias: R.Tensor((384,), dtype="float32") = packed_params[224]
            decoder_model_layers_2_block_layers_3_block_branches_0_layers_0_alpha: R.Tensor((1, 384, 1), dtype="float32") = packed_params[225]
            decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_weight_g: R.Tensor((384, 1, 1), dtype="float32") = packed_params[226]
            decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_weight_v: R.Tensor((384, 384, 7), dtype="float32") = packed_params[227]
            decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_bias: R.Tensor((384,), dtype="float32") = packed_params[228]
            decoder_model_layers_2_block_layers_3_block_branches_0_layers_2_alpha: R.Tensor((1, 384, 1), dtype="float32") = packed_params[229]
            decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_weight_g: R.Tensor((384, 1, 1), dtype="float32") = packed_params[230]
            decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_weight_v: R.Tensor((384, 384, 1), dtype="float32") = packed_params[231]
            decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_bias: R.Tensor((384,), dtype="float32") = packed_params[232]
            decoder_model_layers_2_block_layers_4_block_branches_0_layers_0_alpha: R.Tensor((1, 384, 1), dtype="float32") = packed_params[233]
            decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_weight_g: R.Tensor((384, 1, 1), dtype="float32") = packed_params[234]
            decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_weight_v: R.Tensor((384, 384, 7), dtype="float32") = packed_params[235]
            decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_bias: R.Tensor((384,), dtype="float32") = packed_params[236]
            decoder_model_layers_2_block_layers_4_block_branches_0_layers_2_alpha: R.Tensor((1, 384, 1), dtype="float32") = packed_params[237]
            decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_weight_g: R.Tensor((384, 1, 1), dtype="float32") = packed_params[238]
            decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_weight_v: R.Tensor((384, 384, 1), dtype="float32") = packed_params[239]
            decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_bias: R.Tensor((384,), dtype="float32") = packed_params[240]
            decoder_model_layers_3_block_layers_0_alpha: R.Tensor((1, 384, 1), dtype="float32") = packed_params[241]
            decoder_model_layers_3_block_layers_1_weight_g: R.Tensor((384, 1, 1), dtype="float32") = packed_params[242]
            decoder_model_layers_3_block_layers_1_weight_v: R.Tensor((384, 192, 8), dtype="float32") = packed_params[243]
            decoder_model_layers_3_block_layers_1_bias: R.Tensor((192,), dtype="float32") = packed_params[244]
            decoder_model_layers_3_block_layers_2_block_branches_0_layers_0_alpha: R.Tensor((1, 192, 1), dtype="float32") = packed_params[245]
            decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_weight_g: R.Tensor((192, 1, 1), dtype="float32") = packed_params[246]
            decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_weight_v: R.Tensor((192, 192, 7), dtype="float32") = packed_params[247]
            decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_bias: R.Tensor((192,), dtype="float32") = packed_params[248]
            decoder_model_layers_3_block_layers_2_block_branches_0_layers_2_alpha: R.Tensor((1, 192, 1), dtype="float32") = packed_params[249]
            decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_weight_g: R.Tensor((192, 1, 1), dtype="float32") = packed_params[250]
            decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_weight_v: R.Tensor((192, 192, 1), dtype="float32") = packed_params[251]
            decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_bias: R.Tensor((192,), dtype="float32") = packed_params[252]
            decoder_model_layers_3_block_layers_3_block_branches_0_layers_0_alpha: R.Tensor((1, 192, 1), dtype="float32") = packed_params[253]
            decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_weight_g: R.Tensor((192, 1, 1), dtype="float32") = packed_params[254]
            decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_weight_v: R.Tensor((192, 192, 7), dtype="float32") = packed_params[255]
            decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_bias: R.Tensor((192,), dtype="float32") = packed_params[256]
            decoder_model_layers_3_block_layers_3_block_branches_0_layers_2_alpha: R.Tensor((1, 192, 1), dtype="float32") = packed_params[257]
            decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_weight_g: R.Tensor((192, 1, 1), dtype="float32") = packed_params[258]
            decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_weight_v: R.Tensor((192, 192, 1), dtype="float32") = packed_params[259]
            decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_bias: R.Tensor((192,), dtype="float32") = packed_params[260]
            decoder_model_layers_3_block_layers_4_block_branches_0_layers_0_alpha: R.Tensor((1, 192, 1), dtype="float32") = packed_params[261]
            decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_weight_g: R.Tensor((192, 1, 1), dtype="float32") = packed_params[262]
            decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_weight_v: R.Tensor((192, 192, 7), dtype="float32") = packed_params[263]
            decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_bias: R.Tensor((192,), dtype="float32") = packed_params[264]
            decoder_model_layers_3_block_layers_4_block_branches_0_layers_2_alpha: R.Tensor((1, 192, 1), dtype="float32") = packed_params[265]
            decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_weight_g: R.Tensor((192, 1, 1), dtype="float32") = packed_params[266]
            decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_weight_v: R.Tensor((192, 192, 1), dtype="float32") = packed_params[267]
            decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_bias: R.Tensor((192,), dtype="float32") = packed_params[268]
            decoder_model_layers_4_block_layers_0_alpha: R.Tensor((1, 192, 1), dtype="float32") = packed_params[269]
            decoder_model_layers_4_block_layers_1_weight_g: R.Tensor((192, 1, 1), dtype="float32") = packed_params[270]
            decoder_model_layers_4_block_layers_1_weight_v: R.Tensor((192, 96, 4), dtype="float32") = packed_params[271]
            decoder_model_layers_4_block_layers_1_bias: R.Tensor((96,), dtype="float32") = packed_params[272]
            decoder_model_layers_4_block_layers_2_block_branches_0_layers_0_alpha: R.Tensor((1, 96, 1), dtype="float32") = packed_params[273]
            decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_weight_g: R.Tensor((96, 1, 1), dtype="float32") = packed_params[274]
            decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_weight_v: R.Tensor((96, 96, 7), dtype="float32") = packed_params[275]
            decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_bias: R.Tensor((96,), dtype="float32") = packed_params[276]
            decoder_model_layers_4_block_layers_2_block_branches_0_layers_2_alpha: R.Tensor((1, 96, 1), dtype="float32") = packed_params[277]
            decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_weight_g: R.Tensor((96, 1, 1), dtype="float32") = packed_params[278]
            decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_weight_v: R.Tensor((96, 96, 1), dtype="float32") = packed_params[279]
            decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_bias: R.Tensor((96,), dtype="float32") = packed_params[280]
            decoder_model_layers_4_block_layers_3_block_branches_0_layers_0_alpha: R.Tensor((1, 96, 1), dtype="float32") = packed_params[281]
            decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_weight_g: R.Tensor((96, 1, 1), dtype="float32") = packed_params[282]
            decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_weight_v: R.Tensor((96, 96, 7), dtype="float32") = packed_params[283]
            decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_bias: R.Tensor((96,), dtype="float32") = packed_params[284]
            decoder_model_layers_4_block_layers_3_block_branches_0_layers_2_alpha: R.Tensor((1, 96, 1), dtype="float32") = packed_params[285]
            decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_weight_g: R.Tensor((96, 1, 1), dtype="float32") = packed_params[286]
            decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_weight_v: R.Tensor((96, 96, 1), dtype="float32") = packed_params[287]
            decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_bias: R.Tensor((96,), dtype="float32") = packed_params[288]
            decoder_model_layers_4_block_layers_4_block_branches_0_layers_0_alpha: R.Tensor((1, 96, 1), dtype="float32") = packed_params[289]
            decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_weight_g: R.Tensor((96, 1, 1), dtype="float32") = packed_params[290]
            decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_weight_v: R.Tensor((96, 96, 7), dtype="float32") = packed_params[291]
            decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_bias: R.Tensor((96,), dtype="float32") = packed_params[292]
            decoder_model_layers_4_block_layers_4_block_branches_0_layers_2_alpha: R.Tensor((1, 96, 1), dtype="float32") = packed_params[293]
            decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_weight_g: R.Tensor((96, 1, 1), dtype="float32") = packed_params[294]
            decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_weight_v: R.Tensor((96, 96, 1), dtype="float32") = packed_params[295]
            decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_bias: R.Tensor((96,), dtype="float32") = packed_params[296]
            decoder_model_layers_5_alpha: R.Tensor((1, 96, 1), dtype="float32") = packed_params[297]
            decoder_model_layers_6_weight_g: R.Tensor((1, 1, 1), dtype="float32") = packed_params[298]
            decoder_model_layers_6_weight_v: R.Tensor((1, 96, 7), dtype="float32") = packed_params[299]
            decoder_model_layers_6_bias: R.Tensor((1,), dtype="float32") = packed_params[300]
            lv1: R.Tensor((1, 1, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_0_downsampling_delay_cache, audio_data, sinfo_args=(R.Tensor((1, 1, 512), dtype="float32"),))
            lv2: R.Tensor((1, 1, 518), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_0_cache_cache, lv1, sinfo_args=(R.Tensor((1, 1, 518), dtype="float32"),))
            lv3: R.Tensor((64, 1, 7), dtype="float32") = R.square(encoder_block_layers_0_weight_v)
            lv4: R.Tensor((64, 1, 1), dtype="float32") = R.sum(lv3, axis=[1, 2], keepdims=True)
            lv5: R.Tensor((64, 1, 1), dtype="float32") = R.sqrt(lv4)
            lv6: R.Tensor((64, 1, 7), dtype="float32") = R.divide(encoder_block_layers_0_weight_v, lv5)
            wnconv1d: R.Tensor((64, 1, 7), dtype="float32") = R.multiply(encoder_block_layers_0_weight_g, lv6)
            lv7: R.Tensor((1, 64, 512), dtype="float32") = R.nn.conv1d(lv2, wnconv1d, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv8: R.Tensor((1, 64, 1), dtype="float32") = R.reshape(encoder_block_layers_0_bias, R.shape([1, 64, 1]))
            conv1d: R.Tensor((1, 64, 512), dtype="float32") = R.add(lv7, lv8)
            lv9: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_0_block_paddings_0_cache, conv1d, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            reshape: R.Tensor((1, 64, 512), dtype="float32") = R.reshape(lv9, R.shape([1, 64, 512]))
            lv10 = R.call_tir(cls.snake, (reshape, encoder_block_layers_1_block_layers_0_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 64, 512), dtype="float32"))
            reshape1: R.Tensor((1, 64, 512), dtype="float32") = R.reshape(lv10, R.shape([1, 64, 512]))
            lv11: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, reshape1, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv12: R.Tensor((1, 64, 518), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_cache_cache, lv11, sinfo_args=(R.Tensor((1, 64, 518), dtype="float32"),))
            lv13: R.Tensor((64, 64, 7), dtype="float32") = R.square(encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_weight_v)
            lv14: R.Tensor((64, 1, 1), dtype="float32") = R.sum(lv13, axis=[1, 2], keepdims=True)
            lv15: R.Tensor((64, 1, 1), dtype="float32") = R.sqrt(lv14)
            lv16: R.Tensor((64, 64, 7), dtype="float32") = R.divide(encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_weight_v, lv15)
            wnconv1d1: R.Tensor((64, 64, 7), dtype="float32") = R.multiply(encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_weight_g, lv16)
            lv17: R.Tensor((1, 64, 512), dtype="float32") = R.nn.conv1d(lv12, wnconv1d1, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv18: R.Tensor((1, 64, 1), dtype="float32") = R.reshape(encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_bias, R.shape([1, 64, 1]))
            conv1d1: R.Tensor((1, 64, 512), dtype="float32") = R.add(lv17, lv18)
            reshape2: R.Tensor((1, 64, 512), dtype="float32") = R.reshape(conv1d1, R.shape([1, 64, 512]))
            lv19 = R.call_tir(cls.snake, (reshape2, encoder_block_layers_1_block_layers_0_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 64, 512), dtype="float32"))
            reshape3: R.Tensor((1, 64, 512), dtype="float32") = R.reshape(lv19, R.shape([1, 64, 512]))
            lv20: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, reshape3, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv21: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_cache_cache, lv20, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv22: R.Tensor((64, 64, 1), dtype="float32") = R.square(encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_weight_v)
            lv23: R.Tensor((64, 1, 1), dtype="float32") = R.sum(lv22, axis=[1, 2], keepdims=True)
            lv24: R.Tensor((64, 1, 1), dtype="float32") = R.sqrt(lv23)
            lv25: R.Tensor((64, 64, 1), dtype="float32") = R.divide(encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_weight_v, lv24)
            wnconv1d2: R.Tensor((64, 64, 1), dtype="float32") = R.multiply(encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_weight_g, lv25)
            lv26: R.Tensor((1, 64, 512), dtype="float32") = R.nn.conv1d(lv21, wnconv1d2, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv27: R.Tensor((1, 64, 1), dtype="float32") = R.reshape(encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_bias, R.shape([1, 64, 1]))
            conv1d2: R.Tensor((1, 64, 512), dtype="float32") = R.add(lv26, lv27)
            lv28: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_0_block_paddings_1_cache, conv1d, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            add: R.Tensor((1, 64, 512), dtype="float32") = R.add(conv1d2, R.const(0.0, "float32"))
            add1: R.Tensor((1, 64, 512), dtype="float32") = R.add(add, lv28)
            lv29: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_1_block_paddings_0_cache, add1, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            reshape4: R.Tensor((1, 64, 512), dtype="float32") = R.reshape(lv29, R.shape([1, 64, 512]))
            lv30 = R.call_tir(cls.snake, (reshape4, encoder_block_layers_1_block_layers_1_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 64, 512), dtype="float32"))
            reshape5: R.Tensor((1, 64, 512), dtype="float32") = R.reshape(lv30, R.shape([1, 64, 512]))
            lv31: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, reshape5, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv32: R.Tensor((1, 64, 530), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_cache_cache, lv31, sinfo_args=(R.Tensor((1, 64, 530), dtype="float32"),))
            lv33: R.Tensor((64, 64, 7), dtype="float32") = R.square(encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_weight_v)
            lv34: R.Tensor((64, 1, 1), dtype="float32") = R.sum(lv33, axis=[1, 2], keepdims=True)
            lv35: R.Tensor((64, 1, 1), dtype="float32") = R.sqrt(lv34)
            lv36: R.Tensor((64, 64, 7), dtype="float32") = R.divide(encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_weight_v, lv35)
            wnconv1d3: R.Tensor((64, 64, 7), dtype="float32") = R.multiply(encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_weight_g, lv36)
            lv37: R.Tensor((1, 64, 512), dtype="float32") = R.nn.conv1d(lv32, wnconv1d3, strides=[1], padding=[0, 0], dilation=[3], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv38: R.Tensor((1, 64, 1), dtype="float32") = R.reshape(encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_bias, R.shape([1, 64, 1]))
            conv1d3: R.Tensor((1, 64, 512), dtype="float32") = R.add(lv37, lv38)
            reshape6: R.Tensor((1, 64, 512), dtype="float32") = R.reshape(conv1d3, R.shape([1, 64, 512]))
            lv39 = R.call_tir(cls.snake, (reshape6, encoder_block_layers_1_block_layers_1_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 64, 512), dtype="float32"))
            reshape7: R.Tensor((1, 64, 512), dtype="float32") = R.reshape(lv39, R.shape([1, 64, 512]))
            lv40: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, reshape7, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv41: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_cache_cache, lv40, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv42: R.Tensor((64, 64, 1), dtype="float32") = R.square(encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_weight_v)
            lv43: R.Tensor((64, 1, 1), dtype="float32") = R.sum(lv42, axis=[1, 2], keepdims=True)
            lv44: R.Tensor((64, 1, 1), dtype="float32") = R.sqrt(lv43)
            lv45: R.Tensor((64, 64, 1), dtype="float32") = R.divide(encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_weight_v, lv44)
            wnconv1d4: R.Tensor((64, 64, 1), dtype="float32") = R.multiply(encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_weight_g, lv45)
            lv46: R.Tensor((1, 64, 512), dtype="float32") = R.nn.conv1d(lv41, wnconv1d4, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv47: R.Tensor((1, 64, 1), dtype="float32") = R.reshape(encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_bias, R.shape([1, 64, 1]))
            conv1d4: R.Tensor((1, 64, 512), dtype="float32") = R.add(lv46, lv47)
            lv48: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_1_block_paddings_1_cache, add1, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            add2: R.Tensor((1, 64, 512), dtype="float32") = R.add(conv1d4, R.const(0.0, "float32"))
            add3: R.Tensor((1, 64, 512), dtype="float32") = R.add(add2, lv48)
            lv49: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_2_block_paddings_0_cache, add3, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            reshape8: R.Tensor((1, 64, 512), dtype="float32") = R.reshape(lv49, R.shape([1, 64, 512]))
            lv50 = R.call_tir(cls.snake, (reshape8, encoder_block_layers_1_block_layers_2_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 64, 512), dtype="float32"))
            reshape9: R.Tensor((1, 64, 512), dtype="float32") = R.reshape(lv50, R.shape([1, 64, 512]))
            lv51: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, reshape9, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv52: R.Tensor((1, 64, 566), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache, lv51, sinfo_args=(R.Tensor((1, 64, 566), dtype="float32"),))
            lv53: R.Tensor((64, 64, 7), dtype="float32") = R.square(encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_weight_v)
            lv54: R.Tensor((64, 1, 1), dtype="float32") = R.sum(lv53, axis=[1, 2], keepdims=True)
            lv55: R.Tensor((64, 1, 1), dtype="float32") = R.sqrt(lv54)
            lv56: R.Tensor((64, 64, 7), dtype="float32") = R.divide(encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_weight_v, lv55)
            wnconv1d5: R.Tensor((64, 64, 7), dtype="float32") = R.multiply(encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_weight_g, lv56)
            lv57: R.Tensor((1, 64, 512), dtype="float32") = R.nn.conv1d(lv52, wnconv1d5, strides=[1], padding=[0, 0], dilation=[9], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv58: R.Tensor((1, 64, 1), dtype="float32") = R.reshape(encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_bias, R.shape([1, 64, 1]))
            conv1d5: R.Tensor((1, 64, 512), dtype="float32") = R.add(lv57, lv58)
            reshape10: R.Tensor((1, 64, 512), dtype="float32") = R.reshape(conv1d5, R.shape([1, 64, 512]))
            lv59 = R.call_tir(cls.snake, (reshape10, encoder_block_layers_1_block_layers_2_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 64, 512), dtype="float32"))
            reshape11: R.Tensor((1, 64, 512), dtype="float32") = R.reshape(lv59, R.shape([1, 64, 512]))
            lv60: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, reshape11, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv61: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache, lv60, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv62: R.Tensor((64, 64, 1), dtype="float32") = R.square(encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_weight_v)
            lv63: R.Tensor((64, 1, 1), dtype="float32") = R.sum(lv62, axis=[1, 2], keepdims=True)
            lv64: R.Tensor((64, 1, 1), dtype="float32") = R.sqrt(lv63)
            lv65: R.Tensor((64, 64, 1), dtype="float32") = R.divide(encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_weight_v, lv64)
            wnconv1d6: R.Tensor((64, 64, 1), dtype="float32") = R.multiply(encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_weight_g, lv65)
            lv66: R.Tensor((1, 64, 512), dtype="float32") = R.nn.conv1d(lv61, wnconv1d6, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv67: R.Tensor((1, 64, 1), dtype="float32") = R.reshape(encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_bias, R.shape([1, 64, 1]))
            conv1d6: R.Tensor((1, 64, 512), dtype="float32") = R.add(lv66, lv67)
            lv68: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_2_block_paddings_1_cache, add3, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            add4: R.Tensor((1, 64, 512), dtype="float32") = R.add(conv1d6, R.const(0.0, "float32"))
            add5: R.Tensor((1, 64, 512), dtype="float32") = R.add(add4, lv68)
            reshape12: R.Tensor((1, 64, 512), dtype="float32") = R.reshape(add5, R.shape([1, 64, 512]))
            lv69 = R.call_tir(cls.snake, (reshape12, encoder_block_layers_1_block_layers_3_alpha), out_sinfo=R.Tensor((1, 64, 512), dtype="float32"))
            reshape13: R.Tensor((1, 64, 512), dtype="float32") = R.reshape(lv69, R.shape([1, 64, 512]))
            lv70: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_4_downsampling_delay_cache, reshape13, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv71: R.Tensor((1, 64, 514), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_4_cache_cache, lv70, sinfo_args=(R.Tensor((1, 64, 514), dtype="float32"),))
            lv72: R.Tensor((128, 64, 4), dtype="float32") = R.square(encoder_block_layers_1_block_layers_4_weight_v)
            lv73: R.Tensor((128, 1, 1), dtype="float32") = R.sum(lv72, axis=[1, 2], keepdims=True)
            lv74: R.Tensor((128, 1, 1), dtype="float32") = R.sqrt(lv73)
            lv75: R.Tensor((128, 64, 4), dtype="float32") = R.divide(encoder_block_layers_1_block_layers_4_weight_v, lv74)
            wnconv1d7: R.Tensor((128, 64, 4), dtype="float32") = R.multiply(encoder_block_layers_1_block_layers_4_weight_g, lv75)
            lv76: R.Tensor((1, 128, 256), dtype="float32") = R.nn.conv1d(lv71, wnconv1d7, strides=[2], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv77: R.Tensor((1, 128, 1), dtype="float32") = R.reshape(encoder_block_layers_1_block_layers_4_bias, R.shape([1, 128, 1]))
            conv1d7: R.Tensor((1, 128, 256), dtype="float32") = R.add(lv76, lv77)
            lv78: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_0_block_paddings_0_cache, conv1d7, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            reshape14: R.Tensor((1, 128, 256), dtype="float32") = R.reshape(lv78, R.shape([1, 128, 256]))
            lv79 = R.call_tir(cls.snake1, (reshape14, encoder_block_layers_2_block_layers_0_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 128, 256), dtype="float32"))
            reshape15: R.Tensor((1, 128, 256), dtype="float32") = R.reshape(lv79, R.shape([1, 128, 256]))
            lv80: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, reshape15, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv81: R.Tensor((1, 128, 262), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_cache_cache, lv80, sinfo_args=(R.Tensor((1, 128, 262), dtype="float32"),))
            lv82: R.Tensor((128, 128, 7), dtype="float32") = R.square(encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_weight_v)
            lv83: R.Tensor((128, 1, 1), dtype="float32") = R.sum(lv82, axis=[1, 2], keepdims=True)
            lv84: R.Tensor((128, 1, 1), dtype="float32") = R.sqrt(lv83)
            lv85: R.Tensor((128, 128, 7), dtype="float32") = R.divide(encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_weight_v, lv84)
            wnconv1d8: R.Tensor((128, 128, 7), dtype="float32") = R.multiply(encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_weight_g, lv85)
            lv86: R.Tensor((1, 128, 256), dtype="float32") = R.nn.conv1d(lv81, wnconv1d8, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv87: R.Tensor((1, 128, 1), dtype="float32") = R.reshape(encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_bias, R.shape([1, 128, 1]))
            conv1d8: R.Tensor((1, 128, 256), dtype="float32") = R.add(lv86, lv87)
            reshape16: R.Tensor((1, 128, 256), dtype="float32") = R.reshape(conv1d8, R.shape([1, 128, 256]))
            lv88 = R.call_tir(cls.snake1, (reshape16, encoder_block_layers_2_block_layers_0_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 128, 256), dtype="float32"))
            reshape17: R.Tensor((1, 128, 256), dtype="float32") = R.reshape(lv88, R.shape([1, 128, 256]))
            lv89: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, reshape17, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv90: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_cache_cache, lv89, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv91: R.Tensor((128, 128, 1), dtype="float32") = R.square(encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_weight_v)
            lv92: R.Tensor((128, 1, 1), dtype="float32") = R.sum(lv91, axis=[1, 2], keepdims=True)
            lv93: R.Tensor((128, 1, 1), dtype="float32") = R.sqrt(lv92)
            lv94: R.Tensor((128, 128, 1), dtype="float32") = R.divide(encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_weight_v, lv93)
            wnconv1d9: R.Tensor((128, 128, 1), dtype="float32") = R.multiply(encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_weight_g, lv94)
            lv95: R.Tensor((1, 128, 256), dtype="float32") = R.nn.conv1d(lv90, wnconv1d9, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv96: R.Tensor((1, 128, 1), dtype="float32") = R.reshape(encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_bias, R.shape([1, 128, 1]))
            conv1d9: R.Tensor((1, 128, 256), dtype="float32") = R.add(lv95, lv96)
            lv97: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_0_block_paddings_1_cache, conv1d7, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            add6: R.Tensor((1, 128, 256), dtype="float32") = R.add(conv1d9, R.const(0.0, "float32"))
            add7: R.Tensor((1, 128, 256), dtype="float32") = R.add(add6, lv97)
            lv98: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_1_block_paddings_0_cache, add7, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            reshape18: R.Tensor((1, 128, 256), dtype="float32") = R.reshape(lv98, R.shape([1, 128, 256]))
            lv99 = R.call_tir(cls.snake1, (reshape18, encoder_block_layers_2_block_layers_1_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 128, 256), dtype="float32"))
            reshape19: R.Tensor((1, 128, 256), dtype="float32") = R.reshape(lv99, R.shape([1, 128, 256]))
            lv100: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, reshape19, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv101: R.Tensor((1, 128, 274), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_cache_cache, lv100, sinfo_args=(R.Tensor((1, 128, 274), dtype="float32"),))
            lv102: R.Tensor((128, 128, 7), dtype="float32") = R.square(encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_weight_v)
            lv103: R.Tensor((128, 1, 1), dtype="float32") = R.sum(lv102, axis=[1, 2], keepdims=True)
            lv104: R.Tensor((128, 1, 1), dtype="float32") = R.sqrt(lv103)
            lv105: R.Tensor((128, 128, 7), dtype="float32") = R.divide(encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_weight_v, lv104)
            wnconv1d10: R.Tensor((128, 128, 7), dtype="float32") = R.multiply(encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_weight_g, lv105)
            lv106: R.Tensor((1, 128, 256), dtype="float32") = R.nn.conv1d(lv101, wnconv1d10, strides=[1], padding=[0, 0], dilation=[3], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv107: R.Tensor((1, 128, 1), dtype="float32") = R.reshape(encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_bias, R.shape([1, 128, 1]))
            conv1d10: R.Tensor((1, 128, 256), dtype="float32") = R.add(lv106, lv107)
            reshape20: R.Tensor((1, 128, 256), dtype="float32") = R.reshape(conv1d10, R.shape([1, 128, 256]))
            lv108 = R.call_tir(cls.snake1, (reshape20, encoder_block_layers_2_block_layers_1_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 128, 256), dtype="float32"))
            reshape21: R.Tensor((1, 128, 256), dtype="float32") = R.reshape(lv108, R.shape([1, 128, 256]))
            lv109: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, reshape21, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv110: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_cache_cache, lv109, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv111: R.Tensor((128, 128, 1), dtype="float32") = R.square(encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_weight_v)
            lv112: R.Tensor((128, 1, 1), dtype="float32") = R.sum(lv111, axis=[1, 2], keepdims=True)
            lv113: R.Tensor((128, 1, 1), dtype="float32") = R.sqrt(lv112)
            lv114: R.Tensor((128, 128, 1), dtype="float32") = R.divide(encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_weight_v, lv113)
            wnconv1d11: R.Tensor((128, 128, 1), dtype="float32") = R.multiply(encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_weight_g, lv114)
            lv115: R.Tensor((1, 128, 256), dtype="float32") = R.nn.conv1d(lv110, wnconv1d11, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv116: R.Tensor((1, 128, 1), dtype="float32") = R.reshape(encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_bias, R.shape([1, 128, 1]))
            conv1d11: R.Tensor((1, 128, 256), dtype="float32") = R.add(lv115, lv116)
            lv117: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_1_block_paddings_1_cache, add7, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            add8: R.Tensor((1, 128, 256), dtype="float32") = R.add(conv1d11, R.const(0.0, "float32"))
            add9: R.Tensor((1, 128, 256), dtype="float32") = R.add(add8, lv117)
            lv118: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_2_block_paddings_0_cache, add9, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            reshape22: R.Tensor((1, 128, 256), dtype="float32") = R.reshape(lv118, R.shape([1, 128, 256]))
            lv119 = R.call_tir(cls.snake1, (reshape22, encoder_block_layers_2_block_layers_2_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 128, 256), dtype="float32"))
            reshape23: R.Tensor((1, 128, 256), dtype="float32") = R.reshape(lv119, R.shape([1, 128, 256]))
            lv120: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, reshape23, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv121: R.Tensor((1, 128, 310), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache, lv120, sinfo_args=(R.Tensor((1, 128, 310), dtype="float32"),))
            lv122: R.Tensor((128, 128, 7), dtype="float32") = R.square(encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_weight_v)
            lv123: R.Tensor((128, 1, 1), dtype="float32") = R.sum(lv122, axis=[1, 2], keepdims=True)
            lv124: R.Tensor((128, 1, 1), dtype="float32") = R.sqrt(lv123)
            lv125: R.Tensor((128, 128, 7), dtype="float32") = R.divide(encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_weight_v, lv124)
            wnconv1d12: R.Tensor((128, 128, 7), dtype="float32") = R.multiply(encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_weight_g, lv125)
            lv126: R.Tensor((1, 128, 256), dtype="float32") = R.nn.conv1d(lv121, wnconv1d12, strides=[1], padding=[0, 0], dilation=[9], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv127: R.Tensor((1, 128, 1), dtype="float32") = R.reshape(encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_bias, R.shape([1, 128, 1]))
            conv1d12: R.Tensor((1, 128, 256), dtype="float32") = R.add(lv126, lv127)
            reshape24: R.Tensor((1, 128, 256), dtype="float32") = R.reshape(conv1d12, R.shape([1, 128, 256]))
            lv128 = R.call_tir(cls.snake1, (reshape24, encoder_block_layers_2_block_layers_2_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 128, 256), dtype="float32"))
            reshape25: R.Tensor((1, 128, 256), dtype="float32") = R.reshape(lv128, R.shape([1, 128, 256]))
            lv129: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, reshape25, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv130: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache, lv129, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv131: R.Tensor((128, 128, 1), dtype="float32") = R.square(encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_weight_v)
            lv132: R.Tensor((128, 1, 1), dtype="float32") = R.sum(lv131, axis=[1, 2], keepdims=True)
            lv133: R.Tensor((128, 1, 1), dtype="float32") = R.sqrt(lv132)
            lv134: R.Tensor((128, 128, 1), dtype="float32") = R.divide(encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_weight_v, lv133)
            wnconv1d13: R.Tensor((128, 128, 1), dtype="float32") = R.multiply(encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_weight_g, lv134)
            lv135: R.Tensor((1, 128, 256), dtype="float32") = R.nn.conv1d(lv130, wnconv1d13, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv136: R.Tensor((1, 128, 1), dtype="float32") = R.reshape(encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_bias, R.shape([1, 128, 1]))
            conv1d13: R.Tensor((1, 128, 256), dtype="float32") = R.add(lv135, lv136)
            lv137: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_2_block_paddings_1_cache, add9, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            add10: R.Tensor((1, 128, 256), dtype="float32") = R.add(conv1d13, R.const(0.0, "float32"))
            add11: R.Tensor((1, 128, 256), dtype="float32") = R.add(add10, lv137)
            reshape26: R.Tensor((1, 128, 256), dtype="float32") = R.reshape(add11, R.shape([1, 128, 256]))
            lv138 = R.call_tir(cls.snake1, (reshape26, encoder_block_layers_2_block_layers_3_alpha), out_sinfo=R.Tensor((1, 128, 256), dtype="float32"))
            reshape27: R.Tensor((1, 128, 256), dtype="float32") = R.reshape(lv138, R.shape([1, 128, 256]))
            lv139: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_4_downsampling_delay_cache, reshape27, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv140: R.Tensor((1, 128, 260), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_4_cache_cache, lv139, sinfo_args=(R.Tensor((1, 128, 260), dtype="float32"),))
            lv141: R.Tensor((256, 128, 8), dtype="float32") = R.square(encoder_block_layers_2_block_layers_4_weight_v)
            lv142: R.Tensor((256, 1, 1), dtype="float32") = R.sum(lv141, axis=[1, 2], keepdims=True)
            lv143: R.Tensor((256, 1, 1), dtype="float32") = R.sqrt(lv142)
            lv144: R.Tensor((256, 128, 8), dtype="float32") = R.divide(encoder_block_layers_2_block_layers_4_weight_v, lv143)
            wnconv1d14: R.Tensor((256, 128, 8), dtype="float32") = R.multiply(encoder_block_layers_2_block_layers_4_weight_g, lv144)
            lv145: R.Tensor((1, 256, 64), dtype="float32") = R.nn.conv1d(lv140, wnconv1d14, strides=[4], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv146: R.Tensor((1, 256, 1), dtype="float32") = R.reshape(encoder_block_layers_2_block_layers_4_bias, R.shape([1, 256, 1]))
            conv1d14: R.Tensor((1, 256, 64), dtype="float32") = R.add(lv145, lv146)
            lv147: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_0_block_paddings_0_cache, conv1d14, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            reshape28: R.Tensor((1, 256, 64), dtype="float32") = R.reshape(lv147, R.shape([1, 256, 64]))
            lv148 = R.call_tir(cls.snake2, (reshape28, encoder_block_layers_3_block_layers_0_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 256, 64), dtype="float32"))
            reshape29: R.Tensor((1, 256, 64), dtype="float32") = R.reshape(lv148, R.shape([1, 256, 64]))
            lv149: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, reshape29, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv150: R.Tensor((1, 256, 70), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_cache_cache, lv149, sinfo_args=(R.Tensor((1, 256, 70), dtype="float32"),))
            lv151: R.Tensor((256, 256, 7), dtype="float32") = R.square(encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_weight_v)
            lv152: R.Tensor((256, 1, 1), dtype="float32") = R.sum(lv151, axis=[1, 2], keepdims=True)
            lv153: R.Tensor((256, 1, 1), dtype="float32") = R.sqrt(lv152)
            lv154: R.Tensor((256, 256, 7), dtype="float32") = R.divide(encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_weight_v, lv153)
            wnconv1d15: R.Tensor((256, 256, 7), dtype="float32") = R.multiply(encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_weight_g, lv154)
            lv155: R.Tensor((1, 256, 64), dtype="float32") = R.nn.conv1d(lv150, wnconv1d15, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv156: R.Tensor((1, 256, 1), dtype="float32") = R.reshape(encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_bias, R.shape([1, 256, 1]))
            conv1d15: R.Tensor((1, 256, 64), dtype="float32") = R.add(lv155, lv156)
            reshape30: R.Tensor((1, 256, 64), dtype="float32") = R.reshape(conv1d15, R.shape([1, 256, 64]))
            lv157 = R.call_tir(cls.snake2, (reshape30, encoder_block_layers_3_block_layers_0_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 256, 64), dtype="float32"))
            reshape31: R.Tensor((1, 256, 64), dtype="float32") = R.reshape(lv157, R.shape([1, 256, 64]))
            lv158: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, reshape31, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv159: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_cache_cache, lv158, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv160: R.Tensor((256, 256, 1), dtype="float32") = R.square(encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_weight_v)
            lv161: R.Tensor((256, 1, 1), dtype="float32") = R.sum(lv160, axis=[1, 2], keepdims=True)
            lv162: R.Tensor((256, 1, 1), dtype="float32") = R.sqrt(lv161)
            lv163: R.Tensor((256, 256, 1), dtype="float32") = R.divide(encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_weight_v, lv162)
            wnconv1d16: R.Tensor((256, 256, 1), dtype="float32") = R.multiply(encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_weight_g, lv163)
            lv164: R.Tensor((1, 256, 64), dtype="float32") = R.nn.conv1d(lv159, wnconv1d16, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv165: R.Tensor((1, 256, 1), dtype="float32") = R.reshape(encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_bias, R.shape([1, 256, 1]))
            conv1d16: R.Tensor((1, 256, 64), dtype="float32") = R.add(lv164, lv165)
            lv166: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_0_block_paddings_1_cache, conv1d14, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            add12: R.Tensor((1, 256, 64), dtype="float32") = R.add(conv1d16, R.const(0.0, "float32"))
            add13: R.Tensor((1, 256, 64), dtype="float32") = R.add(add12, lv166)
            lv167: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_1_block_paddings_0_cache, add13, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            reshape32: R.Tensor((1, 256, 64), dtype="float32") = R.reshape(lv167, R.shape([1, 256, 64]))
            lv168 = R.call_tir(cls.snake2, (reshape32, encoder_block_layers_3_block_layers_1_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 256, 64), dtype="float32"))
            reshape33: R.Tensor((1, 256, 64), dtype="float32") = R.reshape(lv168, R.shape([1, 256, 64]))
            lv169: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, reshape33, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv170: R.Tensor((1, 256, 82), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_cache_cache, lv169, sinfo_args=(R.Tensor((1, 256, 82), dtype="float32"),))
            lv171: R.Tensor((256, 256, 7), dtype="float32") = R.square(encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_weight_v)
            lv172: R.Tensor((256, 1, 1), dtype="float32") = R.sum(lv171, axis=[1, 2], keepdims=True)
            lv173: R.Tensor((256, 1, 1), dtype="float32") = R.sqrt(lv172)
            lv174: R.Tensor((256, 256, 7), dtype="float32") = R.divide(encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_weight_v, lv173)
            wnconv1d17: R.Tensor((256, 256, 7), dtype="float32") = R.multiply(encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_weight_g, lv174)
            lv175: R.Tensor((1, 256, 64), dtype="float32") = R.nn.conv1d(lv170, wnconv1d17, strides=[1], padding=[0, 0], dilation=[3], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv176: R.Tensor((1, 256, 1), dtype="float32") = R.reshape(encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_bias, R.shape([1, 256, 1]))
            conv1d17: R.Tensor((1, 256, 64), dtype="float32") = R.add(lv175, lv176)
            reshape34: R.Tensor((1, 256, 64), dtype="float32") = R.reshape(conv1d17, R.shape([1, 256, 64]))
            lv177 = R.call_tir(cls.snake2, (reshape34, encoder_block_layers_3_block_layers_1_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 256, 64), dtype="float32"))
            reshape35: R.Tensor((1, 256, 64), dtype="float32") = R.reshape(lv177, R.shape([1, 256, 64]))
            lv178: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, reshape35, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv179: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_cache_cache, lv178, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv180: R.Tensor((256, 256, 1), dtype="float32") = R.square(encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_weight_v)
            lv181: R.Tensor((256, 1, 1), dtype="float32") = R.sum(lv180, axis=[1, 2], keepdims=True)
            lv182: R.Tensor((256, 1, 1), dtype="float32") = R.sqrt(lv181)
            lv183: R.Tensor((256, 256, 1), dtype="float32") = R.divide(encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_weight_v, lv182)
            wnconv1d18: R.Tensor((256, 256, 1), dtype="float32") = R.multiply(encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_weight_g, lv183)
            lv184: R.Tensor((1, 256, 64), dtype="float32") = R.nn.conv1d(lv179, wnconv1d18, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv185: R.Tensor((1, 256, 1), dtype="float32") = R.reshape(encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_bias, R.shape([1, 256, 1]))
            conv1d18: R.Tensor((1, 256, 64), dtype="float32") = R.add(lv184, lv185)
            lv186: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_1_block_paddings_1_cache, add13, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            add14: R.Tensor((1, 256, 64), dtype="float32") = R.add(conv1d18, R.const(0.0, "float32"))
            add15: R.Tensor((1, 256, 64), dtype="float32") = R.add(add14, lv186)
            lv187: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_2_block_paddings_0_cache, add15, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            reshape36: R.Tensor((1, 256, 64), dtype="float32") = R.reshape(lv187, R.shape([1, 256, 64]))
            lv188 = R.call_tir(cls.snake2, (reshape36, encoder_block_layers_3_block_layers_2_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 256, 64), dtype="float32"))
            reshape37: R.Tensor((1, 256, 64), dtype="float32") = R.reshape(lv188, R.shape([1, 256, 64]))
            lv189: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, reshape37, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv190: R.Tensor((1, 256, 118), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache, lv189, sinfo_args=(R.Tensor((1, 256, 118), dtype="float32"),))
            lv191: R.Tensor((256, 256, 7), dtype="float32") = R.square(encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_weight_v)
            lv192: R.Tensor((256, 1, 1), dtype="float32") = R.sum(lv191, axis=[1, 2], keepdims=True)
            lv193: R.Tensor((256, 1, 1), dtype="float32") = R.sqrt(lv192)
            lv194: R.Tensor((256, 256, 7), dtype="float32") = R.divide(encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_weight_v, lv193)
            wnconv1d19: R.Tensor((256, 256, 7), dtype="float32") = R.multiply(encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_weight_g, lv194)
            lv195: R.Tensor((1, 256, 64), dtype="float32") = R.nn.conv1d(lv190, wnconv1d19, strides=[1], padding=[0, 0], dilation=[9], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv196: R.Tensor((1, 256, 1), dtype="float32") = R.reshape(encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_bias, R.shape([1, 256, 1]))
            conv1d19: R.Tensor((1, 256, 64), dtype="float32") = R.add(lv195, lv196)
            reshape38: R.Tensor((1, 256, 64), dtype="float32") = R.reshape(conv1d19, R.shape([1, 256, 64]))
            lv197 = R.call_tir(cls.snake2, (reshape38, encoder_block_layers_3_block_layers_2_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 256, 64), dtype="float32"))
            reshape39: R.Tensor((1, 256, 64), dtype="float32") = R.reshape(lv197, R.shape([1, 256, 64]))
            lv198: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, reshape39, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv199: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache, lv198, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv200: R.Tensor((256, 256, 1), dtype="float32") = R.square(encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_weight_v)
            lv201: R.Tensor((256, 1, 1), dtype="float32") = R.sum(lv200, axis=[1, 2], keepdims=True)
            lv202: R.Tensor((256, 1, 1), dtype="float32") = R.sqrt(lv201)
            lv203: R.Tensor((256, 256, 1), dtype="float32") = R.divide(encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_weight_v, lv202)
            wnconv1d20: R.Tensor((256, 256, 1), dtype="float32") = R.multiply(encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_weight_g, lv203)
            lv204: R.Tensor((1, 256, 64), dtype="float32") = R.nn.conv1d(lv199, wnconv1d20, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv205: R.Tensor((1, 256, 1), dtype="float32") = R.reshape(encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_bias, R.shape([1, 256, 1]))
            conv1d20: R.Tensor((1, 256, 64), dtype="float32") = R.add(lv204, lv205)
            lv206: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_2_block_paddings_1_cache, add15, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            add16: R.Tensor((1, 256, 64), dtype="float32") = R.add(conv1d20, R.const(0.0, "float32"))
            add17: R.Tensor((1, 256, 64), dtype="float32") = R.add(add16, lv206)
            reshape40: R.Tensor((1, 256, 64), dtype="float32") = R.reshape(add17, R.shape([1, 256, 64]))
            lv207 = R.call_tir(cls.snake2, (reshape40, encoder_block_layers_3_block_layers_3_alpha), out_sinfo=R.Tensor((1, 256, 64), dtype="float32"))
            reshape41: R.Tensor((1, 256, 64), dtype="float32") = R.reshape(lv207, R.shape([1, 256, 64]))
            lv208: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_4_downsampling_delay_cache, reshape41, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv209: R.Tensor((1, 256, 72), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_4_cache_cache, lv208, sinfo_args=(R.Tensor((1, 256, 72), dtype="float32"),))
            lv210: R.Tensor((512, 256, 16), dtype="float32") = R.square(encoder_block_layers_3_block_layers_4_weight_v)
            lv211: R.Tensor((512, 1, 1), dtype="float32") = R.sum(lv210, axis=[1, 2], keepdims=True)
            lv212: R.Tensor((512, 1, 1), dtype="float32") = R.sqrt(lv211)
            lv213: R.Tensor((512, 256, 16), dtype="float32") = R.divide(encoder_block_layers_3_block_layers_4_weight_v, lv212)
            wnconv1d21: R.Tensor((512, 256, 16), dtype="float32") = R.multiply(encoder_block_layers_3_block_layers_4_weight_g, lv213)
            lv214: R.Tensor((1, 512, 8), dtype="float32") = R.nn.conv1d(lv209, wnconv1d21, strides=[8], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv215: R.Tensor((1, 512, 1), dtype="float32") = R.reshape(encoder_block_layers_3_block_layers_4_bias, R.shape([1, 512, 1]))
            conv1d21: R.Tensor((1, 512, 8), dtype="float32") = R.add(lv214, lv215)
            lv216: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_0_block_paddings_0_cache, conv1d21, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            reshape42: R.Tensor((1, 512, 8), dtype="float32") = R.reshape(lv216, R.shape([1, 512, 8]))
            lv217 = R.call_tir(cls.snake3, (reshape42, encoder_block_layers_4_block_layers_0_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 512, 8), dtype="float32"))
            reshape43: R.Tensor((1, 512, 8), dtype="float32") = R.reshape(lv217, R.shape([1, 512, 8]))
            lv218: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, reshape43, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv219: R.Tensor((1, 512, 14), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_cache_cache, lv218, sinfo_args=(R.Tensor((1, 512, 14), dtype="float32"),))
            lv220: R.Tensor((512, 512, 7), dtype="float32") = R.square(encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_weight_v)
            lv221: R.Tensor((512, 1, 1), dtype="float32") = R.sum(lv220, axis=[1, 2], keepdims=True)
            lv222: R.Tensor((512, 1, 1), dtype="float32") = R.sqrt(lv221)
            lv223: R.Tensor((512, 512, 7), dtype="float32") = R.divide(encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_weight_v, lv222)
            wnconv1d22: R.Tensor((512, 512, 7), dtype="float32") = R.multiply(encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_weight_g, lv223)
            lv224: R.Tensor((1, 512, 8), dtype="float32") = R.nn.conv1d(lv219, wnconv1d22, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv225: R.Tensor((1, 512, 1), dtype="float32") = R.reshape(encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_bias, R.shape([1, 512, 1]))
            conv1d22: R.Tensor((1, 512, 8), dtype="float32") = R.add(lv224, lv225)
            reshape44: R.Tensor((1, 512, 8), dtype="float32") = R.reshape(conv1d22, R.shape([1, 512, 8]))
            lv226 = R.call_tir(cls.snake3, (reshape44, encoder_block_layers_4_block_layers_0_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 512, 8), dtype="float32"))
            reshape45: R.Tensor((1, 512, 8), dtype="float32") = R.reshape(lv226, R.shape([1, 512, 8]))
            lv227: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, reshape45, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv228: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_cache_cache, lv227, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv229: R.Tensor((512, 512, 1), dtype="float32") = R.square(encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_weight_v)
            lv230: R.Tensor((512, 1, 1), dtype="float32") = R.sum(lv229, axis=[1, 2], keepdims=True)
            lv231: R.Tensor((512, 1, 1), dtype="float32") = R.sqrt(lv230)
            lv232: R.Tensor((512, 512, 1), dtype="float32") = R.divide(encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_weight_v, lv231)
            wnconv1d23: R.Tensor((512, 512, 1), dtype="float32") = R.multiply(encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_weight_g, lv232)
            lv233: R.Tensor((1, 512, 8), dtype="float32") = R.nn.conv1d(lv228, wnconv1d23, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv234: R.Tensor((1, 512, 1), dtype="float32") = R.reshape(encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_bias, R.shape([1, 512, 1]))
            conv1d23: R.Tensor((1, 512, 8), dtype="float32") = R.add(lv233, lv234)
            lv235: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_0_block_paddings_1_cache, conv1d21, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            add18: R.Tensor((1, 512, 8), dtype="float32") = R.add(conv1d23, R.const(0.0, "float32"))
            add19: R.Tensor((1, 512, 8), dtype="float32") = R.add(add18, lv235)
            lv236: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_1_block_paddings_0_cache, add19, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            reshape46: R.Tensor((1, 512, 8), dtype="float32") = R.reshape(lv236, R.shape([1, 512, 8]))
            lv237 = R.call_tir(cls.snake3, (reshape46, encoder_block_layers_4_block_layers_1_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 512, 8), dtype="float32"))
            reshape47: R.Tensor((1, 512, 8), dtype="float32") = R.reshape(lv237, R.shape([1, 512, 8]))
            lv238: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, reshape47, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv239: R.Tensor((1, 512, 26), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_cache_cache, lv238, sinfo_args=(R.Tensor((1, 512, 26), dtype="float32"),))
            lv240: R.Tensor((512, 512, 7), dtype="float32") = R.square(encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_weight_v)
            lv241: R.Tensor((512, 1, 1), dtype="float32") = R.sum(lv240, axis=[1, 2], keepdims=True)
            lv242: R.Tensor((512, 1, 1), dtype="float32") = R.sqrt(lv241)
            lv243: R.Tensor((512, 512, 7), dtype="float32") = R.divide(encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_weight_v, lv242)
            wnconv1d24: R.Tensor((512, 512, 7), dtype="float32") = R.multiply(encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_weight_g, lv243)
            lv244: R.Tensor((1, 512, 8), dtype="float32") = R.nn.conv1d(lv239, wnconv1d24, strides=[1], padding=[0, 0], dilation=[3], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv245: R.Tensor((1, 512, 1), dtype="float32") = R.reshape(encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_bias, R.shape([1, 512, 1]))
            conv1d24: R.Tensor((1, 512, 8), dtype="float32") = R.add(lv244, lv245)
            reshape48: R.Tensor((1, 512, 8), dtype="float32") = R.reshape(conv1d24, R.shape([1, 512, 8]))
            lv246 = R.call_tir(cls.snake3, (reshape48, encoder_block_layers_4_block_layers_1_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 512, 8), dtype="float32"))
            reshape49: R.Tensor((1, 512, 8), dtype="float32") = R.reshape(lv246, R.shape([1, 512, 8]))
            lv247: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, reshape49, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv248: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_cache_cache, lv247, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv249: R.Tensor((512, 512, 1), dtype="float32") = R.square(encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_weight_v)
            lv250: R.Tensor((512, 1, 1), dtype="float32") = R.sum(lv249, axis=[1, 2], keepdims=True)
            lv251: R.Tensor((512, 1, 1), dtype="float32") = R.sqrt(lv250)
            lv252: R.Tensor((512, 512, 1), dtype="float32") = R.divide(encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_weight_v, lv251)
            wnconv1d25: R.Tensor((512, 512, 1), dtype="float32") = R.multiply(encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_weight_g, lv252)
            lv253: R.Tensor((1, 512, 8), dtype="float32") = R.nn.conv1d(lv248, wnconv1d25, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv254: R.Tensor((1, 512, 1), dtype="float32") = R.reshape(encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_bias, R.shape([1, 512, 1]))
            conv1d25: R.Tensor((1, 512, 8), dtype="float32") = R.add(lv253, lv254)
            lv255: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_1_block_paddings_1_cache, add19, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            add20: R.Tensor((1, 512, 8), dtype="float32") = R.add(conv1d25, R.const(0.0, "float32"))
            add21: R.Tensor((1, 512, 8), dtype="float32") = R.add(add20, lv255)
            lv256: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_2_block_paddings_0_cache, add21, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            reshape50: R.Tensor((1, 512, 8), dtype="float32") = R.reshape(lv256, R.shape([1, 512, 8]))
            lv257 = R.call_tir(cls.snake3, (reshape50, encoder_block_layers_4_block_layers_2_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 512, 8), dtype="float32"))
            reshape51: R.Tensor((1, 512, 8), dtype="float32") = R.reshape(lv257, R.shape([1, 512, 8]))
            lv258: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, reshape51, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv259: R.Tensor((1, 512, 62), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache, lv258, sinfo_args=(R.Tensor((1, 512, 62), dtype="float32"),))
            lv260: R.Tensor((512, 512, 7), dtype="float32") = R.square(encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_weight_v)
            lv261: R.Tensor((512, 1, 1), dtype="float32") = R.sum(lv260, axis=[1, 2], keepdims=True)
            lv262: R.Tensor((512, 1, 1), dtype="float32") = R.sqrt(lv261)
            lv263: R.Tensor((512, 512, 7), dtype="float32") = R.divide(encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_weight_v, lv262)
            wnconv1d26: R.Tensor((512, 512, 7), dtype="float32") = R.multiply(encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_weight_g, lv263)
            lv264: R.Tensor((1, 512, 8), dtype="float32") = R.nn.conv1d(lv259, wnconv1d26, strides=[1], padding=[0, 0], dilation=[9], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv265: R.Tensor((1, 512, 1), dtype="float32") = R.reshape(encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_bias, R.shape([1, 512, 1]))
            conv1d26: R.Tensor((1, 512, 8), dtype="float32") = R.add(lv264, lv265)
            reshape52: R.Tensor((1, 512, 8), dtype="float32") = R.reshape(conv1d26, R.shape([1, 512, 8]))
            lv266 = R.call_tir(cls.snake3, (reshape52, encoder_block_layers_4_block_layers_2_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 512, 8), dtype="float32"))
            reshape53: R.Tensor((1, 512, 8), dtype="float32") = R.reshape(lv266, R.shape([1, 512, 8]))
            lv267: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, reshape53, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv268: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache, lv267, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv269: R.Tensor((512, 512, 1), dtype="float32") = R.square(encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_weight_v)
            lv270: R.Tensor((512, 1, 1), dtype="float32") = R.sum(lv269, axis=[1, 2], keepdims=True)
            lv271: R.Tensor((512, 1, 1), dtype="float32") = R.sqrt(lv270)
            lv272: R.Tensor((512, 512, 1), dtype="float32") = R.divide(encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_weight_v, lv271)
            wnconv1d27: R.Tensor((512, 512, 1), dtype="float32") = R.multiply(encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_weight_g, lv272)
            lv273: R.Tensor((1, 512, 8), dtype="float32") = R.nn.conv1d(lv268, wnconv1d27, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv274: R.Tensor((1, 512, 1), dtype="float32") = R.reshape(encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_bias, R.shape([1, 512, 1]))
            conv1d27: R.Tensor((1, 512, 8), dtype="float32") = R.add(lv273, lv274)
            lv275: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_2_block_paddings_1_cache, add21, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            add22: R.Tensor((1, 512, 8), dtype="float32") = R.add(conv1d27, R.const(0.0, "float32"))
            add23: R.Tensor((1, 512, 8), dtype="float32") = R.add(add22, lv275)
            reshape54: R.Tensor((1, 512, 8), dtype="float32") = R.reshape(add23, R.shape([1, 512, 8]))
            lv276 = R.call_tir(cls.snake3, (reshape54, encoder_block_layers_4_block_layers_3_alpha), out_sinfo=R.Tensor((1, 512, 8), dtype="float32"))
            reshape55: R.Tensor((1, 512, 8), dtype="float32") = R.reshape(lv276, R.shape([1, 512, 8]))
            lv277: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_4_downsampling_delay_cache, reshape55, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv278: R.Tensor((1, 512, 16), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_4_cache_cache, lv277, sinfo_args=(R.Tensor((1, 512, 16), dtype="float32"),))
            lv279: R.Tensor((1024, 512, 16), dtype="float32") = R.square(encoder_block_layers_4_block_layers_4_weight_v)
            lv280: R.Tensor((1024, 1, 1), dtype="float32") = R.sum(lv279, axis=[1, 2], keepdims=True)
            lv281: R.Tensor((1024, 1, 1), dtype="float32") = R.sqrt(lv280)
            lv282: R.Tensor((1024, 512, 16), dtype="float32") = R.divide(encoder_block_layers_4_block_layers_4_weight_v, lv281)
            wnconv1d28: R.Tensor((1024, 512, 16), dtype="float32") = R.multiply(encoder_block_layers_4_block_layers_4_weight_g, lv282)
            lv283: R.Tensor((1, 1024, 1), dtype="float32") = R.nn.conv1d(lv278, wnconv1d28, strides=[8], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv284: R.Tensor((1, 1024, 1), dtype="float32") = R.reshape(encoder_block_layers_4_block_layers_4_bias, R.shape([1, 1024, 1]))
            conv1d28: R.Tensor((1, 1024, 1), dtype="float32") = R.add(lv283, lv284)
            reshape56: R.Tensor((1, 1024, 1), dtype="float32") = R.reshape(conv1d28, R.shape([1, 1024, 1]))
            lv285 = R.call_tir(cls.snake4, (reshape56, encoder_block_layers_5_alpha), out_sinfo=R.Tensor((1, 1024, 1), dtype="float32"))
            reshape57: R.Tensor((1, 1024, 1), dtype="float32") = R.reshape(lv285, R.shape([1, 1024, 1]))
            lv286: R.Tensor((1, 1024, 1), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_6_downsampling_delay_cache, reshape57, sinfo_args=(R.Tensor((1, 1024, 1), dtype="float32"),))
            lv287: R.Tensor((1, 1024, 3), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_6_cache_cache, lv286, sinfo_args=(R.Tensor((1, 1024, 3), dtype="float32"),))
            lv288: R.Tensor((1024, 1024, 3), dtype="float32") = R.square(encoder_block_layers_6_weight_v)
            lv289: R.Tensor((1024, 1, 1), dtype="float32") = R.sum(lv288, axis=[1, 2], keepdims=True)
            lv290: R.Tensor((1024, 1, 1), dtype="float32") = R.sqrt(lv289)
            lv291: R.Tensor((1024, 1024, 3), dtype="float32") = R.divide(encoder_block_layers_6_weight_v, lv290)
            wnconv1d29: R.Tensor((1024, 1024, 3), dtype="float32") = R.multiply(encoder_block_layers_6_weight_g, lv291)
            lv292: R.Tensor((1, 1024, 1), dtype="float32") = R.nn.conv1d(lv287, wnconv1d29, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv293: R.Tensor((1, 1024, 1), dtype="float32") = R.reshape(encoder_block_layers_6_bias, R.shape([1, 1024, 1]))
            conv1d29: R.Tensor((1, 1024, 1), dtype="float32") = R.add(lv292, lv293)
            zeros: R.Tensor((1, 1024, 1), dtype="float32") = R.zeros(R.shape([1, 1024, 1]), dtype="float32")
            lv294: R.Tensor((8, 1024, 1), dtype="float32") = R.square(quantizer_quantizers_0_in_proj_weight_v)
            lv295: R.Tensor((8, 1, 1), dtype="float32") = R.sum(lv294, axis=[1, 2], keepdims=True)
            lv296: R.Tensor((8, 1, 1), dtype="float32") = R.sqrt(lv295)
            lv297: R.Tensor((8, 1024, 1), dtype="float32") = R.divide(quantizer_quantizers_0_in_proj_weight_v, lv296)
            wnconv1d30: R.Tensor((8, 1024, 1), dtype="float32") = R.multiply(quantizer_quantizers_0_in_proj_weight_g, lv297)
            lv298: R.Tensor((1, 8, 1), dtype="float32") = R.nn.conv1d(conv1d29, wnconv1d30, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv299: R.Tensor((1, 8, 1), dtype="float32") = R.reshape(quantizer_quantizers_0_in_proj_bias, R.shape([1, 8, 1]))
            conv1d30: R.Tensor((1, 8, 1), dtype="float32") = R.add(lv298, lv299)
            permute_dims: R.Tensor((1, 1, 8), dtype="float32") = R.permute_dims(conv1d30, axes=[0, 2, 1])
            reshape58: R.Tensor((1, 8), dtype="float32") = R.reshape(permute_dims, R.shape([1, 8]))
            square: R.Tensor((1, 8), dtype="float32") = R.square(reshape58)
            sum: R.Tensor((1, 1), dtype="float32") = R.sum(square, axis=[1], keepdims=True)
            broadcast_to: R.Tensor((1, 8), dtype="float32") = R.broadcast_to(sum, R.shape([1, 8]))
            maximum: R.Tensor((1, 8), dtype="float32") = R.maximum(broadcast_to, R.const(9.999999960041972e-13, "float32"))
            sqrt: R.Tensor((1, 8), dtype="float32") = R.sqrt(maximum)
            divide: R.Tensor((1, 8), dtype="float32") = R.divide(reshape58, sqrt)
            square1: R.Tensor((1024, 8), dtype="float32") = R.square(quantizer_quantizers_0_codebook_weight)
            sum1: R.Tensor((1024, 1), dtype="float32") = R.sum(square1, axis=[1], keepdims=True)
            broadcast_to1: R.Tensor((1024, 8), dtype="float32") = R.broadcast_to(sum1, R.shape([1024, 8]))
            maximum1: R.Tensor((1024, 8), dtype="float32") = R.maximum(broadcast_to1, R.const(9.999999960041972e-13, "float32"))
            sqrt1: R.Tensor((1024, 8), dtype="float32") = R.sqrt(maximum1)
            divide1: R.Tensor((1024, 8), dtype="float32") = R.divide(quantizer_quantizers_0_codebook_weight, sqrt1)
            square2: R.Tensor((1, 8), dtype="float32") = R.square(divide)
            sum2: R.Tensor((1, 1), dtype="float32") = R.sum(square2, axis=[1], keepdims=True)
            permute_dims1: R.Tensor((8, 1024), dtype="float32") = R.permute_dims(divide1, axes=[1, 0])
            matmul: R.Tensor((1, 1024), dtype="float32") = R.matmul(divide, permute_dims1, out_dtype="void")
            mul: R.Tensor((1, 1024), dtype="float32") = R.multiply(matmul, R.const(2.0, "float32"))
            subtract: R.Tensor((1, 1024), dtype="float32") = R.subtract(sum2, mul)
            square3: R.Tensor((1024, 8), dtype="float32") = R.square(divide1)
            sum3: R.Tensor((1024, 1), dtype="float32") = R.sum(square3, axis=[1], keepdims=True)
            permute_dims2: R.Tensor((1, 1024), dtype="float32") = R.permute_dims(sum3, axes=[1, 0])
            add24: R.Tensor((1, 1024), dtype="float32") = R.add(subtract, permute_dims2)
            argsort: R.Tensor((1, 1024), dtype="int32") = R.argsort(add24, axis=1, descending=False, dtype="int32")
            take: R.Tensor((1, 1), dtype="int32") = R.take(argsort, metadata["relax.expr.Constant"][0], axis=1)
            reshape59: R.Tensor((1, 1), dtype="int32") = R.reshape(take, R.shape([1, 1]))
            reshape60: R.Tensor((1,), dtype="int32") = R.reshape(reshape59, R.shape([1]))
            take1: R.Tensor((1, 8), dtype="float32") = R.take(quantizer_quantizers_0_codebook_weight, reshape60, axis=0)
            reshape61: R.Tensor((1, 1, 8), dtype="float32") = R.reshape(take1, R.shape([1, 1, 8]))
            permute_dims3: R.Tensor((1, 8, 1), dtype="float32") = R.permute_dims(reshape61, axes=[0, 2, 1])
            lv300: R.Tensor((1024, 8, 1), dtype="float32") = R.square(quantizer_quantizers_0_out_proj_weight_v)
            lv301: R.Tensor((1024, 1, 1), dtype="float32") = R.sum(lv300, axis=[1, 2], keepdims=True)
            lv302: R.Tensor((1024, 1, 1), dtype="float32") = R.sqrt(lv301)
            lv303: R.Tensor((1024, 8, 1), dtype="float32") = R.divide(quantizer_quantizers_0_out_proj_weight_v, lv302)
            wnconv1d31: R.Tensor((1024, 8, 1), dtype="float32") = R.multiply(quantizer_quantizers_0_out_proj_weight_g, lv303)
            lv304: R.Tensor((1, 1024, 1), dtype="float32") = R.nn.conv1d(permute_dims3, wnconv1d31, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv305: R.Tensor((1, 1024, 1), dtype="float32") = R.reshape(quantizer_quantizers_0_out_proj_bias, R.shape([1, 1024, 1]))
            conv1d31: R.Tensor((1, 1024, 1), dtype="float32") = R.add(lv304, lv305)
            add25: R.Tensor((1, 1024, 1), dtype="float32") = R.add(zeros, conv1d31)
            subtract1: R.Tensor((1, 1024, 1), dtype="float32") = R.subtract(conv1d29, conv1d31)
            lv306: R.Tensor((8, 1024, 1), dtype="float32") = R.square(quantizer_quantizers_1_in_proj_weight_v)
            lv307: R.Tensor((8, 1, 1), dtype="float32") = R.sum(lv306, axis=[1, 2], keepdims=True)
            lv308: R.Tensor((8, 1, 1), dtype="float32") = R.sqrt(lv307)
            lv309: R.Tensor((8, 1024, 1), dtype="float32") = R.divide(quantizer_quantizers_1_in_proj_weight_v, lv308)
            wnconv1d32: R.Tensor((8, 1024, 1), dtype="float32") = R.multiply(quantizer_quantizers_1_in_proj_weight_g, lv309)
            lv310: R.Tensor((1, 8, 1), dtype="float32") = R.nn.conv1d(subtract1, wnconv1d32, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv311: R.Tensor((1, 8, 1), dtype="float32") = R.reshape(quantizer_quantizers_1_in_proj_bias, R.shape([1, 8, 1]))
            conv1d32: R.Tensor((1, 8, 1), dtype="float32") = R.add(lv310, lv311)
            permute_dims4: R.Tensor((1, 1, 8), dtype="float32") = R.permute_dims(conv1d32, axes=[0, 2, 1])
            reshape62: R.Tensor((1, 8), dtype="float32") = R.reshape(permute_dims4, R.shape([1, 8]))
            square4: R.Tensor((1, 8), dtype="float32") = R.square(reshape62)
            sum4: R.Tensor((1, 1), dtype="float32") = R.sum(square4, axis=[1], keepdims=True)
            broadcast_to2: R.Tensor((1, 8), dtype="float32") = R.broadcast_to(sum4, R.shape([1, 8]))
            maximum2: R.Tensor((1, 8), dtype="float32") = R.maximum(broadcast_to2, R.const(9.999999960041972e-13, "float32"))
            sqrt2: R.Tensor((1, 8), dtype="float32") = R.sqrt(maximum2)
            divide2: R.Tensor((1, 8), dtype="float32") = R.divide(reshape62, sqrt2)
            square5: R.Tensor((1024, 8), dtype="float32") = R.square(quantizer_quantizers_1_codebook_weight)
            sum5: R.Tensor((1024, 1), dtype="float32") = R.sum(square5, axis=[1], keepdims=True)
            broadcast_to3: R.Tensor((1024, 8), dtype="float32") = R.broadcast_to(sum5, R.shape([1024, 8]))
            maximum3: R.Tensor((1024, 8), dtype="float32") = R.maximum(broadcast_to3, R.const(9.999999960041972e-13, "float32"))
            sqrt3: R.Tensor((1024, 8), dtype="float32") = R.sqrt(maximum3)
            divide3: R.Tensor((1024, 8), dtype="float32") = R.divide(quantizer_quantizers_1_codebook_weight, sqrt3)
            square6: R.Tensor((1, 8), dtype="float32") = R.square(divide2)
            sum6: R.Tensor((1, 1), dtype="float32") = R.sum(square6, axis=[1], keepdims=True)
            permute_dims5: R.Tensor((8, 1024), dtype="float32") = R.permute_dims(divide3, axes=[1, 0])
            matmul1: R.Tensor((1, 1024), dtype="float32") = R.matmul(divide2, permute_dims5, out_dtype="void")
            mul1: R.Tensor((1, 1024), dtype="float32") = R.multiply(matmul1, R.const(2.0, "float32"))
            subtract2: R.Tensor((1, 1024), dtype="float32") = R.subtract(sum6, mul1)
            square7: R.Tensor((1024, 8), dtype="float32") = R.square(divide3)
            sum7: R.Tensor((1024, 1), dtype="float32") = R.sum(square7, axis=[1], keepdims=True)
            permute_dims6: R.Tensor((1, 1024), dtype="float32") = R.permute_dims(sum7, axes=[1, 0])
            add26: R.Tensor((1, 1024), dtype="float32") = R.add(subtract2, permute_dims6)
            argsort1: R.Tensor((1, 1024), dtype="int32") = R.argsort(add26, axis=1, descending=False, dtype="int32")
            take2: R.Tensor((1, 1), dtype="int32") = R.take(argsort1, metadata["relax.expr.Constant"][1], axis=1)
            reshape63: R.Tensor((1, 1), dtype="int32") = R.reshape(take2, R.shape([1, 1]))
            reshape64: R.Tensor((1,), dtype="int32") = R.reshape(reshape63, R.shape([1]))
            take3: R.Tensor((1, 8), dtype="float32") = R.take(quantizer_quantizers_1_codebook_weight, reshape64, axis=0)
            reshape65: R.Tensor((1, 1, 8), dtype="float32") = R.reshape(take3, R.shape([1, 1, 8]))
            permute_dims7: R.Tensor((1, 8, 1), dtype="float32") = R.permute_dims(reshape65, axes=[0, 2, 1])
            lv312: R.Tensor((1024, 8, 1), dtype="float32") = R.square(quantizer_quantizers_1_out_proj_weight_v)
            lv313: R.Tensor((1024, 1, 1), dtype="float32") = R.sum(lv312, axis=[1, 2], keepdims=True)
            lv314: R.Tensor((1024, 1, 1), dtype="float32") = R.sqrt(lv313)
            lv315: R.Tensor((1024, 8, 1), dtype="float32") = R.divide(quantizer_quantizers_1_out_proj_weight_v, lv314)
            wnconv1d33: R.Tensor((1024, 8, 1), dtype="float32") = R.multiply(quantizer_quantizers_1_out_proj_weight_g, lv315)
            lv316: R.Tensor((1, 1024, 1), dtype="float32") = R.nn.conv1d(permute_dims7, wnconv1d33, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv317: R.Tensor((1, 1024, 1), dtype="float32") = R.reshape(quantizer_quantizers_1_out_proj_bias, R.shape([1, 1024, 1]))
            conv1d33: R.Tensor((1, 1024, 1), dtype="float32") = R.add(lv316, lv317)
            add27: R.Tensor((1, 1024, 1), dtype="float32") = R.add(add25, conv1d33)
            subtract3: R.Tensor((1, 1024, 1), dtype="float32") = R.subtract(subtract1, conv1d33)
            lv318: R.Tensor((8, 1024, 1), dtype="float32") = R.square(quantizer_quantizers_2_in_proj_weight_v)
            lv319: R.Tensor((8, 1, 1), dtype="float32") = R.sum(lv318, axis=[1, 2], keepdims=True)
            lv320: R.Tensor((8, 1, 1), dtype="float32") = R.sqrt(lv319)
            lv321: R.Tensor((8, 1024, 1), dtype="float32") = R.divide(quantizer_quantizers_2_in_proj_weight_v, lv320)
            wnconv1d34: R.Tensor((8, 1024, 1), dtype="float32") = R.multiply(quantizer_quantizers_2_in_proj_weight_g, lv321)
            lv322: R.Tensor((1, 8, 1), dtype="float32") = R.nn.conv1d(subtract3, wnconv1d34, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv323: R.Tensor((1, 8, 1), dtype="float32") = R.reshape(quantizer_quantizers_2_in_proj_bias, R.shape([1, 8, 1]))
            conv1d34: R.Tensor((1, 8, 1), dtype="float32") = R.add(lv322, lv323)
            permute_dims8: R.Tensor((1, 1, 8), dtype="float32") = R.permute_dims(conv1d34, axes=[0, 2, 1])
            reshape66: R.Tensor((1, 8), dtype="float32") = R.reshape(permute_dims8, R.shape([1, 8]))
            square8: R.Tensor((1, 8), dtype="float32") = R.square(reshape66)
            sum8: R.Tensor((1, 1), dtype="float32") = R.sum(square8, axis=[1], keepdims=True)
            broadcast_to4: R.Tensor((1, 8), dtype="float32") = R.broadcast_to(sum8, R.shape([1, 8]))
            maximum4: R.Tensor((1, 8), dtype="float32") = R.maximum(broadcast_to4, R.const(9.999999960041972e-13, "float32"))
            sqrt4: R.Tensor((1, 8), dtype="float32") = R.sqrt(maximum4)
            divide4: R.Tensor((1, 8), dtype="float32") = R.divide(reshape66, sqrt4)
            square9: R.Tensor((1024, 8), dtype="float32") = R.square(quantizer_quantizers_2_codebook_weight)
            sum9: R.Tensor((1024, 1), dtype="float32") = R.sum(square9, axis=[1], keepdims=True)
            broadcast_to5: R.Tensor((1024, 8), dtype="float32") = R.broadcast_to(sum9, R.shape([1024, 8]))
            maximum5: R.Tensor((1024, 8), dtype="float32") = R.maximum(broadcast_to5, R.const(9.999999960041972e-13, "float32"))
            sqrt5: R.Tensor((1024, 8), dtype="float32") = R.sqrt(maximum5)
            divide5: R.Tensor((1024, 8), dtype="float32") = R.divide(quantizer_quantizers_2_codebook_weight, sqrt5)
            square10: R.Tensor((1, 8), dtype="float32") = R.square(divide4)
            sum10: R.Tensor((1, 1), dtype="float32") = R.sum(square10, axis=[1], keepdims=True)
            permute_dims9: R.Tensor((8, 1024), dtype="float32") = R.permute_dims(divide5, axes=[1, 0])
            matmul2: R.Tensor((1, 1024), dtype="float32") = R.matmul(divide4, permute_dims9, out_dtype="void")
            mul2: R.Tensor((1, 1024), dtype="float32") = R.multiply(matmul2, R.const(2.0, "float32"))
            subtract4: R.Tensor((1, 1024), dtype="float32") = R.subtract(sum10, mul2)
            square11: R.Tensor((1024, 8), dtype="float32") = R.square(divide5)
            sum11: R.Tensor((1024, 1), dtype="float32") = R.sum(square11, axis=[1], keepdims=True)
            permute_dims10: R.Tensor((1, 1024), dtype="float32") = R.permute_dims(sum11, axes=[1, 0])
            add28: R.Tensor((1, 1024), dtype="float32") = R.add(subtract4, permute_dims10)
            argsort2: R.Tensor((1, 1024), dtype="int32") = R.argsort(add28, axis=1, descending=False, dtype="int32")
            take4: R.Tensor((1, 1), dtype="int32") = R.take(argsort2, metadata["relax.expr.Constant"][2], axis=1)
            reshape67: R.Tensor((1, 1), dtype="int32") = R.reshape(take4, R.shape([1, 1]))
            reshape68: R.Tensor((1,), dtype="int32") = R.reshape(reshape67, R.shape([1]))
            take5: R.Tensor((1, 8), dtype="float32") = R.take(quantizer_quantizers_2_codebook_weight, reshape68, axis=0)
            reshape69: R.Tensor((1, 1, 8), dtype="float32") = R.reshape(take5, R.shape([1, 1, 8]))
            permute_dims11: R.Tensor((1, 8, 1), dtype="float32") = R.permute_dims(reshape69, axes=[0, 2, 1])
            lv324: R.Tensor((1024, 8, 1), dtype="float32") = R.square(quantizer_quantizers_2_out_proj_weight_v)
            lv325: R.Tensor((1024, 1, 1), dtype="float32") = R.sum(lv324, axis=[1, 2], keepdims=True)
            lv326: R.Tensor((1024, 1, 1), dtype="float32") = R.sqrt(lv325)
            lv327: R.Tensor((1024, 8, 1), dtype="float32") = R.divide(quantizer_quantizers_2_out_proj_weight_v, lv326)
            wnconv1d35: R.Tensor((1024, 8, 1), dtype="float32") = R.multiply(quantizer_quantizers_2_out_proj_weight_g, lv327)
            lv328: R.Tensor((1, 1024, 1), dtype="float32") = R.nn.conv1d(permute_dims11, wnconv1d35, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv329: R.Tensor((1, 1024, 1), dtype="float32") = R.reshape(quantizer_quantizers_2_out_proj_bias, R.shape([1, 1024, 1]))
            conv1d35: R.Tensor((1, 1024, 1), dtype="float32") = R.add(lv328, lv329)
            add29: R.Tensor((1, 1024, 1), dtype="float32") = R.add(add27, conv1d35)
            subtract5: R.Tensor((1, 1024, 1), dtype="float32") = R.subtract(subtract3, conv1d35)
            lv330: R.Tensor((8, 1024, 1), dtype="float32") = R.square(quantizer_quantizers_3_in_proj_weight_v)
            lv331: R.Tensor((8, 1, 1), dtype="float32") = R.sum(lv330, axis=[1, 2], keepdims=True)
            lv332: R.Tensor((8, 1, 1), dtype="float32") = R.sqrt(lv331)
            lv333: R.Tensor((8, 1024, 1), dtype="float32") = R.divide(quantizer_quantizers_3_in_proj_weight_v, lv332)
            wnconv1d36: R.Tensor((8, 1024, 1), dtype="float32") = R.multiply(quantizer_quantizers_3_in_proj_weight_g, lv333)
            lv334: R.Tensor((1, 8, 1), dtype="float32") = R.nn.conv1d(subtract5, wnconv1d36, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv335: R.Tensor((1, 8, 1), dtype="float32") = R.reshape(quantizer_quantizers_3_in_proj_bias, R.shape([1, 8, 1]))
            conv1d36: R.Tensor((1, 8, 1), dtype="float32") = R.add(lv334, lv335)
            permute_dims12: R.Tensor((1, 1, 8), dtype="float32") = R.permute_dims(conv1d36, axes=[0, 2, 1])
            reshape70: R.Tensor((1, 8), dtype="float32") = R.reshape(permute_dims12, R.shape([1, 8]))
            square12: R.Tensor((1, 8), dtype="float32") = R.square(reshape70)
            sum12: R.Tensor((1, 1), dtype="float32") = R.sum(square12, axis=[1], keepdims=True)
            broadcast_to6: R.Tensor((1, 8), dtype="float32") = R.broadcast_to(sum12, R.shape([1, 8]))
            maximum6: R.Tensor((1, 8), dtype="float32") = R.maximum(broadcast_to6, R.const(9.999999960041972e-13, "float32"))
            sqrt6: R.Tensor((1, 8), dtype="float32") = R.sqrt(maximum6)
            divide6: R.Tensor((1, 8), dtype="float32") = R.divide(reshape70, sqrt6)
            square13: R.Tensor((1024, 8), dtype="float32") = R.square(quantizer_quantizers_3_codebook_weight)
            sum13: R.Tensor((1024, 1), dtype="float32") = R.sum(square13, axis=[1], keepdims=True)
            broadcast_to7: R.Tensor((1024, 8), dtype="float32") = R.broadcast_to(sum13, R.shape([1024, 8]))
            maximum7: R.Tensor((1024, 8), dtype="float32") = R.maximum(broadcast_to7, R.const(9.999999960041972e-13, "float32"))
            sqrt7: R.Tensor((1024, 8), dtype="float32") = R.sqrt(maximum7)
            divide7: R.Tensor((1024, 8), dtype="float32") = R.divide(quantizer_quantizers_3_codebook_weight, sqrt7)
            square14: R.Tensor((1, 8), dtype="float32") = R.square(divide6)
            sum14: R.Tensor((1, 1), dtype="float32") = R.sum(square14, axis=[1], keepdims=True)
            permute_dims13: R.Tensor((8, 1024), dtype="float32") = R.permute_dims(divide7, axes=[1, 0])
            matmul3: R.Tensor((1, 1024), dtype="float32") = R.matmul(divide6, permute_dims13, out_dtype="void")
            mul3: R.Tensor((1, 1024), dtype="float32") = R.multiply(matmul3, R.const(2.0, "float32"))
            subtract6: R.Tensor((1, 1024), dtype="float32") = R.subtract(sum14, mul3)
            square15: R.Tensor((1024, 8), dtype="float32") = R.square(divide7)
            sum15: R.Tensor((1024, 1), dtype="float32") = R.sum(square15, axis=[1], keepdims=True)
            permute_dims14: R.Tensor((1, 1024), dtype="float32") = R.permute_dims(sum15, axes=[1, 0])
            add30: R.Tensor((1, 1024), dtype="float32") = R.add(subtract6, permute_dims14)
            argsort3: R.Tensor((1, 1024), dtype="int32") = R.argsort(add30, axis=1, descending=False, dtype="int32")
            take6: R.Tensor((1, 1), dtype="int32") = R.take(argsort3, metadata["relax.expr.Constant"][3], axis=1)
            reshape71: R.Tensor((1, 1), dtype="int32") = R.reshape(take6, R.shape([1, 1]))
            reshape72: R.Tensor((1,), dtype="int32") = R.reshape(reshape71, R.shape([1]))
            take7: R.Tensor((1, 8), dtype="float32") = R.take(quantizer_quantizers_3_codebook_weight, reshape72, axis=0)
            reshape73: R.Tensor((1, 1, 8), dtype="float32") = R.reshape(take7, R.shape([1, 1, 8]))
            permute_dims15: R.Tensor((1, 8, 1), dtype="float32") = R.permute_dims(reshape73, axes=[0, 2, 1])
            lv336: R.Tensor((1024, 8, 1), dtype="float32") = R.square(quantizer_quantizers_3_out_proj_weight_v)
            lv337: R.Tensor((1024, 1, 1), dtype="float32") = R.sum(lv336, axis=[1, 2], keepdims=True)
            lv338: R.Tensor((1024, 1, 1), dtype="float32") = R.sqrt(lv337)
            lv339: R.Tensor((1024, 8, 1), dtype="float32") = R.divide(quantizer_quantizers_3_out_proj_weight_v, lv338)
            wnconv1d37: R.Tensor((1024, 8, 1), dtype="float32") = R.multiply(quantizer_quantizers_3_out_proj_weight_g, lv339)
            lv340: R.Tensor((1, 1024, 1), dtype="float32") = R.nn.conv1d(permute_dims15, wnconv1d37, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv341: R.Tensor((1, 1024, 1), dtype="float32") = R.reshape(quantizer_quantizers_3_out_proj_bias, R.shape([1, 1024, 1]))
            conv1d37: R.Tensor((1, 1024, 1), dtype="float32") = R.add(lv340, lv341)
            add31: R.Tensor((1, 1024, 1), dtype="float32") = R.add(add29, conv1d37)
            subtract7: R.Tensor((1, 1024, 1), dtype="float32") = R.subtract(subtract5, conv1d37)
            lv342: R.Tensor((8, 1024, 1), dtype="float32") = R.square(quantizer_quantizers_4_in_proj_weight_v)
            lv343: R.Tensor((8, 1, 1), dtype="float32") = R.sum(lv342, axis=[1, 2], keepdims=True)
            lv344: R.Tensor((8, 1, 1), dtype="float32") = R.sqrt(lv343)
            lv345: R.Tensor((8, 1024, 1), dtype="float32") = R.divide(quantizer_quantizers_4_in_proj_weight_v, lv344)
            wnconv1d38: R.Tensor((8, 1024, 1), dtype="float32") = R.multiply(quantizer_quantizers_4_in_proj_weight_g, lv345)
            lv346: R.Tensor((1, 8, 1), dtype="float32") = R.nn.conv1d(subtract7, wnconv1d38, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv347: R.Tensor((1, 8, 1), dtype="float32") = R.reshape(quantizer_quantizers_4_in_proj_bias, R.shape([1, 8, 1]))
            conv1d38: R.Tensor((1, 8, 1), dtype="float32") = R.add(lv346, lv347)
            permute_dims16: R.Tensor((1, 1, 8), dtype="float32") = R.permute_dims(conv1d38, axes=[0, 2, 1])
            reshape74: R.Tensor((1, 8), dtype="float32") = R.reshape(permute_dims16, R.shape([1, 8]))
            square16: R.Tensor((1, 8), dtype="float32") = R.square(reshape74)
            sum16: R.Tensor((1, 1), dtype="float32") = R.sum(square16, axis=[1], keepdims=True)
            broadcast_to8: R.Tensor((1, 8), dtype="float32") = R.broadcast_to(sum16, R.shape([1, 8]))
            maximum8: R.Tensor((1, 8), dtype="float32") = R.maximum(broadcast_to8, R.const(9.999999960041972e-13, "float32"))
            sqrt8: R.Tensor((1, 8), dtype="float32") = R.sqrt(maximum8)
            divide8: R.Tensor((1, 8), dtype="float32") = R.divide(reshape74, sqrt8)
            square17: R.Tensor((1024, 8), dtype="float32") = R.square(quantizer_quantizers_4_codebook_weight)
            sum17: R.Tensor((1024, 1), dtype="float32") = R.sum(square17, axis=[1], keepdims=True)
            broadcast_to9: R.Tensor((1024, 8), dtype="float32") = R.broadcast_to(sum17, R.shape([1024, 8]))
            maximum9: R.Tensor((1024, 8), dtype="float32") = R.maximum(broadcast_to9, R.const(9.999999960041972e-13, "float32"))
            sqrt9: R.Tensor((1024, 8), dtype="float32") = R.sqrt(maximum9)
            divide9: R.Tensor((1024, 8), dtype="float32") = R.divide(quantizer_quantizers_4_codebook_weight, sqrt9)
            square18: R.Tensor((1, 8), dtype="float32") = R.square(divide8)
            sum18: R.Tensor((1, 1), dtype="float32") = R.sum(square18, axis=[1], keepdims=True)
            permute_dims17: R.Tensor((8, 1024), dtype="float32") = R.permute_dims(divide9, axes=[1, 0])
            matmul4: R.Tensor((1, 1024), dtype="float32") = R.matmul(divide8, permute_dims17, out_dtype="void")
            mul4: R.Tensor((1, 1024), dtype="float32") = R.multiply(matmul4, R.const(2.0, "float32"))
            subtract8: R.Tensor((1, 1024), dtype="float32") = R.subtract(sum18, mul4)
            square19: R.Tensor((1024, 8), dtype="float32") = R.square(divide9)
            sum19: R.Tensor((1024, 1), dtype="float32") = R.sum(square19, axis=[1], keepdims=True)
            permute_dims18: R.Tensor((1, 1024), dtype="float32") = R.permute_dims(sum19, axes=[1, 0])
            add32: R.Tensor((1, 1024), dtype="float32") = R.add(subtract8, permute_dims18)
            argsort4: R.Tensor((1, 1024), dtype="int32") = R.argsort(add32, axis=1, descending=False, dtype="int32")
            take8: R.Tensor((1, 1), dtype="int32") = R.take(argsort4, metadata["relax.expr.Constant"][4], axis=1)
            reshape75: R.Tensor((1, 1), dtype="int32") = R.reshape(take8, R.shape([1, 1]))
            reshape76: R.Tensor((1,), dtype="int32") = R.reshape(reshape75, R.shape([1]))
            take9: R.Tensor((1, 8), dtype="float32") = R.take(quantizer_quantizers_4_codebook_weight, reshape76, axis=0)
            reshape77: R.Tensor((1, 1, 8), dtype="float32") = R.reshape(take9, R.shape([1, 1, 8]))
            permute_dims19: R.Tensor((1, 8, 1), dtype="float32") = R.permute_dims(reshape77, axes=[0, 2, 1])
            lv348: R.Tensor((1024, 8, 1), dtype="float32") = R.square(quantizer_quantizers_4_out_proj_weight_v)
            lv349: R.Tensor((1024, 1, 1), dtype="float32") = R.sum(lv348, axis=[1, 2], keepdims=True)
            lv350: R.Tensor((1024, 1, 1), dtype="float32") = R.sqrt(lv349)
            lv351: R.Tensor((1024, 8, 1), dtype="float32") = R.divide(quantizer_quantizers_4_out_proj_weight_v, lv350)
            wnconv1d39: R.Tensor((1024, 8, 1), dtype="float32") = R.multiply(quantizer_quantizers_4_out_proj_weight_g, lv351)
            lv352: R.Tensor((1, 1024, 1), dtype="float32") = R.nn.conv1d(permute_dims19, wnconv1d39, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv353: R.Tensor((1, 1024, 1), dtype="float32") = R.reshape(quantizer_quantizers_4_out_proj_bias, R.shape([1, 1024, 1]))
            conv1d39: R.Tensor((1, 1024, 1), dtype="float32") = R.add(lv352, lv353)
            add33: R.Tensor((1, 1024, 1), dtype="float32") = R.add(add31, conv1d39)
            subtract9: R.Tensor((1, 1024, 1), dtype="float32") = R.subtract(subtract7, conv1d39)
            lv354: R.Tensor((8, 1024, 1), dtype="float32") = R.square(quantizer_quantizers_5_in_proj_weight_v)
            lv355: R.Tensor((8, 1, 1), dtype="float32") = R.sum(lv354, axis=[1, 2], keepdims=True)
            lv356: R.Tensor((8, 1, 1), dtype="float32") = R.sqrt(lv355)
            lv357: R.Tensor((8, 1024, 1), dtype="float32") = R.divide(quantizer_quantizers_5_in_proj_weight_v, lv356)
            wnconv1d40: R.Tensor((8, 1024, 1), dtype="float32") = R.multiply(quantizer_quantizers_5_in_proj_weight_g, lv357)
            lv358: R.Tensor((1, 8, 1), dtype="float32") = R.nn.conv1d(subtract9, wnconv1d40, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv359: R.Tensor((1, 8, 1), dtype="float32") = R.reshape(quantizer_quantizers_5_in_proj_bias, R.shape([1, 8, 1]))
            conv1d40: R.Tensor((1, 8, 1), dtype="float32") = R.add(lv358, lv359)
            permute_dims20: R.Tensor((1, 1, 8), dtype="float32") = R.permute_dims(conv1d40, axes=[0, 2, 1])
            reshape78: R.Tensor((1, 8), dtype="float32") = R.reshape(permute_dims20, R.shape([1, 8]))
            square20: R.Tensor((1, 8), dtype="float32") = R.square(reshape78)
            sum20: R.Tensor((1, 1), dtype="float32") = R.sum(square20, axis=[1], keepdims=True)
            broadcast_to10: R.Tensor((1, 8), dtype="float32") = R.broadcast_to(sum20, R.shape([1, 8]))
            maximum10: R.Tensor((1, 8), dtype="float32") = R.maximum(broadcast_to10, R.const(9.999999960041972e-13, "float32"))
            sqrt10: R.Tensor((1, 8), dtype="float32") = R.sqrt(maximum10)
            divide10: R.Tensor((1, 8), dtype="float32") = R.divide(reshape78, sqrt10)
            square21: R.Tensor((1024, 8), dtype="float32") = R.square(quantizer_quantizers_5_codebook_weight)
            sum21: R.Tensor((1024, 1), dtype="float32") = R.sum(square21, axis=[1], keepdims=True)
            broadcast_to11: R.Tensor((1024, 8), dtype="float32") = R.broadcast_to(sum21, R.shape([1024, 8]))
            maximum11: R.Tensor((1024, 8), dtype="float32") = R.maximum(broadcast_to11, R.const(9.999999960041972e-13, "float32"))
            sqrt11: R.Tensor((1024, 8), dtype="float32") = R.sqrt(maximum11)
            divide11: R.Tensor((1024, 8), dtype="float32") = R.divide(quantizer_quantizers_5_codebook_weight, sqrt11)
            square22: R.Tensor((1, 8), dtype="float32") = R.square(divide10)
            sum22: R.Tensor((1, 1), dtype="float32") = R.sum(square22, axis=[1], keepdims=True)
            permute_dims21: R.Tensor((8, 1024), dtype="float32") = R.permute_dims(divide11, axes=[1, 0])
            matmul5: R.Tensor((1, 1024), dtype="float32") = R.matmul(divide10, permute_dims21, out_dtype="void")
            mul5: R.Tensor((1, 1024), dtype="float32") = R.multiply(matmul5, R.const(2.0, "float32"))
            subtract10: R.Tensor((1, 1024), dtype="float32") = R.subtract(sum22, mul5)
            square23: R.Tensor((1024, 8), dtype="float32") = R.square(divide11)
            sum23: R.Tensor((1024, 1), dtype="float32") = R.sum(square23, axis=[1], keepdims=True)
            permute_dims22: R.Tensor((1, 1024), dtype="float32") = R.permute_dims(sum23, axes=[1, 0])
            add34: R.Tensor((1, 1024), dtype="float32") = R.add(subtract10, permute_dims22)
            argsort5: R.Tensor((1, 1024), dtype="int32") = R.argsort(add34, axis=1, descending=False, dtype="int32")
            take10: R.Tensor((1, 1), dtype="int32") = R.take(argsort5, metadata["relax.expr.Constant"][5], axis=1)
            reshape79: R.Tensor((1, 1), dtype="int32") = R.reshape(take10, R.shape([1, 1]))
            reshape80: R.Tensor((1,), dtype="int32") = R.reshape(reshape79, R.shape([1]))
            take11: R.Tensor((1, 8), dtype="float32") = R.take(quantizer_quantizers_5_codebook_weight, reshape80, axis=0)
            reshape81: R.Tensor((1, 1, 8), dtype="float32") = R.reshape(take11, R.shape([1, 1, 8]))
            permute_dims23: R.Tensor((1, 8, 1), dtype="float32") = R.permute_dims(reshape81, axes=[0, 2, 1])
            lv360: R.Tensor((1024, 8, 1), dtype="float32") = R.square(quantizer_quantizers_5_out_proj_weight_v)
            lv361: R.Tensor((1024, 1, 1), dtype="float32") = R.sum(lv360, axis=[1, 2], keepdims=True)
            lv362: R.Tensor((1024, 1, 1), dtype="float32") = R.sqrt(lv361)
            lv363: R.Tensor((1024, 8, 1), dtype="float32") = R.divide(quantizer_quantizers_5_out_proj_weight_v, lv362)
            wnconv1d41: R.Tensor((1024, 8, 1), dtype="float32") = R.multiply(quantizer_quantizers_5_out_proj_weight_g, lv363)
            lv364: R.Tensor((1, 1024, 1), dtype="float32") = R.nn.conv1d(permute_dims23, wnconv1d41, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv365: R.Tensor((1, 1024, 1), dtype="float32") = R.reshape(quantizer_quantizers_5_out_proj_bias, R.shape([1, 1024, 1]))
            conv1d41: R.Tensor((1, 1024, 1), dtype="float32") = R.add(lv364, lv365)
            add35: R.Tensor((1, 1024, 1), dtype="float32") = R.add(add33, conv1d41)
            subtract11: R.Tensor((1, 1024, 1), dtype="float32") = R.subtract(subtract9, conv1d41)
            lv366: R.Tensor((8, 1024, 1), dtype="float32") = R.square(quantizer_quantizers_6_in_proj_weight_v)
            lv367: R.Tensor((8, 1, 1), dtype="float32") = R.sum(lv366, axis=[1, 2], keepdims=True)
            lv368: R.Tensor((8, 1, 1), dtype="float32") = R.sqrt(lv367)
            lv369: R.Tensor((8, 1024, 1), dtype="float32") = R.divide(quantizer_quantizers_6_in_proj_weight_v, lv368)
            wnconv1d42: R.Tensor((8, 1024, 1), dtype="float32") = R.multiply(quantizer_quantizers_6_in_proj_weight_g, lv369)
            lv370: R.Tensor((1, 8, 1), dtype="float32") = R.nn.conv1d(subtract11, wnconv1d42, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv371: R.Tensor((1, 8, 1), dtype="float32") = R.reshape(quantizer_quantizers_6_in_proj_bias, R.shape([1, 8, 1]))
            conv1d42: R.Tensor((1, 8, 1), dtype="float32") = R.add(lv370, lv371)
            permute_dims24: R.Tensor((1, 1, 8), dtype="float32") = R.permute_dims(conv1d42, axes=[0, 2, 1])
            reshape82: R.Tensor((1, 8), dtype="float32") = R.reshape(permute_dims24, R.shape([1, 8]))
            square24: R.Tensor((1, 8), dtype="float32") = R.square(reshape82)
            sum24: R.Tensor((1, 1), dtype="float32") = R.sum(square24, axis=[1], keepdims=True)
            broadcast_to12: R.Tensor((1, 8), dtype="float32") = R.broadcast_to(sum24, R.shape([1, 8]))
            maximum12: R.Tensor((1, 8), dtype="float32") = R.maximum(broadcast_to12, R.const(9.999999960041972e-13, "float32"))
            sqrt12: R.Tensor((1, 8), dtype="float32") = R.sqrt(maximum12)
            divide12: R.Tensor((1, 8), dtype="float32") = R.divide(reshape82, sqrt12)
            square25: R.Tensor((1024, 8), dtype="float32") = R.square(quantizer_quantizers_6_codebook_weight)
            sum25: R.Tensor((1024, 1), dtype="float32") = R.sum(square25, axis=[1], keepdims=True)
            broadcast_to13: R.Tensor((1024, 8), dtype="float32") = R.broadcast_to(sum25, R.shape([1024, 8]))
            maximum13: R.Tensor((1024, 8), dtype="float32") = R.maximum(broadcast_to13, R.const(9.999999960041972e-13, "float32"))
            sqrt13: R.Tensor((1024, 8), dtype="float32") = R.sqrt(maximum13)
            divide13: R.Tensor((1024, 8), dtype="float32") = R.divide(quantizer_quantizers_6_codebook_weight, sqrt13)
            square26: R.Tensor((1, 8), dtype="float32") = R.square(divide12)
            sum26: R.Tensor((1, 1), dtype="float32") = R.sum(square26, axis=[1], keepdims=True)
            permute_dims25: R.Tensor((8, 1024), dtype="float32") = R.permute_dims(divide13, axes=[1, 0])
            matmul6: R.Tensor((1, 1024), dtype="float32") = R.matmul(divide12, permute_dims25, out_dtype="void")
            mul6: R.Tensor((1, 1024), dtype="float32") = R.multiply(matmul6, R.const(2.0, "float32"))
            subtract12: R.Tensor((1, 1024), dtype="float32") = R.subtract(sum26, mul6)
            square27: R.Tensor((1024, 8), dtype="float32") = R.square(divide13)
            sum27: R.Tensor((1024, 1), dtype="float32") = R.sum(square27, axis=[1], keepdims=True)
            permute_dims26: R.Tensor((1, 1024), dtype="float32") = R.permute_dims(sum27, axes=[1, 0])
            add36: R.Tensor((1, 1024), dtype="float32") = R.add(subtract12, permute_dims26)
            argsort6: R.Tensor((1, 1024), dtype="int32") = R.argsort(add36, axis=1, descending=False, dtype="int32")
            take12: R.Tensor((1, 1), dtype="int32") = R.take(argsort6, metadata["relax.expr.Constant"][6], axis=1)
            reshape83: R.Tensor((1, 1), dtype="int32") = R.reshape(take12, R.shape([1, 1]))
            reshape84: R.Tensor((1,), dtype="int32") = R.reshape(reshape83, R.shape([1]))
            take13: R.Tensor((1, 8), dtype="float32") = R.take(quantizer_quantizers_6_codebook_weight, reshape84, axis=0)
            reshape85: R.Tensor((1, 1, 8), dtype="float32") = R.reshape(take13, R.shape([1, 1, 8]))
            permute_dims27: R.Tensor((1, 8, 1), dtype="float32") = R.permute_dims(reshape85, axes=[0, 2, 1])
            lv372: R.Tensor((1024, 8, 1), dtype="float32") = R.square(quantizer_quantizers_6_out_proj_weight_v)
            lv373: R.Tensor((1024, 1, 1), dtype="float32") = R.sum(lv372, axis=[1, 2], keepdims=True)
            lv374: R.Tensor((1024, 1, 1), dtype="float32") = R.sqrt(lv373)
            lv375: R.Tensor((1024, 8, 1), dtype="float32") = R.divide(quantizer_quantizers_6_out_proj_weight_v, lv374)
            wnconv1d43: R.Tensor((1024, 8, 1), dtype="float32") = R.multiply(quantizer_quantizers_6_out_proj_weight_g, lv375)
            lv376: R.Tensor((1, 1024, 1), dtype="float32") = R.nn.conv1d(permute_dims27, wnconv1d43, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv377: R.Tensor((1, 1024, 1), dtype="float32") = R.reshape(quantizer_quantizers_6_out_proj_bias, R.shape([1, 1024, 1]))
            conv1d43: R.Tensor((1, 1024, 1), dtype="float32") = R.add(lv376, lv377)
            add37: R.Tensor((1, 1024, 1), dtype="float32") = R.add(add35, conv1d43)
            subtract13: R.Tensor((1, 1024, 1), dtype="float32") = R.subtract(subtract11, conv1d43)
            lv378: R.Tensor((8, 1024, 1), dtype="float32") = R.square(quantizer_quantizers_7_in_proj_weight_v)
            lv379: R.Tensor((8, 1, 1), dtype="float32") = R.sum(lv378, axis=[1, 2], keepdims=True)
            lv380: R.Tensor((8, 1, 1), dtype="float32") = R.sqrt(lv379)
            lv381: R.Tensor((8, 1024, 1), dtype="float32") = R.divide(quantizer_quantizers_7_in_proj_weight_v, lv380)
            wnconv1d44: R.Tensor((8, 1024, 1), dtype="float32") = R.multiply(quantizer_quantizers_7_in_proj_weight_g, lv381)
            lv382: R.Tensor((1, 8, 1), dtype="float32") = R.nn.conv1d(subtract13, wnconv1d44, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv383: R.Tensor((1, 8, 1), dtype="float32") = R.reshape(quantizer_quantizers_7_in_proj_bias, R.shape([1, 8, 1]))
            conv1d44: R.Tensor((1, 8, 1), dtype="float32") = R.add(lv382, lv383)
            permute_dims28: R.Tensor((1, 1, 8), dtype="float32") = R.permute_dims(conv1d44, axes=[0, 2, 1])
            reshape86: R.Tensor((1, 8), dtype="float32") = R.reshape(permute_dims28, R.shape([1, 8]))
            square28: R.Tensor((1, 8), dtype="float32") = R.square(reshape86)
            sum28: R.Tensor((1, 1), dtype="float32") = R.sum(square28, axis=[1], keepdims=True)
            broadcast_to14: R.Tensor((1, 8), dtype="float32") = R.broadcast_to(sum28, R.shape([1, 8]))
            maximum14: R.Tensor((1, 8), dtype="float32") = R.maximum(broadcast_to14, R.const(9.999999960041972e-13, "float32"))
            sqrt14: R.Tensor((1, 8), dtype="float32") = R.sqrt(maximum14)
            divide14: R.Tensor((1, 8), dtype="float32") = R.divide(reshape86, sqrt14)
            square29: R.Tensor((1024, 8), dtype="float32") = R.square(quantizer_quantizers_7_codebook_weight)
            sum29: R.Tensor((1024, 1), dtype="float32") = R.sum(square29, axis=[1], keepdims=True)
            broadcast_to15: R.Tensor((1024, 8), dtype="float32") = R.broadcast_to(sum29, R.shape([1024, 8]))
            maximum15: R.Tensor((1024, 8), dtype="float32") = R.maximum(broadcast_to15, R.const(9.999999960041972e-13, "float32"))
            sqrt15: R.Tensor((1024, 8), dtype="float32") = R.sqrt(maximum15)
            divide15: R.Tensor((1024, 8), dtype="float32") = R.divide(quantizer_quantizers_7_codebook_weight, sqrt15)
            square30: R.Tensor((1, 8), dtype="float32") = R.square(divide14)
            sum30: R.Tensor((1, 1), dtype="float32") = R.sum(square30, axis=[1], keepdims=True)
            permute_dims29: R.Tensor((8, 1024), dtype="float32") = R.permute_dims(divide15, axes=[1, 0])
            matmul7: R.Tensor((1, 1024), dtype="float32") = R.matmul(divide14, permute_dims29, out_dtype="void")
            mul7: R.Tensor((1, 1024), dtype="float32") = R.multiply(matmul7, R.const(2.0, "float32"))
            subtract14: R.Tensor((1, 1024), dtype="float32") = R.subtract(sum30, mul7)
            square31: R.Tensor((1024, 8), dtype="float32") = R.square(divide15)
            sum31: R.Tensor((1024, 1), dtype="float32") = R.sum(square31, axis=[1], keepdims=True)
            permute_dims30: R.Tensor((1, 1024), dtype="float32") = R.permute_dims(sum31, axes=[1, 0])
            add38: R.Tensor((1, 1024), dtype="float32") = R.add(subtract14, permute_dims30)
            argsort7: R.Tensor((1, 1024), dtype="int32") = R.argsort(add38, axis=1, descending=False, dtype="int32")
            take14: R.Tensor((1, 1), dtype="int32") = R.take(argsort7, metadata["relax.expr.Constant"][7], axis=1)
            reshape87: R.Tensor((1, 1), dtype="int32") = R.reshape(take14, R.shape([1, 1]))
            reshape88: R.Tensor((1,), dtype="int32") = R.reshape(reshape87, R.shape([1]))
            take15: R.Tensor((1, 8), dtype="float32") = R.take(quantizer_quantizers_7_codebook_weight, reshape88, axis=0)
            reshape89: R.Tensor((1, 1, 8), dtype="float32") = R.reshape(take15, R.shape([1, 1, 8]))
            permute_dims31: R.Tensor((1, 8, 1), dtype="float32") = R.permute_dims(reshape89, axes=[0, 2, 1])
            lv384: R.Tensor((1024, 8, 1), dtype="float32") = R.square(quantizer_quantizers_7_out_proj_weight_v)
            lv385: R.Tensor((1024, 1, 1), dtype="float32") = R.sum(lv384, axis=[1, 2], keepdims=True)
            lv386: R.Tensor((1024, 1, 1), dtype="float32") = R.sqrt(lv385)
            lv387: R.Tensor((1024, 8, 1), dtype="float32") = R.divide(quantizer_quantizers_7_out_proj_weight_v, lv386)
            wnconv1d45: R.Tensor((1024, 8, 1), dtype="float32") = R.multiply(quantizer_quantizers_7_out_proj_weight_g, lv387)
            lv388: R.Tensor((1, 1024, 1), dtype="float32") = R.nn.conv1d(permute_dims31, wnconv1d45, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv389: R.Tensor((1, 1024, 1), dtype="float32") = R.reshape(quantizer_quantizers_7_out_proj_bias, R.shape([1, 1024, 1]))
            conv1d45: R.Tensor((1, 1024, 1), dtype="float32") = R.add(lv388, lv389)
            add39: R.Tensor((1, 1024, 1), dtype="float32") = R.add(add37, conv1d45)
            subtract15: R.Tensor((1, 1024, 1), dtype="float32") = R.subtract(subtract13, conv1d45)
            lv390: R.Tensor((8, 1024, 1), dtype="float32") = R.square(quantizer_quantizers_8_in_proj_weight_v)
            lv391: R.Tensor((8, 1, 1), dtype="float32") = R.sum(lv390, axis=[1, 2], keepdims=True)
            lv392: R.Tensor((8, 1, 1), dtype="float32") = R.sqrt(lv391)
            lv393: R.Tensor((8, 1024, 1), dtype="float32") = R.divide(quantizer_quantizers_8_in_proj_weight_v, lv392)
            wnconv1d46: R.Tensor((8, 1024, 1), dtype="float32") = R.multiply(quantizer_quantizers_8_in_proj_weight_g, lv393)
            lv394: R.Tensor((1, 8, 1), dtype="float32") = R.nn.conv1d(subtract15, wnconv1d46, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv395: R.Tensor((1, 8, 1), dtype="float32") = R.reshape(quantizer_quantizers_8_in_proj_bias, R.shape([1, 8, 1]))
            conv1d46: R.Tensor((1, 8, 1), dtype="float32") = R.add(lv394, lv395)
            permute_dims32: R.Tensor((1, 1, 8), dtype="float32") = R.permute_dims(conv1d46, axes=[0, 2, 1])
            reshape90: R.Tensor((1, 8), dtype="float32") = R.reshape(permute_dims32, R.shape([1, 8]))
            square32: R.Tensor((1, 8), dtype="float32") = R.square(reshape90)
            sum32: R.Tensor((1, 1), dtype="float32") = R.sum(square32, axis=[1], keepdims=True)
            broadcast_to16: R.Tensor((1, 8), dtype="float32") = R.broadcast_to(sum32, R.shape([1, 8]))
            maximum16: R.Tensor((1, 8), dtype="float32") = R.maximum(broadcast_to16, R.const(9.999999960041972e-13, "float32"))
            sqrt16: R.Tensor((1, 8), dtype="float32") = R.sqrt(maximum16)
            divide16: R.Tensor((1, 8), dtype="float32") = R.divide(reshape90, sqrt16)
            square33: R.Tensor((1024, 8), dtype="float32") = R.square(quantizer_quantizers_8_codebook_weight)
            sum33: R.Tensor((1024, 1), dtype="float32") = R.sum(square33, axis=[1], keepdims=True)
            broadcast_to17: R.Tensor((1024, 8), dtype="float32") = R.broadcast_to(sum33, R.shape([1024, 8]))
            maximum17: R.Tensor((1024, 8), dtype="float32") = R.maximum(broadcast_to17, R.const(9.999999960041972e-13, "float32"))
            sqrt17: R.Tensor((1024, 8), dtype="float32") = R.sqrt(maximum17)
            divide17: R.Tensor((1024, 8), dtype="float32") = R.divide(quantizer_quantizers_8_codebook_weight, sqrt17)
            square34: R.Tensor((1, 8), dtype="float32") = R.square(divide16)
            sum34: R.Tensor((1, 1), dtype="float32") = R.sum(square34, axis=[1], keepdims=True)
            permute_dims33: R.Tensor((8, 1024), dtype="float32") = R.permute_dims(divide17, axes=[1, 0])
            matmul8: R.Tensor((1, 1024), dtype="float32") = R.matmul(divide16, permute_dims33, out_dtype="void")
            mul8: R.Tensor((1, 1024), dtype="float32") = R.multiply(matmul8, R.const(2.0, "float32"))
            subtract16: R.Tensor((1, 1024), dtype="float32") = R.subtract(sum34, mul8)
            square35: R.Tensor((1024, 8), dtype="float32") = R.square(divide17)
            sum35: R.Tensor((1024, 1), dtype="float32") = R.sum(square35, axis=[1], keepdims=True)
            permute_dims34: R.Tensor((1, 1024), dtype="float32") = R.permute_dims(sum35, axes=[1, 0])
            add40: R.Tensor((1, 1024), dtype="float32") = R.add(subtract16, permute_dims34)
            argsort8: R.Tensor((1, 1024), dtype="int32") = R.argsort(add40, axis=1, descending=False, dtype="int32")
            take16: R.Tensor((1, 1), dtype="int32") = R.take(argsort8, metadata["relax.expr.Constant"][8], axis=1)
            reshape91: R.Tensor((1, 1), dtype="int32") = R.reshape(take16, R.shape([1, 1]))
            reshape92: R.Tensor((1,), dtype="int32") = R.reshape(reshape91, R.shape([1]))
            take17: R.Tensor((1, 8), dtype="float32") = R.take(quantizer_quantizers_8_codebook_weight, reshape92, axis=0)
            reshape93: R.Tensor((1, 1, 8), dtype="float32") = R.reshape(take17, R.shape([1, 1, 8]))
            permute_dims35: R.Tensor((1, 8, 1), dtype="float32") = R.permute_dims(reshape93, axes=[0, 2, 1])
            lv396: R.Tensor((1024, 8, 1), dtype="float32") = R.square(quantizer_quantizers_8_out_proj_weight_v)
            lv397: R.Tensor((1024, 1, 1), dtype="float32") = R.sum(lv396, axis=[1, 2], keepdims=True)
            lv398: R.Tensor((1024, 1, 1), dtype="float32") = R.sqrt(lv397)
            lv399: R.Tensor((1024, 8, 1), dtype="float32") = R.divide(quantizer_quantizers_8_out_proj_weight_v, lv398)
            wnconv1d47: R.Tensor((1024, 8, 1), dtype="float32") = R.multiply(quantizer_quantizers_8_out_proj_weight_g, lv399)
            lv400: R.Tensor((1, 1024, 1), dtype="float32") = R.nn.conv1d(permute_dims35, wnconv1d47, strides=[1], padding=[0, 0], dilation=[1], groups=1, data_layout="NCW", kernel_layout="OIW", out_layout="NCW", out_dtype="void")
            lv401: R.Tensor((1, 1024, 1), dtype="float32") = R.reshape(quantizer_quantizers_8_out_proj_bias, R.shape([1, 1024, 1]))
            conv1d47: R.Tensor((1, 1024, 1), dtype="float32") = R.add(lv400, lv401)
            add41: R.Tensor((1, 1024, 1), dtype="float32") = R.add(add39, conv1d47)
            subtract17: R.Tensor((1, 1024, 1), dtype="float32") = R.subtract(subtract15, conv1d47)
            gv1: R.Tuple(R.Tuple(R.Tensor((1, 1024, 1), dtype="float32"), R.Tuple(R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"))), R.Tuple(R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object)) = (add41, (reshape59, reshape63, reshape67, reshape71, reshape75, reshape79, reshape83, reshape87, reshape91)), (_io, encoder_block_layers_0_cache_cache, encoder_block_layers_0_downsampling_delay_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_1_block_layers_0_block_paddings_0_cache, encoder_block_layers_1_block_layers_0_block_paddings_1_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_1_block_layers_1_block_paddings_0_cache, encoder_block_layers_1_block_layers_1_block_paddings_1_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_1_block_layers_2_block_paddings_0_cache, encoder_block_layers_1_block_layers_2_block_paddings_1_cache, encoder_block_layers_1_block_layers_4_cache_cache, encoder_block_layers_1_block_layers_4_downsampling_delay_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_2_block_layers_0_block_paddings_0_cache, encoder_block_layers_2_block_layers_0_block_paddings_1_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_2_block_layers_1_block_paddings_0_cache, encoder_block_layers_2_block_layers_1_block_paddings_1_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_2_block_layers_2_block_paddings_0_cache, encoder_block_layers_2_block_layers_2_block_paddings_1_cache, encoder_block_layers_2_block_layers_4_cache_cache, encoder_block_layers_2_block_layers_4_downsampling_delay_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_3_block_layers_0_block_paddings_0_cache, encoder_block_layers_3_block_layers_0_block_paddings_1_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_3_block_layers_1_block_paddings_0_cache, encoder_block_layers_3_block_layers_1_block_paddings_1_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_3_block_layers_2_block_paddings_0_cache, encoder_block_layers_3_block_layers_2_block_paddings_1_cache, encoder_block_layers_3_block_layers_4_cache_cache, encoder_block_layers_3_block_layers_4_downsampling_delay_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_4_block_layers_0_block_paddings_0_cache, encoder_block_layers_4_block_layers_0_block_paddings_1_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_4_block_layers_1_block_paddings_0_cache, encoder_block_layers_4_block_layers_1_block_paddings_1_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_4_block_layers_2_block_paddings_0_cache, encoder_block_layers_4_block_layers_2_block_paddings_1_cache, encoder_block_layers_4_block_layers_4_cache_cache, encoder_block_layers_4_block_layers_4_downsampling_delay_cache, encoder_block_layers_6_cache_cache, encoder_block_layers_6_downsampling_delay_cache, decoder_model_layers_0_cache_cache, decoder_model_layers_0_downsampling_delay_cache, decoder_model_layers_1_block_layers_1_cache_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_1_block_layers_2_block_paddings_0_cache, decoder_model_layers_1_block_layers_2_block_paddings_1_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_1_block_layers_3_block_paddings_0_cache, decoder_model_layers_1_block_layers_3_block_paddings_1_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_1_block_layers_4_block_paddings_0_cache, decoder_model_layers_1_block_layers_4_block_paddings_1_cache, decoder_model_layers_2_block_layers_1_cache_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_2_block_layers_2_block_paddings_0_cache, decoder_model_layers_2_block_layers_2_block_paddings_1_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_2_block_layers_3_block_paddings_0_cache, decoder_model_layers_2_block_layers_3_block_paddings_1_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_2_block_layers_4_block_paddings_0_cache, decoder_model_layers_2_block_layers_4_block_paddings_1_cache, decoder_model_layers_3_block_layers_1_cache_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_3_block_layers_2_block_paddings_0_cache, decoder_model_layers_3_block_layers_2_block_paddings_1_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_3_block_layers_3_block_paddings_0_cache, decoder_model_layers_3_block_layers_3_block_paddings_1_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_3_block_layers_4_block_paddings_0_cache, decoder_model_layers_3_block_layers_4_block_paddings_1_cache, decoder_model_layers_4_block_layers_1_cache_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_4_block_layers_2_block_paddings_0_cache, decoder_model_layers_4_block_layers_2_block_paddings_1_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_4_block_layers_3_block_paddings_0_cache, decoder_model_layers_4_block_layers_3_block_paddings_1_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_4_block_layers_4_block_paddings_0_cache, decoder_model_layers_4_block_layers_4_block_paddings_1_cache, decoder_model_layers_6_cache_cache, decoder_model_layers_6_downsampling_delay_cache)
            R.output(gv1)
        return gv1
