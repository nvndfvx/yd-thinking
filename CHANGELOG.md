# CHANGELOG

## v0.2.0

架构从"看起来有七层"重做成"七层都能被机械验证"。核心改动：

### 修掉的 6 处硬矛盾（v0.1 会跑错）
1. `guards`（至少 1 个 analysis 算子）与 5/8 条规则冲突 → 改为 4 个可判轴。
2. `min_check` 未定义且 R1/R5/R7 不可能满足 → 删除。
3. quick 模式被要求填它允许跳过的字段 → `mode` 改由物理属性推导，不再由用户声明。
4. 状态机与模式表对"是否跳过 CHECK"说法不一 → 统一进 state-machine.md。
5. 示例一用了 R6 没有的算子 → 路由改为"分类优先、规则守卫"。
6. SKILL.md 无 `description` → 补触发词。

### 结构重排
- `operators/` 由 12 个平级算子 → **verbs(6) / flows(6) / lenses(2) / loop(1)**，消除重复劳动。
- 两个"九步"改名：`vertical`（单线到底）/ `spiral`（螺旋升维）。

### 契约层
- `guardrails_passed: {7×bool}`（自证）→ `self_check` 七条证据，禁 9 个词。
- `root: string` → `root_chain`（≥2 条，≥1 条被否）。
- `can_afford: bool` → `loss.{amount, share_of_resources, ceiling}`。
- 新增 `strongest_counterargument` / `kill_criteria` / `unknowns` / `signals`(领先+滞后) / `reentry`。
- `yinyang` 全局必填 → 条件必填（multi/oneway 且未发生）。

### 内容层（修 3 处不可证伪）
- 支点必须可测（`fulcrum.{metric, floor, invariant}`）。
- 压必须三件套（`deadline / signal / review_at`）。
- 极点必须事前定义（`pivot` 可证伪）。

### 工程层
- 新增 `evals/cases.jsonl` + `evals/run.py` + GitHub Action（无需 LLM 的结构自检）。
- 新增 `examples/` 6 个跨域示例（含 1 个 INSUFFICIENT 拒答）。
- 新增 `CONTRIBUTING.md`（算子准入 5 条）、双许可 `LICENSE`。

### 文档
- README 重写：补 11 个原始模型 → 操作符的映射表、六条公理、安装与使用说明、拒答示例。
- 新增 `.gitattributes`：关闭 Markdown/YAML 语言统计，避免仓库被误标为 Python 项目。

## v0.1.0

- 首次把 YD 思维模型封装为推理技能。
- 建立 Kernel / Router / Operators / Orchestrator / Compiler / Guardrails / Evals 七层。
- 封装 12 个算子、统一 Schema、7 项布尔门禁、3 类文档型 eval。

> v0.1 的问题是"文档型"：规则不可判、门禁自证、eval 不执行。
> v0.2 把它变成了"可判"：规则可推导、门禁交证据、eval 能跑。
