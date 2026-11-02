# 示例 5：这个剧本第二幕塌了

> 覆盖：`structure`（两头中间）· `lean`（结构问题是可逆的反复迭代）
> 演示重点：**结果倒推路径——先定弧线两头，再填中间；转折点是心脏，删得掉的就是过场。**

## 四轴

```yaml
settled: false
choose: false       # 不是选哪个方案，是结构修不好
multi: false
oneway: false
structure: true     # 附加判定轴
```

→ `flow: structure`　`mode: lean`

## answer

**结论**：第二幕塌不是"中间没戏"，是弧线的终点没定死——先把结尾改成一个不可逆的改变，再回头删事件。

**为什么**
1. 现在结尾是"主角终于敢上台"，但"敢上台"在第二幕就已经完成了，第三幕没有新的改变，所以第二幕显得又长又空。
2. 真正的心脏是"演砸之后没死"——它现在被埋在第五场，应该提到第三场。
3. 顺着倒推，能删掉两个与弧线无关的支线事件，第二幕自然就紧了。

**第一步**：今天把结尾句改成"主角把半成品当成品示人"，写死这一句。

**我会在什么情况下改主意**：改完后发现"演砸"这个转折与主角的恐惧（被看见）其实无关。

## payload

<!-- payload -->
```yaml
run:
  flow: structure
  modifiers: []
  mode: lean
  axes: {settled: false, choose: false, multi: false, oneway: false}
  reversibility: two-way

problem:
  one_line: "剧本第二幕拖沓空洞，第三幕没有新变化"
  owner: "我"
  by_when: "2026-04-10 交改稿"

answer:
  verdict: "不是中间没戏，是弧线终点没定死；先改结尾，再回头删事件"
  why:
    - "结尾的『敢上台』在第二幕已发生，第三幕没有新改变，所以第二幕显得空"
    - "真正的心脏是『演砸之后没死』，应从第五场提前到第三场"
    - "倒推后能删掉两个支线事件，第二幕自然收紧"
  first_step: "今天把结尾改写成『主角把半成品当成品示人』这一句，写死不动"
  what_would_change_my_mind: "改完发现『演砸』这个转折与主角的核心恐惧『被看见』无关"

root_chain:
  - question: "为什么第二幕看起来空？"
    candidate: "中间事件太少"
    status: rejected
    why: "事件有 7 个，不是少，是它们没有共同的因果指向，各自为政"
  - question: "为什么事件没有共同指向？"
    candidate: "弧线终点没定死，中间不知道该为哪件事服务"
    status: kept
    why: "一旦结尾是模糊的『获得成长』，任何事件都能被解释成在成长，等于没有筛选标准"

open_frontier: "我还没验证『演砸之后没死』这个转折，能不能同时完成『怕被看见』的恐惧线"

weights:
  - {dimension: "弧线（人物改变是否成立）", weight: 5, evidence: "现在结尾与第二幕重复，人物没有第二次改变", only_one: true}
  - {dimension: "人物动机", weight: 4, evidence: "主角的恐惧是『被看见』，但中间事件没有一件直接戳它", only_one: false}
  - {dimension: "节奏（事件密度）", weight: 2, evidence: "事件 7 个本身够用，密度不是问题", only_one: false}

strongest_counterargument: "也可能问题根本不在弧线，而在主角的对手不够强——第二幕的对抗强度不足，再好的弧线也走不出来"

decision:
  choice: "把转折点『演砸之后没死』提到第三场，删两个支线事件，结尾改成不可逆的改变"
  rationale: "结构问题用倒推解决：先钉死弧线两头，中间的事件就有了共同的筛选标准"
  confidence: mid
  kill_criteria:
    - "改完重读，若删掉转折点后结局依然成立，说明转折点还是选错了"
    - "若前两幕没有一件障碍直接指向『被看见』的恐惧"

plan:
  first_step: {verb: "改写", object: "结尾句为『把半成品当成品示人』", when: "今天 23:00 前", done_marker: "这一句写进文档并标注『已锁死』"}
  steps:
    - "把『演砸之后没死』从第五场挪到第三场，重排因果链"
    - "删掉与弧线无关的两个支线事件"
    - "逐对检查相邻事件的因果链"
  owner: "我"
  deadline: "2026-04-10"

arc:
  start: {lacks: "不知道自己真正想要什么", fears: "被看见", wants: "被认可"}
  end: {gains: "站上台的勇气", lets_go: "对完美的执念", becomes: "敢把半成品示人的人"}
  turn: "在第二轮公开选拨里主动演砸一次，然后发现没死"
  obstacles:
    - "第一次登台忘词，被观众笑"
    - "被对手当众羞辱『你就是个半吊子』"
    - "发现导师原来是自己『怕被看见』的化身"
  actions:
    - "把『我怕被看见』写成台词当众念出来"
    - "报名第二轮选拨，明知会演砸"
    - "演砸后主动公布练习过程，不再藏半成品"
  causal_ok: true

signals:
  system_turning:
    - "每个障碍都能直接戳中『怕被看见』，而不是泛泛的困难"
    - "删掉转折点后结局不再成立（说明转折点选对了）"
  outcome:
    - "第二幕与第三幕之间出现一次不可逆的人物改变"

unknowns:
  - unchecked: "『演砸』这个转折与恐惧线是否真相关"
    how: "把转折单独拎出来，问它服务的恐惧是哪一条"
    cost: "一次重读，30 分钟"
  - unchecked: "删掉的两个支线是否藏着必要的铺垫"
    how: "把铺垫信息并进主线事件，而不是保留支线"
    cost: "改稿时处理"

reentry:
  check_on: "2026-04-09（交稿前一天）"
  question: "删掉转折点后结局还成立吗？"
  carries: ["arc.turn", "decision.kill_criteria"]

self_check:
  root_chain: "否掉了『事件太少』，落在『弧线终点没定死导致中间没有筛选标准』"
  multi_view: "弧线(5)、人物动机(4)、节奏(2)三视角结论冲突：节奏看够用，动机看没戳中"
  weighted: "弧线 5 分 vs 节奏 2 分，2.5 倍；只留一个留弧线"
  worst_case: "改砸了还能再改，结构迭代是两向门，损失可忽略，未触发风控"
  first_step: "改写结尾句，今天 23:00 前，完成标志是写进文档并标『已锁死』"
  signals: "领先是障碍直接戳恐惧、转折删掉后结局不成立，滞后是两幕间出现不可逆改变"
  falsifier: "删转折点结局仍成立，或前两幕障碍没有一件指向『被看见』"
```
