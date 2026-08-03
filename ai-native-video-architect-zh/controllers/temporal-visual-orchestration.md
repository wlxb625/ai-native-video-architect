# Temporal Visual Orchestration Controller V4.5

## 目标

在现有导演、摄影、灯光、表演、环境、材质、声音与剪辑系统之间建立项目专属的时序和关系编排。

本模块不规定“谁必须先动”“摄影机必须跟随”“灯光必须响应人物”或“背景必须与人物同步”。它要求导演根据当前项目证据，从多个合法策略中选择，并解释这种关系为何适合当前镜头或序列。

核心问题：

> 人物、环境、摄影机、灯光、声音、道具、材质和剪辑之间，谁主导、谁响应、谁保持、谁对抗、谁故意脱节，以及观众为什么需要这种关系？

## 一、启用范围

### 必须启用

- 两个以上视觉或听觉系统在同一镜头中明显变化；
- 人物动作与环境、材质、灯光或摄影机存在关系；
- 视觉序列、MV、抽象段落、奇观、梦境、仪式、动作高潮；
- 镜头内部需要建立、发展、峰值和收束；
- 相邻镜头依赖运动、形状、节奏、光色、声音或语义接力；
- 实测出现“人物动人物的、背景动背景的”或“漂亮静态图只是分别摇动”的问题。

### 简化启用

单一人物微动作、固定机位对话或纯功能性镜头，只需明确主导者、摄影机角色、环境关系和结束状态，不强制复杂能量传递。

## 二、导演形式

```yaml
directing_form:
  mode: NARRATIVE_DRIVEN | VISUAL_SEQUENCE_DRIVEN | HYBRID
  project_or_sequence_scope:
  evidence: []
  dominant_communication:
  must_not_sacrifice: []
```

- `NARRATIVE_DRIVEN`：事实、人物行动、关系和信息因果优先；
- `VISUAL_SEQUENCE_DRIVEN`：形式、母题、运动、材质、节奏和感知体验优先；
- `HYBRID`：叙事行动与视觉序列共同承担表达。

这是导演形式字段，不是新的顶层操作模式。

## 三、主导权

```yaml
agency_map:
  dominant_agency: CHARACTER | ENVIRONMENT | CAMERA | LIGHT | SOUND | EDIT | OBJECT | GROUP | NONE | PROJECT_SPECIFIC
  secondary_agencies: []
  passive_or_resistant_systems: []
  agency_shift_during_shot:
  director_reason:
  audience_effect:
```

可能的合法关系包括但不限于：

- 人物发起，环境响应；
- 环境发起，人物被迫反应；
- 摄影机先发现，人物尚未察觉；
- 声音先出现，画面延迟揭示；
- 道具状态变化主导人物动作；
- 灯光变化先于事件，形成预兆；
- 剪辑建立因果，而单镜内部保持中性；
- 没有单一主导者，多系统由同一形式规则驱动。

不得默认人物拥有主导权。

## 四、耦合方式

```yaml
coupling_design:
  participating_systems: []
  mode: CAUSAL | SYNCHRONOUS | ANTICIPATORY | DELAYED | COUNTERPOINT | RESISTANT | PARTIALLY_DECOUPLED | INDEPENDENT | PROJECT_SPECIFIC
  relation_description:
  intended_readability:
  acceptable_ambiguity:
  accidental_disconnect_risk:
```

### CAUSAL

一个系统的可见变化触发另一个系统。必须看得出原因和响应。

### SYNCHRONOUS

多个系统同时变化，适合统一、仪式、机械秩序、群体行动或形式节奏。同步必须有规则，不能只是所有元素一起摇动。

### ANTICIPATORY

摄影机、声音、灯光或环境先于人物或事件变化，用于预兆、信息优势或观众先知位置。

### DELAYED

响应故意滞后，用于重量、规模、喜剧反应、迟来的情绪或世界惯性。

### COUNTERPOINT

两个系统在方向、节奏、情绪或意义上形成对位。例如人物崩溃而环境保持日常，或欢快音乐覆盖危险画面。

### RESISTANT

摄影机、环境、光线或道具拒绝顺从主体，强调阻力、冷漠、压迫或控制失败。

### PARTIALLY_DECOUPLED

部分关联、部分独立，适合复杂现实、精神分裂、主观感知或多层叙事。

### INDEPENDENT

各系统独立，但必须是有意设计并对观众有效。若无法说明理由，通常属于随机漂移。

## 五、时序角色

### 摄影机

```yaml
camera_temporal_role:
  role: LEAD | FOLLOW | SYNCHRONIZE | HOLD | RESIST | REVEAL | DESTABILIZE | PROJECT_SPECIFIC
  start_relation:
  delay_or_lead_time:
  motion_reason:
  stop_condition:
  competing_motion_control:
```

### 灯光

```yaml
light_event_relation:
  role: REVEAL | FOLLOW | ANTICIPATE | CONTRADICT | ISOLATE | IGNORE | STABILIZE | PULSE_WITH | PROJECT_SPECIFIC
  trigger:
  lead_or_delay:
  affected_story_area:
  physical_or_formal_rule:
  emotional_effect:
  continuity_limit:
```

### 环境

