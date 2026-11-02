#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""yd-thinking 结构自检（不需要 LLM）。

做三件事：
1. 路由一致性：cases.jsonl 每个 case 的 expect_flow/modifiers/mode，
   必须等于从四轴重新推导的结果（防止规则表与实现漂移）。
2. 契约校验：examples/*.md 里标了 `<!-- payload -->` 的 YAML 块，
   必须满足 compiler/schema.yaml 的必填字段与可证伪规则。
3. 门禁机械项：root_chain / weights / kill_criteria / first_step /
   signals / unknowns 等能机械检查的部分逐条验证。

运行：python evals/run.py   依赖：pip install pyyaml
"""
import json
import os
import re
import sys

try:
    import yaml
except ImportError:
    print("缺少 PyYAML：pip install pyyaml")
    sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FLOWS = {"vertical", "spiral", "diagnose", "retro", "structure"}
BANNED_SELF = {"是", "否", "通过", "已通过", "全过", "true", "false", "n/a", "无"}
BANNED_WHEN = ["尽快", "以后", "有空", "下周", "改天"]
BANNED_REENTRY = ["以后", "定期", "持续关注"]
BANNED_KILL = ["感觉不对", "情况变化", "不合适", "视情况"]


# ── 路由推导（必须与 router/axes.yaml 一致）─────────────────────────
def derive_flow(axes):
    if axes.get("structure"):
        return "structure"
    if "settled" not in axes or "choose" not in axes:
        return "insufficient"
    if axes["settled"]:
        return "retro"
    if not axes["choose"]:
        return "diagnose"
    if axes.get("multi"):
        return "spiral"
    return "vertical"


def derive_mods(axes):
    m = []
    if axes.get("oneway") and not axes.get("settled"):
        m += ["defensive", "premortem"]
    if axes.get("multi") or axes.get("blind_spot"):
        m.append("collide")
    if axes.get("settled") or axes.get("prevent_repeat"):
        m.append("failure_list")
    return sorted(set(m))


def derive_mode(axes, flow):
    m = "deep" if (axes.get("oneway") or axes.get("multi")) else "lean"
    if flow == "retro":
        m = "deep"
    if flow == "structure":
        m = "lean"
    return m


# ── 契约校验 ───────────────────────────────────────────────────────
def chk(cond, errs, msg):
    if not cond:
        errs.append(msg)


def required_blocks(p):
    axes = p["run"]["axes"]
    flow = p["run"]["flow"]
    settled = axes.get("settled")
    multi = axes.get("multi")
    oneway = axes.get("oneway")
    req = []
    if (multi or oneway) and not settled:
        req.append("opposing_forces")
    if oneway and not settled:
        req += ["risks", "premortem"]
    if flow == "diagnose":
        req.append("anchors")
    if flow == "retro":
        req.append("failure_chain")
    if flow == "structure":
        req.append("arc")
    return req


def validate(p):
    errs = []

    if not isinstance(p, dict):
        return ["payload 不是 dict"]

    # run
    run = p.get("run", {})
    chk(run.get("flow") in FLOWS, errs, "run.flow 非法或缺失")
    chk(run.get("mode") in {"deep", "lean"}, errs, "run.mode 非法或缺失")
    axes = run.get("axes", {})
    for k in ("settled", "choose", "multi", "oneway"):
        chk(k in axes and isinstance(axes[k], bool), errs, f"run.axes.{k} 缺失或非 bool")
    if run.get("flow") == "retro":
        chk(run.get("mode") == "deep", errs, "retro 流程 mode 必须是 deep")
    if run.get("flow") == "structure":
        chk(run.get("mode") == "lean", errs, "structure 流程 mode 必须是 lean")
    if axes.get("oneway") and not axes.get("settled"):
        mods = run.get("modifiers", [])
        chk("defensive" in mods, errs, "oneway 且未发生 → 必须叠加 defensive")
        chk("premortem" in mods, errs, "oneway 且未发生 → 必须叠加 premortem")

    # problem / answer
    prob = p.get("problem", {})
    for k in ("one_line", "owner", "by_when"):
        chk(bool(prob.get(k)), errs, f"problem.{k} 缺失")
    ans = p.get("answer", {})
    chk(bool(ans.get("verdict")), errs, "answer.verdict 缺失")
    chk(isinstance(ans.get("why"), list) and 1 <= len(ans["why"]) <= 3, errs, "answer.why 应为 1-3 条")
    chk(bool(ans.get("first_step")), errs, "answer.first_step 缺失")
    chk(len(str(ans.get("what_would_change_my_mind", ""))) >= 15, errs, "answer.what_would_change_my_mind <15 字")

    # root_chain
    rc = p.get("root_chain", [])
    chk(isinstance(rc, list) and len(rc) >= 2, errs, "root_chain 需 ≥2 条")
    if isinstance(rc, list):
        chk(any(r.get("status") == "rejected" for r in rc), errs, "root_chain 至少 1 条 rejected")
        chk(all(len(str(r.get("why", ""))) >= 15 for r in rc), errs, "root_chain.why 需 ≥15 字")
    chk(len(str(p.get("open_frontier", ""))) >= 15, errs, "open_frontier <15 字")

    # weights
    w = p.get("weights", [])
    chk(isinstance(w, list) and len(w) >= 2, errs, "weights 需 ≥2 条")
    if isinstance(w, list) and len(w) >= 2:
        vals = [x.get("weight") for x in w]
        chk(all(isinstance(v, int) and 1 <= v <= 5 for v in vals), errs, "weight 应为 1-5 的 int")
        if all(isinstance(v, int) for v in vals):
            chk(max(vals) >= 2 * min(vals), errs, "weights 必须 max >= 2*min（不许平均）")
            chk(len(set(vals)) >= 2, errs, "weights 不能全部相同")
        chk(sum(1 for x in w if x.get("only_one")) == 1, errs, "only_one 必须恰好 1 条为 true")
        chk(all(bool(x.get("evidence")) for x in w), errs, "weights.evidence 不能为空")

    chk(len(str(p.get("strongest_counterargument", ""))) >= 25, errs, "strongest_counterargument <25 字")

    # decision
    dec = p.get("decision", {})
    chk(bool(dec.get("choice")), errs, "decision.choice 缺失")
    kc = dec.get("kill_criteria", [])
    chk(isinstance(kc, list) and len(kc) >= 1, errs, "kill_criteria 需 ≥1 条")
    if isinstance(kc, list):
        chk(not any(any(b in str(k) for b in BANNED_KILL) for k in kc), errs, "kill_criteria 含不可观测词")

    # plan.first_step
    fs = p.get("plan", {}).get("first_step", {})
    for k in ("verb", "object", "when", "done_marker"):
        chk(bool(fs.get(k)), errs, f"plan.first_step.{k} 缺失")
    chk(not any(b in str(fs.get("when", "")) for b in BANNED_WHEN), errs, "first_step.when 含禁用词")

    # signals
    sig = p.get("signals", {})
    st = sig.get("system_turning", [])
    oc = sig.get("outcome", [])
    chk(isinstance(st, list) and len(st) >= 1, errs, "signals.system_turning 需 ≥1 条")
    chk(isinstance(oc, list) and len(oc) >= 1, errs, "signals.outcome 需 ≥1 条")
    if isinstance(st, list) and isinstance(oc, list):
        chk(set(st) != set(oc), errs, "领先与滞后信号不能相同")

    # unknowns
    un = p.get("unknowns", [])
    chk(isinstance(un, list) and len(un) >= 1, errs, "unknowns 需 ≥1 条")
    if isinstance(un, list):
        chk(all(all(bool(x.get(k)) for k in ("unchecked", "how", "cost")) for x in un), errs, "unknowns 每项需 unchecked/how/cost")

    # reentry
    re_ = p.get("reentry", {})
    chk(bool(re_.get("check_on")), errs, "reentry.check_on 缺失")
    chk(not any(b in str(re_.get("check_on", "")) for b in BANNED_REENTRY), errs, "reentry.check_on 含禁用词")
    chk(bool(re_.get("question")), errs, "reentry.question 缺失")

    # self_check（证据，不是布尔）
    sc = p.get("self_check", {})
    for k in ("root_chain", "multi_view", "weighted", "worst_case", "first_step", "signals", "falsifier"):
        chk(k in sc and isinstance(sc.get(k), str), errs, f"self_check.{k} 缺失或非字符串")
    for k, v in (sc.items() if isinstance(sc, dict) else []):
        if isinstance(v, str):
            chk(v.strip() not in BANNED_SELF, errs, f"self_check.{k} 是禁用词")
            chk(len(v) >= 12, errs, f"self_check.{k} 证据 <12 字")

    # 条件块
    for blk in required_blocks(p):
        chk(blk in p and p.get(blk), errs, f"缺少条件必填块 {blk}")

    of = p.get("opposing_forces", {})
    if of:
        chk(isinstance(of.get("yang"), list) and len(of["yang"]) >= 1, errs, "opposing_forces.yang 需 ≥1")
        chk(isinstance(of.get("yin"), list) and len(of["yin"]) >= 1, errs, "opposing_forces.yin 需 ≥1")
        chk(all(all(bool(i.get(k)) for k in ("claim", "magnitude")) for i in of.get("yang", []) + of.get("yin", [])), errs, "阴阳每条需 claim+magnitude")
        chk(bool(of.get("pivot")), errs, "opposing_forces.pivot 缺失")

    rs = p.get("risks", {})
    if rs:
        loss = rs.get("loss", {})
        chk(bool(rs.get("worst_case")), errs, "risks.worst_case 缺失")
        for k in ("amount", "unit", "share_of_resources", "ceiling"):
            chk(bool(loss.get(k)), errs, f"risks.loss.{k} 缺失")
        chk("%" in str(loss.get("share_of_resources", "")), errs, "loss.share_of_resources 需含百分比")
        chk(bool(rs.get("mitigation")), errs, "risks.mitigation 缺失")

    pm = p.get("premortem", {})
    if pm:
        chk(bool(pm.get("failed_at")), errs, "premortem.failed_at 缺失")
        chk(isinstance(pm.get("causes"), list) and len(pm["causes"]) >= 2, errs, "premortem.causes 需 ≥2")
        chk(bool(pm.get("earliest_signal")), errs, "premortem.earliest_signal 缺失")

    an = p.get("anchors", {})
    if an:
        ful = an.get("fulcrum", {})
        for k in ("metric", "floor", "invariant"):
            chk(bool(ful.get(k)), errs, f"anchors.fulcrum.{k} 缺失")
        for k in ("gap", "deadline", "signal", "review_at"):
            chk(bool(an.get(k)), errs, f"anchors.{k} 缺失")

    fc = p.get("failure_chain", {})
    if fc:
        chk(isinstance(fc.get("stage"), int) and 1 <= fc["stage"] <= 7, errs, "failure_chain.stage 应为 1-7 int")
        chk(bool(fc.get("earliest_failure")), errs, "failure_chain.earliest_failure 缺失")
        chk(bool(fc.get("root")), errs, "failure_chain.root 缺失")
        chk(isinstance(fc.get("warning_triggers"), list) and len(fc["warning_triggers"]) >= 1, errs, "warning_triggers 需 ≥1")

    ar = p.get("arc", {})
    if ar:
        st_ = ar.get("start", {}); en = ar.get("end", {})
        for k in ("lacks", "fears", "wants"):
            chk(bool(st_.get(k)), errs, f"arc.start.{k} 缺失")
        for k in ("gains", "lets_go", "becomes"):
            chk(bool(en.get(k)), errs, f"arc.end.{k} 缺失")
        chk(bool(ar.get("turn")), errs, "arc.turn 缺失")
        chk(isinstance(ar.get("obstacles"), list) and len(ar["obstacles"]) >= 2, errs, "arc.obstacles 需 ≥2")
        chk(isinstance(ar.get("actions"), list) and len(ar["actions"]) >= 1, errs, "arc.actions 需 ≥1")
        chk("causal_ok" in ar, errs, "arc.causal_ok 缺失")

    return errs


def extract_payloads():
    out = {}
    exdir = os.path.join(ROOT, "examples")
    for fn in sorted(os.listdir(exdir)):
        if not fn.endswith(".md"):
            continue
        path = os.path.join(exdir, fn)
        text = open(path, encoding="utf-8").read()
        if "<!-- payload -->" not in text:
            continue
        i = text.index("<!-- payload -->")
        j = text.find("```yaml", i)
        if j < 0:
            out[fn] = ("NO_YAML_FENCE", None)
            continue
        k = text.find("```", j + 3)
        block = text[j + len("```yaml"):k]
        try:
            out[fn] = ("OK", yaml.safe_load(block))
        except Exception as e:  # noqa: BLE001
            out[fn] = ("YAML_ERROR", str(e))
    return out


def main():
    fails = 0

    # 1. 路由一致性
    cases_path = os.path.join(ROOT, "evals", "cases.jsonl")
    cases = [json.loads(l) for l in open(cases_path, encoding="utf-8") if l.strip()]
    print(f"== 路由一致性：{len(cases)} cases ==")
    for c in cases:
        axes = c["axes"]
        flow = derive_flow(axes)
        mods = derive_mods(axes)
        mode = derive_mode(axes, flow) if flow != "insufficient" else None
        errs = []
        if flow != c["expect_flow"]:
            errs.append(f"flow: 推导 {flow} != 期望 {c['expect_flow']}")
        if mods != sorted(c["expect_mods"]):
            errs.append(f"mods: 推导 {mods} != 期望 {c['expect_mods']}")
        if c["expect_mode"] is not None and mode != c["expect_mode"]:
            errs.append(f"mode: 推导 {mode} != 期望 {c['expect_mode']}")
        status = "PASS" if not errs else "FAIL"
        if errs:
            fails += 1
        print(f"  [{status}] {c['id']:<22} flow={flow:<12} mods={mods}")
        for e in errs:
            print(f"        - {e}")

    # 2. 契约校验
    print("\n== 契约校验：examples/*.md payload ==")
    payloads = extract_payloads()
    for fn, (kind, data) in payloads.items():
        if kind != "OK":
            print(f"  [FAIL] {fn}: {kind} {data}")
            fails += 1
            continue
        errs = validate(data)
        if errs:
            fails += 1
            print(f"  [FAIL] {fn} ({len(errs)} 处)")
            for e in errs:
                print(f"        - {e}")
        else:
            print(f"  [PASS] {fn}")

    print()
    if fails:
        print(f"RESULT: FAIL（{fails} 处）")
        sys.exit(1)
    print("RESULT: PASS（全部通过）")
    sys.exit(0)


if __name__ == "__main__":
    main()
