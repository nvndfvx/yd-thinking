# CONTRIBUTING：加一个算子的准入条件

本仓库防腐烂的机制不是 review，是**准入条件**。任何新增或改动算子，必须同时满足 5 条，否则 PR 不合并。

## 算子准入 5 条

| # | 条件 | 怎么证明 |
|---|---|---|
| 1 | 有一条轴能选中它 | `router/axes.yaml` 里存在一条路径或一个 modifier 会触发它 |
| 2 | 契约里有它的位置 | 要么在 `compiler/schema.yaml` 新增字段，要么明确复用已有字段（写明复用哪个） |
| 3 | 有回归用例 | `evals/cases.jsonl` 至少 1 条；若是流程，`examples/` 至少 1 个带 payload 的完整例子 |
| 4 | 与现有 verb 不重叠 | PR 里写一句"它和 ___ 的区别是 ___"；说不出来就是重复 |
| 5 | CHANGELOG 记一笔 | 按下面的版本规则 |

## 版本规则（语义化）

- **major**（0.x → 1.0）：删字段、改 `derive()` 的路由结论、改六条公理
- **minor**：新增字段（向后兼容）、新增算子、新增例子
- **patch**：改措辞、修错字、补测试用例

`derive()`（`evals/run.py`）和 `router/axes.yaml` **必须同步改**，CI 会抓漂移。

## 改契约字段时的硬要求

1. 先改 `compiler/schema.yaml`（唯一真相）
2. 再同步 `templates/output.md`（派生）
3. 再同步 `evals/run.py` 的 `validate()`（校验）
4. 最后改 `guardrails/checklist.yaml` 里对应的门禁（如果有）

顺序不能反，否则会出现"模板和 schema 打架"的老毛病。

## 一条纪律

> 没有测试的算子 = 没有算子。
> 写不出可证伪字段的能力 = 不该进这个仓库的能力。
