# 示例 2：要不要辞职全职做账号

> 覆盖：`spiral` + `defensive` + `premortem` · `deep` · **不可逆** · 多方
> 演示重点：**"最坏情况占 60% > 天花板 50%"直接把最优选项打掉。**
> 这是本仓库最核心的一次演示：防守型决策选最稳，不选收益最高。

## 四轴

```yaml
settled: false
choose: true        # 辞 / 不辞 / 部分辞
multi: true         # 我 + 家庭现金流 + 未来的自己
oneway: true        # 辞了很难回到同一个位置
```

→ `flow: spiral`（多维并存，找转化）
→ `modifiers: [defensive, premortem]`（oneway 强制）
→ `mode: deep`

## answer

**结论**：不裸辞。用「3 个月副业验证 + 每月 4000 元投放预算」换一次真实答案。

**为什么**
1. 裸辞的最坏情况吃掉 60% 现金储备，超过 50% 的天花板——这个选项在数字上就不成立，跟信心无关。
2. 真正要回答的问题是"账号能不能养活我"，这件事不需要辞职才能测。
3. 但"边上班边做"确实会拖慢 3 个月，这个代价值得付，因为它把不可逆换成了可逆。

**第一步**：今天把副业账本建起来，记下当前月收入基数（现有副业 0 元）与可用时间。

**我会在什么情况下改主意**：连续 3 个月副业收入 ≥ 工资 60% 且增长未停。

## payload

