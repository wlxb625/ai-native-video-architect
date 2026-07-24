# AI Production Controller

## 目标

把已成立的概念、视觉叙事与镜头语言转译为可生成、可连续、可剪辑、可修复的AI视频生产方案。

禁止在视觉身份、角色和空间尚未锁定前直接批量写视频提示词。

## 生产前置

必须先建立：

- Visual Bible：色彩、光线、材质、空间尺度、摄影基调；
- Character Lock：外观、服装、标志物、动作习惯、禁止漂移项；
- Environment Lock：建筑结构、光源方向、关键物件位置、时间和天气；
- Shot Contract：每个镜头的输入状态与输出状态；
- Cinematic Master Spec：画幅、摄影机基准、镜头系统、帧率、快门、高光、暗部、颗粒、锐度和运镜策略。

用户要求具体分镜或可直接生成的逐镜头方案时，必须读取 `controllers/detailed-storyboard.md` 与 `templates/detailed-storyboard.md`。

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

## 电影摄影主规格

用户未指定时，详细电影分镜默认采用：

```yaml
cinematic_master_spec:
  aspect_ratio: 21:9
  camera_reference: ARRI Alexa 35 or ARRI Alexa LF
  lens_system: anamorphic
  frame_rate: 24fps
  shutter_angle: 180deg
  dynamic_range: wide, natural exposure relationship
  highlight_rolloff: soft and gradual
  shadow_detail: preserved
  grain: subtle and fine
  sharpening: restrained
  actor_realism: ordinary real actor, natural skin texture
  material_realism: visible use, age and environmental traces
  movement_policy: motivated and physically plausible
```

这是成像和制作基准，不是空泛质量词。每个镜头仍需具体说明构图、焦段、运动、光源、曝光、材质、动作和连续性。

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

角色应保留真实演员的皮肤毛孔、轻微不对称、自然泛红、细纹、眼袋、嘴唇纹理、眉毛、发际线、发丝和区域色差。禁止网红脸、明星脸、模特脸、过度美颜、塑料皮肤和商业精修感。

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
  use_and_age_traces:
  allowed_changes:
  forbidden_changes:
```

场景、家具、服装和道具必须有与故事相符的真实使用痕迹，例如自然褶皱、洗涤痕迹、磨损、灰尘、水渍、油渍、木材旧痕和金属氧化。不得平均做旧，也不得生成无来源的脏污。

## 镜头工程

每个镜头必须说明：

- 上一镜结束时人物、物件和空间状态；
- 本镜只需要生成的主要动作；
- 本镜完成后下一镜可继承的状态；
- 21:9构图中的准确位置、占比和空间层次；
- 摄影机、镜头、焦段感和变形宽银幕光学表现；
- 运镜的起止位置、速度、设备逻辑和动机；
- 人物微表演、呼吸、视线、手部和动作停顿；
- 光源方向、色温、曝光、高光滚降和暗部纹理；
- 帧率、快门和运动模糊；
- 需要用视频模型生成、图像转视频、局部动画、后期合成还是实拍补充；
- 最小稳定替代方案。

## 提示词结构

```text
全片固定摄影基准
+ 主体身份与稳定锚点
+ 真实演员皮肤、发丝和非精修特征
+ 当前服装、道具和使用状态
+ 当前唯一动作、微表演和动作速度
+ 固定环境、空间布局与真实材质
+ 21:9构图、景别、机位和焦段感
+ 变形宽银幕光学特征
+ 单一明确运镜、起止位置和速度
+ 光源方向、曝光、色温、高光和暗部
+ 24fps、180度快门或特殊设置
+ 前后镜头连续性要求
+ 禁止漂移项和负面视觉约束
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

- 所有镜头是否统一21:9，不混入16:9或9:16；
- 角色脸、发型、服装、标志物和真实演员质感；
- 时间、天气、光源方向和空间布局；
- 人物出入方向、视线、手持物和动作结果；
- 摄影机基准、变形宽银幕特征、24fps和快门逻辑；
- 色彩、颗粒、锐度、高光滚降、暗部层次和运动气质；
- 建筑、家具、服装和道具的使用痕迹；
- 关键规则的视觉表现方式。

## 失败恢复

- 脸漂移：加强参考资产、减少角度跨度、拆短镜头；
- 皮肤过度精修：强化普通演员、自然皮肤纹理和禁止美颜约束；
- 手部失败：换为轮廓、局部遮挡、物件结果镜头或后期；
- 动作失败：降低速度和关节复杂度，拆成多个状态；
- 环境漂移：固定场景参考、减少自由镜头运动、使用局部变化；
- 画幅错误：按21:9安全构图区重新生成，不依赖后期盲裁；
- 光线跳变：锁定光源方向、时间和基础曝光，重做异常镜头；
- 无法剪辑：补输入状态、输出状态和连接镜头；
- 奇观失控：保留规则结果，降低同时运动层数；
- CG或动画感：减少过度锐化、过饱和、塑料材质和无来源光效，增加真实使用痕迹与物理曝光关系。

## 输出要求

ADAPT或制作任务至少输出：

1. 视觉、角色、环境和全片摄影主规格；
2. 逐镜头构图、摄影、动作、光线、材质、声音与连续性；
3. 镜头生成方法；
4. 中文Prompt、英文Prompt和负面约束；
5. 一致性风险；
6. 理想、稳定、最低成本三档实现；
7. 失败镜头替代方案；
8. 剪辑与声音连接建议。
