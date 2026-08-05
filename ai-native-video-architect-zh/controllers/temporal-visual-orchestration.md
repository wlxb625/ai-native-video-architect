# Temporal Visual Orchestration Controller V4.5

## 目标

统筹人物、环境、摄影机、灯光、声音、道具与剪辑之间的**主导权、先后顺序、耦合关系和跨镜接力**。

本模块是协调层，不是摄影、灯光、表演、环境或连续性模块的替代品。它只回答：

> 谁先变化，谁响应、保持、对抗或故意脱节；这种关系为什么适合当前镜头；关系最终如何交给下一镜。

## 一、职责边界

本模块负责：

- 导演形式：叙事驱动、视觉序列驱动或混合；
- 当前镜头或序列的主导系统；
- 系统之间的因果、同步、预示、延迟、对位、抵抗、部分脱节或独立关系；
- 摄影机、灯光、环境和声音相对主事件的时序角色；
- 镜头内关系的发展、峰值、收束和精确结束关系；
- 相邻镜头通过哪些感知通道接力，或为何有意断裂。

以下内容由原模块负责，本模块只引用结果，不重复填写：

- 景别、焦段、机位、构图、运镜幅度和终点：`camera-director.md`；
- 光源位置、光质、色温、光比、阴影与曝光：`lighting-director.md`；
- 视线、呼吸、手部、重心、微表情和情绪节拍：`performance-director.md`；
- 人物知识、道具归属、伤损、空间、动作完成度与跨镜状态：`continuity-repair-system.md`；
- 场景结构、材质、背景大形和项目美学：`project-visual-strategy.md`及相关美术模块；
- 声音素材、混音和剪辑参数：声音与后期模块。

不得在本模块中重新写一套摄影参数、完整灯光合同、完整表演时间轴或连续性台账。

## 二、启用判断

### 完整启用

出现以下任一情况：

- 同镜头两个以上系统明显变化；
- 人物、环境、摄影机、灯光或声音存在明确先后、响应、对抗或脱节；
- 视觉序列、MV、梦境、奇观、动作高潮、复杂转场；
- 相邻镜头依赖运动、声音、视线、亮度、空间、语义或情绪接力；
- 生成结果容易出现“人物动人物的、背景动背景的”。

### 简化启用

普通叙事镜头只需确认：

- 谁主导；
- 摄影机相对事件是保持、领先、跟随还是其他关系；
- 环境和灯光是否响应；
- 本镜关系如何结束并交给下一镜。

### 不需要

静态资产板、纯结构图、无时间变化的单张图片和纯后期字幕，可标记：

```yaml
orchestration_required: false
reason:
```

不强迫为简单任务填写空洞字段。

## 三、导演形式

```yaml
directing_form:
  mode: NARRATIVE_DRIVEN | VISUAL_SEQUENCE_DRIVEN | HYBRID
  scope:
  evidence:
  must_not_sacrifice: []
```

- `NARRATIVE_DRIVEN`：人物行动、事实、关系和信息因果优先；
- `VISUAL_SEQUENCE_DRIVEN`：形式、母题、运动、材质、节奏和感知体验优先；
- `HYBRID`：叙事推进与视觉序列共同承担表达。

这是当前项目或段落的导演判断，不是新的顶层操作模式。

## 四、主导权与耦合方式

### 主导系统

```text
CHARACTER | ENVIRONMENT | CAMERA | LIGHT | SOUND | EDIT | OBJECT | GROUP | NONE | PROJECT_SPECIFIC
```

主导权表示“谁首先改变观众对画面的理解或推动事件”，不等于谁运动幅度最大。

### 耦合方式

```text
CAUSAL | SYNCHRONOUS | ANTICIPATORY | DELAYED | COUNTERPOINT | RESISTANT | PARTIALLY_DECOUPLED | INDEPENDENT | PROJECT_SPECIFIC
```

- `CAUSAL`：一个变化触发另一个变化；
- `SYNCHRONOUS`：多个系统服从共同节拍或规则；
- `ANTICIPATORY`：某系统先于人物或事件提供预兆；
- `DELAYED`：响应故意滞后，表现重量、规模、迟来的情绪或喜剧节拍；
- `COUNTERPOINT`：方向、节奏、情绪或语义形成对位；
- `RESISTANT`：某系统拒绝顺从主体，形成阻力或压迫；
- `PARTIALLY_DECOUPLED`：部分连续、部分错位；
- `INDEPENDENT`：系统按各自规律运行，但独立必须具有导演意义；
- `PROJECT_SPECIFIC`：使用当前项目专属规则，并写清可观察结果。

