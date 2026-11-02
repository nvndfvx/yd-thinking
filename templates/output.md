# 输出模板

> **本文件由 `compiler/schema.yaml` 派生。改字段先改 schema，再同步这里。**
> 不要单独改这份。CI 会用 schema 的字段表校验 examples 里的 payload。

输出分两段：**先给 `answer`（给人），再给 `payload`（给 agent / 存档）。**

---

## 第一段：answer（≤200 字，第一句就是结论）

```markdown
**结论**：{verdict，≤40 字，一句话说完}

**为什么**
1. {why-1}
2. {why-2}
3. {why-3}（最多三条）

**第一步**：{verb + object + when + done_marker}（今天/明天就能做）

**我会在什么情况下改主意**：{what_would_change_my_mind}
```

写完之后自检三句：
- 如果对方只读这 200 字，能不能直接动手？
- 第一句是不是结论，而不是背景？
- 有没有一句是"因人而异"式的免责？

---

## 第二段：payload

```yaml
run:
  flow: vertical | spiral | diagnose | retro | structure
  modifiers: [defensive, premortem, collide, failure_list]
  mode: deep | lean
  axes: {settled: false, choose: true, multi: true, oneway: true}
  reversibility: one-way | two-way | partial

problem:
  one_line: ""
  owner: ""
  by_when: ""

answer:
  verdict: ""
  why: ["", ""]
  first_step: ""
  what_would_change_my_mind: ""

root_chain:            # ≥2 条，≥1 条 rejected
  - {question: "", candidate: "", status: rejected, why: ""}
  - {question: "", candidate: "", status: kept, why: ""}

open_frontier: ""

weights:               # ≥2 条；max >= 2*min；恰好 1 条 only_one
  - {dimension: "", weight: 5, evidence: "", only_one: true}
  - {dimension: "", weight: 2, evidence: "", only_one: false}

strongest_counterargument: ""

decision:
  choice: ""
  rationale: ""
  confidence: low | mid | high
  kill_criteria: [""]

plan:
  first_step: {verb: "", object: "", when: "今天", done_marker: ""}
  steps: [""]
  owner: ""
  deadline: ""

signals:
  system_turning: [""]     # 领先：早出现、说明结构在动
  outcome: [""]            # 滞后：结果指标

unknowns:                  # ≥1
  - {unchecked: "", how: "", cost: ""}

reentry:
  check_on: ""             # 具体日期或具体事件
  question: ""
  carries: [""]

self_check:                # 交证据，不许写"是/通过/全过"
  root_chain: ""
  multi_view: ""
  weighted: ""
  worst_case: ""
  first_step: ""
  signals: ""
  falsifier: ""

# ── 条件块 ──
opposing_forces:           # multi 或 oneway 时
  yang: [{claim: "", magnitude: ""}]
  yin:  [{claim: "", magnitude: ""}]
  pivot: ""                # 可证伪的质变条件

risks:                     # oneway 时
  worst_case: ""
  loss: {amount: "", unit: "", share_of_resources: "", ceiling: ""}
  reversible: one-way | partial
  mitigation: ""

premortem:                 # oneway 时
  failed_at: ""
  causes: ["", ""]
  earliest_signal: ""

anchors:                   # diagnose 时
  fulcrum: {metric: "", floor: "", invariant: ""}
  gap: ""
  deadline: ""
  signal: ""
  review_at: ""

failure_chain:             # retro 时
  stage: 1-7
  earliest_failure: ""
  root: ""
  warning_triggers: [""]

arc:                       # structure 时
  start: {lacks: "", fears: "", wants: ""}
  end: {gains: "", lets_go: "", becomes: ""}
  turn: ""
  obstacles: [""]
  actions: [""]
  causal_ok: true
```

---

## INSUFFICIENT 的输出（唯一例外）

不写 payload。固定三行，然后停：

```
我需要先知道两件事：
1. ___
2. ___

（拿到这两个答案我再判。现在给结论会是编的。）
```
