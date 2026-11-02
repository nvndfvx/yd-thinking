# 示例 3：我的视频号做不起来

> 覆盖：`diagnose`（追根 + 找缝隙）· `lean`（可逆：试错成本低）
> 演示重点：**支点必须可测、"压"必须带三件套。**
> 这是 v0.1 → v0.2 改动最明显的一条：老版本会给出"多拍就好了"。

## 四轴

```yaml
settled: false
choose: false       # 不是在选，是卡住了
multi: false
oneway: false       # 换个方向做，损失可控
```

→ `flow: diagnose`　`mode: lean`

## answer

**结论**：不是拍得少，是没有一个"看完想找你"的落点。补落点，别加频率。

**为什么**
1. 追下来根不是频率也不是剪辑，是"我从来没定过这条是给谁看的"。
2. 现有 47 条里完播最高的那条，恰好是唯一一条写给具体人的。
3. 频率从每周 1 条提到 3 条，只会把没有落点的内容多生产两遍。

**第一步**：今天把完播率最高的 3 条列出来，写下它们各自是写给谁的（具体到一个人）。

**我会在什么情况下改主意**：连续 10 条都写给了具体的人，完播率仍低于 25%。

## payload

<!-- payload -->
```yaml
run:
  flow: diagnose
  modifiers: [collide]
  mode: lean
  axes: {settled: false, choose: false, multi: false, oneway: false}
  reversibility: two-way

problem:
  one_line: "视频号做了 8 个月、47 条内容，涨粉停在 300，做不起来"
  owner: "我"
  by_when: "2026-06-30 给自己一个季度"

answer:
  verdict: "不是拍得少，是没有『看完想找你』的落点。补落点，别再提频率"
  why:
    - "追到的根是定位：我从没定过这条是给谁看的"
    - "47 条里完播最高的那条，恰好是唯一写给一个具体人的"
    - "频率翻三倍只会把一个没有落点的结构多生产两遍"
  first_step: "今天列完播率最高的 3 条，写下它们各自是写给谁的（具体到一个人）"
  what_would_change_my_mind: "连续 10 条都写给具体的人，完播率仍低于 25%"

root_chain:
  - question: "为什么涨粉停住？"
    candidate: "发得太少，算法不给量"
    status: rejected
    why: "相邻两个同量级账号周更 1 条也能起，且我有一条自然播放 8 万，说明不是频率问题"
  - question: "为什么完播低？"
    candidate: "前 3 秒没有钩子"
    status: rejected
    why: "我试过 6 种开场钩子，完播只从 18% 涨到 21%，说明钩子不是主要变量"
  - question: "为什么钩子改了也没用？"
    candidate: "我从没定过这条是给谁看的，所以钩子没有对象可钩"
    status: kept
    why: "唯一一条写给具体朋友的内容完播 62%，是我全部内容里唯一的异常值"

open_frontier: "我还不知道『给具体的人写』能不能规模化——如果只能对熟人有效，这条根就不成立"

weights:
  - {dimension: "定位（写给谁）", weight: 5, evidence: "唯一一条定位明确的完播 62%，其余中位数 19%", only_one: true}
  - {dimension: "发布频率", weight: 2, evidence: "同期周更 1 条与周更 3 条的月份，播放中位数无差异", only_one: false}
  - {dimension: "剪辑质量", weight: 3, evidence: "两条换了外包剪辑，完播提升 3 个百分点", only_one: false}

strongest_counterargument: "也可能是我的题材本身没有需求——定位只是让它变成了一条好片子给错的人看，而不是把对的人找出来"

decision:
  choice: "停止提频率，用 10 条内容做定位实验：每条写给一个具体的人"
  rationale: "异常值比平均数有信息量：47 条里唯一有定位的那条完播是其余的 3 倍，先把这个变量单独验证"
  confidence: mid
  kill_criteria:
    - "连续 10 条定位明确，完播率中位数未超过 25%"
    - "写具体的人时我连续 3 条卡住超过 2 小时（说明我根本不知道我的观众是谁）"

plan:
  first_step: {verb: "列出", object: "完播率最高的 3 条并写明各自写给谁", when: "今天 23:00 前", done_marker: "纸上写下 3 条内容 + 3 个具体人名或人群描述"}
  steps:
    - "接下来 10 条，每条开头写明『这条给谁』，写在脚本第一行"
    - "第 5 条后做一次中途检查，只看完播率"
  owner: "我"
  deadline: "2026-06-15"

anchors:
  fulcrum: {metric: "单条完播率", floor: ">= 35%", invariant: "不随选题变，这是我的表达下限，换平台也不变"}
  gap: "还没有一个看完想找我的落点（评论区无人提问，主页无入口）"
  deadline: "2026-06-15"
  signal: "连续 10 条完播 >35%，且出现陌生人提问"
  review_at: "2026-06-15 无条件复盘，不看当期心情"

signals:
  system_turning:
    - "写脚本时我能一句话说出这条给谁（不需要想超过 10 秒）"
    - "同一条内容下出现 2 个以上陌生人追问细节"
  outcome:
    - "完播率中位数从 19% 到 35%"

unknowns:
  - unchecked: "我的目标观众到底在不在这个平台"
    how: "看完播最高的 3 条的观众画像，看是否与我想服务的人重合"
    cost: "后台数据 30 分钟"
  - unchecked: "定位明确后我能不能保持产出"
    how: "先用 10 条测，不预先扩产"
    cost: "约 3 周"

reentry:
  check_on: "2026-05-20（第 5 条之后）"
  question: "完播中位数动了吗？"
  carries: ["anchors.signal", "decision.kill_criteria"]

self_check:
  root_chain: "否掉了『频率』和『钩子』两条，落在『没定过给谁看』，且用唯一异常值做了支撑"
  multi_view: "定位(5)与频率(2)结论直接冲突：加频率能立刻多做，定位要求先少做"
  weighted: "定位 5 分 vs 频率 2 分，2.5 倍；只留一个留定位"
  worst_case: "三个月只有 10 条内容、涨粉可能更慢，损失是可接受的时间，占比 15% 内，未触发天花板"
  first_step: "列 3 条内容 + 写明对象，今天 23:00 前，完成标志是纸上写出 3 个人"
  signals: "领先是能一句话说出给谁 / 陌生人追问，滞后是完播中位数到 35%"
  falsifier: "10 条都定位明确、完播仍不过 25% → 根不成立，回头查选题需求"
```
