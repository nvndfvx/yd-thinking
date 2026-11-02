# YD Thinking

一套用于**复杂问题分析、决策、风险排查与复盘**的推理技能（agent skill）。

不是"思维模型笔记合集"，而是一个**会拒绝的分析器**：它给最稳解 + 验证标准 + 证伪条件，信息不足时宁可拒答，不硬编。

## 一句话

> 追是方向，压是力度，判要能推翻。

## 什么时候用（触发词）

- 「我要不要 / 该不该选 X」「值不值得投入 / 学」
- 「这件事为什么做不起来」「我该怎么突破」
- 「帮我追根因」「这个方案有什么风险」
- 「帮我复盘这次失败」「为什么我总是三分钟热度」
- 「这个剧本 / 内容第二幕塌了」

**不用于**：知识问答、情绪陪聊、写文档。

## 30 秒看它做了什么

输入："我的视频号做了 8 个月还是起不来。"

别的工具会回"多拍、蹭热点、优化封面"。
本技能会回：

```
结论：不是拍得少，是没有一个『看完想找你』的落点。补落点，别加频率。
第一步：今天列完播率最高的 3 条，写下它们各自是写给谁的。
改主意的条件：连续 10 条都写给具体的人，完播率仍低于 25%。
```

区别不在结论，在**结论被追过根、排过权重、还附了一个能推翻它的条件**。

## 安装

把本目录放进你的 agent skills 目录（以 Claude Code 为例）：

```bash
git clone <repo-url> ~/.claude/skills/yd-thinking
```

DSH 用户放进 `D:\dsh-home\skills\yd-thinking\`，并在技能索引里登记。

## 目录结构

```
SKILL.md                 入口：公理 + 四轴路由 + 加载顺序 + 七道门禁
kernel/principles.md     六条公理长版（含可证伪要求）
router/axes.yaml         四轴路由表（机器可读）
router/fallback.md       轴判不出来时的降级与拒答
orchestrator/state-machine.md
compiler/schema.yaml     输出契约（唯一真相）
templates/output.md      输出模板（由 schema 派生）
guardrails/checklist.yaml 七道门禁的可检验定义
operators/
  verbs/                 frame / decompose / weigh / trace / collide / choose
  flows/                 vertical / spiral / diagnose / retro / structure / defensive
  lenses/                failure-list / premortem
  loop/                  feedback
examples/                6 个跨域完整示例（含 1 个"拒答"）
evals/                   cases.jsonl + run.py + CI（无需 LLM 的结构自检）
```

## 设计原则

> **Kernel 内联不可变，Operators 按需加载，Router 用 4 个可判的轴，Compiler 固定，Guardrails 交证据不交布尔，Evals 可回归。**

## 测试

```bash
pip install pyyaml
python evals/run.py
```

CI 在每次 push 跑同一套检查。

## 许可

代码（`evals/run.py`）：MIT
文档（其余全部）：CC BY 4.0
