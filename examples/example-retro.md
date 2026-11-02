# 示例 4：上一个项目为什么会失败

> 覆盖：`retro`（复盘）· `deep`（强制）· 叠加 `failure_list` 镜子
> 演示重点：**找最早失效点，不是最显眼的那个；根要落在一个"没做过的决定"上。**

## 四轴

```yaml
settled: true        # 已经失败了
choose: false
multi: true          # 我 + 合伙人 + 早期用户
oneway: true         # 已经发生，不可逆
```

→ `flow: retro`　`mode: deep`（复盘一律 deep）
→ `modifiers: [failure_list]`

## answer

**结论**：真因不在执行，在我从没验证过"谁愿意付钱"就招了人。

**为什么**
1. 显眼的失效点是第 4 个月的现金流断，但那只是结果。
2. 往前追，最早的失效点是第 2 步：凭"身边人都说好"替掉了需求验证。
3. 招人这个决定一旦做了就锁死了每月 8 万支出，它把可逆变成了不可逆——这才是根。

**第一步**：今天把当时"身边人说好"的原话逐条写下来，标出哪几句是客套。

**我会在什么情况下改主意**：发现当时其实做过付费访谈，只是我没看结论。

## payload

<!-- payload -->
```yaml
run:
  flow: retro
  modifiers: [failure_list, collide]
  mode: deep
  axes: {settled: true, choose: false, multi: true, oneway: true}
  reversibility: one-way

problem:
  one_line: "上一个项目做了 11 个月、烧掉 96 万后关停，为什么会失败"
  owner: "我（复盘主体）"
  by_when: "2026-04-30 复盘会前"

answer:
  verdict: "真因不在执行，在我没验证过谁愿意付钱就招了人"
  why:
    - "现金流断在第 4 个月，那是结果不是原因"
    - "最早的失效点在第 2 步：用『身边人都说好』替代了需求验证"
    - "招人锁死每月 8 万支出，把可逆变成了不可逆，这才是根"
  first_step: "今天把当时『身边人说好』的原话逐条写下来，标出哪几句是客套"
  what_would_change_my_mind: "翻记录发现当时做过付费访谈，只是结论被我忽略了"

root_chain:
  - question: "为什么项目死了？"
    candidate: "现金流断了，融资没到位"
    status: rejected
    why: "同期两个竞品也融不到钱却活着，区别是它们的月支出是 2 万，我们是 8 万"
  - question: "为什么支出是 8 万？"
    candidate: "团队配置过重，招了 5 个人"
    status: rejected
    why: "招人本身不是错，错在招的时机——需求还没被验证就上了产能"
  - question: "为什么在没验证时就招人？"
    candidate: "我把『身边人都说好』当成了需求验证，从没让人付过钱"
    status: kept
    why: "整份记录里没有任何一次『收钱』或『让人预付』的动作，全是口头反馈"

open_frontier: "我还不知道自己当时是『不敢听拒绝』还是『真的没意识到要验证』——这两者的修法不同"

weights:
  - {dimension: "需求是否被付钱验证过", weight: 5, evidence: "11 个月里 0 次收费，0 次预付定金", only_one: true}
  - {dimension: "现金消耗节奏", weight: 4, evidence: "月固定支出 8 万，可支撑 12 个月，实际第 11 个月关停", only_one: false}
  - {dimension: "团队能力", weight: 2, evidence: "5 个人都能独立交付，离职面谈无人抱怨能力问题", only_one: false}

strongest_counterargument: "就算当时先验证需求，我大概率还是会招这么多人——因为我真正需要的不是验证，是『看起来像一家公司』带来的安全感"

decision:
  choice: "把『收钱验证』作为未来任何项目的启动前置动作，写进决策清单"
  rationale: "唯一能改变结果的变量是验证时机；团队、融资、执行力都不是最早失效点"
  confidence: high
  kill_criteria:
    - "下个项目启动 6 周内仍未收到任何一笔真实付款"
    - "我又开始用『大家都说好』作为继续投入的理由"

plan:
  first_step: {verb: "整理", object: "当时所有『说好』的原话并标注客套与真实", when: "今天 23:00 前", done_marker: "一张两列表格：原话 / 我的判断"}
  steps:
    - "把复盘结论写成一条可检查的规则：任何项目在招第 2 个人之前必须收到 3 笔付款"
    - "下次启动前把这条规则贴在需求文档第一行"
  owner: "我"
  deadline: "2026-04-30"

risks:
  worst_case: "把原因归给『太相信别人』这类品质问题，下次换个场景照样犯"
  loss: {amount: "96 万与 11 个月", unit: "元/月", share_of_resources: "70%", ceiling: "50%"}
  reversible: one-way
  mitigation: "只接受可检查的规则型结论，拒绝感想型结论"

premortem:
  failed_at: "2026 年 10 月，下个项目又在第 5 个月招人时"
  causes:
    - "新项目的『大家都说好』换了个说法，叫『行业共识』，我没认出来"
    - "我把『收到 3 笔付款』打折扣成『有人明确表示会买』"
  earliest_signal: "我开始用『这次不一样』解释为什么可以先招人——这个句式出现就是信号"

failure_chain:
  stage: 2
  earliest_failure: "第 2 步就该做的需求验证，被口头好评替代了，之后每一步都在为这个缺口买单"
  root: "我从没做过『让人付钱』这个决定，只做了『让人说好』这个动作"
  warning_triggers:
    - "我用『大家都说』『行业共识』『朋友都很看好』作为继续投入的理由"
    - "支出增加发生在收入出现之前"

signals:
  system_turning:
    - "在招第 2 个人之前，账上出现了 3 笔真实付款"
    - "用户开始主动复购而不是被我追问反馈"
  outcome:
    - "第 6 个月时付费用户留存 >40%"

unknowns:
  - unchecked: "当时是否存在我忽略掉的反面反馈"
    how: "翻聊天记录搜索『不过』『可能有点问题』这类转折词"
    cost: "2 小时"
  - unchecked: "合伙人是否早提出过疑虑而我没听"
    how: "直接问他一次，问具体哪次会议"
    cost: "一次对话"

reentry:
  check_on: "2026-10-31（下个项目启动第 5 个月）"
  question: "我在招第 2 个人之前收到 3 笔付款了吗？"
  carries: ["failure_chain.warning_triggers", "decision.kill_criteria"]

self_check:
  root_chain: "否掉了『现金流』与『团队配置』，落在『没做过让人付钱这个决定』上"
  multi_view: "现金节奏(4)看是烧钱过快，需求验证(5)看是根没扎；两条指向不同修法，采信更靠前的那条"
  weighted: "需求验证 5 分 vs 团队能力 2 分，2.5 倍；只留一个留需求验证"
  worst_case: "若归因错成品质问题，下次照犯，损失量级与这次相同，占当时储备 70%，已超天花板，属不可承受"
  first_step: "整理原话并标注，今天 23:00 前，完成标志是两列表格"
  signals: "领先是招人前有 3 笔付款与用户主动复购，滞后是第 6 月留存"
  falsifier: "下个项目启动 6 周无任何真实付款，或我再用『这次不一样』解释例外"
```