```yaml
environment_relation:
  role: SUPPORT | RESPOND | INITIATE | OPPOSE | IGNORE | CONTAIN | DELAY | MIRROR | MISLEAD | COLLAPSE | REMAIN_NEUTRAL | PROJECT_SPECIFIC
  trigger_or_independence:
  layer_order:
  strength_curve:
  relation_to_subject:
  end_state:
```

### 声音

```yaml
sound_temporal_role:
  role: LEAD | FOLLOW | SYNCHRONIZE | COUNTERPOINT | BRIDGE | WITHHOLD | PROJECT_SPECIFIC
  cue:
  phrase_relation:
  reveal_relation:
  cut_relation:
```

这些枚举是策略空间，不是固定答案。允许`PROJECT_SPECIFIC`，但必须写清可观察规则。

## 六、能量与信息传递

```yaml
energy_information_transfer:
  source:
  carriers: []
  receiver:
  transfer_type: FORCE | MOTION | ATTENTION | LIGHT | COLOR | SOUND | EMOTION | SEMANTIC | PROJECT_SPECIFIC
  amplification_or_decay:
  interruption_or_resistance:
  peak_owner:
  residual_state:
```

“能量传递”不要求真实物理接触，也可以是注意力、情绪、语义或剪辑关系。只有项目需要时才使用流体、衣料、粒子或变形。

## 七、感知连续通道

相邻状态或镜头不要求固定继承形状、方向或速度。必须选择一个或多个连续通道，或者明确把断裂作为意图。

```yaml
perceptual_continuity_channels:
  shape:
  motion:
  rhythm:
  color:
  brightness:
  material:
  spatial_position:
  scale:
  semantic_motif:
  gaze_or_action:
  sound:
  emotional_energy:
  intentional_discontinuity:
  discontinuity_reason:
```

连续不是越多越好。应选择最能服务当前切镜理由的通道。

## 八、镜头内发展

每个适用Shot必须建立：

```yaml
shot_orchestration:
  initial_relation:
  initiating_system:
  first_change:
  response_order: []
  lead_and_delay_values: []
  dominant_spatial_relation:
  development:
  peak:
  settling_or_cut:
  exact_end_relation:
  handoff_channels: []
```

镜头可以采用：

- 起势—响应—放大—峰值—收束；
- 预兆—等待—揭示—冻结；
- 同步建立—突然脱节；
- 环境持续—人物短暂反抗—环境恢复；
- 摄影机发现—人物察觉—声音确认；
- 静止对抗—一个系统破坏平衡；
- 其他项目专属结构。

不得把某一种发展结构写成所有镜头默认。

## 九、序列级变化与呼吸

```yaml
sequence_orchestration:
  sequence_id:
  directing_form:
  governing_relation:
  relation_variations: []
  motif_or_rule_variations: []
  density_curve: []
  motion_energy_curve: []
  information_curve: []
  emotional_curve: []
  breathing_points: []
  climax_relation:
  final_residual_state:
```

整段序列不能只重复同一关系。例如全部镜头都是“人物先动—背景响应—摄影机跟随”，会形成机械模板。应根据段落发展改变主导权、延迟、尺度、连续通道或耦合方式，但变化必须有导演理由。

## 十、项目选择步骤

1. 读取`NARRATIVE_LOCK`、`PROJECT_VISUAL_STRATEGY`和Shot场景功能；
2. 判断观众需要知道、感到、误判、等待还是被冲击；
3. 判断哪个系统最适合拥有当前主导权；
4. 从耦合方式中选择关系；
5. 分别决定摄影机、灯光、环境和声音的时序角色；
6. 选择镜头内发展结构；
7. 选择跨镜头连续通道或有意断裂；
8. 检查是否出现系统竞争、随机同步或无动机变化；
9. 将结论编译进视频Prompt和连续性传递。

## 十一、冲突处理

出现以下冲突时不得靠继续加Prompt解决：

- 微表演需要静止观察，但环境和摄影机都要求高强度运动；
- 观众应先发现危险，但灯光和景深完全隐藏异常；
- 人物应被环境忽视，Prompt却让环境同步回应；
- 喜剧依赖延迟反应，但所有系统同时动作；
- 现实主义要求世界稳定，视觉效果却无原因跟随情绪；
- 有意断裂被连续性规则错误修平；
- 多个系统争夺峰值，没有主次。

处理顺序：降低从属系统强度 → 改变时序角色 → 更换连续通道 → 拆镜 → 分层或后期。

## 十二、编译要求

最终视频Prompt不能只列并列动作，必须写清：

- 主导系统；
- 参与系统；
- 耦合方式；
- 谁先、谁后、谁保持或对抗；
- 摄影机、灯光、环境和声音的角色；
- 镜头内发展和峰值；
- 精确结束关系；
- 交给下一镜的连续通道。

但不得机械输出枚举名。必须转译为当前项目可见、可听、可执行的自然语言。

## 十三、硬失败

- 把单一案例顺序写成默认；
- 未根据项目证据选择主导权；
- 人物、环境、摄影机、灯光和声音无意各自随机运动；
- 所有系统同时高强度变化，没有主次；
- 摄影机、灯光或环境响应与导演意图冲突；
- 使用`PROJECT_SPECIFIC`却没有可观察规则；
- 连续性只能靠相同配色，切镜理由不成立；
- 有意断裂没有理由，或需要断裂却被机械匹配；
- 同一序列机械重复同一种耦合关系；
- 最终Prompt仍只是“人物动、背景动、镜头动”的并列清单。