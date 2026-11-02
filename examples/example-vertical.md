# 示例 1：要不要花 6800 报一个剪辑课

> 覆盖：`vertical`（单线到底）· `lean` 模式 · 可逆决策 · 单方
> 演示重点：**可逆的小决策要快，但"快"不等于"不做根"**

## 四轴

```yaml
settled: false      # 还没报名
choose: true        # 报 / 不报，互斥
multi: false        # 只有我
oneway: false       # 报了也能退、也能自学
```

→ `flow: vertical`　`mode: lean`（可逆 + 单方 → 配快）
→ 没有 `defensive`，没有 `premortem`

## answer

**结论**：报，但只报首期，第三周没出成片就退。

**为什么**
1. 我卡的不是"不会剪"，是"没有交付感"——这事只有产出倒逼才治得了。
2. 6800 占我可用现金 8%，最坏情况能承受，不需要走风控。
3. 但课程的真实风险是"买了不看"，所以判定点是第 3 周的成片，不是结课。

**第一步**：今天 20:00 前付首期 6800，付款成功后拿到课表与作业提交入口。

**我会在什么情况下改主意**：开课后发现作业点评是 AI 批的、且没有公布排期。

## payload

<!-- payload -->
```yaml
run:
  flow: vertical
  modifiers: []
  mode: lean
  axes: {settled: false, choose: true, multi: false, oneway: false}
  reversibility: two-way

problem:
  one_line: "要不要花 6800 报一个为期 8 周的剪辑课"
  owner: "我"
  by_when: "2026-03-08 开课前"

answer:
  verdict: "报首期，第三周没出成片就退"
  why:
    - "卡的是交付感不是技术，需要产出倒逼"
    - "6800 占可用现金 8%，最坏情况可承受"
    - "真实风险是买了不看，判定点放在第 3 周"
  first_step: "今天 20:00 前付首期 6800，拿到课表与作业入口"
  what_would_change_my_mind: "开课后发现作业点评是 AI 批的，且没有公布点评排期"

root_chain:
  - question: "为什么想报课？"
    candidate: "剪辑技术不够，需要系统学一遍"
    status: rejected
    why: "我去年已经自学完基础剪辑，能独立出片，技术不是卡点"
  - question: "那为什么还是出不了片？"
    candidate: "没有交付节奏，作品停在没有截止日期的状态"
    status: rejected
    why: "这个原因成立，但它指向的是『找个截止日期』，不一定指向报课"
  - question: "报课真正提供的是什么？"
    candidate: "一个不可协商的外部截止日期 + 同侪压力"
    status: kept
    why: "这是我自己造不出来的东西，也是唯一值 6800 的部分"

open_frontier: "我还没验证『同侪压力』对我是否有效——过去两次打卡社群我都中途退出了"

weights:
  - {dimension: "能不能逼我按时出片", weight: 5, evidence: "过去 6 个月我自学产出 0 条成片", only_one: true}
  - {dimension: "课程内容本身的新增知识", weight: 2, evidence: "大纲里 80% 我已会", only_one: false}
  - {dimension: "同学的行业资源", weight: 3, evidence: "上一期学员里有 2 个在接商单", only_one: false}

strongest_counterargument: "我过去两次付费社群都中途退出，说明我买的不是截止日期，是『我已经努力了』的安心感"

decision:
  choice: "报首期，设第 3 周为退出点"
  rationale: "唯一值得买的交付节奏可以用一个 3 周的截止日期检验，检验不过就退，损失只有时间"
  confidence: mid
  kill_criteria:
    - "第 3 周结束还没有交出第一条完整成片"
    - "开课后发现作业点评由 AI 批量生成且无排期"

plan:
  first_step: {verb: "支付", object: "首期学费 6800 元", when: "今天 20:00 前", done_marker: "支付成功截图 + 收到课表"}
  steps:
    - "把第 3 周作业的截止日写进日历，设两个提醒"
    - "先剪一条 30 秒旧素材练手，确认工具链没坏"
  owner: "我"
  deadline: "2026-05-03 结课"

signals:
  system_turning:
    - "第 3 天我能不看教程独立导出一条成片"
    - "每周至少一次主动打开工程文件（不用提醒）"
  outcome:
    - "第 8 周结束时手上有 1 条能发出去的成片"

unknowns:
  - unchecked: "老师最近三个月是否还在更新课程"
    how: "翻课程目录最后更新时间和最近一次直播回放"
    cost: "10 分钟"
  - unchecked: "退费条款是否包含『已开课』情况"
    how: "下单前把退费条款截图存档"
    cost: "5 分钟"

reentry:
  check_on: "2026-04-05（第 3 周作业截止后 48 小时）"
  question: "我交出第一条完整成片了吗？"
  carries: ["signals.system_turning", "decision.kill_criteria"]

self_check:
  root_chain: "否掉了『技术不够』和『没系统学过』两条，最后落在『买的是外部截止日期』这个可验证的假设上"
  multi_view: "三个维度分别看内容价值(2)、同侪资源(3)、交付压力(5)，结论指向同一处，但分数差距大"
  weighted: "交付压力 5 分 vs 内容 2 分，差 2.5 倍；只留一个就留交付压力"
  worst_case: "6800 损失 + 8 周时间，占可用现金 8%，远低于 30% 天花板；本决策可逆，未展开"
  first_step: "支付 + 拿到课表，今天 20:00 前，完成标志是截图与课表"
  signals: "领先信号是『不看教程能导出』和『主动打开工程』，滞后信号是第 8 周有成片，两者不同"
  falsifier: "第 3 周没出成片，或点评是 AI 批量生成 → 停掉改自学"
```
