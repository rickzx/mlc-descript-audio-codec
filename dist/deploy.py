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
      \"data\": [3, 11, 19, 27, 35, 43, 51, 59, 67, 75]
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
    }, 
    {
      \"type_key\": \"relax.expr.Constant\", 
      \"attrs\": {
        \"_checked_type_\": \"84\", 
        \"data\": \"9\", 
        \"span\": \"0\", 
        \"struct_info_\": \"76\"
      }
    }, 
    {
      \"type_key\": \"relax.TensorStructInfo\", 
      \"attrs\": {
        \"dtype\": \"float32\", 
        \"ndim\": \"3\", 
        \"shape\": \"77\", 
        \"span\": \"0\", 
        \"vdevice\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.expr.ShapeExpr\", 
      \"attrs\": {
        \"_checked_type_\": \"83\", 
        \"span\": \"0\", 
        \"struct_info_\": \"82\", 
        \"values\": \"78\"
      }
    }, 
    {
      \"type_key\": \"Array\", 
      \"data\": [79, 80, 81]
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
      \"type_key\": \"IntImm\", 
      \"attrs\": {
        \"dtype\": \"int64\", 
        \"span\": \"0\", 
        \"value\": \"1024\"
      }
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
        \"ndim\": \"3\", 
        \"span\": \"0\", 
        \"values\": \"78\"
      }
    }, 
    {
      \"type_key\": \"relax.ShapeType\", 
      \"attrs\": {
        \"ndim\": \"3\", 
        \"span\": \"0\"
      }
    }, 
    {
      \"type_key\": \"relax.DynTensorType\", 
      \"attrs\": {
        \"dtype\": \"float32\", 
        \"ndim\": \"3\", 
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
    \"P6G0lvBAXt0AAAAAAAAAAAEAAAAAAAAAAQAAAAAgAQABAAAAAAAAAAQAAAAAAAAAAAAAAA==\", 
    \"P6G0lvBAXt0AAAAAAAAAAAEAAAAAAAAAAwAAAAIgAQABAAAAAAAAAAAEAAAAAAAAAQAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=\"
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
        T.func_attr({"op_pattern": 0})
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
        T.func_attr({"op_pattern": 0})
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
        T.func_attr({"op_pattern": 8})
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
        T.func_attr({"op_pattern": 8})
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
    def conv1d_transpose11(reshape109: T.Buffer((T.int64(1), T.int64(768), T.int64(8)), "float32"), wnconvtranspose1d1: T.Buffer((T.int64(768), T.int64(384), T.int64(16)), "float32"), compute: T.Buffer((T.int64(1), T.int64(384), T.int64(72)), "float32")):
        T.func_attr({"layout_free_buffers": [], "op_pattern": 4, "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        compute_local = T.alloc_buffer((T.int64(1), T.int64(384), T.int64(72)), scope="local")
        data_pad_shared = T.alloc_buffer((T.int64(1), T.int64(768), T.int64(87)), scope="shared")
        kernel_shared = T.alloc_buffer((T.int64(384), T.int64(768), T.int64(16)), scope="shared")
        for b_0_c_0_w_0_fused in T.thread_binding(T.int64(96), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 512, "pragma_unroll_explicit": 1}):
            for b_1_c_1_w_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for b_2_c_2_w_2_fused in T.thread_binding(T.int64(144), thread="threadIdx.x"):
                    for b_3_init, c_3_init, w_3_init, b_4_init, c_4_init, w_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2)):
                        with T.block("compute_init"):
                            v_b = T.axis.spatial(T.int64(1), b_3_init + b_4_init)
                            v_c = T.axis.spatial(T.int64(384), b_0_c_0_w_0_fused * T.int64(4) + b_2_c_2_w_2_fused // T.int64(36) + c_3_init + c_4_init)
                            v_w = T.axis.spatial(T.int64(72), b_2_c_2_w_2_fused % T.int64(36) * T.int64(2) + w_3_init * T.int64(2) + w_4_init)
                            T.reads()
                            T.writes(compute_local[v_b, v_c, v_w])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            compute_local[v_b, v_c, v_w] = T.float32(0.0)
                    for dc_0, dw_0 in T.grid(T.int64(16), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(8)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(144), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("data_pad_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(768), dc_0 * T.int64(48) + (ax0_ax1_ax2_fused_0 * T.int64(576) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(87))
                                        v2 = T.axis.spatial(T.int64(87), (ax0_ax1_ax2_fused_0 * T.int64(576) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(87))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(144) + ax0_ax1_ax2_fused_1) * T.int64(4) + ax0_ax1_ax2_fused_2 < T.int64(4176))
                                        T.reads(reshape109[v0, v1, (v2 - T.int64(15)) // T.int64(8)])
                                        T.writes(data_pad_shared[v0, v1, v2])
                                        data_pad_shared[v0, v1, v2] = T.if_then_else(T.int64(15) <= v2 and v2 < T.int64(72), T.if_then_else((v2 - T.int64(15)) % T.int64(8) == T.int64(0), reshape109[v0, v1, (v2 - T.int64(15)) // T.int64(8)], T.float32(0.0)), T.float32(0.0))
                        for ax0_ax1_ax2_fused_0 in range(T.int64(22)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(144), thread="threadIdx.x"):
                                with T.block("kernel_shared"):
                                    v0 = T.axis.spatial(T.int64(384), b_0_c_0_w_0_fused * T.int64(4) + (ax0_ax1_ax2_fused_0 * T.int64(144) + ax0_ax1_ax2_fused_1) // T.int64(768))
                                    v1 = T.axis.spatial(T.int64(768), dc_0 * T.int64(48) + (ax0_ax1_ax2_fused_0 * T.int64(144) + ax0_ax1_ax2_fused_1) % T.int64(768) // T.int64(16))
                                    v2 = T.axis.spatial(T.int64(16), (ax0_ax1_ax2_fused_0 * T.int64(144) + ax0_ax1_ax2_fused_1) % T.int64(16))
                                    T.where(ax0_ax1_ax2_fused_0 * T.int64(144) + ax0_ax1_ax2_fused_1 < T.int64(3072))
                                    T.reads(wnconvtranspose1d1[v1, v0, T.int64(15) - v2])
                                    T.writes(kernel_shared[v0, v1, v2])
                                    kernel_shared[v0, v1, v2] = wnconvtranspose1d1[v1, v0, T.int64(15) - v2]
                        for dc_1, dw_1, b_3, c_3, w_3, dc_2, dw_2, b_4, c_4, w_4 in T.grid(T.int64(1), T.int64(2), T.int64(1), T.int64(1), T.int64(1), T.int64(48), T.int64(8), T.int64(1), T.int64(1), T.int64(2)):
                            with T.block("compute_update"):
                                v_b = T.axis.spatial(T.int64(1), b_3 + b_4)
                                v_c = T.axis.spatial(T.int64(384), b_0_c_0_w_0_fused * T.int64(4) + b_2_c_2_w_2_fused // T.int64(36) + c_3 + c_4)
                                v_w = T.axis.spatial(T.int64(72), b_2_c_2_w_2_fused % T.int64(36) * T.int64(2) + w_3 * T.int64(2) + w_4)
                                v_dc = T.axis.reduce(T.int64(768), dc_0 * T.int64(48) + dc_1 * T.int64(48) + dc_2)
                                v_dw = T.axis.reduce(T.int64(16), dw_0 * T.int64(16) + dw_1 * T.int64(8) + dw_2)
                                T.reads(compute_local[v_b, v_c, v_w], data_pad_shared[v_b, v_dc, v_w + v_dw], kernel_shared[v_c, v_dc, v_dw])
                                T.writes(compute_local[v_b, v_c, v_w])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                compute_local[v_b, v_c, v_w] = compute_local[v_b, v_c, v_w] + data_pad_shared[v_b, v_dc, v_w + v_dw] * kernel_shared[v_c, v_dc, v_dw]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(2)):
                        with T.block("compute_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(384), b_0_c_0_w_0_fused * T.int64(4) + b_2_c_2_w_2_fused // T.int64(36) + ax1)
                            v2 = T.axis.spatial(T.int64(72), b_2_c_2_w_2_fused % T.int64(36) * T.int64(2) + ax2)
                            T.reads(compute_local[v0, v1, v2])
                            T.writes(compute[v0, v1, v2])
                            compute[v0, v1, v2] = compute_local[v0, v1, v2]

    @T.prim_func(private=True)
    def conv1d_transpose21(reshape123: T.Buffer((T.int64(1), T.int64(384), T.int64(64)), "float32"), wnconvtranspose1d2: T.Buffer((T.int64(384), T.int64(192), T.int64(8)), "float32"), compute: T.Buffer((T.int64(1), T.int64(192), T.int64(260)), "float32")):
        T.func_attr({"layout_free_buffers": [], "op_pattern": 4, "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        compute_local = T.alloc_buffer((T.int64(1), T.int64(192), T.int64(260)), scope="local")
        data_pad_shared = T.alloc_buffer((T.int64(1), T.int64(384), T.int64(267)), scope="shared")
        kernel_shared = T.alloc_buffer((T.int64(192), T.int64(384), T.int64(8)), scope="shared")
        for b_0_c_0_w_0_fused in T.thread_binding(T.int64(160), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for b_1_c_1_w_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for b_2_c_2_w_2_fused in T.thread_binding(T.int64(156), thread="threadIdx.x"):
                    for b_3_init, c_3_init, w_3_init, b_4_init, c_4_init, w_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2)):
                        with T.block("compute_init"):
                            v_b = T.axis.spatial(T.int64(1), b_3_init + b_4_init)
                            v_c = T.axis.spatial(T.int64(192), b_0_c_0_w_0_fused // T.int64(10) * T.int64(12) + b_2_c_2_w_2_fused // T.int64(13) + c_3_init + c_4_init)
                            v_w = T.axis.spatial(T.int64(260), b_0_c_0_w_0_fused % T.int64(10) * T.int64(26) + b_2_c_2_w_2_fused % T.int64(13) * T.int64(2) + w_3_init * T.int64(2) + w_4_init)
                            T.reads()
                            T.writes(compute_local[v_b, v_c, v_w])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            compute_local[v_b, v_c, v_w] = T.float32(0.0)
                    for dc_0, dw_0 in T.grid(T.int64(16), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(2)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(156), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(3)):
                                    with T.block("data_pad_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(384), dc_0 * T.int64(24) + (ax0_ax1_ax2_fused_0 * T.int64(468) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) // T.int64(33))
                                        v2 = T.axis.spatial(T.int64(267), b_0_c_0_w_0_fused % T.int64(10) * T.int64(26) + (ax0_ax1_ax2_fused_0 * T.int64(468) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) % T.int64(33))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(156) + ax0_ax1_ax2_fused_1) * T.int64(3) + ax0_ax1_ax2_fused_2 < T.int64(792))
                                        T.reads(reshape123[v0, v1, (v2 - T.int64(7)) // T.int64(4)])
                                        T.writes(data_pad_shared[v0, v1, v2])
                                        data_pad_shared[v0, v1, v2] = T.if_then_else(T.int64(7) <= v2 and v2 < T.int64(260), T.if_then_else((v2 - T.int64(7)) % T.int64(4) == T.int64(0), reshape123[v0, v1, (v2 - T.int64(7)) // T.int64(4)], T.float32(0.0)), T.float32(0.0))
                        for ax0_ax1_ax2_fused_0 in range(T.int64(5)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(156), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(3)):
                                    with T.block("kernel_shared"):
                                        v0 = T.axis.spatial(T.int64(192), b_0_c_0_w_0_fused // T.int64(10) * T.int64(12) + (ax0_ax1_ax2_fused_0 * T.int64(468) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) // T.int64(192))
                                        v1 = T.axis.spatial(T.int64(384), dc_0 * T.int64(24) + (ax0_ax1_ax2_fused_0 * T.int64(468) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) % T.int64(192) // T.int64(8))
                                        v2 = T.axis.spatial(T.int64(8), (ax0_ax1_ax2_fused_0 * T.int64(468) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) % T.int64(8))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(156) + ax0_ax1_ax2_fused_1) * T.int64(3) + ax0_ax1_ax2_fused_2 < T.int64(2304))
                                        T.reads(wnconvtranspose1d2[v1, v0, T.int64(7) - v2])
                                        T.writes(kernel_shared[v0, v1, v2])
                                        kernel_shared[v0, v1, v2] = wnconvtranspose1d2[v1, v0, T.int64(7) - v2]
                        for dc_1, dw_1, b_3, c_3, w_3, dc_2, dw_2, b_4, c_4, w_4 in T.grid(T.int64(24), T.int64(2), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(4), T.int64(1), T.int64(1), T.int64(2)):
                            with T.block("compute_update"):
                                v_b = T.axis.spatial(T.int64(1), b_3 + b_4)
                                v_c = T.axis.spatial(T.int64(192), b_0_c_0_w_0_fused // T.int64(10) * T.int64(12) + b_2_c_2_w_2_fused // T.int64(13) + c_3 + c_4)
                                v_w = T.axis.spatial(T.int64(260), b_0_c_0_w_0_fused % T.int64(10) * T.int64(26) + b_2_c_2_w_2_fused % T.int64(13) * T.int64(2) + w_3 * T.int64(2) + w_4)
                                v_dc = T.axis.reduce(T.int64(384), dc_0 * T.int64(24) + dc_1 + dc_2)
                                v_dw = T.axis.reduce(T.int64(8), dw_0 * T.int64(8) + dw_1 * T.int64(4) + dw_2)
                                T.reads(compute_local[v_b, v_c, v_w], data_pad_shared[v_b, v_dc, v_w + v_dw], kernel_shared[v_c, v_dc, v_dw])
                                T.writes(compute_local[v_b, v_c, v_w])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                compute_local[v_b, v_c, v_w] = compute_local[v_b, v_c, v_w] + data_pad_shared[v_b, v_dc, v_w + v_dw] * kernel_shared[v_c, v_dc, v_dw]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(2)):
                        with T.block("compute_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(192), b_0_c_0_w_0_fused // T.int64(10) * T.int64(12) + b_2_c_2_w_2_fused // T.int64(13) + ax1)
                            v2 = T.axis.spatial(T.int64(260), b_0_c_0_w_0_fused % T.int64(10) * T.int64(26) + b_2_c_2_w_2_fused % T.int64(13) * T.int64(2) + ax2)
                            T.reads(compute_local[v0, v1, v2])
                            T.writes(compute[v0, v1, v2])
                            compute[v0, v1, v2] = compute_local[v0, v1, v2]

    @T.prim_func(private=True)
    def conv1d_transpose31(reshape137: T.Buffer((T.int64(1), T.int64(192), T.int64(256)), "float32"), wnconvtranspose1d3: T.Buffer((T.int64(192), T.int64(96), T.int64(4)), "float32"), compute: T.Buffer((T.int64(1), T.int64(96), T.int64(514)), "float32")):
        T.func_attr({"layout_free_buffers": [], "op_pattern": 4, "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        compute_local = T.alloc_buffer((T.int64(1), T.int64(96), T.int64(514)), scope="local")
        data_pad_shared = T.alloc_buffer((T.int64(1), T.int64(192), T.int64(517)), scope="shared")
        kernel_shared = T.alloc_buffer((T.int64(96), T.int64(192), T.int64(4)), scope="shared")
        for b_0_c_0_w_0_fused in T.thread_binding(T.int64(48), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 16, "pragma_unroll_explicit": 1}):
            for b_1_c_1_w_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for b_2_c_2_w_2_fused in T.thread_binding(T.int64(514), thread="threadIdx.x"):
                    for b_3_init, c_3_init, w_3_init, b_4_init, c_4_init, w_4_init in T.grid(T.int64(1), T.int64(2), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("compute_init"):
                            v_b = T.axis.spatial(T.int64(1), b_3_init + b_4_init)
                            v_c = T.axis.spatial(T.int64(96), b_0_c_0_w_0_fused // T.int64(2) * T.int64(4) + b_2_c_2_w_2_fused // T.int64(257) * T.int64(2) + c_3_init + c_4_init)
                            v_w = T.axis.spatial(T.int64(514), b_0_c_0_w_0_fused % T.int64(2) * T.int64(257) + b_2_c_2_w_2_fused % T.int64(257) + w_3_init + w_4_init)
                            T.reads()
                            T.writes(compute_local[v_b, v_c, v_w])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            compute_local[v_b, v_c, v_w] = T.float32(0.0)
                    for dc_0, dw_0 in T.grid(T.int64(8), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(4)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(514), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("data_pad_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(192), dc_0 * T.int64(24) + (ax0_ax1_ax2_fused_0 * T.int64(2056) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(260))
                                        v2 = T.axis.spatial(T.int64(517), b_0_c_0_w_0_fused % T.int64(2) * T.int64(257) + (ax0_ax1_ax2_fused_0 * T.int64(2056) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(260))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(514) + ax0_ax1_ax2_fused_1) * T.int64(4) + ax0_ax1_ax2_fused_2 < T.int64(6240))
                                        T.reads(reshape137[v0, v1, (v2 - T.int64(3)) // T.int64(2)])
                                        T.writes(data_pad_shared[v0, v1, v2])
                                        data_pad_shared[v0, v1, v2] = T.if_then_else(T.int64(3) <= v2 and v2 < T.int64(514), T.if_then_else((v2 - T.int64(3)) % T.int64(2) == T.int64(0), reshape137[v0, v1, (v2 - T.int64(3)) // T.int64(2)], T.float32(0.0)), T.float32(0.0))
                        for ax0_ax1_ax2_fused_0 in range(T.int64(1)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(514), thread="threadIdx.x"):
                                with T.block("kernel_shared"):
                                    v0 = T.axis.spatial(T.int64(96), b_0_c_0_w_0_fused // T.int64(2) * T.int64(4) + (ax0_ax1_ax2_fused_0 * T.int64(514) + ax0_ax1_ax2_fused_1) // T.int64(96))
                                    v1 = T.axis.spatial(T.int64(192), dc_0 * T.int64(24) + (ax0_ax1_ax2_fused_0 * T.int64(514) + ax0_ax1_ax2_fused_1) % T.int64(96) // T.int64(4))
                                    v2 = T.axis.spatial(T.int64(4), (ax0_ax1_ax2_fused_0 * T.int64(514) + ax0_ax1_ax2_fused_1) % T.int64(4))
                                    T.where(ax0_ax1_ax2_fused_0 * T.int64(514) + ax0_ax1_ax2_fused_1 < T.int64(384))
                                    T.reads(wnconvtranspose1d3[v1, v0, T.int64(3) - v2])
                                    T.writes(kernel_shared[v0, v1, v2])
                                    kernel_shared[v0, v1, v2] = wnconvtranspose1d3[v1, v0, T.int64(3) - v2]
                        for dc_1, dw_1, b_3, c_3, w_3, dc_2, dw_2, b_4, c_4, w_4 in T.grid(T.int64(12), T.int64(1), T.int64(1), T.int64(2), T.int64(1), T.int64(2), T.int64(4), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("compute_update"):
                                v_b = T.axis.spatial(T.int64(1), b_3 + b_4)
                                v_c = T.axis.spatial(T.int64(96), b_0_c_0_w_0_fused // T.int64(2) * T.int64(4) + b_2_c_2_w_2_fused // T.int64(257) * T.int64(2) + c_3 + c_4)
                                v_w = T.axis.spatial(T.int64(514), b_0_c_0_w_0_fused % T.int64(2) * T.int64(257) + b_2_c_2_w_2_fused % T.int64(257) + w_3 + w_4)
                                v_dc = T.axis.reduce(T.int64(192), dc_0 * T.int64(24) + dc_1 * T.int64(2) + dc_2)
                                v_dw = T.axis.reduce(T.int64(4), dw_0 * T.int64(4) + dw_1 * T.int64(4) + dw_2)
                                T.reads(compute_local[v_b, v_c, v_w], data_pad_shared[v_b, v_dc, v_w + v_dw], kernel_shared[v_c, v_dc, v_dw])
                                T.writes(compute_local[v_b, v_c, v_w])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                compute_local[v_b, v_c, v_w] = compute_local[v_b, v_c, v_w] + data_pad_shared[v_b, v_dc, v_w + v_dw] * kernel_shared[v_c, v_dc, v_dw]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(2), T.int64(1)):
                        with T.block("compute_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(96), b_0_c_0_w_0_fused // T.int64(2) * T.int64(4) + b_2_c_2_w_2_fused // T.int64(257) * T.int64(2) + ax1)
                            v2 = T.axis.spatial(T.int64(514), b_0_c_0_w_0_fused % T.int64(2) * T.int64(257) + b_2_c_2_w_2_fused % T.int64(257) + ax2)
                            T.reads(compute_local[v0, v1, v2])
                            T.writes(compute[v0, v1, v2])
                            compute[v0, v1, v2] = compute_local[v0, v1, v2]

    @T.prim_func(private=True)
    def conv1d_transpose4(reshape95: T.Buffer((T.int64(1), T.int64(1536), T.int64(1)), "float32"), wnconvtranspose1d: T.Buffer((T.int64(1536), T.int64(768), T.int64(16)), "float32"), compute: T.Buffer((T.int64(1), T.int64(768), T.int64(16)), "float32")):
        T.func_attr({"layout_free_buffers": [], "op_pattern": 4, "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        compute_local = T.alloc_buffer((T.int64(1), T.int64(768), T.int64(16)), scope="local")
        data_pad_shared = T.alloc_buffer((T.int64(1), T.int64(1536), T.int64(31)), scope="shared")
        kernel_shared = T.alloc_buffer((T.int64(768), T.int64(1536), T.int64(16)), scope="shared")
        for b_0_c_0_w_0_fused in T.thread_binding(T.int64(192), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for b_1_c_1_w_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for b_2_c_2_w_2_fused in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                    for b_3_init, c_3_init, w_3_init, b_4_init, c_4_init, w_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("compute_init"):
                            v_b = T.axis.spatial(T.int64(1), b_3_init + b_4_init)
                            v_c = T.axis.spatial(T.int64(768), b_0_c_0_w_0_fused * T.int64(4) + b_2_c_2_w_2_fused // T.int64(16) + c_3_init + c_4_init)
                            v_w = T.axis.spatial(T.int64(16), b_2_c_2_w_2_fused % T.int64(16) + w_3_init + w_4_init)
                            T.reads()
                            T.writes(compute_local[v_b, v_c, v_w])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            compute_local[v_b, v_c, v_w] = T.float32(0.0)
                    for dc_0, dw_0 in T.grid(T.int64(48), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(8)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(2)):
                                    with T.block("data_pad_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(1536), dc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) // T.int64(31))
                                        v2 = T.axis.spatial(T.int64(31), (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(31))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) * T.int64(2) + ax0_ax1_ax2_fused_2 < T.int64(992))
                                        T.reads(reshape95[v0, v1, (v2 - T.int64(15)) // T.int64(8)])
                                        T.writes(data_pad_shared[v0, v1, v2])
                                        data_pad_shared[v0, v1, v2] = T.if_then_else(T.int64(15) <= v2 and v2 < T.int64(16), T.if_then_else((v2 - T.int64(15)) % T.int64(8) == T.int64(0), reshape95[v0, v1, (v2 - T.int64(15)) // T.int64(8)], T.float32(0.0)), T.float32(0.0))
                        for ax0_ax1_ax2_fused_0 in range(T.int64(32)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                                with T.block("kernel_shared"):
                                    v0 = T.axis.spatial(T.int64(768), b_0_c_0_w_0_fused * T.int64(4) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) // T.int64(512))
                                    v1 = T.axis.spatial(T.int64(1536), dc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) % T.int64(512) // T.int64(16))
                                    v2 = T.axis.spatial(T.int64(16), (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) % T.int64(16))
                                    T.reads(wnconvtranspose1d[v1, v0, T.int64(15) - v2])
                                    T.writes(kernel_shared[v0, v1, v2])
                                    kernel_shared[v0, v1, v2] = wnconvtranspose1d[v1, v0, T.int64(15) - v2]
                        for dc_1, dw_1, b_3, c_3, w_3, dc_2, dw_2, b_4, c_4, w_4 in T.grid(T.int64(32), T.int64(2), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(8), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("compute_update"):
                                v_b = T.axis.spatial(T.int64(1), b_3 + b_4)
                                v_c = T.axis.spatial(T.int64(768), b_0_c_0_w_0_fused * T.int64(4) + b_2_c_2_w_2_fused // T.int64(16) + c_3 + c_4)
                                v_w = T.axis.spatial(T.int64(16), b_2_c_2_w_2_fused % T.int64(16) + w_3 + w_4)
                                v_dc = T.axis.reduce(T.int64(1536), dc_0 * T.int64(32) + dc_1 + dc_2)
                                v_dw = T.axis.reduce(T.int64(16), dw_0 * T.int64(16) + dw_1 * T.int64(8) + dw_2)
                                T.reads(compute_local[v_b, v_c, v_w], data_pad_shared[v_b, v_dc, v_w + v_dw], kernel_shared[v_c, v_dc, v_dw])
                                T.writes(compute_local[v_b, v_c, v_w])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                compute_local[v_b, v_c, v_w] = compute_local[v_b, v_c, v_w] + data_pad_shared[v_b, v_dc, v_w + v_dw] * kernel_shared[v_c, v_dc, v_dw]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("compute_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(768), b_0_c_0_w_0_fused * T.int64(4) + b_2_c_2_w_2_fused // T.int64(16) + ax1)
                            v2 = T.axis.spatial(T.int64(16), b_2_c_2_w_2_fused % T.int64(16) + ax2)
                            T.reads(compute_local[v0, v1, v2])
                            T.writes(compute[v0, v1, v2])
                            compute[v0, v1, v2] = compute_local[v0, v1, v2]

    @T.prim_func(private=True)
    def fused_add30_add30_add30_add30_add30_add30_add30_add30_conv1d41_add30_add301(param_0: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32"), conv1d31: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32"), conv1d33: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32"), conv1d35: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32"), conv1d37: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32"), conv1d39: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32"), conv1d41: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32"), conv1d43: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32"), conv1d45: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32"), permute_dims35: T.Buffer((T.int64(1), T.int64(8), T.int64(1)), "float32"), wnconv1d47: T.Buffer((T.int64(1024), T.int64(8), T.int64(1)), "float32"), lv401: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32"), T_add_intermediate_1_2_3_4_5_6_7_8_9: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32")):
        T.func_attr({"layout_free_buffers": [0], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(1)))
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(1)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(8), T.int64(1)), scope="shared")
        wnconv1d47_shared = T.alloc_buffer((T.int64(1024), T.int64(8), T.int64(1)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(2), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 1024, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(4), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(1024), nn_0_ff_0_yy_0_fused * T.int64(512) + nn_2_ff_2_yy_2_fused * T.int64(4) + ff_3_init * T.int64(4) + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(1), yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(1), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(1)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(8), ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2)
                                        v2 = T.axis.spatial(T.int64(1), T.int64(0))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) * T.int64(4) + ax0_ax1_ax2_fused_2 < T.int64(8))
                                        T.reads(permute_dims35[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = permute_dims35[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(32)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                with T.block("wnconv1d47_shared"):
                                    v0 = T.axis.spatial(T.int64(1024), nn_0_ff_0_yy_0_fused * T.int64(512) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) // T.int64(8))
                                    v1 = T.axis.spatial(T.int64(8), (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) % T.int64(8))
                                    v2 = T.axis.spatial(T.int64(1), T.int64(0))
                                    T.reads(wnconv1d47[v0, v1, v2])
                                    T.writes(wnconv1d47_shared[v0, v1, v2])
                                    wnconv1d47_shared[v0, v1, v2] = wnconv1d47[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(4), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2), T.int64(1), T.int64(1), T.int64(4), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(1024), nn_0_ff_0_yy_0_fused * T.int64(512) + nn_2_ff_2_yy_2_fused * T.int64(4) + ff_3 * T.int64(4) + ff_4)
                                v_yy = T.axis.spatial(T.int64(1), yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(8), rc_0 * T.int64(8) + rc_1 * T.int64(2) + rc_2)
                                v_ry = T.axis.reduce(T.int64(1), ry_0 + ry_1 + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d47_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d47_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(4), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(1024), nn_0_ff_0_yy_0_fused * T.int64(512) + nn_2_ff_2_yy_2_fused * T.int64(4) + ax1)
                            v2 = T.axis.spatial(T.int64(1), ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2])
                            T.writes(conv1d_ncw_intermediate[v0, v1, v2])
                            conv1d_ncw_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2]
        for ax0_ax1_ax2_fused_0 in T.thread_binding(T.int64(2), thread="blockIdx.x"):
            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(512), thread="threadIdx.x"):
                with T.block("T_add_9"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(1024), ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1)
                    v_ax2 = T.axis.spatial(T.int64(1), T.int64(0))
                    T.reads(param_0[v_ax0, v_ax1, v_ax2], conv1d31[v_ax0, v_ax1, v_ax2], conv1d33[v_ax0, v_ax1, v_ax2], conv1d35[v_ax0, v_ax1, v_ax2], conv1d37[v_ax0, v_ax1, v_ax2], conv1d39[v_ax0, v_ax1, v_ax2], conv1d41[v_ax0, v_ax1, v_ax2], conv1d43[v_ax0, v_ax1, v_ax2], conv1d45[v_ax0, v_ax1, v_ax2], conv1d_ncw_intermediate[v_ax0, v_ax1, v_ax2], lv401[v_ax0, v_ax1, v_ax2])
                    T.writes(T_add_intermediate_1_2_3_4_5_6_7_8_9[v_ax0, v_ax1, v_ax2])
                    T_add_intermediate_1_2_3_4_5_6_7_8_9[v_ax0, v_ax1, v_ax2] = param_0[v_ax0, v_ax1, v_ax2] + conv1d31[v_ax0, v_ax1, v_ax2] + conv1d33[v_ax0, v_ax1, v_ax2] + conv1d35[v_ax0, v_ax1, v_ax2] + conv1d37[v_ax0, v_ax1, v_ax2] + conv1d39[v_ax0, v_ax1, v_ax2] + conv1d41[v_ax0, v_ax1, v_ax2] + conv1d43[v_ax0, v_ax1, v_ax2] + conv1d45[v_ax0, v_ax1, v_ax2] + (conv1d_ncw_intermediate[v_ax0, v_ax1, v_ax2] + lv401[v_ax0, v_ax1, v_ax2])

    @T.prim_func(private=True)
    def fused_broadcast_to_maximum_tir_sqrt12_divide291(sum: T.Buffer((T.int64(1), T.int64(1)), "float32"), reshape58: T.Buffer((T.int64(1), T.int64(8)), "float32"), T_divide_intermediate: T.Buffer((T.int64(1), T.int64(8)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_fused_0 in T.thread_binding(T.int64(1), thread="blockIdx.x"):
            for ax0_ax1_fused_1 in T.thread_binding(T.int64(8), thread="threadIdx.x"):
                with T.block("T_broadcast_to"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(8), ax0_ax1_fused_0 * T.int64(8) + ax0_ax1_fused_1)
                    T.reads(reshape58[v_ax0, v_ax1], sum[v_ax0, T.int64(0)])
                    T.writes(T_divide_intermediate[v_ax0, v_ax1])
                    T_divide_intermediate[v_ax0, v_ax1] = reshape58[v_ax0, v_ax1] / T.sqrt(T.max(sum[v_ax0, T.int64(0)], T.float32(9.999999960041972e-13)))

    @T.prim_func(private=True)
    def fused_conv1d10_add10_add11_add121(lv560: T.Buffer((T.int64(1), T.int64(192), T.int64(256)), "float32"), wnconv1d62: T.Buffer((T.int64(192), T.int64(192), T.int64(1)), "float32"), lv566: T.Buffer((T.int64(1), T.int64(192), T.int64(1)), "float32"), lv567: T.Buffer((T.int64(1), T.int64(192), T.int64(256)), "float32"), T_add_intermediate_1_2: T.Buffer((T.int64(1), T.int64(192), T.int64(256)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(192), T.int64(256)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(192), T.int64(256)), scope="shared")
        wnconv1d62_shared = T.alloc_buffer((T.int64(192), T.int64(192), T.int64(1)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(64), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(3), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(192), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(48) + nn_1_ff_1_yy_1_fused * T.int64(16) + nn_2_ff_2_yy_2_fused // T.int64(16) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(16) + nn_2_ff_2_yy_2_fused % T.int64(16) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(4), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(1)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(192), rc_0 * T.int64(48) + (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(16))
                                        v2 = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(16))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1) * T.int64(4) + ax0_ax1_ax2_fused_2 < T.int64(768))
                                        T.reads(lv560[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv560[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(9)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                                with T.block("wnconv1d62_shared"):
                                    v0 = T.axis.spatial(T.int64(192), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(48) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1) // T.int64(48))
                                    v1 = T.axis.spatial(T.int64(192), rc_0 * T.int64(48) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1) % T.int64(48))
                                    v2 = T.axis.spatial(T.int64(1), T.int64(0))
                                    T.reads(wnconv1d62[v0, v1, v2])
                                    T.writes(wnconv1d62_shared[v0, v1, v2])
                                    wnconv1d62_shared[v0, v1, v2] = wnconv1d62[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(2), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(24), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(192), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(48) + nn_1_ff_1_yy_1_fused * T.int64(16) + nn_2_ff_2_yy_2_fused // T.int64(16) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(16) + nn_2_ff_2_yy_2_fused % T.int64(16) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(192), rc_0 * T.int64(48) + rc_1 * T.int64(24) + rc_2)
                                v_ry = T.axis.reduce(T.int64(1), ry_0 + ry_1 + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d62_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d62_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(192), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(48) + nn_1_ff_1_yy_1_fused * T.int64(16) + nn_2_ff_2_yy_2_fused // T.int64(16) + ax1)
                            v2 = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(16) + nn_2_ff_2_yy_2_fused % T.int64(16) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv566[v0, v1, T.int64(0)], lv567[v0, v1, v2])
                            T.writes(T_add_intermediate_1_2[v0, v1, v2])
                            T_add_intermediate_1_2[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv566[v0, v1, T.int64(0)] + lv567[v0, v1, v2]

    @T.prim_func(private=True)
    def fused_conv1d11_add101(lv571: T.Buffer((T.int64(1), T.int64(192), T.int64(274)), "float32"), wnconv1d63: T.Buffer((T.int64(192), T.int64(192), T.int64(7)), "float32"), lv577: T.Buffer((T.int64(1), T.int64(192), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(192), T.int64(256)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(192), T.int64(256)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(192), T.int64(274)), scope="shared")
        wnconv1d63_shared = T.alloc_buffer((T.int64(192), T.int64(192), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(96), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 512, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(2), T.int64(1), T.int64(1), T.int64(1), T.int64(2)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(192), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(16) + nn_2_ff_2_yy_2_fused // T.int64(16) * T.int64(2) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(16) * T.int64(2) + yy_3_init * T.int64(2) + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(6), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(4)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(192), rc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(50))
                                        v2 = T.axis.spatial(T.int64(274), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(50))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) * T.int64(4) + ax0_ax1_ax2_fused_2 < T.int64(1600))
                                        T.reads(lv571[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv571[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(7)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("wnconv1d63_shared"):
                                        v0 = T.axis.spatial(T.int64(192), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(224))
                                        v1 = T.axis.spatial(T.int64(192), rc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(224) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.reads(wnconv1d63[v0, v1, v2])
                                        T.writes(wnconv1d63_shared[v0, v1, v2])
                                        wnconv1d63_shared[v0, v1, v2] = wnconv1d63[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(32), T.int64(7), T.int64(1), T.int64(2), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(192), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(16) + nn_2_ff_2_yy_2_fused // T.int64(16) * T.int64(2) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(16) * T.int64(2) + yy_3 * T.int64(2) + yy_4)
                                v_rc = T.axis.reduce(T.int64(192), rc_0 * T.int64(32) + rc_1 + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_ry * T.int64(3) + v_yy], wnconv1d63_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_ry * T.int64(3) + v_yy] * wnconv1d63_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(2), T.int64(2)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(192), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(16) + nn_2_ff_2_yy_2_fused // T.int64(16) * T.int64(2) + ax1)
                            v2 = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(16) * T.int64(2) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv577[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv577[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d12_add101(lv591: T.Buffer((T.int64(1), T.int64(192), T.int64(310)), "float32"), wnconv1d65: T.Buffer((T.int64(192), T.int64(192), T.int64(7)), "float32"), lv597: T.Buffer((T.int64(1), T.int64(192), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(192), T.int64(256)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(192), T.int64(256)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(192), T.int64(310)), scope="shared")
        wnconv1d65_shared = T.alloc_buffer((T.int64(192), T.int64(192), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(256), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 16, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(96), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(2), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(192), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(6) + nn_2_ff_2_yy_2_fused // T.int64(32) * T.int64(2) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(12), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(8)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(96), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(2)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(192), rc_0 * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(192) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) // T.int64(86))
                                        v2 = T.axis.spatial(T.int64(310), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(192) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(86))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(96) + ax0_ax1_ax2_fused_1) * T.int64(2) + ax0_ax1_ax2_fused_2 < T.int64(1376))
                                        T.reads(lv591[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv591[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(7)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(96), thread="threadIdx.x"):
                                with T.block("wnconv1d65_shared"):
                                    v0 = T.axis.spatial(T.int64(192), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(6) + (ax0_ax1_ax2_fused_0 * T.int64(96) + ax0_ax1_ax2_fused_1) // T.int64(112))
                                    v1 = T.axis.spatial(T.int64(192), rc_0 * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(96) + ax0_ax1_ax2_fused_1) % T.int64(112) // T.int64(7))
                                    v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(96) + ax0_ax1_ax2_fused_1) % T.int64(7))
                                    T.reads(wnconv1d65[v0, v1, v2])
                                    T.writes(wnconv1d65_shared[v0, v1, v2])
                                    wnconv1d65_shared[v0, v1, v2] = wnconv1d65[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(16), T.int64(7), T.int64(1), T.int64(2), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(192), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(6) + nn_2_ff_2_yy_2_fused // T.int64(32) * T.int64(2) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(192), rc_0 * T.int64(16) + rc_1 + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_ry * T.int64(9) + v_yy], wnconv1d65_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_ry * T.int64(9) + v_yy] * wnconv1d65_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(2), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(192), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(6) + nn_2_ff_2_yy_2_fused // T.int64(32) * T.int64(2) + ax1)
                            v2 = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv597[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv597[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d13_add141(lv617: T.Buffer((T.int64(1), T.int64(96), T.int64(518)), "float32"), wnconv1d67: T.Buffer((T.int64(96), T.int64(96), T.int64(7)), "float32"), lv623: T.Buffer((T.int64(1), T.int64(96), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(96), T.int64(512)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(96), T.int64(512)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(96), T.int64(518)), scope="shared")
        wnconv1d67_shared = T.alloc_buffer((T.int64(96), T.int64(96), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(96), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(2), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(96), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(32) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(64) + nn_2_ff_2_yy_2_fused % T.int64(32) * T.int64(2) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(4), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(2)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(96), rc_0 * T.int64(24) + (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(70))
                                        v2 = T.axis.spatial(T.int64(518), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(70))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1) * T.int64(4) + ax0_ax1_ax2_fused_2 < T.int64(1680))
                                        T.reads(lv617[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv617[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(2)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("wnconv1d67_shared"):
                                        v0 = T.axis.spatial(T.int64(96), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(8) + (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(168))
                                        v1 = T.axis.spatial(T.int64(96), rc_0 * T.int64(24) + (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(168) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1) * T.int64(4) + ax0_ax1_ax2_fused_2 < T.int64(1344))
                                        T.reads(wnconv1d67[v0, v1, v2])
                                        T.writes(wnconv1d67_shared[v0, v1, v2])
                                        wnconv1d67_shared[v0, v1, v2] = wnconv1d67[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(24), T.int64(1), T.int64(1), T.int64(1), T.int64(2), T.int64(1), T.int64(7), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(96), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(32) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(64) + nn_2_ff_2_yy_2_fused % T.int64(32) * T.int64(2) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(96), rc_0 * T.int64(24) + rc_1 + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 * T.int64(7) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d67_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d67_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(2)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(96), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(32) + ax1)
                            v2 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(64) + nn_2_ff_2_yy_2_fused % T.int64(32) * T.int64(2) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv623[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv623[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d14_add14_add15_add161(lv626: T.Buffer((T.int64(1), T.int64(96), T.int64(512)), "float32"), wnconv1d68: T.Buffer((T.int64(96), T.int64(96), T.int64(1)), "float32"), lv632: T.Buffer((T.int64(1), T.int64(96), T.int64(1)), "float32"), lv633: T.Buffer((T.int64(1), T.int64(96), T.int64(512)), "float32"), T_add_intermediate_1_2: T.Buffer((T.int64(1), T.int64(96), T.int64(512)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(96), T.int64(512)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(96), T.int64(512)), scope="shared")
        wnconv1d68_shared = T.alloc_buffer((T.int64(96), T.int64(96), T.int64(1)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(96), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(96), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(16) + nn_2_ff_2_yy_2_fused // T.int64(16) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(16) * T.int64(2) + yy_3_init * T.int64(2) + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(1), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(12)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                                with T.block("pad_temp_shared"):
                                    v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                    v1 = T.axis.spatial(T.int64(96), (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1) // T.int64(32))
                                    v2 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1) % T.int64(32))
                                    T.reads(lv626[v0, v1, v2])
                                    T.writes(pad_temp_shared[v0, v1, v2])
                                    pad_temp_shared[v0, v1, v2] = lv626[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(6)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                                with T.block("wnconv1d68_shared"):
                                    v0 = T.axis.spatial(T.int64(96), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1) // T.int64(96))
                                    v1 = T.axis.spatial(T.int64(96), (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1) % T.int64(96))
                                    v2 = T.axis.spatial(T.int64(1), T.int64(0))
                                    T.reads(wnconv1d68[v0, v1, v2])
                                    T.writes(wnconv1d68_shared[v0, v1, v2])
                                    wnconv1d68_shared[v0, v1, v2] = wnconv1d68[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(96), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(96), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(16) + nn_2_ff_2_yy_2_fused // T.int64(16) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(16) * T.int64(2) + yy_3 * T.int64(2) + yy_4)
                                v_rc = T.axis.reduce(T.int64(96), rc_0 * T.int64(96) + rc_1 + rc_2)
                                v_ry = T.axis.reduce(T.int64(1), ry_0 + ry_1 + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d68_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d68_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(2)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(96), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(16) + nn_2_ff_2_yy_2_fused // T.int64(16) + ax1)
                            v2 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(16) * T.int64(2) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv632[v0, v1, T.int64(0)], lv633[v0, v1, v2])
                            T.writes(T_add_intermediate_1_2[v0, v1, v2])
                            T_add_intermediate_1_2[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv632[v0, v1, T.int64(0)] + lv633[v0, v1, v2]

    @T.prim_func(private=True)
    def fused_conv1d15_add141(lv637: T.Buffer((T.int64(1), T.int64(96), T.int64(530)), "float32"), wnconv1d69: T.Buffer((T.int64(96), T.int64(96), T.int64(7)), "float32"), lv643: T.Buffer((T.int64(1), T.int64(96), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(96), T.int64(512)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(96), T.int64(512)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(96), T.int64(530)), scope="shared")
        wnconv1d69_shared = T.alloc_buffer((T.int64(96), T.int64(96), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(48), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 16, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(512), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(2), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(96), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(16) + nn_2_ff_2_yy_2_fused // T.int64(64) * T.int64(2) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(64) + nn_2_ff_2_yy_2_fused % T.int64(64) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(4), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(1)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(512), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(96), rc_0 * T.int64(24) + (ax0_ax1_ax2_fused_0 * T.int64(2048) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(82))
                                        v2 = T.axis.spatial(T.int64(530), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(2048) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(82))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1) * T.int64(4) + ax0_ax1_ax2_fused_2 < T.int64(1968))
                                        T.reads(lv637[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv637[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(2)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(512), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("wnconv1d69_shared"):
                                        v0 = T.axis.spatial(T.int64(96), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(2048) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(168))
                                        v1 = T.axis.spatial(T.int64(96), rc_0 * T.int64(24) + (ax0_ax1_ax2_fused_0 * T.int64(2048) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(168) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(2048) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1) * T.int64(4) + ax0_ax1_ax2_fused_2 < T.int64(2688))
                                        T.reads(wnconv1d69[v0, v1, v2])
                                        T.writes(wnconv1d69_shared[v0, v1, v2])
                                        wnconv1d69_shared[v0, v1, v2] = wnconv1d69[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(24), T.int64(1), T.int64(1), T.int64(2), T.int64(1), T.int64(1), T.int64(7), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(96), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(16) + nn_2_ff_2_yy_2_fused // T.int64(64) * T.int64(2) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(64) + nn_2_ff_2_yy_2_fused % T.int64(64) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(96), rc_0 * T.int64(24) + rc_1 + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 * T.int64(7) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_ry * T.int64(3) + v_yy], wnconv1d69_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_ry * T.int64(3) + v_yy] * wnconv1d69_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(2), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(96), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(16) + nn_2_ff_2_yy_2_fused // T.int64(64) * T.int64(2) + ax1)
                            v2 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(64) + nn_2_ff_2_yy_2_fused % T.int64(64) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv643[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv643[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d16_add141(lv657: T.Buffer((T.int64(1), T.int64(96), T.int64(566)), "float32"), wnconv1d71: T.Buffer((T.int64(96), T.int64(96), T.int64(7)), "float32"), lv663: T.Buffer((T.int64(1), T.int64(96), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(96), T.int64(512)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(96), T.int64(512)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(96), T.int64(566)), scope="shared")
        wnconv1d71_shared = T.alloc_buffer((T.int64(96), T.int64(96), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(96), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(2), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(96), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(64) * T.int64(2) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(64) + nn_2_ff_2_yy_2_fused % T.int64(64) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(4), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(6)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(2)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(96), rc_0 * T.int64(24) + (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) // T.int64(118))
                                        v2 = T.axis.spatial(T.int64(566), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(118))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1) * T.int64(2) + ax0_ax1_ax2_fused_2 < T.int64(2832))
                                        T.reads(lv657[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv657[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(2)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(3)):
                                    with T.block("wnconv1d71_shared"):
                                        v0 = T.axis.spatial(T.int64(96), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(8) + (ax0_ax1_ax2_fused_0 * T.int64(768) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) // T.int64(168))
                                        v1 = T.axis.spatial(T.int64(96), rc_0 * T.int64(24) + (ax0_ax1_ax2_fused_0 * T.int64(768) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) % T.int64(168) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(768) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1) * T.int64(3) + ax0_ax1_ax2_fused_2 < T.int64(1344))
                                        T.reads(wnconv1d71[v0, v1, v2])
                                        T.writes(wnconv1d71_shared[v0, v1, v2])
                                        wnconv1d71_shared[v0, v1, v2] = wnconv1d71[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(12), T.int64(1), T.int64(1), T.int64(2), T.int64(1), T.int64(2), T.int64(7), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(96), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(64) * T.int64(2) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(64) + nn_2_ff_2_yy_2_fused % T.int64(64) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(96), rc_0 * T.int64(24) + rc_1 * T.int64(2) + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 * T.int64(7) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_ry * T.int64(9) + v_yy], wnconv1d71_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_ry * T.int64(9) + v_yy] * wnconv1d71_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(2), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(96), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(64) * T.int64(2) + ax1)
                            v2 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(64) + nn_2_ff_2_yy_2_fused % T.int64(64) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv663[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv663[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d17_reshape10_add17_tir_tanh1(lv676: T.Buffer((T.int64(1), T.int64(96), T.int64(518)), "float32"), wnconv1d73: T.Buffer((T.int64(1), T.int64(96), T.int64(7)), "float32"), decoder_model_layers_6_bias1: T.Buffer((T.int64(1),), "float32"), compute_intermediate: T.Buffer((T.int64(1), T.int64(1), T.int64(512)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate = T.alloc_buffer((T.int64(1), T.int64(1), T.int64(512)))
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(1), T.int64(512)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(96), T.int64(518)), scope="shared")
        wnconv1d73_shared = T.alloc_buffer((T.int64(1), T.int64(96), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(4), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 1024, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(1), ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(128) + nn_2_ff_2_yy_2_fused * T.int64(2) + yy_3_init * T.int64(2) + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(8), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(7)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(96), rc_0 * T.int64(12) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(134))
                                        v2 = T.axis.spatial(T.int64(518), nn_0_ff_0_yy_0_fused * T.int64(128) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(134))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) * T.int64(4) + ax0_ax1_ax2_fused_2 < T.int64(1608))
                                        T.reads(lv676[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv676[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(1)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(3)):
                                    with T.block("wnconv1d73_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(96), rc_0 * T.int64(12) + (ax0_ax1_ax2_fused_0 * T.int64(192) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(192) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) * T.int64(3) + ax0_ax1_ax2_fused_2 < T.int64(84))
                                        T.reads(wnconv1d73[v0, v1, v2])
                                        T.writes(wnconv1d73_shared[v0, v1, v2])
                                        wnconv1d73_shared[v0, v1, v2] = wnconv1d73[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(12), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(7), T.int64(1), T.int64(1), T.int64(2)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(1), ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(128) + nn_2_ff_2_yy_2_fused * T.int64(2) + yy_3 * T.int64(2) + yy_4)
                                v_rc = T.axis.reduce(T.int64(96), rc_0 * T.int64(12) + rc_1 + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 * T.int64(7) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d73_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d73_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(2)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0, v1 = T.axis.remap("SS", [ax0, ax1])
                            v2 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(128) + nn_2_ff_2_yy_2_fused * T.int64(2) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2])
                            T.writes(conv1d_ncw_intermediate[v0, v1, v2])
                            conv1d_ncw_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2]
        for ax0_ax1_ax2_fused_0 in T.thread_binding(T.int64(2), thread="blockIdx.x"):
            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                with T.block("T_add"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax2 = T.axis.spatial(T.int64(512), ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1)
                    T.reads(conv1d_ncw_intermediate[v_ax0, v_ax1, v_ax2], decoder_model_layers_6_bias1[T.int64(0)])
                    T.writes(compute_intermediate[v_ax0, v_ax1, v_ax2])
                    compute_intermediate[v_ax0, v_ax1, v_ax2] = T.tanh(conv1d_ncw_intermediate[v_ax0, v_ax1, v_ax2] + decoder_model_layers_6_bias1[T.int64(0)])

    @T.prim_func(private=True)
    def fused_conv1d18_add181(lv2: T.Buffer((T.int64(1), T.int64(1), T.int64(518)), "float32"), wnconv1d: T.Buffer((T.int64(64), T.int64(1), T.int64(7)), "float32"), lv8: T.Buffer((T.int64(1), T.int64(64), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(64), T.int64(512)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(512)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(1), T.int64(518)), scope="shared")
        wnconv1d_shared = T.alloc_buffer((T.int64(64), T.int64(1), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(16), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(2), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(512), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused // T.int64(2) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(64) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(2) * T.int64(256) + nn_1_ff_1_yy_1_fused * T.int64(128) + nn_2_ff_2_yy_2_fused % T.int64(64) * T.int64(2) + yy_3_init * T.int64(2) + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(1), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(1)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(512), thread="threadIdx.x"):
                                with T.block("pad_temp_shared"):
                                    v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                    v1 = T.axis.spatial(T.int64(1), T.int64(0))
                                    v2 = T.axis.spatial(T.int64(518), nn_0_ff_0_yy_0_fused % T.int64(2) * T.int64(256) + (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1))
                                    T.where(ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1 < T.int64(262))
                                    T.reads(lv2[v0, v1, v2])
                                    T.writes(pad_temp_shared[v0, v1, v2])
                                    pad_temp_shared[v0, v1, v2] = lv2[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(1)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(512), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("wnconv1d_shared"):
                                        v0 = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused // T.int64(2) * T.int64(8) + (ax0_ax1_ax2_fused_0 * T.int64(2048) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(7))
                                        v1 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(2048) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1) * T.int64(4) + ax0_ax1_ax2_fused_2 < T.int64(56))
                                        T.reads(wnconv1d[v0, v1, v2])
                                        T.writes(wnconv1d_shared[v0, v1, v2])
                                        wnconv1d_shared[v0, v1, v2] = wnconv1d[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(1), T.int64(7), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused // T.int64(2) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(64) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(2) * T.int64(256) + nn_1_ff_1_yy_1_fused * T.int64(128) + nn_2_ff_2_yy_2_fused % T.int64(64) * T.int64(2) + yy_3 * T.int64(2) + yy_4)
                                v_rc = T.axis.reduce(T.int64(1), rc_0 + rc_1 + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(2)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused // T.int64(2) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(64) + ax1)
                            v2 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(2) * T.int64(256) + nn_1_ff_1_yy_1_fused * T.int64(128) + nn_2_ff_2_yy_2_fused % T.int64(64) * T.int64(2) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv8[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv8[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d19_add181(lv12: T.Buffer((T.int64(1), T.int64(64), T.int64(518)), "float32"), wnconv1d1: T.Buffer((T.int64(64), T.int64(64), T.int64(7)), "float32"), lv18: T.Buffer((T.int64(1), T.int64(64), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(64), T.int64(512)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(512)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(518)), scope="shared")
        wnconv1d1_shared = T.alloc_buffer((T.int64(64), T.int64(64), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(256), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(2), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(16) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(16) * T.int64(2) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(4), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(10)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                                with T.block("pad_temp_shared"):
                                    v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                    v1 = T.axis.spatial(T.int64(64), rc_0 * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) // T.int64(38))
                                    v2 = T.axis.spatial(T.int64(518), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) % T.int64(38))
                                    T.where(ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1 < T.int64(608))
                                    T.reads(lv12[v0, v1, v2])
                                    T.writes(pad_temp_shared[v0, v1, v2])
                                    pad_temp_shared[v0, v1, v2] = lv12[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(2)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("wnconv1d1_shared"):
                                        v0 = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(4) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(112))
                                        v1 = T.axis.spatial(T.int64(64), rc_0 * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(112) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) * T.int64(4) + ax0_ax1_ax2_fused_2 < T.int64(448))
                                        T.reads(wnconv1d1[v0, v1, v2])
                                        T.writes(wnconv1d1_shared[v0, v1, v2])
                                        wnconv1d1_shared[v0, v1, v2] = wnconv1d1[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(8), T.int64(1), T.int64(1), T.int64(1), T.int64(2), T.int64(2), T.int64(7), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(16) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(16) * T.int64(2) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(64), rc_0 * T.int64(16) + rc_1 * T.int64(2) + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 * T.int64(7) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d1_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d1_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(2)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(16) + ax1)
                            v2 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(16) * T.int64(2) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv18[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv18[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d1_add21(lv419: T.Buffer((T.int64(1), T.int64(768), T.int64(14)), "float32"), wnconv1d49: T.Buffer((T.int64(768), T.int64(768), T.int64(7)), "float32"), lv425: T.Buffer((T.int64(1), T.int64(768), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(768), T.int64(8)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(768), T.int64(8)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(768), T.int64(14)), scope="shared")
        wnconv1d49_shared = T.alloc_buffer((T.int64(768), T.int64(768), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(192), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(768), nn_0_ff_0_yy_0_fused * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(16), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(7)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(3)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(768), rc_0 * T.int64(48) + (ax0_ax1_ax2_fused_0 * T.int64(96) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) // T.int64(14))
                                        v2 = T.axis.spatial(T.int64(14), (ax0_ax1_ax2_fused_0 * T.int64(96) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) % T.int64(14))
                                        T.reads(lv419[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv419[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(21)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(2)):
                                    with T.block("wnconv1d49_shared"):
                                        v0 = T.axis.spatial(T.int64(768), nn_0_ff_0_yy_0_fused * T.int64(4) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) // T.int64(336))
                                        v1 = T.axis.spatial(T.int64(768), rc_0 * T.int64(48) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(336) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.reads(wnconv1d49[v0, v1, v2])
                                        T.writes(wnconv1d49_shared[v0, v1, v2])
                                        wnconv1d49_shared[v0, v1, v2] = wnconv1d49[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(16), T.int64(7), T.int64(1), T.int64(1), T.int64(1), T.int64(3), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(768), nn_0_ff_0_yy_0_fused * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(768), rc_0 * T.int64(48) + rc_1 * T.int64(3) + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d49_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d49_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(768), nn_0_ff_0_yy_0_fused * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(8) + ax1)
                            v2 = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv425[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv425[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d20_add18_add19_add201(lv21: T.Buffer((T.int64(1), T.int64(64), T.int64(512)), "float32"), wnconv1d2: T.Buffer((T.int64(64), T.int64(64), T.int64(1)), "float32"), lv27: T.Buffer((T.int64(1), T.int64(64), T.int64(1)), "float32"), lv28: T.Buffer((T.int64(1), T.int64(64), T.int64(512)), "float32"), T_add_intermediate_1_2: T.Buffer((T.int64(1), T.int64(64), T.int64(512)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(512)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(512)), scope="shared")
        wnconv1d2_shared = T.alloc_buffer((T.int64(64), T.int64(64), T.int64(1)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(64), thread="blockIdx.x"):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(2), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(16) + nn_1_ff_1_yy_1_fused * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(32) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(1), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(8)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                                with T.block("pad_temp_shared"):
                                    v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                    v1 = T.axis.spatial(T.int64(64), (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1) // T.int64(32))
                                    v2 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1) % T.int64(32))
                                    T.reads(lv21[v0, v1, v2])
                                    T.writes(pad_temp_shared[v0, v1, v2])
                                    pad_temp_shared[v0, v1, v2] = lv21[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(2)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(2)):
                                    with T.block("wnconv1d2_shared"):
                                        v0 = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) // T.int64(64))
                                        v1 = T.axis.spatial(T.int64(64), (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(64))
                                        v2 = T.axis.spatial(T.int64(1), T.int64(0))
                                        T.reads(wnconv1d2[v0, v1, v2])
                                        T.writes(wnconv1d2_shared[v0, v1, v2])
                                        wnconv1d2_shared[v0, v1, v2] = wnconv1d2[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(64), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(16) + nn_1_ff_1_yy_1_fused * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(32) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(64), rc_0 * T.int64(64) + rc_1 + rc_2)
                                v_ry = T.axis.reduce(T.int64(1), ry_0 + ry_1 + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d2_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d2_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(16) + nn_1_ff_1_yy_1_fused * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(32) + ax1)
                            v2 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv27[v0, v1, T.int64(0)], lv28[v0, v1, v2])
                            T.writes(T_add_intermediate_1_2[v0, v1, v2])
                            T_add_intermediate_1_2[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv27[v0, v1, T.int64(0)] + lv28[v0, v1, v2]

    @T.prim_func(private=True)
    def fused_conv1d21_add181(lv32: T.Buffer((T.int64(1), T.int64(64), T.int64(530)), "float32"), wnconv1d3: T.Buffer((T.int64(64), T.int64(64), T.int64(7)), "float32"), lv38: T.Buffer((T.int64(1), T.int64(64), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(64), T.int64(512)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(512)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(530)), scope="shared")
        wnconv1d3_shared = T.alloc_buffer((T.int64(64), T.int64(64), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(128), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(2), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(8) + nn_1_ff_1_yy_1_fused * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(32) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(2), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(7)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(2)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(64), rc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) // T.int64(50))
                                        v2 = T.axis.spatial(T.int64(530), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(50))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) * T.int64(2) + ax0_ax1_ax2_fused_2 < T.int64(1600))
                                        T.reads(lv32[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv32[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(7)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(2)):
                                    with T.block("wnconv1d3_shared"):
                                        v0 = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(8) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) // T.int64(224))
                                        v1 = T.axis.spatial(T.int64(64), rc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(224) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.reads(wnconv1d3[v0, v1, v2])
                                        T.writes(wnconv1d3_shared[v0, v1, v2])
                                        wnconv1d3_shared[v0, v1, v2] = wnconv1d3[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(32), T.int64(7), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(8) + nn_1_ff_1_yy_1_fused * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(32) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(64), rc_0 * T.int64(32) + rc_1 + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_ry * T.int64(3) + v_yy], wnconv1d3_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_ry * T.int64(3) + v_yy] * wnconv1d3_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(8) + nn_1_ff_1_yy_1_fused * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(32) + ax1)
                            v2 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv38[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv38[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d22_add181(lv52: T.Buffer((T.int64(1), T.int64(64), T.int64(566)), "float32"), wnconv1d5: T.Buffer((T.int64(64), T.int64(64), T.int64(7)), "float32"), lv58: T.Buffer((T.int64(1), T.int64(64), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(64), T.int64(512)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(512)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(566)), scope="shared")
        wnconv1d5_shared = T.alloc_buffer((T.int64(64), T.int64(64), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(128), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 16, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(2), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(8) + nn_1_ff_1_yy_1_fused * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(32) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(2), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(11)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(2)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(64), rc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) // T.int64(86))
                                        v2 = T.axis.spatial(T.int64(566), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(86))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) * T.int64(2) + ax0_ax1_ax2_fused_2 < T.int64(2752))
                                        T.reads(lv52[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv52[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(7)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(2)):
                                    with T.block("wnconv1d5_shared"):
                                        v0 = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(8) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) // T.int64(224))
                                        v1 = T.axis.spatial(T.int64(64), rc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(224) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.reads(wnconv1d5[v0, v1, v2])
                                        T.writes(wnconv1d5_shared[v0, v1, v2])
                                        wnconv1d5_shared[v0, v1, v2] = wnconv1d5[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(32), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(7), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(8) + nn_1_ff_1_yy_1_fused * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(32) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(64), rc_0 * T.int64(32) + rc_1 + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 * T.int64(7) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_ry * T.int64(9) + v_yy], wnconv1d5_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_ry * T.int64(9) + v_yy] * wnconv1d5_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(8) + nn_1_ff_1_yy_1_fused * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(32) + ax1)
                            v2 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv58[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv58[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d23_add211(lv71: T.Buffer((T.int64(1), T.int64(64), T.int64(514)), "float32"), wnconv1d7: T.Buffer((T.int64(128), T.int64(64), T.int64(4)), "float32"), lv77: T.Buffer((T.int64(1), T.int64(128), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(128), T.int64(256)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(256)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(514)), scope="shared")
        wnconv1d7_shared = T.alloc_buffer((T.int64(128), T.int64(64), T.int64(4)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(128), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 16, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(128), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(32) * T.int64(2) + ff_3_init * T.int64(2) + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(4), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(5)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(2)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(64), rc_0 * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) // T.int64(66))
                                        v2 = T.axis.spatial(T.int64(514), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(66))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) * T.int64(2) + ax0_ax1_ax2_fused_2 < T.int64(1056))
                                        T.reads(lv71[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv71[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(4)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                with T.block("wnconv1d7_shared"):
                                    v0 = T.axis.spatial(T.int64(128), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(8) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) // T.int64(64))
                                    v1 = T.axis.spatial(T.int64(64), rc_0 * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) % T.int64(64) // T.int64(4))
                                    v2 = T.axis.spatial(T.int64(4), (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) % T.int64(4))
                                    T.reads(wnconv1d7[v0, v1, v2])
                                    T.writes(wnconv1d7_shared[v0, v1, v2])
                                    wnconv1d7_shared[v0, v1, v2] = wnconv1d7[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(16), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(4), T.int64(1), T.int64(2), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(128), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(32) * T.int64(2) + ff_3 * T.int64(2) + ff_4)
                                v_yy = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(64), rc_0 * T.int64(16) + rc_1 + rc_2)
                                v_ry = T.axis.reduce(T.int64(4), ry_0 * T.int64(4) + ry_1 * T.int64(4) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy * T.int64(2) + v_ry], wnconv1d7_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy * T.int64(2) + v_ry] * wnconv1d7_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(2), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(128), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(32) * T.int64(2) + ax1)
                            v2 = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv77[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv77[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d24_add211(lv81: T.Buffer((T.int64(1), T.int64(128), T.int64(262)), "float32"), wnconv1d8: T.Buffer((T.int64(128), T.int64(128), T.int64(7)), "float32"), lv87: T.Buffer((T.int64(1), T.int64(128), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(128), T.int64(256)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(256)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(262)), scope="shared")
        wnconv1d8_shared = T.alloc_buffer((T.int64(128), T.int64(128), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(256), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(2), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(128), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(32) * T.int64(2) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(4), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(19)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                                with T.block("pad_temp_shared"):
                                    v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                    v1 = T.axis.spatial(T.int64(128), rc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) // T.int64(38))
                                    v2 = T.axis.spatial(T.int64(262), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) % T.int64(38))
                                    T.reads(lv81[v0, v1, v2])
                                    T.writes(pad_temp_shared[v0, v1, v2])
                                    pad_temp_shared[v0, v1, v2] = lv81[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(7)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(2)):
                                    with T.block("wnconv1d8_shared"):
                                        v0 = T.axis.spatial(T.int64(128), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(4) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) // T.int64(224))
                                        v1 = T.axis.spatial(T.int64(128), rc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(224) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.reads(wnconv1d8[v0, v1, v2])
                                        T.writes(wnconv1d8_shared[v0, v1, v2])
                                        wnconv1d8_shared[v0, v1, v2] = wnconv1d8[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(32), T.int64(7), T.int64(1), T.int64(2), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(128), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(32) * T.int64(2) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(128), rc_0 * T.int64(32) + rc_1 + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d8_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d8_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(2), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(128), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(32) * T.int64(2) + ax1)
                            v2 = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv87[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv87[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d25_add21_add22_add231(lv90: T.Buffer((T.int64(1), T.int64(128), T.int64(256)), "float32"), wnconv1d9: T.Buffer((T.int64(128), T.int64(128), T.int64(1)), "float32"), lv96: T.Buffer((T.int64(1), T.int64(128), T.int64(1)), "float32"), lv97: T.Buffer((T.int64(1), T.int64(128), T.int64(256)), "float32"), T_add_intermediate_1_2: T.Buffer((T.int64(1), T.int64(128), T.int64(256)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(256)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(256)), scope="shared")
        wnconv1d9_shared = T.alloc_buffer((T.int64(128), T.int64(128), T.int64(1)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(128), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(2), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(128), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(16) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(16) + nn_2_ff_2_yy_2_fused % T.int64(8) * T.int64(2) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(1), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(16)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                with T.block("pad_temp_shared"):
                                    v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                    v1 = T.axis.spatial(T.int64(128), (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) // T.int64(16))
                                    v2 = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) % T.int64(16))
                                    T.reads(lv90[v0, v1, v2])
                                    T.writes(pad_temp_shared[v0, v1, v2])
                                    pad_temp_shared[v0, v1, v2] = lv90[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(4)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("wnconv1d9_shared"):
                                        v0 = T.axis.spatial(T.int64(128), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(128))
                                        v1 = T.axis.spatial(T.int64(128), (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(128))
                                        v2 = T.axis.spatial(T.int64(1), T.int64(0))
                                        T.reads(wnconv1d9[v0, v1, v2])
                                        T.writes(wnconv1d9_shared[v0, v1, v2])
                                        wnconv1d9_shared[v0, v1, v2] = wnconv1d9[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(128), T.int64(1), T.int64(1), T.int64(1), T.int64(2), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(128), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(16) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(16) + nn_2_ff_2_yy_2_fused % T.int64(8) * T.int64(2) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(128), rc_0 * T.int64(128) + rc_1 + rc_2)
                                v_ry = T.axis.reduce(T.int64(1), ry_0 + ry_1 + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d9_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d9_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(2)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(128), nn_0_ff_0_yy_0_fused // T.int64(16) * T.int64(16) + nn_2_ff_2_yy_2_fused // T.int64(8) + ax1)
                            v2 = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(16) * T.int64(16) + nn_2_ff_2_yy_2_fused % T.int64(8) * T.int64(2) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv96[v0, v1, T.int64(0)], lv97[v0, v1, v2])
                            T.writes(T_add_intermediate_1_2[v0, v1, v2])
                            T_add_intermediate_1_2[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv96[v0, v1, T.int64(0)] + lv97[v0, v1, v2]

    @T.prim_func(private=True)
    def fused_conv1d26_add211(lv101: T.Buffer((T.int64(1), T.int64(128), T.int64(274)), "float32"), wnconv1d10: T.Buffer((T.int64(128), T.int64(128), T.int64(7)), "float32"), lv107: T.Buffer((T.int64(1), T.int64(128), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(128), T.int64(256)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(256)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(274)), scope="shared")
        wnconv1d10_shared = T.alloc_buffer((T.int64(128), T.int64(128), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(128), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(128), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(32) * T.int64(2) + ff_3_init * T.int64(2) + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(4), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(7)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(2)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(128), rc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) // T.int64(50))
                                        v2 = T.axis.spatial(T.int64(274), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(50))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) * T.int64(2) + ax0_ax1_ax2_fused_2 < T.int64(1600))
                                        T.reads(lv101[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv101[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(7)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(2)):
                                    with T.block("wnconv1d10_shared"):
                                        v0 = T.axis.spatial(T.int64(128), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(8) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) // T.int64(224))
                                        v1 = T.axis.spatial(T.int64(128), rc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(224) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.reads(wnconv1d10[v0, v1, v2])
                                        T.writes(wnconv1d10_shared[v0, v1, v2])
                                        wnconv1d10_shared[v0, v1, v2] = wnconv1d10[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(32), T.int64(7), T.int64(1), T.int64(2), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(128), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(32) * T.int64(2) + ff_3 * T.int64(2) + ff_4)
                                v_yy = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(128), rc_0 * T.int64(32) + rc_1 * T.int64(32) + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 * T.int64(7) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_ry * T.int64(3) + v_yy], wnconv1d10_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_ry * T.int64(3) + v_yy] * wnconv1d10_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(2), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(128), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(32) * T.int64(2) + ax1)
                            v2 = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv107[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv107[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d27_add211(lv121: T.Buffer((T.int64(1), T.int64(128), T.int64(310)), "float32"), wnconv1d12: T.Buffer((T.int64(128), T.int64(128), T.int64(7)), "float32"), lv127: T.Buffer((T.int64(1), T.int64(128), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(128), T.int64(256)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(256)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(310)), scope="shared")
        wnconv1d12_shared = T.alloc_buffer((T.int64(128), T.int64(128), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(128), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(2), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(128), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(32) * T.int64(2) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(4), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(11)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(2)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(128), rc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) // T.int64(86))
                                        v2 = T.axis.spatial(T.int64(310), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(86))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) * T.int64(2) + ax0_ax1_ax2_fused_2 < T.int64(2752))
                                        T.reads(lv121[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv121[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(14)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                with T.block("wnconv1d12_shared"):
                                    v0 = T.axis.spatial(T.int64(128), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(8) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) // T.int64(224))
                                    v1 = T.axis.spatial(T.int64(128), rc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) % T.int64(224) // T.int64(7))
                                    v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) % T.int64(7))
                                    T.reads(wnconv1d12[v0, v1, v2])
                                    T.writes(wnconv1d12_shared[v0, v1, v2])
                                    wnconv1d12_shared[v0, v1, v2] = wnconv1d12[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(16), T.int64(1), T.int64(1), T.int64(2), T.int64(1), T.int64(2), T.int64(7), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(128), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(32) * T.int64(2) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(128), rc_0 * T.int64(32) + rc_1 * T.int64(2) + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 * T.int64(7) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_ry * T.int64(9) + v_yy], wnconv1d12_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_ry * T.int64(9) + v_yy] * wnconv1d12_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(2), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(128), nn_0_ff_0_yy_0_fused // T.int64(8) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(32) * T.int64(2) + ax1)
                            v2 = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(8) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv127[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv127[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d28_add241(lv140: T.Buffer((T.int64(1), T.int64(128), T.int64(260)), "float32"), wnconv1d14: T.Buffer((T.int64(256), T.int64(128), T.int64(8)), "float32"), lv146: T.Buffer((T.int64(1), T.int64(256), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(256), T.int64(64)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(64)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(260)), scope="shared")
        wnconv1d14_shared = T.alloc_buffer((T.int64(256), T.int64(128), T.int64(8)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(128), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(16) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(16) + nn_2_ff_2_yy_2_fused % T.int64(16) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(8), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(9)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                with T.block("pad_temp_shared"):
                                    v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                    v1 = T.axis.spatial(T.int64(128), rc_0 * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) // T.int64(68))
                                    v2 = T.axis.spatial(T.int64(260), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) % T.int64(68))
                                    T.where(ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 < T.int64(1088))
                                    T.reads(lv140[v0, v1, v2])
                                    T.writes(pad_temp_shared[v0, v1, v2])
                                    pad_temp_shared[v0, v1, v2] = lv140[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(8)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                with T.block("wnconv1d14_shared"):
                                    v0 = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(8) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) // T.int64(128))
                                    v1 = T.axis.spatial(T.int64(128), rc_0 * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) % T.int64(128) // T.int64(8))
                                    v2 = T.axis.spatial(T.int64(8), (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) % T.int64(8))
                                    T.reads(wnconv1d14[v0, v1, v2])
                                    T.writes(wnconv1d14_shared[v0, v1, v2])
                                    wnconv1d14_shared[v0, v1, v2] = wnconv1d14[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(8), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2), T.int64(8), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(16) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(16) + nn_2_ff_2_yy_2_fused % T.int64(16) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(128), rc_0 * T.int64(16) + rc_1 * T.int64(2) + rc_2)
                                v_ry = T.axis.reduce(T.int64(8), ry_0 * T.int64(8) + ry_1 * T.int64(8) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy * T.int64(4) + v_ry], wnconv1d14_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy * T.int64(4) + v_ry] * wnconv1d14_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(16) + ax1)
                            v2 = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(16) + nn_2_ff_2_yy_2_fused % T.int64(16) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv146[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv146[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d29_add241(lv150: T.Buffer((T.int64(1), T.int64(256), T.int64(70)), "float32"), wnconv1d15: T.Buffer((T.int64(256), T.int64(256), T.int64(7)), "float32"), lv156: T.Buffer((T.int64(1), T.int64(256), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(256), T.int64(64)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(64)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(70)), scope="shared")
        wnconv1d15_shared = T.alloc_buffer((T.int64(256), T.int64(256), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(512), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(2) + nn_2_ff_2_yy_2_fused // T.int64(16) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(16) + nn_2_ff_2_yy_2_fused % T.int64(16) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(8), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(11)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(2)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(256), rc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) // T.int64(22))
                                        v2 = T.axis.spatial(T.int64(70), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(22))
                                        T.reads(lv150[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv150[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(14)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                                with T.block("wnconv1d15_shared"):
                                    v0 = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(2) + (ax0_ax1_ax2_fused_0 * T.int64(32) + ax0_ax1_ax2_fused_1) // T.int64(224))
                                    v1 = T.axis.spatial(T.int64(256), rc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(32) + ax0_ax1_ax2_fused_1) % T.int64(224) // T.int64(7))
                                    v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(32) + ax0_ax1_ax2_fused_1) % T.int64(7))
                                    T.reads(wnconv1d15[v0, v1, v2])
                                    T.writes(wnconv1d15_shared[v0, v1, v2])
                                    wnconv1d15_shared[v0, v1, v2] = wnconv1d15[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(8), T.int64(7), T.int64(1), T.int64(1), T.int64(1), T.int64(4), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(2) + nn_2_ff_2_yy_2_fused // T.int64(16) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(16) + nn_2_ff_2_yy_2_fused % T.int64(16) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(256), rc_0 * T.int64(32) + rc_1 * T.int64(4) + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d15_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d15_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(2) + nn_2_ff_2_yy_2_fused // T.int64(16) + ax1)
                            v2 = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(16) + nn_2_ff_2_yy_2_fused % T.int64(16) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv156[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv156[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d2_add2_add3_add41(lv428: T.Buffer((T.int64(1), T.int64(768), T.int64(8)), "float32"), wnconv1d50: T.Buffer((T.int64(768), T.int64(768), T.int64(1)), "float32"), lv434: T.Buffer((T.int64(1), T.int64(768), T.int64(1)), "float32"), lv435: T.Buffer((T.int64(1), T.int64(768), T.int64(8)), "float32"), T_add_intermediate_1_2: T.Buffer((T.int64(1), T.int64(768), T.int64(8)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(768), T.int64(8)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(768), T.int64(8)), scope="shared")
        wnconv1d50_shared = T.alloc_buffer((T.int64(768), T.int64(768), T.int64(1)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(96), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(768), nn_0_ff_0_yy_0_fused * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(4), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(6)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(768), rc_0 * T.int64(192) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(8))
                                        v2 = T.axis.spatial(T.int64(8), (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(8))
                                        T.reads(lv428[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv428[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(24)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                                with T.block("wnconv1d50_shared"):
                                    v0 = T.axis.spatial(T.int64(768), nn_0_ff_0_yy_0_fused * T.int64(8) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) // T.int64(192))
                                    v1 = T.axis.spatial(T.int64(768), rc_0 * T.int64(192) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) % T.int64(192))
                                    v2 = T.axis.spatial(T.int64(1), T.int64(0))
                                    T.reads(wnconv1d50[v0, v1, v2])
                                    T.writes(wnconv1d50_shared[v0, v1, v2])
                                    wnconv1d50_shared[v0, v1, v2] = wnconv1d50[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(8), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(24), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(768), nn_0_ff_0_yy_0_fused * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(768), rc_0 * T.int64(192) + rc_1 * T.int64(24) + rc_2)
                                v_ry = T.axis.reduce(T.int64(1), ry_0 + ry_1 + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d50_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d50_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(768), nn_0_ff_0_yy_0_fused * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(8) + ax1)
                            v2 = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv434[v0, v1, T.int64(0)], lv435[v0, v1, v2])
                            T.writes(T_add_intermediate_1_2[v0, v1, v2])
                            T_add_intermediate_1_2[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv434[v0, v1, T.int64(0)] + lv435[v0, v1, v2]

    @T.prim_func(private=True)
    def fused_conv1d30_add24_add25_add261(lv159: T.Buffer((T.int64(1), T.int64(256), T.int64(64)), "float32"), wnconv1d16: T.Buffer((T.int64(256), T.int64(256), T.int64(1)), "float32"), lv165: T.Buffer((T.int64(1), T.int64(256), T.int64(1)), "float32"), lv166: T.Buffer((T.int64(1), T.int64(256), T.int64(64)), "float32"), T_add_intermediate_1_2: T.Buffer((T.int64(1), T.int64(256), T.int64(64)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(64)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(64)), scope="shared")
        wnconv1d16_shared = T.alloc_buffer((T.int64(256), T.int64(256), T.int64(1)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(32), thread="blockIdx.x"):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(32) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(16) + nn_2_ff_2_yy_2_fused % T.int64(8) * T.int64(2) + yy_3_init * T.int64(2) + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(4), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(1)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(256), rc_0 * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(16))
                                        v2 = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(16))
                                        T.reads(lv159[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv159[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(2)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("wnconv1d16_shared"):
                                        v0 = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(64))
                                        v1 = T.axis.spatial(T.int64(256), rc_0 * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(64))
                                        v2 = T.axis.spatial(T.int64(1), T.int64(0))
                                        T.reads(wnconv1d16[v0, v1, v2])
                                        T.writes(wnconv1d16_shared[v0, v1, v2])
                                        wnconv1d16_shared[v0, v1, v2] = wnconv1d16[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(8), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(8), T.int64(1), T.int64(1), T.int64(1), T.int64(2)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(32) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(16) + nn_2_ff_2_yy_2_fused % T.int64(8) * T.int64(2) + yy_3 * T.int64(2) + yy_4)
                                v_rc = T.axis.reduce(T.int64(256), rc_0 * T.int64(64) + rc_1 * T.int64(8) + rc_2)
                                v_ry = T.axis.reduce(T.int64(1), ry_0 + ry_1 + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d16_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d16_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(2)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(32) + nn_2_ff_2_yy_2_fused // T.int64(8) + ax1)
                            v2 = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(16) + nn_2_ff_2_yy_2_fused % T.int64(8) * T.int64(2) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv165[v0, v1, T.int64(0)], lv166[v0, v1, v2])
                            T.writes(T_add_intermediate_1_2[v0, v1, v2])
                            T_add_intermediate_1_2[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv165[v0, v1, T.int64(0)] + lv166[v0, v1, v2]

    @T.prim_func(private=True)
    def fused_conv1d31_add241(lv170: T.Buffer((T.int64(1), T.int64(256), T.int64(82)), "float32"), wnconv1d17: T.Buffer((T.int64(256), T.int64(256), T.int64(7)), "float32"), lv176: T.Buffer((T.int64(1), T.int64(256), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(256), T.int64(64)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(64)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(82)), scope="shared")
        wnconv1d17_shared = T.alloc_buffer((T.int64(256), T.int64(256), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(256), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(16) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(16) + nn_2_ff_2_yy_2_fused % T.int64(16) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(8), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(17)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                                with T.block("pad_temp_shared"):
                                    v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                    v1 = T.axis.spatial(T.int64(256), rc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) // T.int64(34))
                                    v2 = T.axis.spatial(T.int64(82), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) % T.int64(34))
                                    T.reads(lv170[v0, v1, v2])
                                    T.writes(pad_temp_shared[v0, v1, v2])
                                    pad_temp_shared[v0, v1, v2] = lv170[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(14)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                                with T.block("wnconv1d17_shared"):
                                    v0 = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(4) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) // T.int64(224))
                                    v1 = T.axis.spatial(T.int64(256), rc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) % T.int64(224) // T.int64(7))
                                    v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) % T.int64(7))
                                    T.reads(wnconv1d17[v0, v1, v2])
                                    T.writes(wnconv1d17_shared[v0, v1, v2])
                                    wnconv1d17_shared[v0, v1, v2] = wnconv1d17[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(16), T.int64(7), T.int64(1), T.int64(1), T.int64(1), T.int64(2), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(16) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(16) + nn_2_ff_2_yy_2_fused % T.int64(16) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(256), rc_0 * T.int64(32) + rc_1 * T.int64(2) + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_ry * T.int64(3) + v_yy], wnconv1d17_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_ry * T.int64(3) + v_yy] * wnconv1d17_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(16) + ax1)
                            v2 = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(16) + nn_2_ff_2_yy_2_fused % T.int64(16) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv176[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv176[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d32_add241(lv190: T.Buffer((T.int64(1), T.int64(256), T.int64(118)), "float32"), wnconv1d19: T.Buffer((T.int64(256), T.int64(256), T.int64(7)), "float32"), lv196: T.Buffer((T.int64(1), T.int64(256), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(256), T.int64(64)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(64)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(118)), scope="shared")
        wnconv1d19_shared = T.alloc_buffer((T.int64(256), T.int64(256), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(128), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused * T.int64(2) + nn_2_ff_2_yy_2_fused // T.int64(64) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(64), nn_2_ff_2_yy_2_fused % T.int64(64) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(8), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(15)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(2)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(256), rc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) // T.int64(118))
                                        v2 = T.axis.spatial(T.int64(118), (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(118))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) * T.int64(2) + ax0_ax1_ax2_fused_2 < T.int64(3776))
                                        T.reads(lv190[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv190[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(1)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("wnconv1d19_shared"):
                                        v0 = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused * T.int64(2) + (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(224))
                                        v1 = T.axis.spatial(T.int64(256), rc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(224) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) * T.int64(4) + ax0_ax1_ax2_fused_2 < T.int64(448))
                                        T.reads(wnconv1d19[v0, v1, v2])
                                        T.writes(wnconv1d19_shared[v0, v1, v2])
                                        wnconv1d19_shared[v0, v1, v2] = wnconv1d19[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(16), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2), T.int64(7), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused * T.int64(2) + nn_2_ff_2_yy_2_fused // T.int64(64) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(64), nn_2_ff_2_yy_2_fused % T.int64(64) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(256), rc_0 * T.int64(32) + rc_1 * T.int64(2) + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 * T.int64(7) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_ry * T.int64(9) + v_yy], wnconv1d19_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_ry * T.int64(9) + v_yy] * wnconv1d19_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused * T.int64(2) + nn_2_ff_2_yy_2_fused // T.int64(64) + ax1)
                            v2 = T.axis.spatial(T.int64(64), nn_2_ff_2_yy_2_fused % T.int64(64) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv196[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv196[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d33_add271(lv209: T.Buffer((T.int64(1), T.int64(256), T.int64(72)), "float32"), wnconv1d21: T.Buffer((T.int64(512), T.int64(256), T.int64(16)), "float32"), lv215: T.Buffer((T.int64(1), T.int64(512), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(512), T.int64(8)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(8)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(72)), scope="shared")
        wnconv1d21_shared = T.alloc_buffer((T.int64(512), T.int64(256), T.int64(16)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(64), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(16), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(6)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(3)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(256), rc_0 * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(192) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) // T.int64(72))
                                        v2 = T.axis.spatial(T.int64(72), (ax0_ax1_ax2_fused_0 * T.int64(192) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) % T.int64(72))
                                        T.reads(lv209[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv209[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(32)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                                with T.block("wnconv1d21_shared"):
                                    v0 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(8) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) // T.int64(256))
                                    v1 = T.axis.spatial(T.int64(256), rc_0 * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) % T.int64(256) // T.int64(16))
                                    v2 = T.axis.spatial(T.int64(16), (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) % T.int64(16))
                                    T.reads(wnconv1d21[v0, v1, v2])
                                    T.writes(wnconv1d21_shared[v0, v1, v2])
                                    wnconv1d21_shared[v0, v1, v2] = wnconv1d21[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(8), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2), T.int64(16), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(256), rc_0 * T.int64(16) + rc_1 * T.int64(2) + rc_2)
                                v_ry = T.axis.reduce(T.int64(16), ry_0 * T.int64(16) + ry_1 * T.int64(16) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy * T.int64(8) + v_ry], wnconv1d21_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy * T.int64(8) + v_ry] * wnconv1d21_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(8) + ax1)
                            v2 = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv215[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv215[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d34_add271(lv219: T.Buffer((T.int64(1), T.int64(512), T.int64(14)), "float32"), wnconv1d22: T.Buffer((T.int64(512), T.int64(512), T.int64(7)), "float32"), lv225: T.Buffer((T.int64(1), T.int64(512), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(512), T.int64(8)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(8)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(14)), scope="shared")
        wnconv1d22_shared = T.alloc_buffer((T.int64(512), T.int64(512), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(128), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(8), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(7)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(512), rc_0 * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(14))
                                        v2 = T.axis.spatial(T.int64(14), (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(14))
                                        T.reads(lv219[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv219[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(14)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("wnconv1d22_shared"):
                                        v0 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(4) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(448))
                                        v1 = T.axis.spatial(T.int64(512), rc_0 * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(448) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.reads(wnconv1d22[v0, v1, v2])
                                        T.writes(wnconv1d22_shared[v0, v1, v2])
                                        wnconv1d22_shared[v0, v1, v2] = wnconv1d22[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(32), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2), T.int64(7), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(512), rc_0 * T.int64(64) + rc_1 * T.int64(2) + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 * T.int64(7) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d22_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d22_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(8) + ax1)
                            v2 = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv225[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv225[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d35_add27_add28_add291(lv228: T.Buffer((T.int64(1), T.int64(512), T.int64(8)), "float32"), wnconv1d23: T.Buffer((T.int64(512), T.int64(512), T.int64(1)), "float32"), lv234: T.Buffer((T.int64(1), T.int64(512), T.int64(1)), "float32"), lv235: T.Buffer((T.int64(1), T.int64(512), T.int64(8)), "float32"), T_add_intermediate_1_2: T.Buffer((T.int64(1), T.int64(512), T.int64(8)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(8)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(8)), scope="shared")
        wnconv1d23_shared = T.alloc_buffer((T.int64(512), T.int64(512), T.int64(1)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(32), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(16) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(8), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(2)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(2)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(512), rc_0 * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) // T.int64(8))
                                        v2 = T.axis.spatial(T.int64(8), (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(8))
                                        T.reads(lv228[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv228[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(8)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                with T.block("wnconv1d23_shared"):
                                    v0 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) // T.int64(64))
                                    v1 = T.axis.spatial(T.int64(512), rc_0 * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) % T.int64(64))
                                    v2 = T.axis.spatial(T.int64(1), T.int64(0))
                                    T.reads(wnconv1d23[v0, v1, v2])
                                    T.writes(wnconv1d23_shared[v0, v1, v2])
                                    wnconv1d23_shared[v0, v1, v2] = wnconv1d23[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(2), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(32), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(16) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(512), rc_0 * T.int64(64) + rc_1 * T.int64(32) + rc_2)
                                v_ry = T.axis.reduce(T.int64(1), ry_0 + ry_1 + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d23_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d23_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(16) + nn_2_ff_2_yy_2_fused // T.int64(8) + ax1)
                            v2 = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv234[v0, v1, T.int64(0)], lv235[v0, v1, v2])
                            T.writes(T_add_intermediate_1_2[v0, v1, v2])
                            T_add_intermediate_1_2[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv234[v0, v1, T.int64(0)] + lv235[v0, v1, v2]

    @T.prim_func(private=True)
    def fused_conv1d36_add271(lv239: T.Buffer((T.int64(1), T.int64(512), T.int64(26)), "float32"), wnconv1d24: T.Buffer((T.int64(512), T.int64(512), T.int64(7)), "float32"), lv245: T.Buffer((T.int64(1), T.int64(512), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(512), T.int64(8)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(8)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(26)), scope="shared")
        wnconv1d24_shared = T.alloc_buffer((T.int64(512), T.int64(512), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(128), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 16, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(8), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(13)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(512), rc_0 * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(26))
                                        v2 = T.axis.spatial(T.int64(26), (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(26))
                                        T.reads(lv239[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv239[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(14)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("wnconv1d24_shared"):
                                        v0 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(4) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(448))
                                        v1 = T.axis.spatial(T.int64(512), rc_0 * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(448) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.reads(wnconv1d24[v0, v1, v2])
                                        T.writes(wnconv1d24_shared[v0, v1, v2])
                                        wnconv1d24_shared[v0, v1, v2] = wnconv1d24[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(32), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2), T.int64(7), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(512), rc_0 * T.int64(64) + rc_1 * T.int64(2) + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 * T.int64(7) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_ry * T.int64(3) + v_yy], wnconv1d24_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_ry * T.int64(3) + v_yy] * wnconv1d24_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(8) + ax1)
                            v2 = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv245[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv245[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d37_add271(lv259: T.Buffer((T.int64(1), T.int64(512), T.int64(62)), "float32"), wnconv1d26: T.Buffer((T.int64(512), T.int64(512), T.int64(7)), "float32"), lv265: T.Buffer((T.int64(1), T.int64(512), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(512), T.int64(8)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(8)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(62)), scope="shared")
        wnconv1d26_shared = T.alloc_buffer((T.int64(512), T.int64(512), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(64), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(8), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(16)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(512), rc_0 * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(62))
                                        v2 = T.axis.spatial(T.int64(62), (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(62))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) * T.int64(4) + ax0_ax1_ax2_fused_2 < T.int64(3968))
                                        T.reads(lv259[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv259[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(56)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                                with T.block("wnconv1d26_shared"):
                                    v0 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(8) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) // T.int64(448))
                                    v1 = T.axis.spatial(T.int64(512), rc_0 * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) % T.int64(448) // T.int64(7))
                                    v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) % T.int64(7))
                                    T.reads(wnconv1d26[v0, v1, v2])
                                    T.writes(wnconv1d26_shared[v0, v1, v2])
                                    wnconv1d26_shared[v0, v1, v2] = wnconv1d26[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(16), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(4), T.int64(7), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(512), rc_0 * T.int64(64) + rc_1 * T.int64(4) + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 * T.int64(7) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_ry * T.int64(9) + v_yy], wnconv1d26_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_ry * T.int64(9) + v_yy] * wnconv1d26_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(512), nn_0_ff_0_yy_0_fused * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(8) + ax1)
                            v2 = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv265[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv265[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d38_add301(lv278: T.Buffer((T.int64(1), T.int64(512), T.int64(16)), "float32"), wnconv1d28: T.Buffer((T.int64(1024), T.int64(512), T.int64(16)), "float32"), lv284: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(1)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(16)), scope="shared")
        wnconv1d28_shared = T.alloc_buffer((T.int64(1024), T.int64(512), T.int64(16)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(32), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(1024), nn_0_ff_0_yy_0_fused * T.int64(32) + nn_2_ff_2_yy_2_fused + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(1), yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(64), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(4)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                                with T.block("pad_temp_shared"):
                                    v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                    v1 = T.axis.spatial(T.int64(512), rc_0 * T.int64(8) + (ax0_ax1_ax2_fused_0 * T.int64(32) + ax0_ax1_ax2_fused_1) // T.int64(16))
                                    v2 = T.axis.spatial(T.int64(16), (ax0_ax1_ax2_fused_0 * T.int64(32) + ax0_ax1_ax2_fused_1) % T.int64(16))
                                    T.reads(lv278[v0, v1, v2])
                                    T.writes(pad_temp_shared[v0, v1, v2])
                                    pad_temp_shared[v0, v1, v2] = lv278[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(32)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("wnconv1d28_shared"):
                                        v0 = T.axis.spatial(T.int64(1024), nn_0_ff_0_yy_0_fused * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(128))
                                        v1 = T.axis.spatial(T.int64(512), rc_0 * T.int64(8) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(128) // T.int64(16))
                                        v2 = T.axis.spatial(T.int64(16), (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(16))
                                        T.reads(wnconv1d28[v0, v1, v2])
                                        T.writes(wnconv1d28_shared[v0, v1, v2])
                                        wnconv1d28_shared[v0, v1, v2] = wnconv1d28[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(1), T.int64(8), T.int64(1), T.int64(1), T.int64(1), T.int64(8), T.int64(2), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(1024), nn_0_ff_0_yy_0_fused * T.int64(32) + nn_2_ff_2_yy_2_fused + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(1), yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(512), rc_0 * T.int64(8) + rc_1 * T.int64(8) + rc_2)
                                v_ry = T.axis.reduce(T.int64(16), ry_0 * T.int64(16) + ry_1 * T.int64(2) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy * T.int64(8) + v_ry], wnconv1d28_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy * T.int64(8) + v_ry] * wnconv1d28_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(1024), nn_0_ff_0_yy_0_fused * T.int64(32) + nn_2_ff_2_yy_2_fused + ax1)
                            v2 = T.axis.spatial(T.int64(1), ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv284[v0, v1, v2])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv284[v0, v1, v2]

    @T.prim_func(private=True)
    def fused_conv1d39_add301(lv287: T.Buffer((T.int64(1), T.int64(1024), T.int64(3)), "float32"), wnconv1d29: T.Buffer((T.int64(1024), T.int64(1024), T.int64(3)), "float32"), lv293: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(1)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(3)), scope="shared")
        wnconv1d29_shared = T.alloc_buffer((T.int64(1024), T.int64(1024), T.int64(3)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(32), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(1024), nn_0_ff_0_yy_0_fused * T.int64(32) + nn_2_ff_2_yy_2_fused + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(1), yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(16), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(6)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                                with T.block("pad_temp_shared"):
                                    v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                    v1 = T.axis.spatial(T.int64(1024), rc_0 * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(32) + ax0_ax1_ax2_fused_1) // T.int64(3))
                                    v2 = T.axis.spatial(T.int64(3), (ax0_ax1_ax2_fused_0 * T.int64(32) + ax0_ax1_ax2_fused_1) % T.int64(3))
                                    T.reads(lv287[v0, v1, v2])
                                    T.writes(pad_temp_shared[v0, v1, v2])
                                    pad_temp_shared[v0, v1, v2] = lv287[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(48)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("wnconv1d29_shared"):
                                        v0 = T.axis.spatial(T.int64(1024), nn_0_ff_0_yy_0_fused * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(192))
                                        v1 = T.axis.spatial(T.int64(1024), rc_0 * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(192) // T.int64(3))
                                        v2 = T.axis.spatial(T.int64(3), (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(3))
                                        T.reads(wnconv1d29[v0, v1, v2])
                                        T.writes(wnconv1d29_shared[v0, v1, v2])
                                        wnconv1d29_shared[v0, v1, v2] = wnconv1d29[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(32), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2), T.int64(3), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(1024), nn_0_ff_0_yy_0_fused * T.int64(32) + nn_2_ff_2_yy_2_fused + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(1), yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(1024), rc_0 * T.int64(64) + rc_1 * T.int64(2) + rc_2)
                                v_ry = T.axis.reduce(T.int64(3), ry_0 * T.int64(3) + ry_1 * T.int64(3) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d29_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d29_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(1024), nn_0_ff_0_yy_0_fused * T.int64(32) + nn_2_ff_2_yy_2_fused + ax1)
                            v2 = T.axis.spatial(T.int64(1), ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv293[v0, v1, v2])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv293[v0, v1, v2]

    @T.prim_func(private=True)
    def fused_conv1d3_add21(lv439: T.Buffer((T.int64(1), T.int64(768), T.int64(26)), "float32"), wnconv1d51: T.Buffer((T.int64(768), T.int64(768), T.int64(7)), "float32"), lv445: T.Buffer((T.int64(1), T.int64(768), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(768), T.int64(8)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(768), T.int64(8)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(768), T.int64(26)), scope="shared")
        wnconv1d51_shared = T.alloc_buffer((T.int64(768), T.int64(768), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(192), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(768), nn_0_ff_0_yy_0_fused * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(16), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(13)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(3)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(768), rc_0 * T.int64(48) + (ax0_ax1_ax2_fused_0 * T.int64(96) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) // T.int64(26))
                                        v2 = T.axis.spatial(T.int64(26), (ax0_ax1_ax2_fused_0 * T.int64(96) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) % T.int64(26))
                                        T.reads(lv439[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv439[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(14)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(3)):
                                    with T.block("wnconv1d51_shared"):
                                        v0 = T.axis.spatial(T.int64(768), nn_0_ff_0_yy_0_fused * T.int64(4) + (ax0_ax1_ax2_fused_0 * T.int64(96) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) // T.int64(336))
                                        v1 = T.axis.spatial(T.int64(768), rc_0 * T.int64(48) + (ax0_ax1_ax2_fused_0 * T.int64(96) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) % T.int64(336) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(96) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.reads(wnconv1d51[v0, v1, v2])
                                        T.writes(wnconv1d51_shared[v0, v1, v2])
                                        wnconv1d51_shared[v0, v1, v2] = wnconv1d51[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(12), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(4), T.int64(7), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(768), nn_0_ff_0_yy_0_fused * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(768), rc_0 * T.int64(48) + rc_1 * T.int64(4) + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 * T.int64(7) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_ry * T.int64(3) + v_yy], wnconv1d51_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_ry * T.int64(3) + v_yy] * wnconv1d51_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(768), nn_0_ff_0_yy_0_fused * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(8) + ax1)
                            v2 = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv445[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv445[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d40_add311(conv1d29: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32"), wnconv1d30: T.Buffer((T.int64(8), T.int64(1024), T.int64(1)), "float32"), lv299: T.Buffer((T.int64(1), T.int64(8), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(8), T.int64(1)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(8), T.int64(1)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(1)), scope="shared")
        wnconv1d30_shared = T.alloc_buffer((T.int64(8), T.int64(1024), T.int64(1)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(8), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(1), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(8), nn_0_ff_0_yy_0_fused + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(1), yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 1, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(32), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(32)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(1), thread="threadIdx.x"):
                                with T.block("pad_temp_shared"):
                                    v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                    v1 = T.axis.spatial(T.int64(1024), rc_0 * T.int64(32) + ax0_ax1_ax2_fused_0 + ax0_ax1_ax2_fused_1)
                                    v2 = T.axis.spatial(T.int64(1), T.int64(0))
                                    T.reads(conv1d29[v0, v1, v2])
                                    T.writes(pad_temp_shared[v0, v1, v2])
                                    pad_temp_shared[v0, v1, v2] = conv1d29[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(32)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(1), thread="threadIdx.x"):
                                with T.block("wnconv1d30_shared"):
                                    v0 = T.axis.spatial(T.int64(8), nn_0_ff_0_yy_0_fused)
                                    v1 = T.axis.spatial(T.int64(1024), rc_0 * T.int64(32) + ax0_ax1_ax2_fused_0 + ax0_ax1_ax2_fused_1)
                                    v2 = T.axis.spatial(T.int64(1), T.int64(0))
                                    T.reads(wnconv1d30[v0, v1, v2])
                                    T.writes(wnconv1d30_shared[v0, v1, v2])
                                    wnconv1d30_shared[v0, v1, v2] = wnconv1d30[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(8), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(4), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(8), nn_0_ff_0_yy_0_fused + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(1), yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(1024), rc_0 * T.int64(32) + rc_1 * T.int64(4) + rc_2)
                                v_ry = T.axis.reduce(T.int64(1), ry_0 + ry_1 + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d30_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 1, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d30_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(8), nn_0_ff_0_yy_0_fused + ax1)
                            v2 = T.axis.spatial(T.int64(1), ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv299[v0, v1, v2])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv299[v0, v1, v2]

    @T.prim_func(private=True)
    def fused_conv1d41_add301(permute_dims3: T.Buffer((T.int64(1), T.int64(8), T.int64(1)), "float32"), wnconv1d31: T.Buffer((T.int64(1024), T.int64(8), T.int64(1)), "float32"), lv305: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(1)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(8), T.int64(1)), scope="shared")
        wnconv1d31_shared = T.alloc_buffer((T.int64(1024), T.int64(8), T.int64(1)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(2), thread="blockIdx.x"):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(512), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(1024), nn_0_ff_0_yy_0_fused * T.int64(512) + nn_2_ff_2_yy_2_fused + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(1), yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(1), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(1)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(512), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(8), ax0_ax1_ax2_fused_0 * T.int64(2048) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2)
                                        v2 = T.axis.spatial(T.int64(1), T.int64(0))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1) * T.int64(4) + ax0_ax1_ax2_fused_2 < T.int64(8))
                                        T.reads(permute_dims3[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = permute_dims3[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(4)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(512), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(2)):
                                    with T.block("wnconv1d31_shared"):
                                        v0 = T.axis.spatial(T.int64(1024), nn_0_ff_0_yy_0_fused * T.int64(512) + (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) // T.int64(8))
                                        v1 = T.axis.spatial(T.int64(8), (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(8))
                                        v2 = T.axis.spatial(T.int64(1), T.int64(0))
                                        T.reads(wnconv1d31[v0, v1, v2])
                                        T.writes(wnconv1d31_shared[v0, v1, v2])
                                        wnconv1d31_shared[v0, v1, v2] = wnconv1d31[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(2), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(4), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(1024), nn_0_ff_0_yy_0_fused * T.int64(512) + nn_2_ff_2_yy_2_fused + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(1), yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(8), rc_0 * T.int64(8) + rc_1 * T.int64(4) + rc_2)
                                v_ry = T.axis.reduce(T.int64(1), ry_0 + ry_1 + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d31_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d31_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(1024), nn_0_ff_0_yy_0_fused * T.int64(512) + nn_2_ff_2_yy_2_fused + ax1)
                            v2 = T.axis.spatial(T.int64(1), ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv305[v0, v1, v2])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv305[v0, v1, v2]

    @T.prim_func(private=True)
    def fused_conv1d4_add21(lv459: T.Buffer((T.int64(1), T.int64(768), T.int64(62)), "float32"), wnconv1d53: T.Buffer((T.int64(768), T.int64(768), T.int64(7)), "float32"), lv465: T.Buffer((T.int64(1), T.int64(768), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(768), T.int64(8)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(768), T.int64(8)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(768), T.int64(62)), scope="shared")
        wnconv1d53_shared = T.alloc_buffer((T.int64(768), T.int64(768), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(64), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(96), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(768), nn_0_ff_0_yy_0_fused * T.int64(12) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(16), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(31)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(96), thread="threadIdx.x"):
                                with T.block("pad_temp_shared"):
                                    v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                    v1 = T.axis.spatial(T.int64(768), rc_0 * T.int64(48) + (ax0_ax1_ax2_fused_0 * T.int64(96) + ax0_ax1_ax2_fused_1) // T.int64(62))
                                    v2 = T.axis.spatial(T.int64(62), (ax0_ax1_ax2_fused_0 * T.int64(96) + ax0_ax1_ax2_fused_1) % T.int64(62))
                                    T.reads(lv459[v0, v1, v2])
                                    T.writes(pad_temp_shared[v0, v1, v2])
                                    pad_temp_shared[v0, v1, v2] = lv459[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(14)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(96), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(3)):
                                    with T.block("wnconv1d53_shared"):
                                        v0 = T.axis.spatial(T.int64(768), nn_0_ff_0_yy_0_fused * T.int64(12) + (ax0_ax1_ax2_fused_0 * T.int64(288) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) // T.int64(336))
                                        v1 = T.axis.spatial(T.int64(768), rc_0 * T.int64(48) + (ax0_ax1_ax2_fused_0 * T.int64(288) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) % T.int64(336) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(288) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.reads(wnconv1d53[v0, v1, v2])
                                        T.writes(wnconv1d53_shared[v0, v1, v2])
                                        wnconv1d53_shared[v0, v1, v2] = wnconv1d53[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(12), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(4), T.int64(7), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(768), nn_0_ff_0_yy_0_fused * T.int64(12) + nn_2_ff_2_yy_2_fused // T.int64(8) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(768), rc_0 * T.int64(48) + rc_1 * T.int64(4) + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 * T.int64(7) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_ry * T.int64(9) + v_yy], wnconv1d53_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_ry * T.int64(9) + v_yy] * wnconv1d53_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(768), nn_0_ff_0_yy_0_fused * T.int64(12) + nn_2_ff_2_yy_2_fused // T.int64(8) + ax1)
                            v2 = T.axis.spatial(T.int64(8), nn_2_ff_2_yy_2_fused % T.int64(8) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv465[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv465[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d5_add61(lv485: T.Buffer((T.int64(1), T.int64(384), T.int64(70)), "float32"), wnconv1d55: T.Buffer((T.int64(384), T.int64(384), T.int64(7)), "float32"), lv491: T.Buffer((T.int64(1), T.int64(384), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(384), T.int64(64)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(384), T.int64(64)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(384), T.int64(70)), scope="shared")
        wnconv1d55_shared = T.alloc_buffer((T.int64(384), T.int64(384), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(96), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 512, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(384), nn_0_ff_0_yy_0_fused // T.int64(2) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(16) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(2) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(16) * T.int64(2) + yy_3_init * T.int64(2) + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(8), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(5)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(3)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(384), rc_0 * T.int64(48) + (ax0_ax1_ax2_fused_0 * T.int64(384) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) // T.int64(38))
                                        v2 = T.axis.spatial(T.int64(70), nn_0_ff_0_yy_0_fused % T.int64(2) * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(384) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) % T.int64(38))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) * T.int64(3) + ax0_ax1_ax2_fused_2 < T.int64(1824))
                                        T.reads(lv485[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv485[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(7)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(3)):
                                    with T.block("wnconv1d55_shared"):
                                        v0 = T.axis.spatial(T.int64(384), nn_0_ff_0_yy_0_fused // T.int64(2) * T.int64(8) + (ax0_ax1_ax2_fused_0 * T.int64(384) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) // T.int64(336))
                                        v1 = T.axis.spatial(T.int64(384), rc_0 * T.int64(48) + (ax0_ax1_ax2_fused_0 * T.int64(384) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) % T.int64(336) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(384) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.reads(wnconv1d55[v0, v1, v2])
                                        T.writes(wnconv1d55_shared[v0, v1, v2])
                                        wnconv1d55_shared[v0, v1, v2] = wnconv1d55[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(24), T.int64(7), T.int64(1), T.int64(1), T.int64(1), T.int64(2), T.int64(1), T.int64(1), T.int64(1), T.int64(2)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(384), nn_0_ff_0_yy_0_fused // T.int64(2) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(16) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(2) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(16) * T.int64(2) + yy_3 * T.int64(2) + yy_4)
                                v_rc = T.axis.reduce(T.int64(384), rc_0 * T.int64(48) + rc_1 * T.int64(2) + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d55_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d55_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(2)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(384), nn_0_ff_0_yy_0_fused // T.int64(2) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(16) + ax1)
                            v2 = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(2) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(16) * T.int64(2) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv491[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv491[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d6_add6_add7_add81(lv494: T.Buffer((T.int64(1), T.int64(384), T.int64(64)), "float32"), wnconv1d56: T.Buffer((T.int64(384), T.int64(384), T.int64(1)), "float32"), lv500: T.Buffer((T.int64(1), T.int64(384), T.int64(1)), "float32"), lv501: T.Buffer((T.int64(1), T.int64(384), T.int64(64)), "float32"), T_add_intermediate_1_2: T.Buffer((T.int64(1), T.int64(384), T.int64(64)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(384), T.int64(64)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(384), T.int64(64)), scope="shared")
        wnconv1d56_shared = T.alloc_buffer((T.int64(384), T.int64(384), T.int64(1)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(192), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(2), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(384), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(8) + nn_1_ff_1_yy_1_fused * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(16) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(16) + nn_2_ff_2_yy_2_fused % T.int64(16) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(6), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(8)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(2)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(384), rc_0 * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) // T.int64(16))
                                        v2 = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(16) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(16))
                                        T.reads(lv494[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv494[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(8)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(64), thread="threadIdx.x"):
                                with T.block("wnconv1d56_shared"):
                                    v0 = T.axis.spatial(T.int64(384), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(8) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) // T.int64(64))
                                    v1 = T.axis.spatial(T.int64(384), rc_0 * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(64) + ax0_ax1_ax2_fused_1) % T.int64(64))
                                    v2 = T.axis.spatial(T.int64(1), T.int64(0))
                                    T.reads(wnconv1d56[v0, v1, v2])
                                    T.writes(wnconv1d56_shared[v0, v1, v2])
                                    wnconv1d56_shared[v0, v1, v2] = wnconv1d56[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(8), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(8), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(384), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(8) + nn_1_ff_1_yy_1_fused * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(16) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(16) + nn_2_ff_2_yy_2_fused % T.int64(16) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(384), rc_0 * T.int64(64) + rc_1 * T.int64(8) + rc_2)
                                v_ry = T.axis.reduce(T.int64(1), ry_0 + ry_1 + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d56_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d56_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(384), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(8) + nn_1_ff_1_yy_1_fused * T.int64(4) + nn_2_ff_2_yy_2_fused // T.int64(16) + ax1)
                            v2 = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(16) + nn_2_ff_2_yy_2_fused % T.int64(16) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv500[v0, v1, T.int64(0)], lv501[v0, v1, v2])
                            T.writes(T_add_intermediate_1_2[v0, v1, v2])
                            T_add_intermediate_1_2[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv500[v0, v1, T.int64(0)] + lv501[v0, v1, v2]

    @T.prim_func(private=True)
    def fused_conv1d7_add61(lv505: T.Buffer((T.int64(1), T.int64(384), T.int64(82)), "float32"), wnconv1d57: T.Buffer((T.int64(384), T.int64(384), T.int64(7)), "float32"), lv511: T.Buffer((T.int64(1), T.int64(384), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(384), T.int64(64)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(384), T.int64(64)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(384), T.int64(82)), scope="shared")
        wnconv1d57_shared = T.alloc_buffer((T.int64(384), T.int64(384), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(96), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 64, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(384), nn_0_ff_0_yy_0_fused // T.int64(2) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(16) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(2) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(16) * T.int64(2) + yy_3_init * T.int64(2) + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(6), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(25)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                with T.block("pad_temp_shared"):
                                    v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                    v1 = T.axis.spatial(T.int64(384), rc_0 * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) // T.int64(50))
                                    v2 = T.axis.spatial(T.int64(82), nn_0_ff_0_yy_0_fused % T.int64(2) * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) % T.int64(50))
                                    T.reads(lv505[v0, v1, v2])
                                    T.writes(pad_temp_shared[v0, v1, v2])
                                    pad_temp_shared[v0, v1, v2] = lv505[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(7)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("wnconv1d57_shared"):
                                        v0 = T.axis.spatial(T.int64(384), nn_0_ff_0_yy_0_fused // T.int64(2) * T.int64(8) + (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(448))
                                        v1 = T.axis.spatial(T.int64(384), rc_0 * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(448) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.reads(wnconv1d57[v0, v1, v2])
                                        T.writes(wnconv1d57_shared[v0, v1, v2])
                                        wnconv1d57_shared[v0, v1, v2] = wnconv1d57[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(32), T.int64(7), T.int64(1), T.int64(1), T.int64(1), T.int64(2), T.int64(1), T.int64(1), T.int64(1), T.int64(2)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(384), nn_0_ff_0_yy_0_fused // T.int64(2) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(16) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(2) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(16) * T.int64(2) + yy_3 * T.int64(2) + yy_4)
                                v_rc = T.axis.reduce(T.int64(384), rc_0 * T.int64(64) + rc_1 * T.int64(2) + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_ry * T.int64(3) + v_yy], wnconv1d57_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_ry * T.int64(3) + v_yy] * wnconv1d57_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(2)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(384), nn_0_ff_0_yy_0_fused // T.int64(2) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(16) + ax1)
                            v2 = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(2) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(16) * T.int64(2) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv511[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv511[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d8_add61(lv525: T.Buffer((T.int64(1), T.int64(384), T.int64(118)), "float32"), wnconv1d59: T.Buffer((T.int64(384), T.int64(384), T.int64(7)), "float32"), lv531: T.Buffer((T.int64(1), T.int64(384), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(384), T.int64(64)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(384), T.int64(64)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(384), T.int64(118)), scope="shared")
        wnconv1d59_shared = T.alloc_buffer((T.int64(384), T.int64(384), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(96), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 512, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(384), nn_0_ff_0_yy_0_fused // T.int64(2) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(32) * T.int64(2) + ff_3_init * T.int64(2) + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(2) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(8), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(17)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(2)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(384), rc_0 * T.int64(48) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) // T.int64(86))
                                        v2 = T.axis.spatial(T.int64(118), nn_0_ff_0_yy_0_fused % T.int64(2) * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(86))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1) * T.int64(2) + ax0_ax1_ax2_fused_2 < T.int64(4128))
                                        T.reads(lv525[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv525[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(7)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(3)):
                                    with T.block("wnconv1d59_shared"):
                                        v0 = T.axis.spatial(T.int64(384), nn_0_ff_0_yy_0_fused // T.int64(2) * T.int64(8) + (ax0_ax1_ax2_fused_0 * T.int64(384) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) // T.int64(336))
                                        v1 = T.axis.spatial(T.int64(384), rc_0 * T.int64(48) + (ax0_ax1_ax2_fused_0 * T.int64(384) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) % T.int64(336) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(384) + ax0_ax1_ax2_fused_1 * T.int64(3) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.reads(wnconv1d59[v0, v1, v2])
                                        T.writes(wnconv1d59_shared[v0, v1, v2])
                                        wnconv1d59_shared[v0, v1, v2] = wnconv1d59[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(24), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2), T.int64(7), T.int64(1), T.int64(2), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(384), nn_0_ff_0_yy_0_fused // T.int64(2) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(32) * T.int64(2) + ff_3 * T.int64(2) + ff_4)
                                v_yy = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(2) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(384), rc_0 * T.int64(48) + rc_1 * T.int64(2) + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 * T.int64(7) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_ry * T.int64(9) + v_yy], wnconv1d59_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_ry * T.int64(9) + v_yy] * wnconv1d59_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(2), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(384), nn_0_ff_0_yy_0_fused // T.int64(2) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(32) * T.int64(2) + ax1)
                            v2 = T.axis.spatial(T.int64(64), nn_0_ff_0_yy_0_fused % T.int64(2) * T.int64(32) + nn_2_ff_2_yy_2_fused % T.int64(32) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv531[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv531[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d9_add101(lv551: T.Buffer((T.int64(1), T.int64(192), T.int64(262)), "float32"), wnconv1d61: T.Buffer((T.int64(192), T.int64(192), T.int64(7)), "float32"), lv557: T.Buffer((T.int64(1), T.int64(192), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(192), T.int64(256)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(192), T.int64(256)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(192), T.int64(262)), scope="shared")
        wnconv1d61_shared = T.alloc_buffer((T.int64(192), T.int64(192), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(96), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 16, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(2), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(192), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(64) * T.int64(2) + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(64) + nn_2_ff_2_yy_2_fused % T.int64(64) + yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(6), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(5)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(2)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(192), rc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) // T.int64(70))
                                        v2 = T.axis.spatial(T.int64(262), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(64) + (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1 * T.int64(2) + ax0_ax1_ax2_fused_2) % T.int64(70))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1) * T.int64(2) + ax0_ax1_ax2_fused_2 < T.int64(2240))
                                        T.reads(lv551[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv551[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(2)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("wnconv1d61_shared"):
                                        v0 = T.axis.spatial(T.int64(192), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(8) + (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(224))
                                        v1 = T.axis.spatial(T.int64(192), rc_0 * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(224) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(256) + ax0_ax1_ax2_fused_1) * T.int64(4) + ax0_ax1_ax2_fused_2 < T.int64(1792))
                                        T.reads(wnconv1d61[v0, v1, v2])
                                        T.writes(wnconv1d61_shared[v0, v1, v2])
                                        wnconv1d61_shared[v0, v1, v2] = wnconv1d61[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(16), T.int64(1), T.int64(1), T.int64(2), T.int64(1), T.int64(2), T.int64(7), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(192), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(64) * T.int64(2) + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(64) + nn_2_ff_2_yy_2_fused % T.int64(64) + yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(192), rc_0 * T.int64(32) + rc_1 * T.int64(2) + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 * T.int64(7) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d61_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d61_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(2), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(192), nn_0_ff_0_yy_0_fused // T.int64(4) * T.int64(8) + nn_2_ff_2_yy_2_fused // T.int64(64) * T.int64(2) + ax1)
                            v2 = T.axis.spatial(T.int64(256), nn_0_ff_0_yy_0_fused % T.int64(4) * T.int64(64) + nn_2_ff_2_yy_2_fused % T.int64(64) + ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv557[v0, v1, T.int64(0)])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv557[v0, v1, T.int64(0)]

    @T.prim_func(private=True)
    def fused_conv1d_add1(lv403: T.Buffer((T.int64(1), T.int64(1024), T.int64(7)), "float32"), wnconv1d48: T.Buffer((T.int64(1536), T.int64(1024), T.int64(7)), "float32"), lv409: T.Buffer((T.int64(1), T.int64(1536), T.int64(1)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(1536), T.int64(1)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        conv1d_ncw_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(1536), T.int64(1)), scope="local")
        pad_temp_shared = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(7)), scope="shared")
        wnconv1d48_shared = T.alloc_buffer((T.int64(1536), T.int64(1024), T.int64(7)), scope="shared")
        for nn_0_ff_0_yy_0_fused in T.thread_binding(T.int64(48), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 16, "pragma_unroll_explicit": 1}):
            for nn_1_ff_1_yy_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for nn_2_ff_2_yy_2_fused in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                    for nn_3_init, ff_3_init, yy_3_init, nn_4_init, ff_4_init, yy_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_init"):
                            v_nn = T.axis.spatial(T.int64(1), nn_3_init + nn_4_init)
                            v_ff = T.axis.spatial(T.int64(1536), nn_0_ff_0_yy_0_fused * T.int64(32) + nn_2_ff_2_yy_2_fused + ff_3_init + ff_4_init)
                            v_yy = T.axis.spatial(T.int64(1), yy_3_init + yy_4_init)
                            T.reads()
                            T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = T.float32(0.0)
                    for rc_0, ry_0 in T.grid(T.int64(128), T.int64(1)):
                        for ax0_ax1_ax2_fused_0 in range(T.int64(1)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("pad_temp_shared"):
                                        v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                        v1 = T.axis.spatial(T.int64(1024), rc_0 * T.int64(8) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.where((ax0_ax1_ax2_fused_0 * T.int64(32) + ax0_ax1_ax2_fused_1) * T.int64(4) + ax0_ax1_ax2_fused_2 < T.int64(56))
                                        T.reads(lv403[v0, v1, v2])
                                        T.writes(pad_temp_shared[v0, v1, v2])
                                        pad_temp_shared[v0, v1, v2] = lv403[v0, v1, v2]
                        for ax0_ax1_ax2_fused_0 in range(T.int64(14)):
                            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(32), thread="threadIdx.x"):
                                for ax0_ax1_ax2_fused_2 in T.vectorized(T.int64(4)):
                                    with T.block("wnconv1d48_shared"):
                                        v0 = T.axis.spatial(T.int64(1536), nn_0_ff_0_yy_0_fused * T.int64(32) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) // T.int64(56))
                                        v1 = T.axis.spatial(T.int64(1024), rc_0 * T.int64(8) + (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(56) // T.int64(7))
                                        v2 = T.axis.spatial(T.int64(7), (ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1 * T.int64(4) + ax0_ax1_ax2_fused_2) % T.int64(7))
                                        T.reads(wnconv1d48[v0, v1, v2])
                                        T.writes(wnconv1d48_shared[v0, v1, v2])
                                        wnconv1d48_shared[v0, v1, v2] = wnconv1d48[v0, v1, v2]
                        for rc_1, ry_1, nn_3, ff_3, yy_3, rc_2, ry_2, nn_4, ff_4, yy_4 in T.grid(T.int64(4), T.int64(1), T.int64(1), T.int64(1), T.int64(1), T.int64(2), T.int64(7), T.int64(1), T.int64(1), T.int64(1)):
                            with T.block("conv1d_ncw_update"):
                                v_nn = T.axis.spatial(T.int64(1), nn_3 + nn_4)
                                v_ff = T.axis.spatial(T.int64(1536), nn_0_ff_0_yy_0_fused * T.int64(32) + nn_2_ff_2_yy_2_fused + ff_3 + ff_4)
                                v_yy = T.axis.spatial(T.int64(1), yy_3 + yy_4)
                                v_rc = T.axis.reduce(T.int64(1024), rc_0 * T.int64(8) + rc_1 * T.int64(2) + rc_2)
                                v_ry = T.axis.reduce(T.int64(7), ry_0 * T.int64(7) + ry_1 * T.int64(7) + ry_2)
                                T.reads(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy], pad_temp_shared[v_nn, v_rc, v_yy + v_ry], wnconv1d48_shared[v_ff, v_rc, v_ry])
                                T.writes(conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] = conv1d_ncw_intermediate_local[v_nn, v_ff, v_yy] + pad_temp_shared[v_nn, v_rc, v_yy + v_ry] * wnconv1d48_shared[v_ff, v_rc, v_ry]
                    for ax0, ax1, ax2 in T.grid(T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("conv1d_ncw_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(1536), nn_0_ff_0_yy_0_fused * T.int64(32) + nn_2_ff_2_yy_2_fused + ax1)
                            v2 = T.axis.spatial(T.int64(1), ax2)
                            T.reads(conv1d_ncw_intermediate_local[v0, v1, v2], lv409[v0, v1, v2])
                            T.writes(T_add_intermediate[v0, v1, v2])
                            T_add_intermediate[v0, v1, v2] = conv1d_ncw_intermediate_local[v0, v1, v2] + lv409[v0, v1, v2]

    @T.prim_func(private=True)
    def fused_expand_dims1_add51(decoder_model_layers_2_block_layers_1_bias1: T.Buffer((T.int64(384),), "float32"), lv481: T.Buffer((T.int64(1), T.int64(384), T.int64(64)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(384), T.int64(64)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_ax2_fused_0 in T.thread_binding(T.int64(48), thread="blockIdx.x"):
            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(512), thread="threadIdx.x"):
                with T.block("T_add"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(384), (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1) // T.int64(64))
                    v_ax2 = T.axis.spatial(T.int64(64), (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1) % T.int64(64))
                    T.reads(lv481[v_ax0, v_ax1, v_ax2], decoder_model_layers_2_block_layers_1_bias1[v_ax1])
                    T.writes(T_add_intermediate[v_ax0, v_ax1, v_ax2])
                    T_add_intermediate[v_ax0, v_ax1, v_ax2] = lv481[v_ax0, v_ax1, v_ax2] + decoder_model_layers_2_block_layers_1_bias1[v_ax1]

    @T.prim_func(private=True)
    def fused_expand_dims2_add91(decoder_model_layers_3_block_layers_1_bias1: T.Buffer((T.int64(192),), "float32"), lv547: T.Buffer((T.int64(1), T.int64(192), T.int64(256)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(192), T.int64(256)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_ax2_fused_0 in T.thread_binding(T.int64(48), thread="blockIdx.x"):
            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(1024), thread="threadIdx.x"):
                with T.block("T_add"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(192), (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1) // T.int64(256))
                    v_ax2 = T.axis.spatial(T.int64(256), (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1) % T.int64(256))
                    T.reads(lv547[v_ax0, v_ax1, v_ax2], decoder_model_layers_3_block_layers_1_bias1[v_ax1])
                    T.writes(T_add_intermediate[v_ax0, v_ax1, v_ax2])
                    T_add_intermediate[v_ax0, v_ax1, v_ax2] = lv547[v_ax0, v_ax1, v_ax2] + decoder_model_layers_3_block_layers_1_bias1[v_ax1]

    @T.prim_func(private=True)
    def fused_expand_dims3_add131(decoder_model_layers_4_block_layers_1_bias1: T.Buffer((T.int64(96),), "float32"), lv613: T.Buffer((T.int64(1), T.int64(96), T.int64(512)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(96), T.int64(512)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_ax2_fused_0 in T.thread_binding(T.int64(48), thread="blockIdx.x"):
            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(1024), thread="threadIdx.x"):
                with T.block("T_add"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(96), (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1) // T.int64(512))
                    v_ax2 = T.axis.spatial(T.int64(512), (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1) % T.int64(512))
                    T.reads(lv613[v_ax0, v_ax1, v_ax2], decoder_model_layers_4_block_layers_1_bias1[v_ax1])
                    T.writes(T_add_intermediate[v_ax0, v_ax1, v_ax2])
                    T_add_intermediate[v_ax0, v_ax1, v_ax2] = lv613[v_ax0, v_ax1, v_ax2] + decoder_model_layers_4_block_layers_1_bias1[v_ax1]

    @T.prim_func(private=True)
    def fused_expand_dims_add11(decoder_model_layers_1_block_layers_1_bias1: T.Buffer((T.int64(768),), "float32"), lv415: T.Buffer((T.int64(1), T.int64(768), T.int64(8)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(768), T.int64(8)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_ax2_fused_0 in T.thread_binding(T.int64(12), thread="blockIdx.x"):
            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(512), thread="threadIdx.x"):
                with T.block("T_add"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(768), (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1) // T.int64(8))
                    v_ax2 = T.axis.spatial(T.int64(8), (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1) % T.int64(8))
                    T.reads(lv415[v_ax0, v_ax1, v_ax2], decoder_model_layers_1_block_layers_1_bias1[v_ax1])
                    T.writes(T_add_intermediate[v_ax0, v_ax1, v_ax2])
                    T_add_intermediate[v_ax0, v_ax1, v_ax2] = lv415[v_ax0, v_ax1, v_ax2] + decoder_model_layers_1_block_layers_1_bias1[v_ax1]

    @T.prim_func(private=True)
    def fused_matmul_multiply29_subtract_add321(divide: T.Buffer((T.int64(1), T.int64(8)), "float32"), permute_dims1: T.Buffer((T.int64(8), T.int64(1024)), "float32"), sum2: T.Buffer((T.int64(1), T.int64(1)), "float32"), permute_dims2: T.Buffer((T.int64(1), T.int64(1024)), "float32"), T_add_intermediate: T.Buffer((T.int64(1), T.int64(1024)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        matmul_intermediate_local = T.alloc_buffer((T.int64(1), T.int64(1024)), scope="local")
        divide_shared = T.alloc_buffer((T.int64(1), T.int64(8)), scope="shared")
        permute_dims1_shared = T.alloc_buffer((T.int64(8), T.int64(1024)), scope="shared")
        for i0_0_i1_0_fused in T.thread_binding(T.int64(4), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 512, "pragma_unroll_explicit": 1}):
            for i0_1_i1_1_fused in T.thread_binding(T.int64(1), thread="vthread.x"):
                for i0_2_i1_2_fused in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                    for i0_3_init, i1_3_init, i0_4_init, i1_4_init in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(1)):
                        with T.block("matmul_init"):
                            v_i0 = T.axis.spatial(T.int64(1), i0_3_init + i0_4_init)
                            v_i1 = T.axis.spatial(T.int64(1024), i0_0_i1_0_fused * T.int64(256) + i0_2_i1_2_fused + i1_3_init + i1_4_init)
                            T.reads()
                            T.writes(matmul_intermediate_local[v_i0, v_i1])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                            matmul_intermediate_local[v_i0, v_i1] = T.float32(0.0)
                    for k_0 in range(T.int64(1)):
                        for ax0_ax1_fused_0 in range(T.int64(1)):
                            for ax0_ax1_fused_1 in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                                with T.block("divide_shared"):
                                    v0 = T.axis.spatial(T.int64(1), T.int64(0))
                                    v1 = T.axis.spatial(T.int64(8), ax0_ax1_fused_0 * T.int64(256) + ax0_ax1_fused_1)
                                    T.where(ax0_ax1_fused_0 * T.int64(256) + ax0_ax1_fused_1 < T.int64(8))
                                    T.reads(divide[v0, v1])
                                    T.writes(divide_shared[v0, v1])
                                    divide_shared[v0, v1] = divide[v0, v1]
                        for ax0_ax1_fused_0 in range(T.int64(8)):
                            for ax0_ax1_fused_1 in T.thread_binding(T.int64(256), thread="threadIdx.x"):
                                with T.block("permute_dims1_shared"):
                                    v0 = T.axis.spatial(T.int64(8), (ax0_ax1_fused_0 * T.int64(256) + ax0_ax1_fused_1) // T.int64(256))
                                    v1 = T.axis.spatial(T.int64(1024), i0_0_i1_0_fused * T.int64(256) + (ax0_ax1_fused_0 * T.int64(256) + ax0_ax1_fused_1) % T.int64(256))
                                    T.reads(permute_dims1[v0, v1])
                                    T.writes(permute_dims1_shared[v0, v1])
                                    permute_dims1_shared[v0, v1] = permute_dims1[v0, v1]
                        for k_1, i0_3, i1_3, k_2, i0_4, i1_4 in T.grid(T.int64(1), T.int64(1), T.int64(1), T.int64(8), T.int64(1), T.int64(1)):
                            with T.block("matmul_update"):
                                v_i0 = T.axis.spatial(T.int64(1), i0_3 + i0_4)
                                v_i1 = T.axis.spatial(T.int64(1024), i0_0_i1_0_fused * T.int64(256) + i0_2_i1_2_fused + i1_3 + i1_4)
                                v_k = T.axis.reduce(T.int64(8), k_0 * T.int64(8) + k_1 * T.int64(8) + k_2)
                                T.reads(matmul_intermediate_local[v_i0, v_i1], divide_shared[v_i0, v_k], permute_dims1_shared[v_k, v_i1])
                                T.writes(matmul_intermediate_local[v_i0, v_i1])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "meta_schedule.tiling_structure": "SSSRRSRS"})
                                matmul_intermediate_local[v_i0, v_i1] = matmul_intermediate_local[v_i0, v_i1] + divide_shared[v_i0, v_k] * permute_dims1_shared[v_k, v_i1]
                    for ax0, ax1 in T.grid(T.int64(1), T.int64(1)):
                        with T.block("matmul_intermediate_local"):
                            v0 = T.axis.spatial(T.int64(1), ax0)
                            v1 = T.axis.spatial(T.int64(1024), i0_0_i1_0_fused * T.int64(256) + i0_2_i1_2_fused + ax1)
                            T.reads(sum2[v0, T.int64(0)], matmul_intermediate_local[v0, v1], permute_dims2[v0, v1])
                            T.writes(T_add_intermediate[v0, v1])
                            T_add_intermediate[v0, v1] = sum2[v0, T.int64(0)] - matmul_intermediate_local[v0, v1] * T.float32(2.0) + permute_dims2[v0, v1]

    @T.prim_func(private=True)
    def fused_reshape12_snake_reshape121(lv9: T.Buffer((T.int64(1), T.int64(64), T.int64(512)), "float32"), encoder_block_layers_1_block_layers_0_block_branches_0_layers_0_alpha: T.Buffer((T.int64(1), T.int64(64), T.int64(1)), "float32"), T_reshape_intermediate_1: T.Buffer((T.int64(1), T.int64(64), T.int64(512)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_ax2_fused_0 in T.thread_binding(T.int64(32), thread="blockIdx.x"):
            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(1024), thread="threadIdx.x"):
                with T.block("T_reshape"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(64), (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1) // T.int64(512))
                    v_ax2 = T.axis.spatial(T.int64(512), (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1) % T.int64(512))
                    T.reads(lv9[T.int64(0), (v_ax2 // T.int64(512) + v_ax1) % T.int64(64), v_ax2 % T.int64(512)], encoder_block_layers_1_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_ax1, T.int64(0)])
                    T.writes(T_reshape_intermediate_1[T.int64(0), v_ax1, v_ax2])
                    T_reshape_intermediate_1[T.int64(0), v_ax1, v_ax2] = lv9[T.int64(0), (v_ax2 // T.int64(512) + v_ax1) % T.int64(64), v_ax2 % T.int64(512)] + T.float32(1.0) / (encoder_block_layers_1_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_ax1, T.int64(0)] + T.float32(1.0000000000000001e-09)) * T.pow(T.sin(encoder_block_layers_1_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_ax1, T.int64(0)] * lv9[T.int64(0), (v_ax2 // T.int64(512) + v_ax1) % T.int64(64), v_ax2 % T.int64(512)]), T.float32(2.0))

    @T.prim_func(private=True)
    def fused_reshape14_snake1_reshape141(lv78: T.Buffer((T.int64(1), T.int64(128), T.int64(256)), "float32"), encoder_block_layers_2_block_layers_0_block_branches_0_layers_0_alpha: T.Buffer((T.int64(1), T.int64(128), T.int64(1)), "float32"), T_reshape_intermediate_1: T.Buffer((T.int64(1), T.int64(128), T.int64(256)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_ax2_fused_0 in T.thread_binding(T.int64(32), thread="blockIdx.x"):
            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(1024), thread="threadIdx.x"):
                with T.block("T_reshape"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(128), (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1) // T.int64(256))
                    v_ax2 = T.axis.spatial(T.int64(256), (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1) % T.int64(256))
                    T.reads(lv78[T.int64(0), (v_ax2 // T.int64(256) + v_ax1) % T.int64(128), v_ax2 % T.int64(256)], encoder_block_layers_2_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_ax1, T.int64(0)])
                    T.writes(T_reshape_intermediate_1[T.int64(0), v_ax1, v_ax2])
                    T_reshape_intermediate_1[T.int64(0), v_ax1, v_ax2] = lv78[T.int64(0), (v_ax2 // T.int64(256) + v_ax1) % T.int64(128), v_ax2 % T.int64(256)] + T.float32(1.0) / (encoder_block_layers_2_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_ax1, T.int64(0)] + T.float32(1.0000000000000001e-09)) * T.pow(T.sin(encoder_block_layers_2_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_ax1, T.int64(0)] * lv78[T.int64(0), (v_ax2 // T.int64(256) + v_ax1) % T.int64(128), v_ax2 % T.int64(256)]), T.float32(2.0))

    @T.prim_func(private=True)
    def fused_reshape16_snake2_reshape161(lv147: T.Buffer((T.int64(1), T.int64(256), T.int64(64)), "float32"), encoder_block_layers_3_block_layers_0_block_branches_0_layers_0_alpha: T.Buffer((T.int64(1), T.int64(256), T.int64(1)), "float32"), T_reshape_intermediate_1: T.Buffer((T.int64(1), T.int64(256), T.int64(64)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_ax2_fused_0 in T.thread_binding(T.int64(16), thread="blockIdx.x"):
            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(1024), thread="threadIdx.x"):
                with T.block("T_reshape"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(256), (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1) // T.int64(64))
                    v_ax2 = T.axis.spatial(T.int64(64), (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1) % T.int64(64))
                    T.reads(lv147[T.int64(0), (v_ax2 // T.int64(64) + v_ax1) % T.int64(256), v_ax2 % T.int64(64)], encoder_block_layers_3_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_ax1, T.int64(0)])
                    T.writes(T_reshape_intermediate_1[T.int64(0), v_ax1, v_ax2])
                    T_reshape_intermediate_1[T.int64(0), v_ax1, v_ax2] = lv147[T.int64(0), (v_ax2 // T.int64(64) + v_ax1) % T.int64(256), v_ax2 % T.int64(64)] + T.float32(1.0) / (encoder_block_layers_3_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_ax1, T.int64(0)] + T.float32(1.0000000000000001e-09)) * T.pow(T.sin(encoder_block_layers_3_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_ax1, T.int64(0)] * lv147[T.int64(0), (v_ax2 // T.int64(64) + v_ax1) % T.int64(256), v_ax2 % T.int64(64)]), T.float32(2.0))

    @T.prim_func(private=True)
    def fused_reshape18_snake3_reshape181(lv216: T.Buffer((T.int64(1), T.int64(512), T.int64(8)), "float32"), encoder_block_layers_4_block_layers_0_block_branches_0_layers_0_alpha: T.Buffer((T.int64(1), T.int64(512), T.int64(1)), "float32"), T_reshape_intermediate_1: T.Buffer((T.int64(1), T.int64(512), T.int64(8)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_ax2_fused_0 in T.thread_binding(T.int64(4), thread="blockIdx.x"):
            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(1024), thread="threadIdx.x"):
                with T.block("T_reshape"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(512), (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1) // T.int64(8))
                    v_ax2 = T.axis.spatial(T.int64(8), (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1) % T.int64(8))
                    T.reads(lv216[T.int64(0), (v_ax2 // T.int64(8) + v_ax1) % T.int64(512), v_ax2 % T.int64(8)], encoder_block_layers_4_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_ax1, T.int64(0)])
                    T.writes(T_reshape_intermediate_1[T.int64(0), v_ax1, v_ax2])
                    T_reshape_intermediate_1[T.int64(0), v_ax1, v_ax2] = lv216[T.int64(0), (v_ax2 // T.int64(8) + v_ax1) % T.int64(512), v_ax2 % T.int64(8)] + T.float32(1.0) / (encoder_block_layers_4_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_ax1, T.int64(0)] + T.float32(1.0000000000000001e-09)) * T.pow(T.sin(encoder_block_layers_4_block_layers_0_block_branches_0_layers_0_alpha[T.int64(0), v_ax1, T.int64(0)] * lv216[T.int64(0), (v_ax2 // T.int64(8) + v_ax1) % T.int64(512), v_ax2 % T.int64(8)]), T.float32(2.0))

    @T.prim_func(private=True)
    def fused_reshape1_snake5_reshape11(conv1d48: T.Buffer((T.int64(1), T.int64(1536), T.int64(1)), "float32"), decoder_model_layers_1_block_layers_0_alpha1: T.Buffer((T.int64(1), T.int64(1536), T.int64(1)), "float32"), T_reshape_intermediate_1: T.Buffer((T.int64(1), T.int64(1536), T.int64(1)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_ax2_fused_0 in T.thread_binding(T.int64(3), thread="blockIdx.x"):
            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(512), thread="threadIdx.x"):
                with T.block("T_reshape"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(1536), ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1)
                    v_ax2 = T.axis.spatial(T.int64(1), T.int64(0))
                    T.reads(conv1d48[T.int64(0), (v_ax1 + v_ax2) % T.int64(1536), T.int64(0)], decoder_model_layers_1_block_layers_0_alpha1[T.int64(0), v_ax1, T.int64(0)])
                    T.writes(T_reshape_intermediate_1[T.int64(0), v_ax1, T.int64(0)])
                    T_reshape_intermediate_1[T.int64(0), v_ax1, T.int64(0)] = conv1d48[T.int64(0), (v_ax1 + v_ax2) % T.int64(1536), T.int64(0)] + T.float32(1.0) / (decoder_model_layers_1_block_layers_0_alpha1[T.int64(0), v_ax1, T.int64(0)] + T.float32(1.0000000000000001e-09)) * T.pow(T.sin(decoder_model_layers_1_block_layers_0_alpha1[T.int64(0), v_ax1, T.int64(0)] * conv1d48[T.int64(0), (v_ax1 + v_ax2) % T.int64(1536), T.int64(0)]), T.float32(2.0))

    @T.prim_func(private=True)
    def fused_reshape20_snake4_reshape201(conv1d28: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32"), encoder_block_layers_5_alpha: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32"), T_reshape_intermediate_1: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_ax2_fused_0 in T.thread_binding(T.int64(2), thread="blockIdx.x"):
            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(512), thread="threadIdx.x"):
                with T.block("T_reshape"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(1024), ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1)
                    v_ax2 = T.axis.spatial(T.int64(1), T.int64(0))
                    T.reads(conv1d28[T.int64(0), (v_ax1 + v_ax2) % T.int64(1024), T.int64(0)], encoder_block_layers_5_alpha[T.int64(0), v_ax1, T.int64(0)])
                    T.writes(T_reshape_intermediate_1[T.int64(0), v_ax1, T.int64(0)])
                    T_reshape_intermediate_1[T.int64(0), v_ax1, T.int64(0)] = conv1d28[T.int64(0), (v_ax1 + v_ax2) % T.int64(1024), T.int64(0)] + T.float32(1.0) / (encoder_block_layers_5_alpha[T.int64(0), v_ax1, T.int64(0)] + T.float32(1.0000000000000001e-09)) * T.pow(T.sin(encoder_block_layers_5_alpha[T.int64(0), v_ax1, T.int64(0)] * conv1d28[T.int64(0), (v_ax1 + v_ax2) % T.int64(1024), T.int64(0)]), T.float32(2.0))

    @T.prim_func(private=True)
    def fused_reshape25_transpose31(take1: T.Buffer((T.int64(1), T.int64(8)), "float32"), T_transpose_intermediate: T.Buffer((T.int64(1), T.int64(8), T.int64(1)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_ax2_fused_0 in T.thread_binding(T.int64(1), thread="blockIdx.x"):
            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(8), thread="threadIdx.x"):
                with T.block("T_reshape"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax2 = T.axis.spatial(T.int64(8), ax0_ax1_ax2_fused_0 * T.int64(8) + ax0_ax1_ax2_fused_1)
                    T.reads(take1[T.int64(0), v_ax2 % T.int64(8)])
                    T.writes(T_transpose_intermediate[v_ax0, v_ax2, v_ax1])
                    T_transpose_intermediate[v_ax0, v_ax2, v_ax1] = take1[T.int64(0), v_ax2 % T.int64(8)]

    @T.prim_func(private=True)
    def fused_reshape2_snake6_reshape21(lv416: T.Buffer((T.int64(1), T.int64(768), T.int64(8)), "float32"), decoder_model_layers_1_block_layers_2_block_branches_0_layers_0_alpha1: T.Buffer((T.int64(1), T.int64(768), T.int64(1)), "float32"), T_reshape_intermediate_1: T.Buffer((T.int64(1), T.int64(768), T.int64(8)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_ax2_fused_0 in T.thread_binding(T.int64(12), thread="blockIdx.x"):
            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(512), thread="threadIdx.x"):
                with T.block("T_reshape"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(768), (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1) // T.int64(8))
                    v_ax2 = T.axis.spatial(T.int64(8), (ax0_ax1_ax2_fused_0 * T.int64(512) + ax0_ax1_ax2_fused_1) % T.int64(8))
                    T.reads(lv416[T.int64(0), (v_ax2 // T.int64(8) + v_ax1) % T.int64(768), v_ax2 % T.int64(8)], decoder_model_layers_1_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_ax1, T.int64(0)])
                    T.writes(T_reshape_intermediate_1[T.int64(0), v_ax1, v_ax2])
                    T_reshape_intermediate_1[T.int64(0), v_ax1, v_ax2] = lv416[T.int64(0), (v_ax2 // T.int64(8) + v_ax1) % T.int64(768), v_ax2 % T.int64(8)] + T.float32(1.0) / (decoder_model_layers_1_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_ax1, T.int64(0)] + T.float32(1.0000000000000001e-09)) * T.pow(T.sin(decoder_model_layers_1_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_ax1, T.int64(0)] * lv416[T.int64(0), (v_ax2 // T.int64(8) + v_ax1) % T.int64(768), v_ax2 % T.int64(8)]), T.float32(2.0))

    @T.prim_func(private=True)
    def fused_reshape4_snake7_reshape41(lv482: T.Buffer((T.int64(1), T.int64(384), T.int64(64)), "float32"), decoder_model_layers_2_block_layers_2_block_branches_0_layers_0_alpha1: T.Buffer((T.int64(1), T.int64(384), T.int64(1)), "float32"), T_reshape_intermediate_1: T.Buffer((T.int64(1), T.int64(384), T.int64(64)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_ax2_fused_0 in T.thread_binding(T.int64(24), thread="blockIdx.x"):
            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(1024), thread="threadIdx.x"):
                with T.block("T_reshape"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(384), (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1) // T.int64(64))
                    v_ax2 = T.axis.spatial(T.int64(64), (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1) % T.int64(64))
                    T.reads(lv482[T.int64(0), (v_ax2 // T.int64(64) + v_ax1) % T.int64(384), v_ax2 % T.int64(64)], decoder_model_layers_2_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_ax1, T.int64(0)])
                    T.writes(T_reshape_intermediate_1[T.int64(0), v_ax1, v_ax2])
                    T_reshape_intermediate_1[T.int64(0), v_ax1, v_ax2] = lv482[T.int64(0), (v_ax2 // T.int64(64) + v_ax1) % T.int64(384), v_ax2 % T.int64(64)] + T.float32(1.0) / (decoder_model_layers_2_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_ax1, T.int64(0)] + T.float32(1.0000000000000001e-09)) * T.pow(T.sin(decoder_model_layers_2_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_ax1, T.int64(0)] * lv482[T.int64(0), (v_ax2 // T.int64(64) + v_ax1) % T.int64(384), v_ax2 % T.int64(64)]), T.float32(2.0))

    @T.prim_func(private=True)
    def fused_reshape6_snake8_reshape61(lv548: T.Buffer((T.int64(1), T.int64(192), T.int64(256)), "float32"), decoder_model_layers_3_block_layers_2_block_branches_0_layers_0_alpha1: T.Buffer((T.int64(1), T.int64(192), T.int64(1)), "float32"), T_reshape_intermediate_1: T.Buffer((T.int64(1), T.int64(192), T.int64(256)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_ax2_fused_0 in T.thread_binding(T.int64(48), thread="blockIdx.x"):
            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(1024), thread="threadIdx.x"):
                with T.block("T_reshape"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(192), (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1) // T.int64(256))
                    v_ax2 = T.axis.spatial(T.int64(256), (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1) % T.int64(256))
                    T.reads(lv548[T.int64(0), (v_ax2 // T.int64(256) + v_ax1) % T.int64(192), v_ax2 % T.int64(256)], decoder_model_layers_3_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_ax1, T.int64(0)])
                    T.writes(T_reshape_intermediate_1[T.int64(0), v_ax1, v_ax2])
                    T_reshape_intermediate_1[T.int64(0), v_ax1, v_ax2] = lv548[T.int64(0), (v_ax2 // T.int64(256) + v_ax1) % T.int64(192), v_ax2 % T.int64(256)] + T.float32(1.0) / (decoder_model_layers_3_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_ax1, T.int64(0)] + T.float32(1.0000000000000001e-09)) * T.pow(T.sin(decoder_model_layers_3_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_ax1, T.int64(0)] * lv548[T.int64(0), (v_ax2 // T.int64(256) + v_ax1) % T.int64(192), v_ax2 % T.int64(256)]), T.float32(2.0))

    @T.prim_func(private=True)
    def fused_reshape8_snake9_reshape81(lv614: T.Buffer((T.int64(1), T.int64(96), T.int64(512)), "float32"), decoder_model_layers_4_block_layers_2_block_branches_0_layers_0_alpha1: T.Buffer((T.int64(1), T.int64(96), T.int64(1)), "float32"), T_reshape_intermediate_1: T.Buffer((T.int64(1), T.int64(96), T.int64(512)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_ax2_fused_0 in T.thread_binding(T.int64(48), thread="blockIdx.x"):
            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(1024), thread="threadIdx.x"):
                with T.block("T_reshape"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(96), (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1) // T.int64(512))
                    v_ax2 = T.axis.spatial(T.int64(512), (ax0_ax1_ax2_fused_0 * T.int64(1024) + ax0_ax1_ax2_fused_1) % T.int64(512))
                    T.reads(lv614[T.int64(0), (v_ax2 // T.int64(512) + v_ax1) % T.int64(96), v_ax2 % T.int64(512)], decoder_model_layers_4_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_ax1, T.int64(0)])
                    T.writes(T_reshape_intermediate_1[T.int64(0), v_ax1, v_ax2])
                    T_reshape_intermediate_1[T.int64(0), v_ax1, v_ax2] = lv614[T.int64(0), (v_ax2 // T.int64(512) + v_ax1) % T.int64(96), v_ax2 % T.int64(512)] + T.float32(1.0) / (decoder_model_layers_4_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_ax1, T.int64(0)] + T.float32(1.0000000000000001e-09)) * T.pow(T.sin(decoder_model_layers_4_block_layers_2_block_branches_0_layers_0_alpha1[T.int64(0), v_ax1, T.int64(0)] * lv614[T.int64(0), (v_ax2 // T.int64(512) + v_ax1) % T.int64(96), v_ax2 % T.int64(512)]), T.float32(2.0))

    @T.prim_func(private=True)
    def fused_tir_square29_sum291(reshape58: T.Buffer((T.int64(1), T.int64(8)), "float32"), square_red_intermediate: T.Buffer((T.int64(1), T.int64(1)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_fused in T.thread_binding(T.int64(1), thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step": 16, "pragma_unroll_explicit": 1}):
            for k1_0 in range(T.int64(2)):
                for k1_1 in T.thread_binding(T.int64(4), thread="threadIdx.x"):
                    with T.block("square_red"):
                        v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                        v_ax1 = T.axis.spatial(T.int64(1), T.int64(0))
                        v_k1 = T.axis.reduce(T.int64(8), k1_0 * T.int64(4) + k1_1)
                        T.reads(reshape58[v_ax0, v_k1])
                        T.writes(square_red_intermediate[v_ax0, v_ax1])
                        with T.init():
                            square_red_intermediate[v_ax0, v_ax1] = T.float32(0.0)
                        square_red_intermediate[v_ax0, v_ax1] = square_red_intermediate[v_ax0, v_ax1] + reshape58[v_ax0, v_k1] * reshape58[v_ax0, v_k1]

    @T.prim_func(private=True)
    def fused_transpose_reshape221(conv1d30: T.Buffer((T.int64(1), T.int64(8), T.int64(1)), "float32"), T_reshape_intermediate: T.Buffer((T.int64(1), T.int64(8)), "float32")):
        T.func_attr({"layout_free_buffers": [], "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_ax2_fused_0 in T.thread_binding(T.int64(1), thread="blockIdx.x"):
            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(8), thread="threadIdx.x"):
                with T.block("T_transpose"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax2 = T.axis.spatial(T.int64(8), ax0_ax1_ax2_fused_0 * T.int64(8) + ax0_ax1_ax2_fused_1)
                    T.reads(conv1d30[v_ax0, v_ax2, v_ax1])
                    T.writes(T_reshape_intermediate[T.int64(0), v_ax2])
                    T_reshape_intermediate[T.int64(0), v_ax2] = conv1d30[v_ax0, v_ax2, v_ax1]

    @T.prim_func(private=True)
    def reshape231(take: T.Buffer((T.int64(1), T.int64(1)), "int32"), T_reshape: T.Buffer((T.int64(1), T.int64(1)), "int32")):
        T.func_attr({"layout_free_buffers": [], "op_pattern": 1, "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_fused_0 in T.thread_binding(T.int64(1), thread="blockIdx.x"):
            for ax0_ax1_fused_1 in T.thread_binding(T.int64(1), thread="threadIdx.x"):
                with T.block("T_reshape"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(1), T.int64(0))
                    T.reads(take[T.int64(0), T.int64(0)])
                    T.writes(T_reshape[v_ax0, v_ax1])
                    T_reshape[v_ax0, v_ax1] = take[T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def reshape241(reshape59: T.Buffer((T.int64(1), T.int64(1)), "int32"), T_reshape: T.Buffer((T.int64(1),), "int32")):
        T.func_attr({"layout_free_buffers": [], "op_pattern": 1, "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_fused_0 in T.thread_binding(T.int64(1), thread="blockIdx.x"):
            for ax0_fused_1 in T.thread_binding(T.int64(1), thread="threadIdx.x"):
                with T.block("T_reshape"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    T.reads(reshape59[T.int64(0), T.int64(0)])
                    T.writes(T_reshape[v_ax0])
                    T_reshape[v_ax0] = reshape59[T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def subtract11(conv1d29: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32"), conv1d31: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32"), T_subtract: T.Buffer((T.int64(1), T.int64(1024), T.int64(1)), "float32")):
        T.func_attr({"layout_free_buffers": [], "op_pattern": 0, "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_ax2_fused_0 in T.thread_binding(T.int64(8), thread="blockIdx.x"):
            for ax0_ax1_ax2_fused_1 in T.thread_binding(T.int64(128), thread="threadIdx.x"):
                with T.block("T_subtract"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(1024), ax0_ax1_ax2_fused_0 * T.int64(128) + ax0_ax1_ax2_fused_1)
                    v_ax2 = T.axis.spatial(T.int64(1), T.int64(0))
                    T.reads(conv1d29[v_ax0, v_ax1, v_ax2], conv1d31[v_ax0, v_ax1, v_ax2])
                    T.writes(T_subtract[v_ax0, v_ax1, v_ax2])
                    T_subtract[v_ax0, v_ax1, v_ax2] = conv1d29[v_ax0, v_ax1, v_ax2] - conv1d31[v_ax0, v_ax1, v_ax2]

    @T.prim_func(private=True)
    def take11(quantizer_quantizers_0_codebook_weight: T.Buffer((T.int64(1024), T.int64(8)), "float32"), reshape60: T.Buffer((T.int64(1),), "int32"), T_take: T.Buffer((T.int64(1), T.int64(8)), "float32")):
        T.func_attr({"layout_free_buffers": [], "op_pattern": 8, "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_fused_0 in T.thread_binding(T.int64(1), thread="blockIdx.x"):
            for ax0_ax1_fused_1 in T.thread_binding(T.int64(8), thread="threadIdx.x"):
                with T.block("T_take"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(8), ax0_ax1_fused_0 * T.int64(8) + ax0_ax1_fused_1)
                    T.reads(quantizer_quantizers_0_codebook_weight[reshape60[v_ax0], v_ax1], reshape60[v_ax0])
                    T.writes(T_take[v_ax0, v_ax1])
                    T_take[v_ax0, v_ax1] = quantizer_quantizers_0_codebook_weight[reshape60[v_ax0], v_ax1]

    @T.prim_func(private=True)
    def take2(argsort: T.Buffer((T.int64(1), T.int64(1024)), "int32"), B: T.Buffer((T.int64(1),), "int32"), T_take: T.Buffer((T.int64(1), T.int64(1)), "int32")):
        T.func_attr({"layout_free_buffers": [1], "op_pattern": 8, "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_fused_0 in T.thread_binding(T.int64(1), thread="blockIdx.x"):
            for ax0_ax1_fused_1 in T.thread_binding(T.int64(1), thread="threadIdx.x"):
                with T.block("T_take"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(1), T.int64(0))
                    T.reads(argsort[v_ax0, B[v_ax1]], B[v_ax1])
                    T.writes(T_take[v_ax0, v_ax1])
                    T_take[v_ax0, v_ax1] = argsort[v_ax0, B[v_ax1]]

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
            gv: R.Tuple(R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object) = _io, encoder_block_layers_0_cache_cache, encoder_block_layers_0_downsampling_delay_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_1_block_layers_0_block_paddings_0_cache, encoder_block_layers_1_block_layers_0_block_paddings_1_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_1_block_layers_1_block_paddings_0_cache, encoder_block_layers_1_block_layers_1_block_paddings_1_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_1_block_layers_2_block_paddings_0_cache, encoder_block_layers_1_block_layers_2_block_paddings_1_cache, encoder_block_layers_1_block_layers_4_cache_cache, encoder_block_layers_1_block_layers_4_downsampling_delay_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_2_block_layers_0_block_paddings_0_cache, encoder_block_layers_2_block_layers_0_block_paddings_1_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_2_block_layers_1_block_paddings_0_cache, encoder_block_layers_2_block_layers_1_block_paddings_1_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_2_block_layers_2_block_paddings_0_cache, encoder_block_layers_2_block_layers_2_block_paddings_1_cache, encoder_block_layers_2_block_layers_4_cache_cache, encoder_block_layers_2_block_layers_4_downsampling_delay_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_3_block_layers_0_block_paddings_0_cache, encoder_block_layers_3_block_layers_0_block_paddings_1_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_3_block_layers_1_block_paddings_0_cache, encoder_block_layers_3_block_layers_1_block_paddings_1_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_3_block_layers_2_block_paddings_0_cache, encoder_block_layers_3_block_layers_2_block_paddings_1_cache, encoder_block_layers_3_block_layers_4_cache_cache, encoder_block_layers_3_block_layers_4_downsampling_delay_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_4_block_layers_0_block_paddings_0_cache, encoder_block_layers_4_block_layers_0_block_paddings_1_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_4_block_layers_1_block_paddings_0_cache, encoder_block_layers_4_block_layers_1_block_paddings_1_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_4_block_layers_2_block_paddings_0_cache, encoder_block_layers_4_block_layers_2_block_paddings_1_cache, encoder_block_layers_4_block_layers_4_cache_cache, encoder_block_layers_4_block_layers_4_downsampling_delay_cache, encoder_block_layers_6_cache_cache, encoder_block_layers_6_downsampling_delay_cache, decoder_model_layers_0_cache_cache, decoder_model_layers_0_downsampling_delay_cache, decoder_model_layers_1_block_layers_1_cache_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_1_block_layers_2_block_paddings_0_cache, decoder_model_layers_1_block_layers_2_block_paddings_1_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_1_block_layers_3_block_paddings_0_cache, decoder_model_layers_1_block_layers_3_block_paddings_1_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_1_block_layers_4_block_paddings_0_cache, decoder_model_layers_1_block_layers_4_block_paddings_1_cache, decoder_model_layers_2_block_layers_1_cache_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_2_block_layers_2_block_paddings_0_cache, decoder_model_layers_2_block_layers_2_block_paddings_1_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_2_block_layers_3_block_paddings_0_cache, decoder_model_layers_2_block_layers_3_block_paddings_1_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_2_block_layers_4_block_paddings_0_cache, decoder_model_layers_2_block_layers_4_block_paddings_1_cache, decoder_model_layers_3_block_layers_1_cache_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_3_block_layers_2_block_paddings_0_cache, decoder_model_layers_3_block_layers_2_block_paddings_1_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_3_block_layers_3_block_paddings_0_cache, decoder_model_layers_3_block_layers_3_block_paddings_1_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_3_block_layers_4_block_paddings_0_cache, decoder_model_layers_3_block_layers_4_block_paddings_1_cache, decoder_model_layers_4_block_layers_1_cache_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_4_block_layers_2_block_paddings_0_cache, decoder_model_layers_4_block_layers_2_block_paddings_1_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_4_block_layers_3_block_paddings_0_cache, decoder_model_layers_4_block_layers_3_block_paddings_1_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_4_block_layers_4_block_paddings_0_cache, decoder_model_layers_4_block_layers_4_block_paddings_1_cache, decoder_model_layers_6_cache_cache, decoder_model_layers_6_downsampling_delay_cache
            R.output(gv)
        return gv

    @R.function
    def decode(z: R.Tensor((1, 1024, 1), dtype="float32"), _io: R.Object, encoder_block_layers_0_cache_cache: R.Object, encoder_block_layers_0_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_0_block_paddings_0_cache: R.Object, encoder_block_layers_1_block_layers_0_block_paddings_1_cache: R.Object, encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_1_block_paddings_0_cache: R.Object, encoder_block_layers_1_block_layers_1_block_paddings_1_cache: R.Object, encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_2_block_paddings_0_cache: R.Object, encoder_block_layers_1_block_layers_2_block_paddings_1_cache: R.Object, encoder_block_layers_1_block_layers_4_cache_cache: R.Object, encoder_block_layers_1_block_layers_4_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_0_block_paddings_0_cache: R.Object, encoder_block_layers_2_block_layers_0_block_paddings_1_cache: R.Object, encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_1_block_paddings_0_cache: R.Object, encoder_block_layers_2_block_layers_1_block_paddings_1_cache: R.Object, encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_2_block_paddings_0_cache: R.Object, encoder_block_layers_2_block_layers_2_block_paddings_1_cache: R.Object, encoder_block_layers_2_block_layers_4_cache_cache: R.Object, encoder_block_layers_2_block_layers_4_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_0_block_paddings_0_cache: R.Object, encoder_block_layers_3_block_layers_0_block_paddings_1_cache: R.Object, encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_1_block_paddings_0_cache: R.Object, encoder_block_layers_3_block_layers_1_block_paddings_1_cache: R.Object, encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_2_block_paddings_0_cache: R.Object, encoder_block_layers_3_block_layers_2_block_paddings_1_cache: R.Object, encoder_block_layers_3_block_layers_4_cache_cache: R.Object, encoder_block_layers_3_block_layers_4_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_0_block_paddings_0_cache: R.Object, encoder_block_layers_4_block_layers_0_block_paddings_1_cache: R.Object, encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_1_block_paddings_0_cache: R.Object, encoder_block_layers_4_block_layers_1_block_paddings_1_cache: R.Object, encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_2_block_paddings_0_cache: R.Object, encoder_block_layers_4_block_layers_2_block_paddings_1_cache: R.Object, encoder_block_layers_4_block_layers_4_cache_cache: R.Object, encoder_block_layers_4_block_layers_4_downsampling_delay_cache: R.Object, encoder_block_layers_6_cache_cache: R.Object, encoder_block_layers_6_downsampling_delay_cache: R.Object, decoder_model_layers_0_cache_cache: R.Object, decoder_model_layers_0_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_1_cache_cache: R.Object, decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_2_block_paddings_0_cache: R.Object, decoder_model_layers_1_block_layers_2_block_paddings_1_cache: R.Object, decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_3_block_paddings_0_cache: R.Object, decoder_model_layers_1_block_layers_3_block_paddings_1_cache: R.Object, decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_4_block_paddings_0_cache: R.Object, decoder_model_layers_1_block_layers_4_block_paddings_1_cache: R.Object, decoder_model_layers_2_block_layers_1_cache_cache: R.Object, decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_2_block_paddings_0_cache: R.Object, decoder_model_layers_2_block_layers_2_block_paddings_1_cache: R.Object, decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_3_block_paddings_0_cache: R.Object, decoder_model_layers_2_block_layers_3_block_paddings_1_cache: R.Object, decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_4_block_paddings_0_cache: R.Object, decoder_model_layers_2_block_layers_4_block_paddings_1_cache: R.Object, decoder_model_layers_3_block_layers_1_cache_cache: R.Object, decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_2_block_paddings_0_cache: R.Object, decoder_model_layers_3_block_layers_2_block_paddings_1_cache: R.Object, decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_3_block_paddings_0_cache: R.Object, decoder_model_layers_3_block_layers_3_block_paddings_1_cache: R.Object, decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_4_block_paddings_0_cache: R.Object, decoder_model_layers_3_block_layers_4_block_paddings_1_cache: R.Object, decoder_model_layers_4_block_layers_1_cache_cache: R.Object, decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_2_block_paddings_0_cache: R.Object, decoder_model_layers_4_block_layers_2_block_paddings_1_cache: R.Object, decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_3_block_paddings_0_cache: R.Object, decoder_model_layers_4_block_layers_3_block_paddings_1_cache: R.Object, decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_4_block_paddings_0_cache: R.Object, decoder_model_layers_4_block_layers_4_block_paddings_1_cache: R.Object, decoder_model_layers_6_cache_cache: R.Object, decoder_model_layers_6_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_0_alpha1: R.Tensor((1, 1536, 1), dtype="float32"), decoder_model_layers_1_block_layers_1_bias1: R.Tensor((768,), dtype="float32"), decoder_model_layers_1_block_layers_2_block_branches_0_layers_0_alpha1: R.Tensor((1, 768, 1), dtype="float32"), decoder_model_layers_1_block_layers_2_block_branches_0_layers_2_alpha1: R.Tensor((1, 768, 1), dtype="float32"), decoder_model_layers_1_block_layers_3_block_branches_0_layers_0_alpha1: R.Tensor((1, 768, 1), dtype="float32"), decoder_model_layers_1_block_layers_3_block_branches_0_layers_2_alpha1: R.Tensor((1, 768, 1), dtype="float32"), decoder_model_layers_1_block_layers_4_block_branches_0_layers_0_alpha1: R.Tensor((1, 768, 1), dtype="float32"), decoder_model_layers_1_block_layers_4_block_branches_0_layers_2_alpha1: R.Tensor((1, 768, 1), dtype="float32"), decoder_model_layers_2_block_layers_0_alpha1: R.Tensor((1, 768, 1), dtype="float32"), decoder_model_layers_2_block_layers_1_bias1: R.Tensor((384,), dtype="float32"), decoder_model_layers_2_block_layers_2_block_branches_0_layers_0_alpha1: R.Tensor((1, 384, 1), dtype="float32"), decoder_model_layers_2_block_layers_2_block_branches_0_layers_2_alpha1: R.Tensor((1, 384, 1), dtype="float32"), decoder_model_layers_2_block_layers_3_block_branches_0_layers_0_alpha1: R.Tensor((1, 384, 1), dtype="float32"), decoder_model_layers_2_block_layers_3_block_branches_0_layers_2_alpha1: R.Tensor((1, 384, 1), dtype="float32"), decoder_model_layers_2_block_layers_4_block_branches_0_layers_0_alpha1: R.Tensor((1, 384, 1), dtype="float32"), decoder_model_layers_2_block_layers_4_block_branches_0_layers_2_alpha1: R.Tensor((1, 384, 1), dtype="float32"), decoder_model_layers_3_block_layers_0_alpha1: R.Tensor((1, 384, 1), dtype="float32"), decoder_model_layers_3_block_layers_1_bias1: R.Tensor((192,), dtype="float32"), decoder_model_layers_3_block_layers_2_block_branches_0_layers_0_alpha1: R.Tensor((1, 192, 1), dtype="float32"), decoder_model_layers_3_block_layers_2_block_branches_0_layers_2_alpha1: R.Tensor((1, 192, 1), dtype="float32"), decoder_model_layers_3_block_layers_3_block_branches_0_layers_0_alpha1: R.Tensor((1, 192, 1), dtype="float32"), decoder_model_layers_3_block_layers_3_block_branches_0_layers_2_alpha1: R.Tensor((1, 192, 1), dtype="float32"), decoder_model_layers_3_block_layers_4_block_branches_0_layers_0_alpha1: R.Tensor((1, 192, 1), dtype="float32"), decoder_model_layers_3_block_layers_4_block_branches_0_layers_2_alpha1: R.Tensor((1, 192, 1), dtype="float32"), decoder_model_layers_4_block_layers_0_alpha1: R.Tensor((1, 192, 1), dtype="float32"), decoder_model_layers_4_block_layers_1_bias1: R.Tensor((96,), dtype="float32"), decoder_model_layers_4_block_layers_2_block_branches_0_layers_0_alpha1: R.Tensor((1, 96, 1), dtype="float32"), decoder_model_layers_4_block_layers_2_block_branches_0_layers_2_alpha1: R.Tensor((1, 96, 1), dtype="float32"), decoder_model_layers_4_block_layers_3_block_branches_0_layers_0_alpha1: R.Tensor((1, 96, 1), dtype="float32"), decoder_model_layers_4_block_layers_3_block_branches_0_layers_2_alpha1: R.Tensor((1, 96, 1), dtype="float32"), decoder_model_layers_4_block_layers_4_block_branches_0_layers_0_alpha1: R.Tensor((1, 96, 1), dtype="float32"), decoder_model_layers_4_block_layers_4_block_branches_0_layers_2_alpha1: R.Tensor((1, 96, 1), dtype="float32"), decoder_model_layers_5_alpha1: R.Tensor((1, 96, 1), dtype="float32"), decoder_model_layers_6_bias1: R.Tensor((1,), dtype="float32"), lv1: R.Tensor((1536, 1024, 7), dtype="float32"), lv409: R.Tensor((1, 1536, 1), dtype="float32"), lv5: R.Tensor((1536, 768, 16), dtype="float32"), lv9: R.Tensor((768, 768, 7), dtype="float32"), lv425: R.Tensor((1, 768, 1), dtype="float32"), lv13: R.Tensor((768, 768, 1), dtype="float32"), lv434: R.Tensor((1, 768, 1), dtype="float32"), lv17: R.Tensor((768, 768, 7), dtype="float32"), lv445: R.Tensor((1, 768, 1), dtype="float32"), lv21: R.Tensor((768, 768, 1), dtype="float32"), lv454: R.Tensor((1, 768, 1), dtype="float32"), lv25: R.Tensor((768, 768, 7), dtype="float32"), lv465: R.Tensor((1, 768, 1), dtype="float32"), lv29: R.Tensor((768, 768, 1), dtype="float32"), lv474: R.Tensor((1, 768, 1), dtype="float32"), lv33: R.Tensor((768, 384, 16), dtype="float32"), lv37: R.Tensor((384, 384, 7), dtype="float32"), lv491: R.Tensor((1, 384, 1), dtype="float32"), lv41: R.Tensor((384, 384, 1), dtype="float32"), lv500: R.Tensor((1, 384, 1), dtype="float32"), lv45: R.Tensor((384, 384, 7), dtype="float32"), lv511: R.Tensor((1, 384, 1), dtype="float32"), lv49: R.Tensor((384, 384, 1), dtype="float32"), lv520: R.Tensor((1, 384, 1), dtype="float32"), lv53: R.Tensor((384, 384, 7), dtype="float32"), lv531: R.Tensor((1, 384, 1), dtype="float32"), lv57: R.Tensor((384, 384, 1), dtype="float32"), lv540: R.Tensor((1, 384, 1), dtype="float32"), lv61: R.Tensor((384, 192, 8), dtype="float32"), lv65: R.Tensor((192, 192, 7), dtype="float32"), lv557: R.Tensor((1, 192, 1), dtype="float32"), lv69: R.Tensor((192, 192, 1), dtype="float32"), lv566: R.Tensor((1, 192, 1), dtype="float32"), lv73: R.Tensor((192, 192, 7), dtype="float32"), lv577: R.Tensor((1, 192, 1), dtype="float32"), lv77: R.Tensor((192, 192, 1), dtype="float32"), lv586: R.Tensor((1, 192, 1), dtype="float32"), lv81: R.Tensor((192, 192, 7), dtype="float32"), lv597: R.Tensor((1, 192, 1), dtype="float32"), lv85: R.Tensor((192, 192, 1), dtype="float32"), lv606: R.Tensor((1, 192, 1), dtype="float32"), lv89: R.Tensor((192, 96, 4), dtype="float32"), lv93: R.Tensor((96, 96, 7), dtype="float32"), lv623: R.Tensor((1, 96, 1), dtype="float32"), lv97: R.Tensor((96, 96, 1), dtype="float32"), lv632: R.Tensor((1, 96, 1), dtype="float32"), lv101: R.Tensor((96, 96, 7), dtype="float32"), lv643: R.Tensor((1, 96, 1), dtype="float32"), lv105: R.Tensor((96, 96, 1), dtype="float32"), lv652: R.Tensor((1, 96, 1), dtype="float32"), lv109: R.Tensor((96, 96, 7), dtype="float32"), lv663: R.Tensor((1, 96, 1), dtype="float32"), lv113: R.Tensor((96, 96, 1), dtype="float32"), lv672: R.Tensor((1, 96, 1), dtype="float32"), lv117: R.Tensor((1, 96, 7), dtype="float32")) -> R.Tuple(R.Tensor((1, 1, 512), dtype="float32"), R.Tuple(R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object)):
        R.func_attr({"num_input": 166})
        cls = Module
        with R.dataflow():
            lv402: R.Tensor((1, 1024, 1), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_0_downsampling_delay_cache, z, sinfo_args=(R.Tensor((1, 1024, 1), dtype="float32"),))
            lv403: R.Tensor((1, 1024, 7), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_0_cache_cache, lv402, sinfo_args=(R.Tensor((1, 1024, 7), dtype="float32"),))
            lv2 = R.call_tir(cls.fused_conv1d_add1, (lv403, lv1, lv409), out_sinfo=R.Tensor((1, 1536, 1), dtype="float32"))
            lv3 = R.call_tir(cls.fused_reshape1_snake5_reshape11, (lv2, decoder_model_layers_1_block_layers_0_alpha1), out_sinfo=R.Tensor((1, 1536, 1), dtype="float32"))
            conv1d_transpose = R.call_tir(cls.conv1d_transpose4, (lv3, lv5), out_sinfo=R.Tensor((1, 768, 16), dtype="float32"))
            lv415: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_1_cache_cache, conv1d_transpose, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv6 = R.call_tir(cls.fused_expand_dims_add11, (decoder_model_layers_1_block_layers_1_bias1, lv415), out_sinfo=R.Tensor((1, 768, 8), dtype="float32"))
            lv416: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_2_block_paddings_0_cache, lv6, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv7 = R.call_tir(cls.fused_reshape2_snake6_reshape21, (lv416, decoder_model_layers_1_block_layers_2_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 768, 8), dtype="float32"))
            lv418: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, lv7, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv419: R.Tensor((1, 768, 14), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache, lv418, sinfo_args=(R.Tensor((1, 768, 14), dtype="float32"),))
            lv10 = R.call_tir(cls.fused_conv1d1_add21, (lv419, lv9, lv425), out_sinfo=R.Tensor((1, 768, 8), dtype="float32"))
            lv11 = R.call_tir(cls.fused_reshape2_snake6_reshape21, (lv10, decoder_model_layers_1_block_layers_2_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 768, 8), dtype="float32"))
            lv427: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, lv11, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv428: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache, lv427, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv435: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_2_block_paddings_1_cache, lv6, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv14 = R.call_tir(cls.fused_conv1d2_add2_add3_add41, (lv428, lv13, lv434, lv435), out_sinfo=R.Tensor((1, 768, 8), dtype="float32"))
            lv436: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_3_block_paddings_0_cache, lv14, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv15 = R.call_tir(cls.fused_reshape2_snake6_reshape21, (lv436, decoder_model_layers_1_block_layers_3_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 768, 8), dtype="float32"))
            lv438: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, lv15, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv439: R.Tensor((1, 768, 26), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_cache_cache, lv438, sinfo_args=(R.Tensor((1, 768, 26), dtype="float32"),))
            lv18 = R.call_tir(cls.fused_conv1d3_add21, (lv439, lv17, lv445), out_sinfo=R.Tensor((1, 768, 8), dtype="float32"))
            lv19 = R.call_tir(cls.fused_reshape2_snake6_reshape21, (lv18, decoder_model_layers_1_block_layers_3_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 768, 8), dtype="float32"))
            lv447: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, lv19, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv448: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_cache_cache, lv447, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv455: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_3_block_paddings_1_cache, lv14, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv22 = R.call_tir(cls.fused_conv1d2_add2_add3_add41, (lv448, lv21, lv454, lv455), out_sinfo=R.Tensor((1, 768, 8), dtype="float32"))
            lv456: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_4_block_paddings_0_cache, lv22, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv23 = R.call_tir(cls.fused_reshape2_snake6_reshape21, (lv456, decoder_model_layers_1_block_layers_4_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 768, 8), dtype="float32"))
            lv458: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, lv23, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv459: R.Tensor((1, 768, 62), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_cache_cache, lv458, sinfo_args=(R.Tensor((1, 768, 62), dtype="float32"),))
            lv26 = R.call_tir(cls.fused_conv1d4_add21, (lv459, lv25, lv465), out_sinfo=R.Tensor((1, 768, 8), dtype="float32"))
            lv27 = R.call_tir(cls.fused_reshape2_snake6_reshape21, (lv26, decoder_model_layers_1_block_layers_4_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 768, 8), dtype="float32"))
            lv467: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, lv27, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv468: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_cache_cache, lv467, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv475: R.Tensor((1, 768, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_1_block_layers_4_block_paddings_1_cache, lv22, sinfo_args=(R.Tensor((1, 768, 8), dtype="float32"),))
            lv30 = R.call_tir(cls.fused_conv1d2_add2_add3_add41, (lv468, lv29, lv474, lv475), out_sinfo=R.Tensor((1, 768, 8), dtype="float32"))
            lv31 = R.call_tir(cls.fused_reshape2_snake6_reshape21, (lv30, decoder_model_layers_2_block_layers_0_alpha1), out_sinfo=R.Tensor((1, 768, 8), dtype="float32"))
            conv1d_transpose1 = R.call_tir(cls.conv1d_transpose11, (lv31, lv33), out_sinfo=R.Tensor((1, 384, 72), dtype="float32"))
            lv481: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_1_cache_cache, conv1d_transpose1, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv34 = R.call_tir(cls.fused_expand_dims1_add51, (decoder_model_layers_2_block_layers_1_bias1, lv481), out_sinfo=R.Tensor((1, 384, 64), dtype="float32"))
            lv482: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_2_block_paddings_0_cache, lv34, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv35 = R.call_tir(cls.fused_reshape4_snake7_reshape41, (lv482, decoder_model_layers_2_block_layers_2_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 384, 64), dtype="float32"))
            lv484: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, lv35, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv485: R.Tensor((1, 384, 70), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache, lv484, sinfo_args=(R.Tensor((1, 384, 70), dtype="float32"),))
            lv38 = R.call_tir(cls.fused_conv1d5_add61, (lv485, lv37, lv491), out_sinfo=R.Tensor((1, 384, 64), dtype="float32"))
            lv39 = R.call_tir(cls.fused_reshape4_snake7_reshape41, (lv38, decoder_model_layers_2_block_layers_2_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 384, 64), dtype="float32"))
            lv493: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, lv39, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv494: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache, lv493, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv501: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_2_block_paddings_1_cache, lv34, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv42 = R.call_tir(cls.fused_conv1d6_add6_add7_add81, (lv494, lv41, lv500, lv501), out_sinfo=R.Tensor((1, 384, 64), dtype="float32"))
            lv502: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_3_block_paddings_0_cache, lv42, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv43 = R.call_tir(cls.fused_reshape4_snake7_reshape41, (lv502, decoder_model_layers_2_block_layers_3_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 384, 64), dtype="float32"))
            lv504: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, lv43, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv505: R.Tensor((1, 384, 82), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_cache_cache, lv504, sinfo_args=(R.Tensor((1, 384, 82), dtype="float32"),))
            lv46 = R.call_tir(cls.fused_conv1d7_add61, (lv505, lv45, lv511), out_sinfo=R.Tensor((1, 384, 64), dtype="float32"))
            lv47 = R.call_tir(cls.fused_reshape4_snake7_reshape41, (lv46, decoder_model_layers_2_block_layers_3_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 384, 64), dtype="float32"))
            lv513: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, lv47, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv514: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_cache_cache, lv513, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv521: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_3_block_paddings_1_cache, lv42, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv50 = R.call_tir(cls.fused_conv1d6_add6_add7_add81, (lv514, lv49, lv520, lv521), out_sinfo=R.Tensor((1, 384, 64), dtype="float32"))
            lv522: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_4_block_paddings_0_cache, lv50, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv51 = R.call_tir(cls.fused_reshape4_snake7_reshape41, (lv522, decoder_model_layers_2_block_layers_4_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 384, 64), dtype="float32"))
            lv524: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, lv51, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv525: R.Tensor((1, 384, 118), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_cache_cache, lv524, sinfo_args=(R.Tensor((1, 384, 118), dtype="float32"),))
            lv54 = R.call_tir(cls.fused_conv1d8_add61, (lv525, lv53, lv531), out_sinfo=R.Tensor((1, 384, 64), dtype="float32"))
            lv55 = R.call_tir(cls.fused_reshape4_snake7_reshape41, (lv54, decoder_model_layers_2_block_layers_4_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 384, 64), dtype="float32"))
            lv533: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, lv55, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv534: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_cache_cache, lv533, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv541: R.Tensor((1, 384, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_2_block_layers_4_block_paddings_1_cache, lv50, sinfo_args=(R.Tensor((1, 384, 64), dtype="float32"),))
            lv58 = R.call_tir(cls.fused_conv1d6_add6_add7_add81, (lv534, lv57, lv540, lv541), out_sinfo=R.Tensor((1, 384, 64), dtype="float32"))
            lv59 = R.call_tir(cls.fused_reshape4_snake7_reshape41, (lv58, decoder_model_layers_3_block_layers_0_alpha1), out_sinfo=R.Tensor((1, 384, 64), dtype="float32"))
            conv1d_transpose2 = R.call_tir(cls.conv1d_transpose21, (lv59, lv61), out_sinfo=R.Tensor((1, 192, 260), dtype="float32"))
            lv547: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_1_cache_cache, conv1d_transpose2, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv62 = R.call_tir(cls.fused_expand_dims2_add91, (decoder_model_layers_3_block_layers_1_bias1, lv547), out_sinfo=R.Tensor((1, 192, 256), dtype="float32"))
            lv548: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_2_block_paddings_0_cache, lv62, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv63 = R.call_tir(cls.fused_reshape6_snake8_reshape61, (lv548, decoder_model_layers_3_block_layers_2_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 192, 256), dtype="float32"))
            lv550: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, lv63, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv551: R.Tensor((1, 192, 262), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache, lv550, sinfo_args=(R.Tensor((1, 192, 262), dtype="float32"),))
            lv66 = R.call_tir(cls.fused_conv1d9_add101, (lv551, lv65, lv557), out_sinfo=R.Tensor((1, 192, 256), dtype="float32"))
            lv67 = R.call_tir(cls.fused_reshape6_snake8_reshape61, (lv66, decoder_model_layers_3_block_layers_2_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 192, 256), dtype="float32"))
            lv559: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, lv67, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv560: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache, lv559, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv567: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_2_block_paddings_1_cache, lv62, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv70 = R.call_tir(cls.fused_conv1d10_add10_add11_add121, (lv560, lv69, lv566, lv567), out_sinfo=R.Tensor((1, 192, 256), dtype="float32"))
            lv568: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_3_block_paddings_0_cache, lv70, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv71 = R.call_tir(cls.fused_reshape6_snake8_reshape61, (lv568, decoder_model_layers_3_block_layers_3_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 192, 256), dtype="float32"))
            lv570: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, lv71, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv571: R.Tensor((1, 192, 274), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_cache_cache, lv570, sinfo_args=(R.Tensor((1, 192, 274), dtype="float32"),))
            lv74 = R.call_tir(cls.fused_conv1d11_add101, (lv571, lv73, lv577), out_sinfo=R.Tensor((1, 192, 256), dtype="float32"))
            lv75 = R.call_tir(cls.fused_reshape6_snake8_reshape61, (lv74, decoder_model_layers_3_block_layers_3_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 192, 256), dtype="float32"))
            lv579: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, lv75, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv580: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_cache_cache, lv579, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv587: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_3_block_paddings_1_cache, lv70, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv78 = R.call_tir(cls.fused_conv1d10_add10_add11_add121, (lv580, lv77, lv586, lv587), out_sinfo=R.Tensor((1, 192, 256), dtype="float32"))
            lv588: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_4_block_paddings_0_cache, lv78, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv79 = R.call_tir(cls.fused_reshape6_snake8_reshape61, (lv588, decoder_model_layers_3_block_layers_4_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 192, 256), dtype="float32"))
            lv590: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, lv79, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv591: R.Tensor((1, 192, 310), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_cache_cache, lv590, sinfo_args=(R.Tensor((1, 192, 310), dtype="float32"),))
            lv82 = R.call_tir(cls.fused_conv1d12_add101, (lv591, lv81, lv597), out_sinfo=R.Tensor((1, 192, 256), dtype="float32"))
            lv83 = R.call_tir(cls.fused_reshape6_snake8_reshape61, (lv82, decoder_model_layers_3_block_layers_4_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 192, 256), dtype="float32"))
            lv599: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, lv83, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv600: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_cache_cache, lv599, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv607: R.Tensor((1, 192, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_3_block_layers_4_block_paddings_1_cache, lv78, sinfo_args=(R.Tensor((1, 192, 256), dtype="float32"),))
            lv86 = R.call_tir(cls.fused_conv1d10_add10_add11_add121, (lv600, lv85, lv606, lv607), out_sinfo=R.Tensor((1, 192, 256), dtype="float32"))
            lv87 = R.call_tir(cls.fused_reshape6_snake8_reshape61, (lv86, decoder_model_layers_4_block_layers_0_alpha1), out_sinfo=R.Tensor((1, 192, 256), dtype="float32"))
            conv1d_transpose3 = R.call_tir(cls.conv1d_transpose31, (lv87, lv89), out_sinfo=R.Tensor((1, 96, 514), dtype="float32"))
            lv613: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_1_cache_cache, conv1d_transpose3, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv90 = R.call_tir(cls.fused_expand_dims3_add131, (decoder_model_layers_4_block_layers_1_bias1, lv613), out_sinfo=R.Tensor((1, 96, 512), dtype="float32"))
            lv614: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_2_block_paddings_0_cache, lv90, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv91 = R.call_tir(cls.fused_reshape8_snake9_reshape81, (lv614, decoder_model_layers_4_block_layers_2_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 96, 512), dtype="float32"))
            lv616: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, lv91, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv617: R.Tensor((1, 96, 518), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache, lv616, sinfo_args=(R.Tensor((1, 96, 518), dtype="float32"),))
            lv94 = R.call_tir(cls.fused_conv1d13_add141, (lv617, lv93, lv623), out_sinfo=R.Tensor((1, 96, 512), dtype="float32"))
            lv95 = R.call_tir(cls.fused_reshape8_snake9_reshape81, (lv94, decoder_model_layers_4_block_layers_2_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 96, 512), dtype="float32"))
            lv625: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, lv95, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv626: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache, lv625, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv633: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_2_block_paddings_1_cache, lv90, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv98 = R.call_tir(cls.fused_conv1d14_add14_add15_add161, (lv626, lv97, lv632, lv633), out_sinfo=R.Tensor((1, 96, 512), dtype="float32"))
            lv634: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_3_block_paddings_0_cache, lv98, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv99 = R.call_tir(cls.fused_reshape8_snake9_reshape81, (lv634, decoder_model_layers_4_block_layers_3_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 96, 512), dtype="float32"))
            lv636: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, lv99, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv637: R.Tensor((1, 96, 530), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_cache_cache, lv636, sinfo_args=(R.Tensor((1, 96, 530), dtype="float32"),))
            lv102 = R.call_tir(cls.fused_conv1d15_add141, (lv637, lv101, lv643), out_sinfo=R.Tensor((1, 96, 512), dtype="float32"))
            lv103 = R.call_tir(cls.fused_reshape8_snake9_reshape81, (lv102, decoder_model_layers_4_block_layers_3_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 96, 512), dtype="float32"))
            lv645: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, lv103, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv646: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_cache_cache, lv645, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv653: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_3_block_paddings_1_cache, lv98, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv106 = R.call_tir(cls.fused_conv1d14_add14_add15_add161, (lv646, lv105, lv652, lv653), out_sinfo=R.Tensor((1, 96, 512), dtype="float32"))
            lv654: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_4_block_paddings_0_cache, lv106, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv107 = R.call_tir(cls.fused_reshape8_snake9_reshape81, (lv654, decoder_model_layers_4_block_layers_4_block_branches_0_layers_0_alpha1), out_sinfo=R.Tensor((1, 96, 512), dtype="float32"))
            lv656: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, lv107, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv657: R.Tensor((1, 96, 566), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_cache_cache, lv656, sinfo_args=(R.Tensor((1, 96, 566), dtype="float32"),))
            lv110 = R.call_tir(cls.fused_conv1d16_add141, (lv657, lv109, lv663), out_sinfo=R.Tensor((1, 96, 512), dtype="float32"))
            lv111 = R.call_tir(cls.fused_reshape8_snake9_reshape81, (lv110, decoder_model_layers_4_block_layers_4_block_branches_0_layers_2_alpha1), out_sinfo=R.Tensor((1, 96, 512), dtype="float32"))
            lv665: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, lv111, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv666: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_cache_cache, lv665, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv673: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_4_block_layers_4_block_paddings_1_cache, lv106, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv114 = R.call_tir(cls.fused_conv1d14_add14_add15_add161, (lv666, lv113, lv672, lv673), out_sinfo=R.Tensor((1, 96, 512), dtype="float32"))
            lv115 = R.call_tir(cls.fused_reshape8_snake9_reshape81, (lv114, decoder_model_layers_5_alpha1), out_sinfo=R.Tensor((1, 96, 512), dtype="float32"))
            lv675: R.Tensor((1, 96, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_6_downsampling_delay_cache, lv115, sinfo_args=(R.Tensor((1, 96, 512), dtype="float32"),))
            lv676: R.Tensor((1, 96, 518), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", decoder_model_layers_6_cache_cache, lv675, sinfo_args=(R.Tensor((1, 96, 518), dtype="float32"),))
            lv118 = R.call_tir(cls.fused_conv1d17_reshape10_add17_tir_tanh1, (lv676, lv117, decoder_model_layers_6_bias1), out_sinfo=R.Tensor((1, 1, 512), dtype="float32"))
            gv2: R.Tuple(R.Tensor((1, 1, 512), dtype="float32"), R.Tuple(R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object)) = lv118, (_io, encoder_block_layers_0_cache_cache, encoder_block_layers_0_downsampling_delay_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_1_block_layers_0_block_paddings_0_cache, encoder_block_layers_1_block_layers_0_block_paddings_1_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_1_block_layers_1_block_paddings_0_cache, encoder_block_layers_1_block_layers_1_block_paddings_1_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_1_block_layers_2_block_paddings_0_cache, encoder_block_layers_1_block_layers_2_block_paddings_1_cache, encoder_block_layers_1_block_layers_4_cache_cache, encoder_block_layers_1_block_layers_4_downsampling_delay_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_2_block_layers_0_block_paddings_0_cache, encoder_block_layers_2_block_layers_0_block_paddings_1_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_2_block_layers_1_block_paddings_0_cache, encoder_block_layers_2_block_layers_1_block_paddings_1_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_2_block_layers_2_block_paddings_0_cache, encoder_block_layers_2_block_layers_2_block_paddings_1_cache, encoder_block_layers_2_block_layers_4_cache_cache, encoder_block_layers_2_block_layers_4_downsampling_delay_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_3_block_layers_0_block_paddings_0_cache, encoder_block_layers_3_block_layers_0_block_paddings_1_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_3_block_layers_1_block_paddings_0_cache, encoder_block_layers_3_block_layers_1_block_paddings_1_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_3_block_layers_2_block_paddings_0_cache, encoder_block_layers_3_block_layers_2_block_paddings_1_cache, encoder_block_layers_3_block_layers_4_cache_cache, encoder_block_layers_3_block_layers_4_downsampling_delay_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_4_block_layers_0_block_paddings_0_cache, encoder_block_layers_4_block_layers_0_block_paddings_1_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_4_block_layers_1_block_paddings_0_cache, encoder_block_layers_4_block_layers_1_block_paddings_1_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_4_block_layers_2_block_paddings_0_cache, encoder_block_layers_4_block_layers_2_block_paddings_1_cache, encoder_block_layers_4_block_layers_4_cache_cache, encoder_block_layers_4_block_layers_4_downsampling_delay_cache, encoder_block_layers_6_cache_cache, encoder_block_layers_6_downsampling_delay_cache, decoder_model_layers_0_cache_cache, decoder_model_layers_0_downsampling_delay_cache, decoder_model_layers_1_block_layers_1_cache_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_1_block_layers_2_block_paddings_0_cache, decoder_model_layers_1_block_layers_2_block_paddings_1_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_1_block_layers_3_block_paddings_0_cache, decoder_model_layers_1_block_layers_3_block_paddings_1_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_1_block_layers_4_block_paddings_0_cache, decoder_model_layers_1_block_layers_4_block_paddings_1_cache, decoder_model_layers_2_block_layers_1_cache_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_2_block_layers_2_block_paddings_0_cache, decoder_model_layers_2_block_layers_2_block_paddings_1_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_2_block_layers_3_block_paddings_0_cache, decoder_model_layers_2_block_layers_3_block_paddings_1_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_2_block_layers_4_block_paddings_0_cache, decoder_model_layers_2_block_layers_4_block_paddings_1_cache, decoder_model_layers_3_block_layers_1_cache_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_3_block_layers_2_block_paddings_0_cache, decoder_model_layers_3_block_layers_2_block_paddings_1_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_3_block_layers_3_block_paddings_0_cache, decoder_model_layers_3_block_layers_3_block_paddings_1_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_3_block_layers_4_block_paddings_0_cache, decoder_model_layers_3_block_layers_4_block_paddings_1_cache, decoder_model_layers_4_block_layers_1_cache_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_4_block_layers_2_block_paddings_0_cache, decoder_model_layers_4_block_layers_2_block_paddings_1_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_4_block_layers_3_block_paddings_0_cache, decoder_model_layers_4_block_layers_3_block_paddings_1_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_4_block_layers_4_block_paddings_0_cache, decoder_model_layers_4_block_layers_4_block_paddings_1_cache, decoder_model_layers_6_cache_cache, decoder_model_layers_6_downsampling_delay_cache)
            R.output(gv2)
        return gv2

    @R.function
    def encode(audio_data: R.Tensor((1, 1, 512), dtype="float32"), _io: R.Object, encoder_block_layers_0_cache_cache: R.Object, encoder_block_layers_0_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_0_block_paddings_0_cache: R.Object, encoder_block_layers_1_block_layers_0_block_paddings_1_cache: R.Object, encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_1_block_paddings_0_cache: R.Object, encoder_block_layers_1_block_layers_1_block_paddings_1_cache: R.Object, encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_2_block_paddings_0_cache: R.Object, encoder_block_layers_1_block_layers_2_block_paddings_1_cache: R.Object, encoder_block_layers_1_block_layers_4_cache_cache: R.Object, encoder_block_layers_1_block_layers_4_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_0_block_paddings_0_cache: R.Object, encoder_block_layers_2_block_layers_0_block_paddings_1_cache: R.Object, encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_1_block_paddings_0_cache: R.Object, encoder_block_layers_2_block_layers_1_block_paddings_1_cache: R.Object, encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_2_block_layers_2_block_paddings_0_cache: R.Object, encoder_block_layers_2_block_layers_2_block_paddings_1_cache: R.Object, encoder_block_layers_2_block_layers_4_cache_cache: R.Object, encoder_block_layers_2_block_layers_4_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_0_block_paddings_0_cache: R.Object, encoder_block_layers_3_block_layers_0_block_paddings_1_cache: R.Object, encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_1_block_paddings_0_cache: R.Object, encoder_block_layers_3_block_layers_1_block_paddings_1_cache: R.Object, encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_3_block_layers_2_block_paddings_0_cache: R.Object, encoder_block_layers_3_block_layers_2_block_paddings_1_cache: R.Object, encoder_block_layers_3_block_layers_4_cache_cache: R.Object, encoder_block_layers_3_block_layers_4_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_0_block_paddings_0_cache: R.Object, encoder_block_layers_4_block_layers_0_block_paddings_1_cache: R.Object, encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_1_block_paddings_0_cache: R.Object, encoder_block_layers_4_block_layers_1_block_paddings_1_cache: R.Object, encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, encoder_block_layers_4_block_layers_2_block_paddings_0_cache: R.Object, encoder_block_layers_4_block_layers_2_block_paddings_1_cache: R.Object, encoder_block_layers_4_block_layers_4_cache_cache: R.Object, encoder_block_layers_4_block_layers_4_downsampling_delay_cache: R.Object, encoder_block_layers_6_cache_cache: R.Object, encoder_block_layers_6_downsampling_delay_cache: R.Object, decoder_model_layers_0_cache_cache: R.Object, decoder_model_layers_0_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_1_cache_cache: R.Object, decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_2_block_paddings_0_cache: R.Object, decoder_model_layers_1_block_layers_2_block_paddings_1_cache: R.Object, decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_3_block_paddings_0_cache: R.Object, decoder_model_layers_1_block_layers_3_block_paddings_1_cache: R.Object, decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_1_block_layers_4_block_paddings_0_cache: R.Object, decoder_model_layers_1_block_layers_4_block_paddings_1_cache: R.Object, decoder_model_layers_2_block_layers_1_cache_cache: R.Object, decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_2_block_paddings_0_cache: R.Object, decoder_model_layers_2_block_layers_2_block_paddings_1_cache: R.Object, decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_3_block_paddings_0_cache: R.Object, decoder_model_layers_2_block_layers_3_block_paddings_1_cache: R.Object, decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_2_block_layers_4_block_paddings_0_cache: R.Object, decoder_model_layers_2_block_layers_4_block_paddings_1_cache: R.Object, decoder_model_layers_3_block_layers_1_cache_cache: R.Object, decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_2_block_paddings_0_cache: R.Object, decoder_model_layers_3_block_layers_2_block_paddings_1_cache: R.Object, decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_3_block_paddings_0_cache: R.Object, decoder_model_layers_3_block_layers_3_block_paddings_1_cache: R.Object, decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_3_block_layers_4_block_paddings_0_cache: R.Object, decoder_model_layers_3_block_layers_4_block_paddings_1_cache: R.Object, decoder_model_layers_4_block_layers_1_cache_cache: R.Object, decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_2_block_paddings_0_cache: R.Object, decoder_model_layers_4_block_layers_2_block_paddings_1_cache: R.Object, decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_3_block_paddings_0_cache: R.Object, decoder_model_layers_4_block_layers_3_block_paddings_1_cache: R.Object, decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_cache_cache: R.Object, decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_cache_cache: R.Object, decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache: R.Object, decoder_model_layers_4_block_layers_4_block_paddings_0_cache: R.Object, decoder_model_layers_4_block_layers_4_block_paddings_1_cache: R.Object, decoder_model_layers_6_cache_cache: R.Object, decoder_model_layers_6_downsampling_delay_cache: R.Object, encoder_block_layers_1_block_layers_0_block_branches_0_layers_0_alpha: R.Tensor((1, 64, 1), dtype="float32"), encoder_block_layers_1_block_layers_0_block_branches_0_layers_2_alpha: R.Tensor((1, 64, 1), dtype="float32"), encoder_block_layers_1_block_layers_1_block_branches_0_layers_0_alpha: R.Tensor((1, 64, 1), dtype="float32"), encoder_block_layers_1_block_layers_1_block_branches_0_layers_2_alpha: R.Tensor((1, 64, 1), dtype="float32"), encoder_block_layers_1_block_layers_2_block_branches_0_layers_0_alpha: R.Tensor((1, 64, 1), dtype="float32"), encoder_block_layers_1_block_layers_2_block_branches_0_layers_2_alpha: R.Tensor((1, 64, 1), dtype="float32"), encoder_block_layers_1_block_layers_3_alpha: R.Tensor((1, 64, 1), dtype="float32"), encoder_block_layers_2_block_layers_0_block_branches_0_layers_0_alpha: R.Tensor((1, 128, 1), dtype="float32"), encoder_block_layers_2_block_layers_0_block_branches_0_layers_2_alpha: R.Tensor((1, 128, 1), dtype="float32"), encoder_block_layers_2_block_layers_1_block_branches_0_layers_0_alpha: R.Tensor((1, 128, 1), dtype="float32"), encoder_block_layers_2_block_layers_1_block_branches_0_layers_2_alpha: R.Tensor((1, 128, 1), dtype="float32"), encoder_block_layers_2_block_layers_2_block_branches_0_layers_0_alpha: R.Tensor((1, 128, 1), dtype="float32"), encoder_block_layers_2_block_layers_2_block_branches_0_layers_2_alpha: R.Tensor((1, 128, 1), dtype="float32"), encoder_block_layers_2_block_layers_3_alpha: R.Tensor((1, 128, 1), dtype="float32"), encoder_block_layers_3_block_layers_0_block_branches_0_layers_0_alpha: R.Tensor((1, 256, 1), dtype="float32"), encoder_block_layers_3_block_layers_0_block_branches_0_layers_2_alpha: R.Tensor((1, 256, 1), dtype="float32"), encoder_block_layers_3_block_layers_1_block_branches_0_layers_0_alpha: R.Tensor((1, 256, 1), dtype="float32"), encoder_block_layers_3_block_layers_1_block_branches_0_layers_2_alpha: R.Tensor((1, 256, 1), dtype="float32"), encoder_block_layers_3_block_layers_2_block_branches_0_layers_0_alpha: R.Tensor((1, 256, 1), dtype="float32"), encoder_block_layers_3_block_layers_2_block_branches_0_layers_2_alpha: R.Tensor((1, 256, 1), dtype="float32"), encoder_block_layers_3_block_layers_3_alpha: R.Tensor((1, 256, 1), dtype="float32"), encoder_block_layers_4_block_layers_0_block_branches_0_layers_0_alpha: R.Tensor((1, 512, 1), dtype="float32"), encoder_block_layers_4_block_layers_0_block_branches_0_layers_2_alpha: R.Tensor((1, 512, 1), dtype="float32"), encoder_block_layers_4_block_layers_1_block_branches_0_layers_0_alpha: R.Tensor((1, 512, 1), dtype="float32"), encoder_block_layers_4_block_layers_1_block_branches_0_layers_2_alpha: R.Tensor((1, 512, 1), dtype="float32"), encoder_block_layers_4_block_layers_2_block_branches_0_layers_0_alpha: R.Tensor((1, 512, 1), dtype="float32"), encoder_block_layers_4_block_layers_2_block_branches_0_layers_2_alpha: R.Tensor((1, 512, 1), dtype="float32"), encoder_block_layers_4_block_layers_3_alpha: R.Tensor((1, 512, 1), dtype="float32"), encoder_block_layers_5_alpha: R.Tensor((1, 1024, 1), dtype="float32"), quantizer_quantizers_0_codebook_weight: R.Tensor((1024, 8), dtype="float32"), quantizer_quantizers_1_codebook_weight: R.Tensor((1024, 8), dtype="float32"), quantizer_quantizers_2_codebook_weight: R.Tensor((1024, 8), dtype="float32"), quantizer_quantizers_3_codebook_weight: R.Tensor((1024, 8), dtype="float32"), quantizer_quantizers_4_codebook_weight: R.Tensor((1024, 8), dtype="float32"), quantizer_quantizers_5_codebook_weight: R.Tensor((1024, 8), dtype="float32"), quantizer_quantizers_6_codebook_weight: R.Tensor((1024, 8), dtype="float32"), quantizer_quantizers_7_codebook_weight: R.Tensor((1024, 8), dtype="float32"), quantizer_quantizers_8_codebook_weight: R.Tensor((1024, 8), dtype="float32"), lv120: R.Tensor((64, 1, 7), dtype="float32"), lv8: R.Tensor((1, 64, 1), dtype="float32"), lv124: R.Tensor((64, 64, 7), dtype="float32"), lv18: R.Tensor((1, 64, 1), dtype="float32"), lv128: R.Tensor((64, 64, 1), dtype="float32"), lv27: R.Tensor((1, 64, 1), dtype="float32"), lv132: R.Tensor((64, 64, 7), dtype="float32"), lv38: R.Tensor((1, 64, 1), dtype="float32"), lv136: R.Tensor((64, 64, 1), dtype="float32"), lv47: R.Tensor((1, 64, 1), dtype="float32"), lv140: R.Tensor((64, 64, 7), dtype="float32"), lv58: R.Tensor((1, 64, 1), dtype="float32"), lv144: R.Tensor((64, 64, 1), dtype="float32"), lv67: R.Tensor((1, 64, 1), dtype="float32"), lv148: R.Tensor((128, 64, 4), dtype="float32"), lv77: R.Tensor((1, 128, 1), dtype="float32"), lv152: R.Tensor((128, 128, 7), dtype="float32"), lv87: R.Tensor((1, 128, 1), dtype="float32"), lv156: R.Tensor((128, 128, 1), dtype="float32"), lv96: R.Tensor((1, 128, 1), dtype="float32"), lv160: R.Tensor((128, 128, 7), dtype="float32"), lv107: R.Tensor((1, 128, 1), dtype="float32"), lv164: R.Tensor((128, 128, 1), dtype="float32"), lv116: R.Tensor((1, 128, 1), dtype="float32"), lv168: R.Tensor((128, 128, 7), dtype="float32"), lv127: R.Tensor((1, 128, 1), dtype="float32"), lv172: R.Tensor((128, 128, 1), dtype="float32"), lv136_1: R.Tensor((1, 128, 1), dtype="float32"), lv176: R.Tensor((256, 128, 8), dtype="float32"), lv146: R.Tensor((1, 256, 1), dtype="float32"), lv180: R.Tensor((256, 256, 7), dtype="float32"), lv156_1: R.Tensor((1, 256, 1), dtype="float32"), lv184: R.Tensor((256, 256, 1), dtype="float32"), lv165: R.Tensor((1, 256, 1), dtype="float32"), lv188: R.Tensor((256, 256, 7), dtype="float32"), lv176_1: R.Tensor((1, 256, 1), dtype="float32"), lv192: R.Tensor((256, 256, 1), dtype="float32"), lv185: R.Tensor((1, 256, 1), dtype="float32"), lv196: R.Tensor((256, 256, 7), dtype="float32"), lv196_1: R.Tensor((1, 256, 1), dtype="float32"), lv200: R.Tensor((256, 256, 1), dtype="float32"), lv205: R.Tensor((1, 256, 1), dtype="float32"), lv204: R.Tensor((512, 256, 16), dtype="float32"), lv215: R.Tensor((1, 512, 1), dtype="float32"), lv208: R.Tensor((512, 512, 7), dtype="float32"), lv225: R.Tensor((1, 512, 1), dtype="float32"), lv212: R.Tensor((512, 512, 1), dtype="float32"), lv234: R.Tensor((1, 512, 1), dtype="float32"), lv216: R.Tensor((512, 512, 7), dtype="float32"), lv245: R.Tensor((1, 512, 1), dtype="float32"), lv220: R.Tensor((512, 512, 1), dtype="float32"), lv254: R.Tensor((1, 512, 1), dtype="float32"), lv224: R.Tensor((512, 512, 7), dtype="float32"), lv265: R.Tensor((1, 512, 1), dtype="float32"), lv228: R.Tensor((512, 512, 1), dtype="float32"), lv274: R.Tensor((1, 512, 1), dtype="float32"), lv232: R.Tensor((1024, 512, 16), dtype="float32"), lv284: R.Tensor((1, 1024, 1), dtype="float32"), lv236: R.Tensor((1024, 1024, 3), dtype="float32"), lv293: R.Tensor((1, 1024, 1), dtype="float32"), lv239: R.Tensor((8, 1024, 1), dtype="float32"), lv299: R.Tensor((1, 8, 1), dtype="float32"), permute_dims1: R.Tensor((8, 1024), dtype="float32"), permute_dims2: R.Tensor((1, 1024), dtype="float32"), lv251: R.Tensor((1024, 8, 1), dtype="float32"), lv305: R.Tensor((1, 1024, 1), dtype="float32"), lv254_1: R.Tensor((8, 1024, 1), dtype="float32"), lv311: R.Tensor((1, 8, 1), dtype="float32"), permute_dims5: R.Tensor((8, 1024), dtype="float32"), permute_dims6: R.Tensor((1, 1024), dtype="float32"), lv266: R.Tensor((1024, 8, 1), dtype="float32"), lv317: R.Tensor((1, 1024, 1), dtype="float32"), lv269: R.Tensor((8, 1024, 1), dtype="float32"), lv323: R.Tensor((1, 8, 1), dtype="float32"), permute_dims9: R.Tensor((8, 1024), dtype="float32"), permute_dims10: R.Tensor((1, 1024), dtype="float32"), lv281: R.Tensor((1024, 8, 1), dtype="float32"), lv329: R.Tensor((1, 1024, 1), dtype="float32"), lv284_1: R.Tensor((8, 1024, 1), dtype="float32"), lv335: R.Tensor((1, 8, 1), dtype="float32"), permute_dims13: R.Tensor((8, 1024), dtype="float32"), permute_dims14: R.Tensor((1, 1024), dtype="float32"), lv296: R.Tensor((1024, 8, 1), dtype="float32"), lv341: R.Tensor((1, 1024, 1), dtype="float32"), lv299_1: R.Tensor((8, 1024, 1), dtype="float32"), lv347: R.Tensor((1, 8, 1), dtype="float32"), permute_dims17: R.Tensor((8, 1024), dtype="float32"), permute_dims18: R.Tensor((1, 1024), dtype="float32"), lv311_1: R.Tensor((1024, 8, 1), dtype="float32"), lv353: R.Tensor((1, 1024, 1), dtype="float32"), lv314: R.Tensor((8, 1024, 1), dtype="float32"), lv359: R.Tensor((1, 8, 1), dtype="float32"), permute_dims21: R.Tensor((8, 1024), dtype="float32"), permute_dims22: R.Tensor((1, 1024), dtype="float32"), lv326: R.Tensor((1024, 8, 1), dtype="float32"), lv365: R.Tensor((1, 1024, 1), dtype="float32"), lv329_1: R.Tensor((8, 1024, 1), dtype="float32"), lv371: R.Tensor((1, 8, 1), dtype="float32"), permute_dims25: R.Tensor((8, 1024), dtype="float32"), permute_dims26: R.Tensor((1, 1024), dtype="float32"), lv341_1: R.Tensor((1024, 8, 1), dtype="float32"), lv377: R.Tensor((1, 1024, 1), dtype="float32"), lv344: R.Tensor((8, 1024, 1), dtype="float32"), lv383: R.Tensor((1, 8, 1), dtype="float32"), permute_dims29: R.Tensor((8, 1024), dtype="float32"), permute_dims30: R.Tensor((1, 1024), dtype="float32"), lv356: R.Tensor((1024, 8, 1), dtype="float32"), lv389: R.Tensor((1, 1024, 1), dtype="float32"), lv359_1: R.Tensor((8, 1024, 1), dtype="float32"), lv395: R.Tensor((1, 8, 1), dtype="float32"), permute_dims33: R.Tensor((8, 1024), dtype="float32"), permute_dims34: R.Tensor((1, 1024), dtype="float32"), lv371_1: R.Tensor((1024, 8, 1), dtype="float32"), lv401: R.Tensor((1, 1024, 1), dtype="float32")) -> R.Tuple(R.Tuple(R.Tensor((1, 1024, 1), dtype="float32"), R.Tuple(R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"))), R.Tuple(R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object)):
        R.func_attr({"num_input": 166})
        cls = Module
        with R.dataflow():
            lv1: R.Tensor((1, 1, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_0_downsampling_delay_cache, audio_data, sinfo_args=(R.Tensor((1, 1, 512), dtype="float32"),))
            lv2: R.Tensor((1, 1, 518), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_0_cache_cache, lv1, sinfo_args=(R.Tensor((1, 1, 518), dtype="float32"),))
            lv121 = R.call_tir(cls.fused_conv1d18_add181, (lv2, lv120, lv8), out_sinfo=R.Tensor((1, 64, 512), dtype="float32"))
            lv9: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_0_block_paddings_0_cache, lv121, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv122 = R.call_tir(cls.fused_reshape12_snake_reshape121, (lv9, encoder_block_layers_1_block_layers_0_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 64, 512), dtype="float32"))
            lv11: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, lv122, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv12: R.Tensor((1, 64, 518), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_cache_cache, lv11, sinfo_args=(R.Tensor((1, 64, 518), dtype="float32"),))
            lv125 = R.call_tir(cls.fused_conv1d19_add181, (lv12, lv124, lv18), out_sinfo=R.Tensor((1, 64, 512), dtype="float32"))
            lv126 = R.call_tir(cls.fused_reshape12_snake_reshape121, (lv125, encoder_block_layers_1_block_layers_0_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 64, 512), dtype="float32"))
            lv20: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, lv126, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv21: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_cache_cache, lv20, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv28: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_0_block_paddings_1_cache, lv121, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv129 = R.call_tir(cls.fused_conv1d20_add18_add19_add201, (lv21, lv128, lv27, lv28), out_sinfo=R.Tensor((1, 64, 512), dtype="float32"))
            lv29: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_1_block_paddings_0_cache, lv129, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv130 = R.call_tir(cls.fused_reshape12_snake_reshape121, (lv29, encoder_block_layers_1_block_layers_1_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 64, 512), dtype="float32"))
            lv31: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, lv130, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv32: R.Tensor((1, 64, 530), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_cache_cache, lv31, sinfo_args=(R.Tensor((1, 64, 530), dtype="float32"),))
            lv133 = R.call_tir(cls.fused_conv1d21_add181, (lv32, lv132, lv38), out_sinfo=R.Tensor((1, 64, 512), dtype="float32"))
            lv134 = R.call_tir(cls.fused_reshape12_snake_reshape121, (lv133, encoder_block_layers_1_block_layers_1_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 64, 512), dtype="float32"))
            lv40: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, lv134, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv41: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_cache_cache, lv40, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv48: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_1_block_paddings_1_cache, lv129, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv137 = R.call_tir(cls.fused_conv1d20_add18_add19_add201, (lv41, lv136, lv47, lv48), out_sinfo=R.Tensor((1, 64, 512), dtype="float32"))
            lv49: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_2_block_paddings_0_cache, lv137, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv138 = R.call_tir(cls.fused_reshape12_snake_reshape121, (lv49, encoder_block_layers_1_block_layers_2_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 64, 512), dtype="float32"))
            lv51: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, lv138, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv52: R.Tensor((1, 64, 566), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache, lv51, sinfo_args=(R.Tensor((1, 64, 566), dtype="float32"),))
            lv141 = R.call_tir(cls.fused_conv1d22_add181, (lv52, lv140, lv58), out_sinfo=R.Tensor((1, 64, 512), dtype="float32"))
            lv142 = R.call_tir(cls.fused_reshape12_snake_reshape121, (lv141, encoder_block_layers_1_block_layers_2_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 64, 512), dtype="float32"))
            lv60: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, lv142, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv61: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache, lv60, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv68: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_2_block_paddings_1_cache, lv137, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv145 = R.call_tir(cls.fused_conv1d20_add18_add19_add201, (lv61, lv144, lv67, lv68), out_sinfo=R.Tensor((1, 64, 512), dtype="float32"))
            lv146_1 = R.call_tir(cls.fused_reshape12_snake_reshape121, (lv145, encoder_block_layers_1_block_layers_3_alpha), out_sinfo=R.Tensor((1, 64, 512), dtype="float32"))
            lv70: R.Tensor((1, 64, 512), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_4_downsampling_delay_cache, lv146_1, sinfo_args=(R.Tensor((1, 64, 512), dtype="float32"),))
            lv71: R.Tensor((1, 64, 514), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_1_block_layers_4_cache_cache, lv70, sinfo_args=(R.Tensor((1, 64, 514), dtype="float32"),))
            lv149 = R.call_tir(cls.fused_conv1d23_add211, (lv71, lv148, lv77), out_sinfo=R.Tensor((1, 128, 256), dtype="float32"))
            lv78: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_0_block_paddings_0_cache, lv149, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv150 = R.call_tir(cls.fused_reshape14_snake1_reshape141, (lv78, encoder_block_layers_2_block_layers_0_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 128, 256), dtype="float32"))
            lv80: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, lv150, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv81: R.Tensor((1, 128, 262), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_cache_cache, lv80, sinfo_args=(R.Tensor((1, 128, 262), dtype="float32"),))
            lv153 = R.call_tir(cls.fused_conv1d24_add211, (lv81, lv152, lv87), out_sinfo=R.Tensor((1, 128, 256), dtype="float32"))
            lv154 = R.call_tir(cls.fused_reshape14_snake1_reshape141, (lv153, encoder_block_layers_2_block_layers_0_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 128, 256), dtype="float32"))
            lv89: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, lv154, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv90: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_cache_cache, lv89, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv97: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_0_block_paddings_1_cache, lv149, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv157 = R.call_tir(cls.fused_conv1d25_add21_add22_add231, (lv90, lv156, lv96, lv97), out_sinfo=R.Tensor((1, 128, 256), dtype="float32"))
            lv98: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_1_block_paddings_0_cache, lv157, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv158 = R.call_tir(cls.fused_reshape14_snake1_reshape141, (lv98, encoder_block_layers_2_block_layers_1_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 128, 256), dtype="float32"))
            lv100: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, lv158, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv101: R.Tensor((1, 128, 274), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_cache_cache, lv100, sinfo_args=(R.Tensor((1, 128, 274), dtype="float32"),))
            lv161 = R.call_tir(cls.fused_conv1d26_add211, (lv101, lv160, lv107), out_sinfo=R.Tensor((1, 128, 256), dtype="float32"))
            lv162 = R.call_tir(cls.fused_reshape14_snake1_reshape141, (lv161, encoder_block_layers_2_block_layers_1_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 128, 256), dtype="float32"))
            lv109: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, lv162, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv110: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_cache_cache, lv109, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv117: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_1_block_paddings_1_cache, lv157, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv165_1 = R.call_tir(cls.fused_conv1d25_add21_add22_add231, (lv110, lv164, lv116, lv117), out_sinfo=R.Tensor((1, 128, 256), dtype="float32"))
            lv118: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_2_block_paddings_0_cache, lv165_1, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv166 = R.call_tir(cls.fused_reshape14_snake1_reshape141, (lv118, encoder_block_layers_2_block_layers_2_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 128, 256), dtype="float32"))
            lv120_1: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, lv166, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv121_1: R.Tensor((1, 128, 310), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache, lv120_1, sinfo_args=(R.Tensor((1, 128, 310), dtype="float32"),))
            lv169 = R.call_tir(cls.fused_conv1d27_add211, (lv121_1, lv168, lv127), out_sinfo=R.Tensor((1, 128, 256), dtype="float32"))
            lv170 = R.call_tir(cls.fused_reshape14_snake1_reshape141, (lv169, encoder_block_layers_2_block_layers_2_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 128, 256), dtype="float32"))
            lv129_1: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, lv170, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv130_1: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache, lv129_1, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv137_1: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_2_block_paddings_1_cache, lv165_1, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv173 = R.call_tir(cls.fused_conv1d25_add21_add22_add231, (lv130_1, lv172, lv136_1, lv137_1), out_sinfo=R.Tensor((1, 128, 256), dtype="float32"))
            lv174 = R.call_tir(cls.fused_reshape14_snake1_reshape141, (lv173, encoder_block_layers_2_block_layers_3_alpha), out_sinfo=R.Tensor((1, 128, 256), dtype="float32"))
            lv139: R.Tensor((1, 128, 256), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_4_downsampling_delay_cache, lv174, sinfo_args=(R.Tensor((1, 128, 256), dtype="float32"),))
            lv140_1: R.Tensor((1, 128, 260), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_2_block_layers_4_cache_cache, lv139, sinfo_args=(R.Tensor((1, 128, 260), dtype="float32"),))
            lv177 = R.call_tir(cls.fused_conv1d28_add241, (lv140_1, lv176, lv146), out_sinfo=R.Tensor((1, 256, 64), dtype="float32"))
            lv147: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_0_block_paddings_0_cache, lv177, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv178 = R.call_tir(cls.fused_reshape16_snake2_reshape161, (lv147, encoder_block_layers_3_block_layers_0_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 256, 64), dtype="float32"))
            lv149_1: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, lv178, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv150_1: R.Tensor((1, 256, 70), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_cache_cache, lv149_1, sinfo_args=(R.Tensor((1, 256, 70), dtype="float32"),))
            lv181 = R.call_tir(cls.fused_conv1d29_add241, (lv150_1, lv180, lv156_1), out_sinfo=R.Tensor((1, 256, 64), dtype="float32"))
            lv182 = R.call_tir(cls.fused_reshape16_snake2_reshape161, (lv181, encoder_block_layers_3_block_layers_0_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 256, 64), dtype="float32"))
            lv158_1: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, lv182, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv159: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_cache_cache, lv158_1, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv166_1: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_0_block_paddings_1_cache, lv177, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv185_1 = R.call_tir(cls.fused_conv1d30_add24_add25_add261, (lv159, lv184, lv165, lv166_1), out_sinfo=R.Tensor((1, 256, 64), dtype="float32"))
            lv167: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_1_block_paddings_0_cache, lv185_1, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv186 = R.call_tir(cls.fused_reshape16_snake2_reshape161, (lv167, encoder_block_layers_3_block_layers_1_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 256, 64), dtype="float32"))
            lv169_1: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, lv186, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv170_1: R.Tensor((1, 256, 82), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_cache_cache, lv169_1, sinfo_args=(R.Tensor((1, 256, 82), dtype="float32"),))
            lv189 = R.call_tir(cls.fused_conv1d31_add241, (lv170_1, lv188, lv176_1), out_sinfo=R.Tensor((1, 256, 64), dtype="float32"))
            lv190 = R.call_tir(cls.fused_reshape16_snake2_reshape161, (lv189, encoder_block_layers_3_block_layers_1_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 256, 64), dtype="float32"))
            lv178_1: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, lv190, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv179: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_cache_cache, lv178_1, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv186_1: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_1_block_paddings_1_cache, lv185_1, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv193 = R.call_tir(cls.fused_conv1d30_add24_add25_add261, (lv179, lv192, lv185, lv186_1), out_sinfo=R.Tensor((1, 256, 64), dtype="float32"))
            lv187: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_2_block_paddings_0_cache, lv193, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv194 = R.call_tir(cls.fused_reshape16_snake2_reshape161, (lv187, encoder_block_layers_3_block_layers_2_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 256, 64), dtype="float32"))
            lv189_1: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, lv194, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv190_1: R.Tensor((1, 256, 118), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache, lv189_1, sinfo_args=(R.Tensor((1, 256, 118), dtype="float32"),))
            lv197 = R.call_tir(cls.fused_conv1d32_add241, (lv190_1, lv196, lv196_1), out_sinfo=R.Tensor((1, 256, 64), dtype="float32"))
            lv198 = R.call_tir(cls.fused_reshape16_snake2_reshape161, (lv197, encoder_block_layers_3_block_layers_2_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 256, 64), dtype="float32"))
            lv198_1: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, lv198, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv199: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache, lv198_1, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv206: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_2_block_paddings_1_cache, lv193, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv201 = R.call_tir(cls.fused_conv1d30_add24_add25_add261, (lv199, lv200, lv205, lv206), out_sinfo=R.Tensor((1, 256, 64), dtype="float32"))
            lv202 = R.call_tir(cls.fused_reshape16_snake2_reshape161, (lv201, encoder_block_layers_3_block_layers_3_alpha), out_sinfo=R.Tensor((1, 256, 64), dtype="float32"))
            lv208_1: R.Tensor((1, 256, 64), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_4_downsampling_delay_cache, lv202, sinfo_args=(R.Tensor((1, 256, 64), dtype="float32"),))
            lv209: R.Tensor((1, 256, 72), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_3_block_layers_4_cache_cache, lv208_1, sinfo_args=(R.Tensor((1, 256, 72), dtype="float32"),))
            lv205_1 = R.call_tir(cls.fused_conv1d33_add271, (lv209, lv204, lv215), out_sinfo=R.Tensor((1, 512, 8), dtype="float32"))
            lv216_1: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_0_block_paddings_0_cache, lv205_1, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv206_1 = R.call_tir(cls.fused_reshape18_snake3_reshape181, (lv216_1, encoder_block_layers_4_block_layers_0_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 512, 8), dtype="float32"))
            lv218: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, lv206_1, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv219: R.Tensor((1, 512, 14), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_cache_cache, lv218, sinfo_args=(R.Tensor((1, 512, 14), dtype="float32"),))
            lv209_1 = R.call_tir(cls.fused_conv1d34_add271, (lv219, lv208, lv225), out_sinfo=R.Tensor((1, 512, 8), dtype="float32"))
            lv210 = R.call_tir(cls.fused_reshape18_snake3_reshape181, (lv209_1, encoder_block_layers_4_block_layers_0_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 512, 8), dtype="float32"))
            lv227: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, lv210, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv228_1: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_cache_cache, lv227, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv235: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_0_block_paddings_1_cache, lv205_1, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv213 = R.call_tir(cls.fused_conv1d35_add27_add28_add291, (lv228_1, lv212, lv234, lv235), out_sinfo=R.Tensor((1, 512, 8), dtype="float32"))
            lv236_1: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_1_block_paddings_0_cache, lv213, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv214 = R.call_tir(cls.fused_reshape18_snake3_reshape181, (lv236_1, encoder_block_layers_4_block_layers_1_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 512, 8), dtype="float32"))
            lv238: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, lv214, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv239_1: R.Tensor((1, 512, 26), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_cache_cache, lv238, sinfo_args=(R.Tensor((1, 512, 26), dtype="float32"),))
            lv217 = R.call_tir(cls.fused_conv1d36_add271, (lv239_1, lv216, lv245), out_sinfo=R.Tensor((1, 512, 8), dtype="float32"))
            lv218_1 = R.call_tir(cls.fused_reshape18_snake3_reshape181, (lv217, encoder_block_layers_4_block_layers_1_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 512, 8), dtype="float32"))
            lv247: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, lv218_1, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv248: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_cache_cache, lv247, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv255: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_1_block_paddings_1_cache, lv213, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv221 = R.call_tir(cls.fused_conv1d35_add27_add28_add291, (lv248, lv220, lv254, lv255), out_sinfo=R.Tensor((1, 512, 8), dtype="float32"))
            lv256: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_2_block_paddings_0_cache, lv221, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv222 = R.call_tir(cls.fused_reshape18_snake3_reshape181, (lv256, encoder_block_layers_4_block_layers_2_block_branches_0_layers_0_alpha), out_sinfo=R.Tensor((1, 512, 8), dtype="float32"))
            lv258: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, lv222, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv259: R.Tensor((1, 512, 62), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache, lv258, sinfo_args=(R.Tensor((1, 512, 62), dtype="float32"),))
            lv225_1 = R.call_tir(cls.fused_conv1d37_add271, (lv259, lv224, lv265), out_sinfo=R.Tensor((1, 512, 8), dtype="float32"))
            lv226 = R.call_tir(cls.fused_reshape18_snake3_reshape181, (lv225_1, encoder_block_layers_4_block_layers_2_block_branches_0_layers_2_alpha), out_sinfo=R.Tensor((1, 512, 8), dtype="float32"))
            lv267: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, lv226, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv268: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache, lv267, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv275: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_2_block_paddings_1_cache, lv221, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv229 = R.call_tir(cls.fused_conv1d35_add27_add28_add291, (lv268, lv228, lv274, lv275), out_sinfo=R.Tensor((1, 512, 8), dtype="float32"))
            lv230 = R.call_tir(cls.fused_reshape18_snake3_reshape181, (lv229, encoder_block_layers_4_block_layers_3_alpha), out_sinfo=R.Tensor((1, 512, 8), dtype="float32"))
            lv277: R.Tensor((1, 512, 8), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_4_downsampling_delay_cache, lv230, sinfo_args=(R.Tensor((1, 512, 8), dtype="float32"),))
            lv278: R.Tensor((1, 512, 16), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_4_block_layers_4_cache_cache, lv277, sinfo_args=(R.Tensor((1, 512, 16), dtype="float32"),))
            lv233 = R.call_tir(cls.fused_conv1d38_add301, (lv278, lv232, lv284), out_sinfo=R.Tensor((1, 1024, 1), dtype="float32"))
            lv234_1 = R.call_tir(cls.fused_reshape20_snake4_reshape201, (lv233, encoder_block_layers_5_alpha), out_sinfo=R.Tensor((1, 1024, 1), dtype="float32"))
            lv286: R.Tensor((1, 1024, 1), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_6_downsampling_delay_cache, lv234_1, sinfo_args=(R.Tensor((1, 1024, 1), dtype="float32"),))
            lv287: R.Tensor((1, 1024, 3), dtype="float32") = R.call_pure_packed("vm.builtin.cached_padding_1d_update", encoder_block_layers_6_cache_cache, lv286, sinfo_args=(R.Tensor((1, 1024, 3), dtype="float32"),))
            lv237 = R.call_tir(cls.fused_conv1d39_add301, (lv287, lv236, lv293), out_sinfo=R.Tensor((1, 1024, 1), dtype="float32"))
            lv240 = R.call_tir(cls.fused_conv1d40_add311, (lv237, lv239, lv299), out_sinfo=R.Tensor((1, 8, 1), dtype="float32"))
            lv241 = R.call_tir(cls.fused_transpose_reshape221, (lv240,), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv242 = R.call_tir(cls.fused_tir_square29_sum291, (lv241,), out_sinfo=R.Tensor((1, 1), dtype="float32"))
            lv243 = R.call_tir(cls.fused_broadcast_to_maximum_tir_sqrt12_divide291, (lv242, lv241), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv246 = R.call_tir(cls.fused_tir_square29_sum291, (lv243,), out_sinfo=R.Tensor((1, 1), dtype="float32"))
            lv248_1 = R.call_tir(cls.fused_matmul_multiply29_subtract_add321, (lv243, permute_dims1, lv246, permute_dims2), out_sinfo=R.Tensor((1, 1024), dtype="float32"))
            topk1: R.Tensor((1, 1), dtype="int32") = R.topk(lv248_1, k=1, axis=1, ret_type="indices", largest=True, dtype="int32")
            reshape60 = R.call_tir(cls.reshape241, (topk1,), out_sinfo=R.Tensor((1,), dtype="int32"))
            take1 = R.call_tir(cls.take11, (quantizer_quantizers_0_codebook_weight, reshape60), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv249 = R.call_tir(cls.fused_reshape25_transpose31, (take1,), out_sinfo=R.Tensor((1, 8, 1), dtype="float32"))
            lv252 = R.call_tir(cls.fused_conv1d41_add301, (lv249, lv251, lv305), out_sinfo=R.Tensor((1, 1024, 1), dtype="float32"))
            subtract1 = R.call_tir(cls.subtract11, (lv237, lv252), out_sinfo=R.Tensor((1, 1024, 1), dtype="float32"))
            lv255_1 = R.call_tir(cls.fused_conv1d40_add311, (subtract1, lv254_1, lv311), out_sinfo=R.Tensor((1, 8, 1), dtype="float32"))
            lv256_1 = R.call_tir(cls.fused_transpose_reshape221, (lv255_1,), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv257 = R.call_tir(cls.fused_tir_square29_sum291, (lv256_1,), out_sinfo=R.Tensor((1, 1), dtype="float32"))
            lv258_1 = R.call_tir(cls.fused_broadcast_to_maximum_tir_sqrt12_divide291, (lv257, lv256_1), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv261 = R.call_tir(cls.fused_tir_square29_sum291, (lv258_1,), out_sinfo=R.Tensor((1, 1), dtype="float32"))
            lv263 = R.call_tir(cls.fused_matmul_multiply29_subtract_add321, (lv258_1, permute_dims5, lv261, permute_dims6), out_sinfo=R.Tensor((1, 1024), dtype="float32"))
            topk2: R.Tensor((1, 1), dtype="int32") = R.topk(lv263, k=1, axis=1, ret_type="indices", largest=True, dtype="int32")
            reshape64 = R.call_tir(cls.reshape241, (topk2,), out_sinfo=R.Tensor((1,), dtype="int32"))
            take3 = R.call_tir(cls.take11, (quantizer_quantizers_1_codebook_weight, reshape64), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv264 = R.call_tir(cls.fused_reshape25_transpose31, (take3,), out_sinfo=R.Tensor((1, 8, 1), dtype="float32"))
            lv267_1 = R.call_tir(cls.fused_conv1d41_add301, (lv264, lv266, lv317), out_sinfo=R.Tensor((1, 1024, 1), dtype="float32"))
            subtract3 = R.call_tir(cls.subtract11, (subtract1, lv267_1), out_sinfo=R.Tensor((1, 1024, 1), dtype="float32"))
            lv270 = R.call_tir(cls.fused_conv1d40_add311, (subtract3, lv269, lv323), out_sinfo=R.Tensor((1, 8, 1), dtype="float32"))
            lv271 = R.call_tir(cls.fused_transpose_reshape221, (lv270,), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv272 = R.call_tir(cls.fused_tir_square29_sum291, (lv271,), out_sinfo=R.Tensor((1, 1), dtype="float32"))
            lv273 = R.call_tir(cls.fused_broadcast_to_maximum_tir_sqrt12_divide291, (lv272, lv271), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv276 = R.call_tir(cls.fused_tir_square29_sum291, (lv273,), out_sinfo=R.Tensor((1, 1), dtype="float32"))
            lv278_1 = R.call_tir(cls.fused_matmul_multiply29_subtract_add321, (lv273, permute_dims9, lv276, permute_dims10), out_sinfo=R.Tensor((1, 1024), dtype="float32"))
            topk3: R.Tensor((1, 1), dtype="int32") = R.topk(lv278_1, k=1, axis=1, ret_type="indices", largest=True, dtype="int32")
            reshape68 = R.call_tir(cls.reshape241, (topk3,), out_sinfo=R.Tensor((1,), dtype="int32"))
            take5 = R.call_tir(cls.take11, (quantizer_quantizers_2_codebook_weight, reshape68), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv279 = R.call_tir(cls.fused_reshape25_transpose31, (take5,), out_sinfo=R.Tensor((1, 8, 1), dtype="float32"))
            lv282 = R.call_tir(cls.fused_conv1d41_add301, (lv279, lv281, lv329), out_sinfo=R.Tensor((1, 1024, 1), dtype="float32"))
            subtract5 = R.call_tir(cls.subtract11, (subtract3, lv282), out_sinfo=R.Tensor((1, 1024, 1), dtype="float32"))
            lv285 = R.call_tir(cls.fused_conv1d40_add311, (subtract5, lv284_1, lv335), out_sinfo=R.Tensor((1, 8, 1), dtype="float32"))
            lv286_1 = R.call_tir(cls.fused_transpose_reshape221, (lv285,), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv287_1 = R.call_tir(cls.fused_tir_square29_sum291, (lv286_1,), out_sinfo=R.Tensor((1, 1), dtype="float32"))
            lv288 = R.call_tir(cls.fused_broadcast_to_maximum_tir_sqrt12_divide291, (lv287_1, lv286_1), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv291 = R.call_tir(cls.fused_tir_square29_sum291, (lv288,), out_sinfo=R.Tensor((1, 1), dtype="float32"))
            lv293_1 = R.call_tir(cls.fused_matmul_multiply29_subtract_add321, (lv288, permute_dims13, lv291, permute_dims14), out_sinfo=R.Tensor((1, 1024), dtype="float32"))
            topk4: R.Tensor((1, 1), dtype="int32") = R.topk(lv293_1, k=1, axis=1, ret_type="indices", largest=True, dtype="int32")
            reshape72 = R.call_tir(cls.reshape241, (topk4,), out_sinfo=R.Tensor((1,), dtype="int32"))
            take7 = R.call_tir(cls.take11, (quantizer_quantizers_3_codebook_weight, reshape72), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv294 = R.call_tir(cls.fused_reshape25_transpose31, (take7,), out_sinfo=R.Tensor((1, 8, 1), dtype="float32"))
            lv297 = R.call_tir(cls.fused_conv1d41_add301, (lv294, lv296, lv341), out_sinfo=R.Tensor((1, 1024, 1), dtype="float32"))
            subtract7 = R.call_tir(cls.subtract11, (subtract5, lv297), out_sinfo=R.Tensor((1, 1024, 1), dtype="float32"))
            lv300 = R.call_tir(cls.fused_conv1d40_add311, (subtract7, lv299_1, lv347), out_sinfo=R.Tensor((1, 8, 1), dtype="float32"))
            lv301 = R.call_tir(cls.fused_transpose_reshape221, (lv300,), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv302 = R.call_tir(cls.fused_tir_square29_sum291, (lv301,), out_sinfo=R.Tensor((1, 1), dtype="float32"))
            lv303 = R.call_tir(cls.fused_broadcast_to_maximum_tir_sqrt12_divide291, (lv302, lv301), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv306 = R.call_tir(cls.fused_tir_square29_sum291, (lv303,), out_sinfo=R.Tensor((1, 1), dtype="float32"))
            lv308 = R.call_tir(cls.fused_matmul_multiply29_subtract_add321, (lv303, permute_dims17, lv306, permute_dims18), out_sinfo=R.Tensor((1, 1024), dtype="float32"))
            topk5: R.Tensor((1, 1), dtype="int32") = R.topk(lv308, k=1, axis=1, ret_type="indices", largest=True, dtype="int32")
            reshape76 = R.call_tir(cls.reshape241, (topk5,), out_sinfo=R.Tensor((1,), dtype="int32"))
            take9 = R.call_tir(cls.take11, (quantizer_quantizers_4_codebook_weight, reshape76), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv309 = R.call_tir(cls.fused_reshape25_transpose31, (take9,), out_sinfo=R.Tensor((1, 8, 1), dtype="float32"))
            lv312 = R.call_tir(cls.fused_conv1d41_add301, (lv309, lv311_1, lv353), out_sinfo=R.Tensor((1, 1024, 1), dtype="float32"))
            subtract9 = R.call_tir(cls.subtract11, (subtract7, lv312), out_sinfo=R.Tensor((1, 1024, 1), dtype="float32"))
            lv315 = R.call_tir(cls.fused_conv1d40_add311, (subtract9, lv314, lv359), out_sinfo=R.Tensor((1, 8, 1), dtype="float32"))
            lv316 = R.call_tir(cls.fused_transpose_reshape221, (lv315,), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv317_1 = R.call_tir(cls.fused_tir_square29_sum291, (lv316,), out_sinfo=R.Tensor((1, 1), dtype="float32"))
            lv318 = R.call_tir(cls.fused_broadcast_to_maximum_tir_sqrt12_divide291, (lv317_1, lv316), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv321 = R.call_tir(cls.fused_tir_square29_sum291, (lv318,), out_sinfo=R.Tensor((1, 1), dtype="float32"))
            lv323_1 = R.call_tir(cls.fused_matmul_multiply29_subtract_add321, (lv318, permute_dims21, lv321, permute_dims22), out_sinfo=R.Tensor((1, 1024), dtype="float32"))
            topk6: R.Tensor((1, 1), dtype="int32") = R.topk(lv323_1, k=1, axis=1, ret_type="indices", largest=True, dtype="int32")
            reshape80 = R.call_tir(cls.reshape241, (topk6,), out_sinfo=R.Tensor((1,), dtype="int32"))
            take11 = R.call_tir(cls.take11, (quantizer_quantizers_5_codebook_weight, reshape80), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv324 = R.call_tir(cls.fused_reshape25_transpose31, (take11,), out_sinfo=R.Tensor((1, 8, 1), dtype="float32"))
            lv327 = R.call_tir(cls.fused_conv1d41_add301, (lv324, lv326, lv365), out_sinfo=R.Tensor((1, 1024, 1), dtype="float32"))
            subtract11 = R.call_tir(cls.subtract11, (subtract9, lv327), out_sinfo=R.Tensor((1, 1024, 1), dtype="float32"))
            lv330 = R.call_tir(cls.fused_conv1d40_add311, (subtract11, lv329_1, lv371), out_sinfo=R.Tensor((1, 8, 1), dtype="float32"))
            lv331 = R.call_tir(cls.fused_transpose_reshape221, (lv330,), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv332 = R.call_tir(cls.fused_tir_square29_sum291, (lv331,), out_sinfo=R.Tensor((1, 1), dtype="float32"))
            lv333 = R.call_tir(cls.fused_broadcast_to_maximum_tir_sqrt12_divide291, (lv332, lv331), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv336 = R.call_tir(cls.fused_tir_square29_sum291, (lv333,), out_sinfo=R.Tensor((1, 1), dtype="float32"))
            lv338 = R.call_tir(cls.fused_matmul_multiply29_subtract_add321, (lv333, permute_dims25, lv336, permute_dims26), out_sinfo=R.Tensor((1, 1024), dtype="float32"))
            topk7: R.Tensor((1, 1), dtype="int32") = R.topk(lv338, k=1, axis=1, ret_type="indices", largest=True, dtype="int32")
            reshape84 = R.call_tir(cls.reshape241, (topk7,), out_sinfo=R.Tensor((1,), dtype="int32"))
            take13 = R.call_tir(cls.take11, (quantizer_quantizers_6_codebook_weight, reshape84), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv339 = R.call_tir(cls.fused_reshape25_transpose31, (take13,), out_sinfo=R.Tensor((1, 8, 1), dtype="float32"))
            lv342 = R.call_tir(cls.fused_conv1d41_add301, (lv339, lv341_1, lv377), out_sinfo=R.Tensor((1, 1024, 1), dtype="float32"))
            subtract13 = R.call_tir(cls.subtract11, (subtract11, lv342), out_sinfo=R.Tensor((1, 1024, 1), dtype="float32"))
            lv345 = R.call_tir(cls.fused_conv1d40_add311, (subtract13, lv344, lv383), out_sinfo=R.Tensor((1, 8, 1), dtype="float32"))
            lv346 = R.call_tir(cls.fused_transpose_reshape221, (lv345,), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv347_1 = R.call_tir(cls.fused_tir_square29_sum291, (lv346,), out_sinfo=R.Tensor((1, 1), dtype="float32"))
            lv348 = R.call_tir(cls.fused_broadcast_to_maximum_tir_sqrt12_divide291, (lv347_1, lv346), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv351 = R.call_tir(cls.fused_tir_square29_sum291, (lv348,), out_sinfo=R.Tensor((1, 1), dtype="float32"))
            lv353_1 = R.call_tir(cls.fused_matmul_multiply29_subtract_add321, (lv348, permute_dims29, lv351, permute_dims30), out_sinfo=R.Tensor((1, 1024), dtype="float32"))
            topk8: R.Tensor((1, 1), dtype="int32") = R.topk(lv353_1, k=1, axis=1, ret_type="indices", largest=True, dtype="int32")
            reshape88 = R.call_tir(cls.reshape241, (topk8,), out_sinfo=R.Tensor((1,), dtype="int32"))
            take15 = R.call_tir(cls.take11, (quantizer_quantizers_7_codebook_weight, reshape88), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv354 = R.call_tir(cls.fused_reshape25_transpose31, (take15,), out_sinfo=R.Tensor((1, 8, 1), dtype="float32"))
            lv357 = R.call_tir(cls.fused_conv1d41_add301, (lv354, lv356, lv389), out_sinfo=R.Tensor((1, 1024, 1), dtype="float32"))
            subtract15 = R.call_tir(cls.subtract11, (subtract13, lv357), out_sinfo=R.Tensor((1, 1024, 1), dtype="float32"))
            lv360 = R.call_tir(cls.fused_conv1d40_add311, (subtract15, lv359_1, lv395), out_sinfo=R.Tensor((1, 8, 1), dtype="float32"))
            lv361 = R.call_tir(cls.fused_transpose_reshape221, (lv360,), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv362 = R.call_tir(cls.fused_tir_square29_sum291, (lv361,), out_sinfo=R.Tensor((1, 1), dtype="float32"))
            lv363 = R.call_tir(cls.fused_broadcast_to_maximum_tir_sqrt12_divide291, (lv362, lv361), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv366 = R.call_tir(cls.fused_tir_square29_sum291, (lv363,), out_sinfo=R.Tensor((1, 1), dtype="float32"))
            lv368 = R.call_tir(cls.fused_matmul_multiply29_subtract_add321, (lv363, permute_dims33, lv366, permute_dims34), out_sinfo=R.Tensor((1, 1024), dtype="float32"))
            topk9: R.Tensor((1, 1), dtype="int32") = R.topk(lv368, k=1, axis=1, ret_type="indices", largest=True, dtype="int32")
            reshape92 = R.call_tir(cls.reshape241, (topk9,), out_sinfo=R.Tensor((1,), dtype="int32"))
            take17 = R.call_tir(cls.take11, (quantizer_quantizers_8_codebook_weight, reshape92), out_sinfo=R.Tensor((1, 8), dtype="float32"))
            lv369 = R.call_tir(cls.fused_reshape25_transpose31, (take17,), out_sinfo=R.Tensor((1, 8, 1), dtype="float32"))
            lv372 = R.call_tir(cls.fused_add30_add30_add30_add30_add30_add30_add30_add30_conv1d41_add30_add301, (metadata["relax.expr.Constant"][9], lv252, lv267_1, lv282, lv297, lv312, lv327, lv342, lv357, lv369, lv371_1, lv401), out_sinfo=R.Tensor((1, 1024, 1), dtype="float32"))
            gv1: R.Tuple(R.Tuple(R.Tensor((1, 1024, 1), dtype="float32"), R.Tuple(R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"), R.Tensor((1, 1), dtype="int32"))), R.Tuple(R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object, R.Object)) = (lv372, (topk1, topk2, topk3, topk4, topk5, topk6, topk7, topk8, topk9)), (_io, encoder_block_layers_0_cache_cache, encoder_block_layers_0_downsampling_delay_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_1_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_1_block_layers_0_block_paddings_0_cache, encoder_block_layers_1_block_layers_0_block_paddings_1_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_1_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_1_block_layers_1_block_paddings_0_cache, encoder_block_layers_1_block_layers_1_block_paddings_1_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_1_block_layers_2_block_paddings_0_cache, encoder_block_layers_1_block_layers_2_block_paddings_1_cache, encoder_block_layers_1_block_layers_4_cache_cache, encoder_block_layers_1_block_layers_4_downsampling_delay_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_2_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_2_block_layers_0_block_paddings_0_cache, encoder_block_layers_2_block_layers_0_block_paddings_1_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_2_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_2_block_layers_1_block_paddings_0_cache, encoder_block_layers_2_block_layers_1_block_paddings_1_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_2_block_layers_2_block_paddings_0_cache, encoder_block_layers_2_block_layers_2_block_paddings_1_cache, encoder_block_layers_2_block_layers_4_cache_cache, encoder_block_layers_2_block_layers_4_downsampling_delay_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_3_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_3_block_layers_0_block_paddings_0_cache, encoder_block_layers_3_block_layers_0_block_paddings_1_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_3_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_3_block_layers_1_block_paddings_0_cache, encoder_block_layers_3_block_layers_1_block_paddings_1_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_3_block_layers_2_block_paddings_0_cache, encoder_block_layers_3_block_layers_2_block_paddings_1_cache, encoder_block_layers_3_block_layers_4_cache_cache, encoder_block_layers_3_block_layers_4_downsampling_delay_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_cache_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_cache_cache, encoder_block_layers_4_block_layers_0_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_4_block_layers_0_block_paddings_0_cache, encoder_block_layers_4_block_layers_0_block_paddings_1_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_cache_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_cache_cache, encoder_block_layers_4_block_layers_1_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_4_block_layers_1_block_paddings_0_cache, encoder_block_layers_4_block_layers_1_block_paddings_1_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache, encoder_block_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, encoder_block_layers_4_block_layers_2_block_paddings_0_cache, encoder_block_layers_4_block_layers_2_block_paddings_1_cache, encoder_block_layers_4_block_layers_4_cache_cache, encoder_block_layers_4_block_layers_4_downsampling_delay_cache, encoder_block_layers_6_cache_cache, encoder_block_layers_6_downsampling_delay_cache, decoder_model_layers_0_cache_cache, decoder_model_layers_0_downsampling_delay_cache, decoder_model_layers_1_block_layers_1_cache_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_1_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_1_block_layers_2_block_paddings_0_cache, decoder_model_layers_1_block_layers_2_block_paddings_1_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_1_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_1_block_layers_3_block_paddings_0_cache, decoder_model_layers_1_block_layers_3_block_paddings_1_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_1_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_1_block_layers_4_block_paddings_0_cache, decoder_model_layers_1_block_layers_4_block_paddings_1_cache, decoder_model_layers_2_block_layers_1_cache_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_2_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_2_block_layers_2_block_paddings_0_cache, decoder_model_layers_2_block_layers_2_block_paddings_1_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_2_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_2_block_layers_3_block_paddings_0_cache, decoder_model_layers_2_block_layers_3_block_paddings_1_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_2_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_2_block_layers_4_block_paddings_0_cache, decoder_model_layers_2_block_layers_4_block_paddings_1_cache, decoder_model_layers_3_block_layers_1_cache_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_3_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_3_block_layers_2_block_paddings_0_cache, decoder_model_layers_3_block_layers_2_block_paddings_1_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_3_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_3_block_layers_3_block_paddings_0_cache, decoder_model_layers_3_block_layers_3_block_paddings_1_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_3_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_3_block_layers_4_block_paddings_0_cache, decoder_model_layers_3_block_layers_4_block_paddings_1_cache, decoder_model_layers_4_block_layers_1_cache_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_cache_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_cache_cache, decoder_model_layers_4_block_layers_2_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_4_block_layers_2_block_paddings_0_cache, decoder_model_layers_4_block_layers_2_block_paddings_1_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_cache_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_cache_cache, decoder_model_layers_4_block_layers_3_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_4_block_layers_3_block_paddings_0_cache, decoder_model_layers_4_block_layers_3_block_paddings_1_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_cache_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_1_downsampling_delay_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_cache_cache, decoder_model_layers_4_block_layers_4_block_branches_0_layers_3_downsampling_delay_cache, decoder_model_layers_4_block_layers_4_block_paddings_0_cache, decoder_model_layers_4_block_layers_4_block_paddings_1_cache, decoder_model_layers_6_cache_cache, decoder_model_layers_6_downsampling_delay_cache)
            R.output(gv1)
        return gv1
