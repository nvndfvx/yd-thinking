# Orchestrator：状态机

> 一条纪律先讲清：**模型不会真的"暂停在某个状态"**。
> 状态机的用处不是让模型等，而是：① 告诉它现在该产出什么 ② 告诉它卡住时**退回哪一步**。
> 所以每个状态都必须有一个**可交付物**，没有交付物就不算走完。

## 状态表

| # | 状态 | 产出物（没有它就没走完） | 退回条件 → 退到哪 |
|---|---|---|---|
| 1 | `INTAKE` | `problem.one_line` 一句话 + `problem.by_when` | 说不清 → 走 `INSUFFICIENT` |
| 2 | `ROUTE` | 四轴取值 + flow + modifiers + mode | 轴缺失且会改结果 → `INSUFFICIENT` |
| 3 | `ANALYZE` | flow 要求的全部步骤产出 | 步骤跳过 → 退回该步 |
| 4 | `CHECK` | 门禁 1/2/3 的证据 | 任一不过 → 回 `ANALYZE` 补对应 verb |
| 5 | `DECIDE` | `decision.choice` + `kill_criteria` ≥1 | 无证伪条件 → 回 `CHECK` |
| 6 | `PLAN` | `plan.first_step` 四要素齐 | 第一步做不了 → 回 `DECIDE` 重新取舍 |
| 7 | `VERIFY` | `signals` 领先 ≥1 + 滞后 ≥1 | 只有滞后指标 → 回 `PLAN` |
| 8 | `DELIVER` | `answer` + `payload` + `self_check` | 任一门禁空白 → 回对应状态 |

```
INTAKE ─→ ROUTE ─→ ANALYZE ─→ CHECK ─→ DECIDE ─→ PLAN ─→ VERIFY ─→ DELIVER
   │        │          ↑         │         │
   └────────┴──────────┴─────────┴─────────┘
             INSUFFICIENT（问 ≤2 问题，停）
```

## INSUFFICIENT（唯一允许停下的状态）

触发（任一成立）：

- 缺 `settled` 或 `choose`，且问题里读不出来
- 缺了会改变结论的关键事实（金额、期限、对方是谁）
- 用户要的是认同，不是判断

产出格式（**固定三行，不多说一个字**）：

```
我需要先知道两件事：
1. ___
2. ___

（拿到这两个答案我再判。现在给结论会是编的。）
```

**这个状态不是失败，是本技能最值钱的部分。** 会拒答的分析器，比永远有答案的可信。

## 硬规则

1. `oneway=yes` → 不可跳过 `CHECK`
2. `DECIDE` 之前不许出现结论句（用"待定"占位）
3. `kill_criteria` 至少 1 条且**可观测**（"感觉不对"不算）
4. `reentry` 必须落到具体日期或具体事件，不许写"以后定期回看"
5. `lean` 模式可省门禁 3/4/6 的**展开**，但字段不许空——空就说明判断做不了，转 `INSUFFICIENT`

## 回炉

一轮对话跑不完第二轮。所以回炉只能写成 **`reentry` 承诺**：

```yaml
reentry:
  check_on: "2026-06-30"        # 或 "交了第一期房租之后"
  question: "领先信号 X 动了吗？"
  carries: ["signals.system_turning", "decision.kill_criteria"]
```

落到日历/文件/待办才算数。**写在输出里不落地的回炉 = 没有回炉。**
