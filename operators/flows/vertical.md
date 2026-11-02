# flow: vertical（单线到底）

> 原「九步深度思维法」。**一个东西，从"这是什么"走到"我能怎么用"。**

## 命中
`choose=yes` 且 `multi=no`，或用户明说要"搞懂 / 吃透 / 学会一个东西"。
`mode = lean`（可逆、单方、代价小）。

## 九步

| # | 步 | 做什么 | 用哪个 verb | 产出 |
|---|---|---|---|---|
| 1 | 定性 | 这是什么？属于哪个领域？ | `frame` | `problem.one_line` |
| 2 | 功能 | 它能干什么？解决什么问题？ | `frame` | — |
| 3 | 机制 | 它怎么起作用？原理是什么？ | `trace` | `root_chain` 第 1 层 |
| 4 | 结构 | 由什么构成？每部分干什么？ | `decompose` | `weights[].dimension` |
| 5 | 差异判断 | 各部分价值排序，哪些核心哪些辅助？ | `weigh` | `weights` + `only_one` |
| 6 | 目标锚定 | 结合我的实际情况，这解决我什么**具体**问题？ | `frame` | `problem.by_when` |
| 7 | 执行路径 | 拆成我能直接执行的步骤 | `choose` | `plan.steps` |
| 8 | 结构对应组合 | 把拆开的部件组合成完整可执行方案 | `choose` | `decision` |
| 9 | 验证 | 怎么知道有效？ | `choose` | `signals` |

## 出口（不全就是没走完）
`problem` / `root_chain≥2` / `weights≥2` / `decision` / `plan.first_step` / `signals` / `unchecked≥1`

## 最容易塌的三步
- **第 5 步**：跳过排序直接给方案 → 后面全是平均用力
- **第 6 步**：不锚定自己，泛泛而谈"这个技术很有前景" → 和你没关系
- **第 9 步**：没有可观测标准 → 三个月后不知道该不该继续

## 与 `spiral` 的区别
- `vertical`：**单车道**，一个问题到一个答案
- `spiral`：**多车道**，多维并存、寻找转化、螺旋往上

选错会怎样：用 vertical 解多方拉扯的问题 → 得出"应该选 A"然后现实里 A 和 B 都得要。
