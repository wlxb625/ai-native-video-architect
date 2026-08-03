# Test Learning Abstraction Protocol V4.5

## 目标

本协议规定如何从用户提供的参考图、参考视频、生成结果和项目实测中学习，而不把单一项目的具体美学、镜头顺序、材质、灯光或运镜固化为整个Skill的默认规则。

核心原则：

> 案例是证据，不是模板；Skill学习的是选择维度、条件化策略与冲突处理，不是复制案例答案。

## 一、适用范围

用户提供以下任一内容并要求参考、测试、总结或改进Skill时启用：

- 完整AI视频；
- 单镜头视频；
- 分镜、关键帧或生成图；
- 成熟影视、广告、MV、实验影像或动画案例；
- 当前Skill生成的测试结果；
- 同一项目多轮生成对照。

## 二、四层抽象

### L1 项目事实层

只记录案例实际采用的手法，不评价其是否应成为通用规则。

```yaml
project_observations:
  narrative_context:
  audience_effect:
  composition:
  performance:
  camera:
  lighting:
  environment:
  material:
  motion:
  editing:
  sound:
```

例如“主体先动、摄影机后跟”“流体经过区域出现高光”只属于该层。

### L2 可迁移机制层

回答这些具体手法解决了什么导演问题。

```yaml
transferable_mechanisms:
  problem_addressed:
  mechanism:
  observable_result:
  failure_without_mechanism:
```

例如可抽象为：多个视觉系统需要明确主次、时间关系与能量传递，避免无意独立随机运动。

### L3 条件化策略空间

把单一做法扩展为多个合法选择，而不是把案例答案设为默认。

```yaml
conditional_strategy_space:
  decision_dimension:
  available_strategies: []
  enabling_conditions: []
  conflicting_conditions: []
  project_specific_other_allowed: true
```

例如摄影机可以领先、跟随、同步、保持、抵抗、揭示或故意失配，具体由项目选择。

### L4 项目选择规则层

根据当前项目的剧本、观众关系、场景功能、情绪、形式目标、平台、时长和生成条件，筛选最合适的策略。

```yaml
project_selection:
  project_evidence: []
  selected_strategy:
  rejected_strategies_and_reasons: []
  expected_audience_effect:
  implementation_constraints:
  continuity_implications:
```

## 三、学习分类报告

每次案例测试完成后必须输出：

```yaml
test_learning_report:
  test_id:
  source_type:
  project_specific_tactics: []
  transferable_mechanisms: []
  conditional_strategies: []
  non_transferable_aesthetic_signatures: []
  conflicts_with_existing_rules: []
  rules_that_should_be_weakened: []
  rules_that_should_be_strengthened: []
  new_selection_dimensions: []
  unresolved_questions: []
  recommended_core_changes: []
  recommended_case_library_entries: []
```

### 可进入核心Skill

- 可迁移机制；
- 条件化策略；
- 新的选择维度；
- 跨类型重复出现的失败模式；
- 冲突解决规则；
- 适用条件和不适用条件。

### 不得直接进入核心Skill

- 当前项目专属色彩；
- 当前项目专属母题；
- 某一种材质；
- 某一种人物形象；
- 某一种固定运镜顺序；
- 某一种固定灯光响应；
- 当前案例独有的审美符号；
- 未经横向验证的单次生成偏好。

这些内容可以进入案例库，但必须标记`CASE_SPECIFIC`。

## 四、横向压力测试

新规则正式进入核心Skill前，至少使用三种具有明显差异的项目条件进行测试。推荐覆盖：

- 现实主义人物关系；
- 悬疑或恐怖；
- 喜剧或荒诞；
- 动作或爽感释放；
- 抽象、MV或视觉奇观；
- 广告或品牌表达。

测试不是要求所有策略在所有项目中成立，而是检查：

1. 规则是否允许不同答案；
2. 选择条件是否能解释差异；
3. 是否出现固定美学污染；
4. 是否与现有导演、摄影、灯光、表演和连续性规则冲突；
5. 是否能在Prompt中落地，而不是只停留在理论层。

## 五、规则升级门槛

一条学习结论只有同时满足以下条件，才能升级为核心规则：

- 不依赖单一题材、风格、颜色、材质或人物类型；
- 至少在三类差异项目中具有解释力；
- 允许多个合法导演答案；
- 有明确的选择条件；
- 有冲突与拆分机制；
- 能被转译为可观察、可生成或可验证的输出；
- 不改变`NARRATIVE_LOCK`；
- 不与项目视觉策略的创作中立原则冲突。

不满足时，保持为：

```text
CASE_SPECIFIC
HYPOTHESIS
EXPERIMENTAL_OPTION
```

不得伪装成硬规则。

## 六、去过拟合检查

每次提交Skill改动前检查：

- 是否把案例里的具体名词写成默认；
- 是否把一个项目的先后顺序写成所有项目的因果；
- 是否把一种摄影、灯光或环境关系写成唯一正确答案；
- 是否只增加了“禁止某模板”，却没有开放替代策略；
- 是否给新策略写了适用和不适用条件；
- 是否保留`PROJECT_SPECIFIC_OTHER`通道；
- 是否允许有意断裂、静止、忽视、对抗和非同步；
- 是否用多个差异案例测试过。

任一项失败，结论不得进入核心规则。

## 七、与正式工作流的关系

```text
案例或生成结果
→ 项目事实记录
→ 可迁移机制提取
→ 条件化策略空间
→ 横向压力测试
→ 冲突与适用条件检查
→ 核心Skill增量 / 案例库 / 保留假设
```

当用户要求完善整个项目时，应先完成以上抽象和横向验证，再修改核心模块；不得围绕同一案例不断增加专属字段。