<!-- payload -->
```yaml
run:
  flow: spiral
  modifiers: [defensive, premortem, collide]
  mode: deep
  axes: {settled: false, choose: true, multi: true, oneway: true}
  reversibility: one-way

problem:
  one_line: "要不要辞掉现在的工作，全职做短视频账号"
  owner: "我（与配偶共同决策）"
  by_when: "2026-04-30 季度述职前"

answer:
  verdict: "不裸辞，用 3 个月副业验证换真实答案"
  why:
    - "裸辞最坏情况吃掉 60% 现金，超过 50% 天花板，选项在数字上不成立"
    - "要回答的是账号能否养活我，这件事不需要辞职才能测"
    - "边做边测会拖慢 3 个月，这个代价值得付，因为它把不可逆换成可逆"
  first_step: "今天建副业账本，记下当前副业月收入基数（0 元）与每周可投入小时数"
  what_would_change_my_mind: "连续三个月副业收入达到工资的 60%，且第四个月仍在增长"

root_chain:
  - question: "为什么想辞职？"
    candidate: "上班占掉了做内容的时间"
    status: rejected
    why: "实测我每周有 22 小时可自由支配，时间不是主要瓶颈"
  - question: "那为什么产出还是少？"
    candidate: "上班消耗的是心力，不是时间"
    status: kept
    why: "这条成立，而且它指向的是『降低心力消耗』，不必然指向辞职"
  - question: "辞职能解决心力，但代价是什么？"
    candidate: "失去现金流后，内容会从表达变成求生，判断会变形"
    status: rejected
    why: "这是真实风险但无法事前验证，只能通过对比副业期与全职期的选题质量来看"

open_frontier: "如果副业 3 个月毫无起色，我仍不知道是『方向错』还是『投入不够』——这个区分还没设计出来"

opposing_forces:
  yang:
    - {claim: "全职后产出可能翻倍，三年窗口不能等", magnitude: "按现在 22 小时/周，全职约 50 小时/周，理论 +127%"}
    - {claim: "心力解放后选题会变，可能突破当前瓶颈", magnitude: "无法量化，但属于结构性质变而非量的增加"}
  yin:
    - {claim: "现金流断掉后被迫接商单，账号定位会漂移", magnitude: "现有储备 18 万 ≈ 12 个月，但会压缩到 6 个月内必须变现"}
    - {claim: "简历空窗一年，回职场要降级", magnitude: "同行案例里回退通常降 1 级，约 20-30% 薪资"}
  pivot: "当副业月收入连续 3 个月 ≥ 工资 60%，且第 4 个月环比仍正增长，就是『阴转阳』的极点；到那时辞职从赌博变成换挡"

weights:
  - {dimension: "现金流安全", weight: 5, evidence: "储备 18 万，家庭月支出 1.5 万，且配偶收入只覆盖房贷", only_one: true}
  - {dimension: "成长速度", weight: 4, evidence: "全职理论上能把周投入从 22 小时提到 50 小时", only_one: false}
  - {dimension: "时间自由度", weight: 2, evidence: "现在上班其实不打卡，自由度损失有限", only_one: false}

strongest_counterargument: "我在用『现金流』这个安全的理由，掩盖一个更难承认的事实：我的内容一年没有增长，跟时间无关，辞职只是把失败推迟到存款烧完那天"

decision:
  choice: "不裸辞。3 个月副业验证期 + 每月 4000 元投放预算，用数据决定是否辞职"
  rationale: "最稳解不是收益最高的解：裸辞的期望收益最高，但最坏情况吃 60% 现金超过 50% 天花板，破产风险不可接受；验证期把不可逆决策拆成 3 次可逆决策"
  confidence: mid
  kill_criteria:
    - "第 2 个月结束时副业收入仍为 0，且单条播放中位数没有环比上升"
    - "验证期内我每周实际投入不足 8 小时（说明问题不在工作，在我）"

plan:
  first_step: {verb: "建立", object: "副业账本与每周投入计时表", when: "今天 22:00 前", done_marker: "表格建好并填入本周基数"}
  steps:
    - "把内容生产固定到工作日 21:00-23:00 与周日上午"
    - "每月 1 号复盘：收入、播放中位数、单条制作时长"
    - "第 3 个月末做一次与述职无关的独立评审"
  owner: "我"
  deadline: "2026-07-31 验证期结束"

risks:
  worst_case: "辞掉工作、账号 6 个月无起色、存款烧到 40% 以下，被迫接不喜欢的商单，回职场降一级"
  loss: {amount: "18 万储备中的 11 万", unit: "元", share_of_resources: "60%", ceiling: "50%"}
  reversible: one-way
  mitigation: "把决策拆成 3 次可逆验证；验证期内每月只看领先信号不看收入"

premortem:
  failed_at: "2026 年 11 月，存款只剩 6 万时"
  causes:
    - "辞职后选题从『我想说』变成『能不能变现』，内容变味，老观众先走"
    - "为了现金流接了三个不想接的商单，账号标签被系统判定为泛商业号"
    - "没人给我定截止日期，产出反而比上班时更低"
  earliest_signal: "辞职后第 5 周，开始用『这条能不能变现』筛选题——这个念头出现就是信号"

signals:
  system_turning:
    - "每周能稳定产出 2 条且单条制作时长从 6 小时降到 4 小时"
    - "评论区开始出现陌生人的具体提问（不是熟人捧场）"
  outcome:
    - "副业月收入连续 3 个月 ≥ 工资 60%"

unknowns:
  - unchecked: "全职后我的实际周投入会不会真的到 50 小时"
    how: "用验证期的计时数据外推，而不是靠估计"
    cost: "需要在验证期完整记录 3 个月"
  - unchecked: "配偶对 12 个月无收入期的真实容忍度"
    how: "把最坏情况数字摆出来谈一次，要一个明确答复"
    cost: "一次谈话，但可能改变整个方案"

reentry:
  check_on: "2026-06-30（验证期第 2 个月末）"
  question: "副业收入是否 >0，且播放中位数环比上升？"
  carries: ["decision.kill_criteria", "signals.system_turning", "risks.loss"]

self_check:
  root_chain: "否掉了『时间不够』，落在『心力消耗』，并进一步否掉了『辞职是唯一解法』这条推断"
  multi_view: "现金流(5)与成长速度(4)结论相反：成长要快就得辞，安全要稳就不能辞，冲突未被抹平，靠 pivot 条件处理"
  weighted: "现金流 5 分 vs 时间自由度 2 分，2.5 倍；只留一个留现金流"
  worst_case: "损失 11 万占储备 60%，超过 50% 天花板，因此裸辞选项出局，改走验证期"
  first_step: "建账本，今天 22:00 前，完成标志是表格建好并填基数"
  signals: "领先是制作时长下降与陌生人提问，滞后是月收入达工资 60%"
  falsifier: "第 2 个月收入仍 0 且播放中位数没上升，或每周实际投入不足 8 小时"
```
