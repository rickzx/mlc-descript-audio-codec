import pickle
from typing import Union

import tvm
from tvm import meta_schedule as ms
from tvm import relax
from tvm.relax import transform, backend
from tvm.relax.pipeline import zero_pipeline

mod = pickle.load(open("../dist/before_scheduling.pkl", "rb"))

def static_shape_tuning_pipeline(
    total_trials: int,
    target: Union[str, tvm.target.Target],
    work_dir: str = "tuning_logs",
    cpu_weight_prepack: bool = False,
):
    @tvm.transform.module_pass(opt_level=0)
    def _pipeline(mod: tvm.ir.IRModule, _ctx: tvm.transform.PassContext) -> tvm.ir.IRModule:
        if cpu_weight_prepack:
            pre_tuning_layout_rewrite = [transform.AttachAttrLayoutFreeBuffers()]
            post_tuning_layout_rewrite = [
                transform.SplitLayoutRewritePreproc(),
                transform.LiftTransformParams(),
                transform.FoldConstant(),
            ]
        else:
            pre_tuning_layout_rewrite = []
            post_tuning_layout_rewrite = []

        with tvm.target.Target(target):
            mod = tvm.transform.Sequential(
                [
                    transform.DecomposeOpsForInference(),
                    transform.CanonicalizeBindings(),
                    zero_pipeline(),
                    *pre_tuning_layout_rewrite,
                    # Skip tuning if total_trials is 0
                    (
                        transform.MetaScheduleTuneIRMod({}, work_dir, total_trials, max_trials_per_task=2500)
                        if total_trials > 0
                        else tvm.transform.Sequential([])
                    ),
                    transform.MetaScheduleApplyDatabase(work_dir, enable_warning=True),
                    *post_tuning_layout_rewrite,
                ]
            )(mod)

        return mod

    return _pipeline


def apply_tuning(target, work_dir):
    @tvm.transform.module_pass(opt_level=0)
    def _pipeline(mod: tvm.ir.IRModule, _ctx: tvm.transform.PassContext) -> tvm.ir.IRModule:
        db = ms.database.create(work_dir=work_dir)

        with db, tvm.target.Target(target):
            mod = tvm.transform.Sequential(
                [
                    transform.DecomposeOpsForInference(),
                    transform.CanonicalizeBindings(),
                    zero_pipeline(),
                    transform.AttachAttrLayoutFreeBuffers(),
                    transform.MetaScheduleApplyDatabase(enable_warning=True),
                    transform.SplitLayoutRewritePreproc(),
                    transform.LiftTransformParams(),
                    transform.FoldConstant(),
                ]
            )(mod)

        return mod

    return _pipeline

tuned_mod = static_shape_tuning_pipeline(
            total_trials=80000,
            target=tvm.target.Target("apple/m2-gpu"),
            work_dir="tuning_logs",
            cpu_weight_prepack=True,
        )(mod)

pickle.dump(tuned_mod, open("../dist/after_scheduling_new.pkl", "wb"))

# after_mod = apply_tuning(tvm.target.Target("apple/m2-gpu"), "tuning_logs_new")(mod)

# pickle.dump(after_mod, open("../dist/after_scheduling.pkl", "wb"))