## 五、相对时序角色

这些角色只定义“相对主事件的关系”，不替代原模块的具体执行参数。

### 摄影机

```text
LEAD | FOLLOW | SYNCHRONIZE | HOLD | RESIST | REVEAL | DESTABILIZE | PROJECT_SPECIFIC
```

### 灯光

```text
REVEAL | FOLLOW | ANTICIPATE | CONTRADICT | ISOLATE | IGNORE | STABILIZE | PULSE_WITH | PROJECT_SPECIFIC
```

### 环境

```text
SUPPORT | RESPOND | INITIATE | OPPOSE | IGNORE | CONTAIN | DELAY | MIRROR | MISLEAD | COLLAPSE | REMAIN_NEUTRAL | PROJECT_SPECIFIC
```

### 声音

```text
LEAD | FOLLOW | SYNCHRONIZE | COUNTERPOINT | BRIDGE | WITHHOLD | PROJECT_SPECIFIC
```

选择角色后，具体机位、光源、表演和声音设计回到对应模块完成。

## 六、Shot级最小合同

完整启用时只记录以下协调信息：

```yaml
orchestration_decision:
  required: true
  evidence:
  dominant_agency:
  participating_systems: []
  coupling_mode:
  initial_relation:
  first_change:
  response_order: []
  camera_relative_role:
  light_relative_role:
  environment_relative_role:
  sound_relative_role:
  peak_owner:
  settling_or_cut:
  exact_end_relation:
  continuity_channels: []
  intentional_discontinuity:
  conflict_or_delegation_note:
```

约束：

- `response_order`只写系统级顺序，不重复人物身体部位动作；
- 相对角色只写“领先、保持、跟随、对抗”等关系，不重复参数；
- `exact_end_relation`描述系统之间最终处于什么关系，人物和道具精确尾态由连续性台账记录；
- `continuity_channels`只选择真正承担接力的通道，不必全部填写。

可用连续通道包括：

```text
shape | motion | rhythm | color | brightness | material | spatial_position |
scale | semantic_motif | gaze_or_action | sound | emotional_energy
```

也可以明确使用有意断裂。

## 七、序列级变化

```yaml
sequence_orchestration:
  sequence_id:
  directing_form:
  governing_relation:
  relation_variations: []
  density_curve: []
  motion_energy_curve: []
  information_curve: []
  emotional_curve: []
  breathing_points: []
  climax_relation:
  final_residual_state:
```

序列级字段只用于控制关系变化和节奏呼吸，不替代每镜摄影、灯光、表演或连续性设计。

同一段不能机械重复“人物先动—环境响应—摄影机跟随”。变化也不能为了丰富而随机，必须由剧情、观众位置或形式规则驱动。

## 八、选择步骤

1. 读取`NARRATIVE_LOCK`、项目视觉策略、Shot场景功能和连续性台账；
2. 判断观众此刻需要知道、感到、等待、误判还是被冲击；
3. 确定谁拥有主导权；
4. 选择耦合方式；
5. 选择摄影机、灯光、环境和声音相对主事件的角色；
6. 确定关系如何发展、由谁承担峰值、如何结束；
7. 选择交给下一镜的连续通道或有意断裂；
8. 把具体执行交给摄影、灯光、表演、环境、声音和连续性模块。

## 九、冲突处理

出现系统竞争时按以下顺序处理：

```text
确认本镜唯一任务
→ 降低从属系统强度
→ 调整先后或延迟
→ 更换相对角色
→ 更换接力通道
→ 拆镜或分层生成
```

不得靠继续堆叠字段和Prompt文字解决以下问题：

- 微表演需要静止观察，但摄影机和环境都高强度运动；
- 观众应先发现危险，但构图和灯光完全隐藏危险；
- 环境应保持中性，却被写成自动回应人物；
- 喜剧依赖延迟，所有系统却同时动作；
- 多个系统同时争夺峰值；
- 有意断裂被连续性规则机械修平。

## 十、硬失败

- 把一个参考案例的运动顺序设为通用默认；
- 本模块重复填写焦段、机位、灯光参数、微表演或完整连续性台账；
- 每个镜头都强制使用完整编排块；
- 只有枚举标签，没有项目证据和可观察关系；
- 人物、环境、摄影机、灯光和声音无意各自随机运动；
- 所有系统同时高强度变化，没有主次；
- 同一序列机械重复同一种响应链；
- 最终Prompt仍只是多个动作的并列清单；
- 为了“视觉流动”破坏剧情事实、镜头设计或跨镜状态连续。