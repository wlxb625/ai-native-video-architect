# DIAGNOSE Mode

只分析作品为什么成立或失效，默认不直接重写。

## 五类发现

- BUG：非预期错误。
- RISK：当前成立但可能失效。
- CHOICE：有意设计，应保护。
- OPPORTUNITY：可选增强。
- PREFERENCE：审美、市场或受众偏好。

## 优先级

P0基础失控；P1核心体验；P2表达效率；P3可选优化。

高概念任务的P1优先顺序：

1. 一句话概念；
2. 单一核心机制；
3. 单一人物任务；
4. 艰难选择；
5. 奇观因果；
6. 最后残像；
7. 其他世界观细节。

不得先纠结术语、镜头风格或设定漏洞，而忽略主线无法复述。

## 每项发现必须包含

位置、证据、已建立规则、影响、最小修复、较强方向、must_protect和下一模式。

## 高概念诊断输出

当适用性为HIGH或MEDIUM时，额外输出：

```yaml
high_concept_diagnosis:
  current_retell_sentence:
  strongest_unique_idea:
  competing_core_ideas: []
  primary_task:
  task_confusion:
  core_mechanism:
  extra_mechanisms: []
  impossible_choice:
  choice_bypass:
  causal_hero_shots: []
  decorative_spectacles: []
  predictable_twist:
  final_afterimage:
  worldbuilding_to_remove_or_merge: []
```

诊断时优先回答：

- 观众会怎样向别人介绍这部片？
- 目前最值得保留的唯一概念是什么？
- 哪些好点子正在互相争夺主角位置？
- 主角到底在做哪一件事？
- 视觉奇观是否改变了剧情？
- 高潮是否真的要求人物选择？
- 结尾是否留下了选择后果？

## 路由

- 改人物、结构、高潮、结尾、机制或热梗结构：TRANSFORM。
- 压缩并列机制、重新建立任务和艰难选择：TRANSFORM LEVEL_2或LEVEL_3。
- 只需拆镜头、后期文字、声音、资产或重剪：ADAPT。
- 只需集中3—5个HERO_SHOT且不改剧情：ADAPT。
- 仅是偏好或可接受风险：NONE。

## 诊断禁止

- 因概念复杂就默认改成简单俗套；
- 因没有反转就强制添加身份反转；
- 把所有超现实画面都判为问题；
- 只说“节奏慢、信息多”，不指出具体 competing core ideas；
- 在用户要求只诊断时直接输出完整替代剧本。