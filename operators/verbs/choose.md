# verb: choose

**一句话**：在约束下选**最稳**的解，不是收益最高的解。**防守型，不是进攻型。**

## 输入
- `weights`（排好序的维度）
- `root_chain`、`opposing_forces`
- 选项列表

## 动作

1. **列全选项，必须包含"什么都不做"。**
   不做也是一个选项，而且经常是最优的那个。不列它，就是在逼自己动。
2. **两路（或多路）推演。** 每个选项推：最好的走向、最可能的走向、最坏的走向。
3. **算最坏情况的占比。** 没有数字就没有风控：
   ```yaml
   loss: {amount: "12 万", unit: "元", share_of_resources: "60%", ceiling: "50%"}
   ```
   `share > ceiling` → 这个选项直接出局，不管收益多高。
4. **选最稳的。** 判据不是"期望收益最大"，是"最坏情况我还能继续玩"。
5. **写证伪条件。** ≥1 条可观测的 `kill_criteria`：什么现象出现，我就承认选错了。
6. **若 `oneway=true`：先做一次尸检**（`lenses/premortem.md`），再回到第 4 步。

## 输出字段
```yaml
decision: {choice, rationale, confidence, kill_criteria}
risks: {worst_case, loss, reversible, mitigation}
premortem: {failed_at, causes, earliest_signal}   # oneway 时必填
plan.first_step
```

## 判据
- 选项里包含"不做"
- 最坏情况有数字和占比
- `kill_criteria` 能被第三方观测到
- 选的是"最稳"，声明里能说出为什么放弃更高收益的那个

## 反模式
| 病 | 说明 |
|---|---|
| 选期望收益最高的 | 这是赌，不是决策 |
| 没有"不做"这个选项 | 隐性假设"必须行动" |
| `confidence: high` 但 `unknowns` 为空 | 要么真懂，要么在装 |
| kill_criteria = "发现不合适就调整" | 不可观测，等于没有 |

## 与 `defensive` 叠加器的关系
`choose` 提供选择逻辑；`flows/defensive.md` 提供更重的推演流程（九步风控）。
`oneway=true` 时两者都要跑。
