# AI Production Controller

## 目标

把已成立的概念、视觉叙事与镜头语言转译为可生成、可连续、可剪辑、可修复的AI视频生产方案。

禁止在视觉身份、角色和空间尚未锁定前直接批量写视频提示词。

## 生产前置

必须先建立：

- Visual Bible：色彩、光线、材质、空间尺度、摄影基调；
- Character Lock：外观、服装、标志物、动作习惯、禁止漂移项；
- Environment Lock：建筑结构、光源方向、关键物件位置、时间和天气；
- Shot Contract：每个镜头的输入状态与输出状态。

## 视觉圣经最小字段

```yaml
visual_bible:
  aspect_ratio:
  palette:
  lighting_rules:
  material_rules:
  atmosphere:
  spatial_scale:
  camera_temperament:
  texture_and_grain:
  forbidden_drift:
```

## 角色锁定

```yaml
character_lock:
  identity:
  age_range:
  face_features:
  hair:
  clothing:
  colors:
  signature_object:
  movement_habit:
  emotional_baseline:
  allowed_changes:
  forbidden_changes:
  reference_assets:
```

后续提示词引用同一角色身份和参考资产，不为每个镜头重新发明外貌。

## 场景锁定

```yaml
environment_lock:
  space_name:
  layout:
  fixed_landmarks:
  entrance_and_exit:
  light_direction:
  time_state:
  weather_or_particles:
  allowed_changes:
  forbidden_changes:
```

## 镜头工程

每个镜头必须说明：

- 上一镜结束时人物、物件和空间状态；
- 本镜只需要生成的主要动作；
- 本镜完成后下一镜可继承的状态；
- 需要用视频模型生成、图像转视频、局部动画、后期合成还是实拍补充；
- 最小稳定替代方案。

## 提示词结构

```text
主体身份与稳定锚点
+ 当前可见动作
+ 固定环境与状态变化
+ 构图、景别和机位
+ 单一明确运镜
+ 光线、材质和色彩
+ 情绪与节奏
+ 连续性要求
+ 禁止漂移项
```

禁止仅使用“cinematic、epic、masterpiece”等空泛质量词替代具体设计。

## 镜头类型与策略

### Establishing

世界建立镜头。优先关键帧或图像转视频，减少无必要复杂运动。

### Performance

人物反应、选择和微动作。缩短镜头，减少同时发生的事件，优先参考图与稳定表演。

### Spectacle

规则产生的核心奇观。拆成前兆、发生、结果三个镜头，必要时分层生成并后期合成。

### Symbol

物件、重复动作和情绪回环。使用精确构图、低动作复杂度和声音强化。

### Connector

视线、手部、脚步、门、光线或物件位置连接。优先稳定而非炫技。

## 一致性检查

- 角色脸、发型、服装和标志物；
- 时间、天气、光源方向和空间布局；
- 人物出入方向、视线、手持物和动作结果；
- 镜头比例、色彩、颗粒、锐度和运动气质；
- 关键规则的视觉表现方式。

## 失败恢复

- 脸漂移：加强参考资产、减少角度跨度、拆短镜头；
- 手部失败：换为轮廓、局部遮挡、物件结果镜头或后期；
- 动作失败：降低速度和关节复杂度，拆成多个状态；
- 环境漂移：固定场景参考、减少自由镜头运动、使用局部变化；
- 无法剪辑：补输入状态、输出状态和连接镜头；
- 奇观失控：保留规则结果，降低同时运动层数。

## 输出要求

ADAPT或制作任务至少输出：

1. 视觉、角色、环境锁定项；
2. 镜头生成方法；
3. 一致性风险；
4. 理想、稳定、最低成本三档实现；
5. 失败镜头替代方案；
6. 剪辑与声音连接建议。
