# Video Prompt Compiler V4.7

编译前读取：

- `prompt-engineering/render-medium-generation-route-contract.md`；
- `prompt-engineering/shot-cf-binding-system.md`；
- `controllers/camera-director.md`；
- `controllers/lighting-director.md`；
- `controllers/performance-director.md`；
- `references/emotion-library.md`；
- `prompt-engineering/performance-prompt-compiler.md`；
- 当前项目`RENDER_MEDIUM_LOCK`、`GENERATION_ROUTE_PLAN`和`CONTINUITY_LEDGER`。

## 一、目标

把已批准的镜头设计、渲染媒介、实际输入媒体、灯光、表演、动画运动、时间控制和连续性计划，编译为可直接用于以下路线的导演级Prompt：

- `PURE_T2V`；
- `REFERENCE_T2V`；
- `IMAGE_TO_VIDEO`；
- `FIRST_LAST_FRAME`；
- `TAIL_FRAME_CONTINUATION`；
- `HYBRID_SUBSHOT`；
- `POST_ONLY`。

动态时间控制只负责让既有导演设计在正确时点发生、形成明确因果并准确收住，不得把完整镜头设计压缩成纯时间表。

## 二、Prompt覆盖前置规则

每个生成型Shot必须具备：

- 可见画面描述；
- `RENDER_MEDIUM_LOCK`引用；
- 当前Shot生成路线及理由；
- 真实存在的输入媒体清单，或对PURE_T2V明确写“无输入媒体”；
- 准确开始状态；
- 唯一核心视觉事件；
- 结束帧合同；
- 下一镜连续性；
- 一条独立可复制的视频正向Prompt；
- 针对性负面Prompt和失败降级路线。

`POST_ONLY`镜头不写伪视频Prompt，但必须写明素材来源、底板、前景层、遮罩、跟踪、后期操作、时长、剪辑点和连续性。

禁止因为镜头是过渡、空镜、纯文生或继承上一镜而省略Prompt块。

## 三、先继承渲染媒介

所有视频Prompt必须按当前媒介翻译人物、环境、材质、光线、摄影机和运动。

```yaml
video_medium_contract:
  render_medium_reference:
  character_rendering:
  environment_rendering:
  material_and_shading:
  lighting_language:
  camera_and_optical_translation:
  animation_language:
  forbidden_medium_drift: []
```

关键规则：

- “电影感”不自动等于真人实拍；
- “真实光源”表示世界内部位置、方向、衰减和阴影成立，不等于照片写实；
- “真实材质”表示材质类别、受力和运动可辨认，不等于必须真人纹理；
- 风格化3D动画按角色建模、设计化面部、动画电影着色器、发束、服装大形、环境形体、关键姿势和次级动作编译；
- 二维、2.5D、绘画、水墨和定格按各自线条、色块、笔触、实体材料与帧间节奏编译；
- 负面Prompt只排除当前项目明确禁止的媒介漂移，不得全局禁止动漫、真人、二维、三维或游戏CG。

## 四、模型执行Prompt前置语义规则

Shot ID、Scene ID、CF ID、作品名、剧名、章节名、场次标题、镜头标题、文件名、版本号、导演解释、剧情主题和“用于某项目”等内容属于管理信息，必须留在视频Prompt块之外。除非某段文字必须实际出现在画面中，否则不得占据模型执行Prompt开头。

不同模型对长Prompt的注意力分配不同，因此不把前20—30个词写成绝对技术定律；实际编译时仍把首句或前20—30个实义词作为高优先级执行区。

### PURE_T2V前置核心块

```text
当前渲染媒介与主体
+ 准确起始状态
+ 唯一核心视觉事件
+ 最重要的时间锚点或运动方向
```

不得写不存在的上传图、首帧、尾帧或参考绑定。

### REFERENCE_T2V前置核心块

```text
真实参考图及其职责
+ 当前渲染媒介与主体起始状态
+ 唯一核心视觉事件
+ 最重要的时间锚点或运动方向
```

参考图不自动等于首帧，不能要求模型复制参考图中职责之外的构图、动作或背景。

### IMAGE_TO_VIDEO前置核心块

```text
输入首帧保护
+ 主体身份与起始状态
+ 唯一核心视觉事件
+ 最重要的时间锚点或运动方向
```

### FIRST_LAST_FRAME前置核心块

```text
首帧与尾帧职责及静态一致性
+ 主体起始状态
+ 唯一核心视觉事件
+ 准确接触、释放、揭示或状态切换锚点
```

### TAIL_FRAME_CONTINUATION前置核心块

```text
上一镜稳定尾帧及必须继承的动作阶段
+ 当前主体起始状态
+ 尚未完成的唯一核心事件
+ 继续运动的方向或时间锚点
```

普通`RELATIVE_PHASE`镜头不必在第一句堆秒数，但仍应先写主体、起始状态和唯一变化。`ABSOLUTE_EVENT_ANCHOR`镜头应把最关键锚点尽早写入；次要延迟、衰减和收住过程在后文展开。

前置权重优化不是缩短Prompt。时间、镜头、视觉、色彩、灯光、材质、表演、环境、声音、尾态和连续性设计仍必须完整保留。

## 五、生成路线判定

### A. PURE_T2V

适合同时满足大部分条件的Shot：

- 画面价值主要来自空间、环境、抽象材质或宏观形体运动；
- 构图允许一定探索；
- 不依赖精确面孔、手部接触、道具结构或唯一尾态；
- 文本运动设计比固定首帧更能释放模型动态能力；
- 与上下镜可以通过大形、方向、声音、色彩或硬切连接。

PURE_T2V仍必须有准确开始状态与结束帧合同，但不伪造静态输入。

### B. REFERENCE_T2V

适合：

- 需要持续角色身份、服装、世界、材质或风格；
- 不需要完全锁死首帧构图；
- 希望保留文生视频的动态和构图自由；
- 平台真实支持角色、风格或图像参考。

每张参考必须说明职责、优先级、允许影响和禁止影响。

### C. IMAGE_TO_VIDEO

适合：

- 首帧构图、角色位置、面孔、服装、场景或光线必须准确继承；
- 动作从一个已批准静态状态发展；
- 尾态可以用文字合同控制或从结果中选择。

首帧保护优先。不得在视频Prompt中重新设计角色、服装、背景或镜头美术。

### D. FIRST_LAST_FRAME

出现以下任一情况时优先评估：

- 下一镜需要继承准确姿势、视线、手部、道具位置或屏幕方向；
- 人物、服装、道具或环境发生明确状态变化；
- 道具被拿起、放下、打开、关闭、翻转、破坏、清理或移动到固定位置；
- 精确手部接触、拆开、闭合、释放或受力；
- 镜头运动改变最终构图、景别或焦点；
- 动作终点承担叙事信息；
- 单首帧或纯文生容易产生随机尾态。

首尾帧不是额外角色资产，而是当前镜头的起终控制帧。静态冲突先修帧。

### E. TAIL_FRAME_CONTINUATION

当一段动作需要分为连续两段时：

1. 第一段生成后抽取身份、手部、道具、背景、媒介和光线稳定的尾帧；
2. 作为下一段唯一首帧；
3. 下一段只继续尚未完成的动作；
4. 不重新设计人物、场景、构图和情绪。

### F. HYBRID_SUBSHOT

当一个计划Shot需要宏观文生奇观与精确人物交互两种控制时，可以拆为相邻子Shot或连续子段，不在同一次生成中叠加所有路线。

### G. POST_ONLY / 分层合成

镜面人物、倒影、准确文字、屏幕内容、复杂多层雾气、遮挡、部分光效和生成模型持续失败的多层状态，优先拆为底板、主体层、效果层和遮罩层。

## 六、完整导演设计继承合同

生成路线和动态时间控制是执行层，不得替代已经批准的导演完整设计。每条最终Prompt必须继续保留：

- 渲染媒介、角色与环境共同设计语言；
- 景别、机位、焦段感或媒介等效关系、构图、前中后景、主体位置、留白、轴线和屏幕方向；
- 摄影机起点、运镜类型、方向、幅度、速度曲线、终点和叙事动机；
- 焦点、景深或层级分离、曝光或明度、高光保护、暗部层次和运动模糊；
- 主光或主明暗来源、世界位置、方向、软硬、色彩、强度、光比、受光区和阴影区；
- 主色、辅助色、点缀色、饱和度、对比度、黑位、高光与光色连续性；
- 人物身份、服装、表演、微表情、呼吸、重心、手部、动作物理和情绪曲线；
- 动画媒介中的关键姿势、剪影、动作曲线、次级动作与延迟；
- 场景结构、背景职责、环境事件、材质分层运动、声音、结束状态和跨镜连续性。

时间容量不足或执行冲突时，优先调整时间分配、减少并发、改路线、拆镜、首尾帧、抽尾帧续拍或分层生成；不得通过删除视觉、色彩、灯光、材质、表演、环境、声音和连续性解决。

## 七、每镜只有一个核心视觉事件

每条4—8秒Prompt先确定唯一核心视觉事件，例如：

- 人物从压抑静止到抬眼确认；
- 后方浪幕逐渐升起形成穹顶；
- 一条纤维从袖口牵动整个空间压缩；
- 门外光线逐渐切开黑暗；
- 手指挑开第一针并释放张力；
- 世界折面从近至远逐层展开。

人物动作、衣料、头发、环境、灯光和运镜都应服务该主事件。允许1—3个从属微动，不得同时争夺视觉中心。

一条长Prompt不能代替多Shot成片。多个机位、场景或核心事件必须拆镜。

## 八、人物动作与动画运动编排

### 身体部位顺序

禁止“人物缓慢起舞、人物转身、人物抬手”这类摘要。必须写清：

- 哪个部位先动；
- 起势的呼吸、视线、手指或重心准备；
- 动作方向、角度、距离和速度曲线；
- 哪些部位保持克制；
- 动作如何收住；
- 最终姿态和稳定停留。

### 风格化动画附加合同

当前媒介包含二维、2.5D、风格化3D、游戏电影CG、定格或绘画动画时，按需明确：

```yaml
animation_motion_contract:
  start_key_pose:
  end_key_pose:
  silhouette_readability:
  anticipation:
  primary_action:
  contact_release_or_reveal:
  overshoot_rebound_or_settle:
  motion_curve:
  primary_secondary_order:
  hair_delay:
  inner_costume_delay:
  outer_costume_delay:
  prop_delay:
  environment_delay:
  stylized_weight_and_inertia:
  critical_clear_frames: []
  motion_blur_or_smear_boundary:
  forbidden_uniform_motion: []
```

动画化不等于所有元素同时飘动。关键姿势和高潮帧必须有清楚剪影，能够作为独立构图成立。

## 九、材质运动分层编舞

不能把头发、内层衣料、外层衣料、丝带、水、雾、火和尘统一写成“随风飘动”。分别说明：

- 动力来源；
- 开始时间和延迟；
- 方向和轨迹；
- 速度和幅度；
- 重量、阻力、惯性、弹性或流体连续性；
- 前景、中景、远景的速度差；
- 哪些允许运动模糊，哪些必须保持清晰；
- 当前媒介中的着色与形变如何保持。

靠近身体的内层通常更稳定，外层可以有更大弧线；近景元素可以更快并短暂虚化，远景大形通常更慢、更重。项目另有风格化规则时以项目合同为准。

## 十、背景必须发生可见事件

背景不能只“有海浪、有雾、有雨”。必须写成时间过程：

```text
初始状态
→ 背景力量开始形成
→ 中段结构或运动扩大
→ 接近高潮时出现局部爆发或揭示
→ 停在准确结束状态
```

背景事件需要有大形、层次和尺度，并与主体动作同向、对抗、包围或延迟响应。背景可以成为第二视觉主体，但不能遮住关键面部、手部和叙事信息。

## 十一、时间轴发展与高潮

短镜头不能平均地“漂”完整段。默认按实际时长划分为：

- 起始稳定与微小起势；
- 主动作或主环境事件形成；
- 画面关系发生明显变化；
- 最后1—2秒达到视觉峰值并收住。

峰值可以是动作停住、背景大形完成、光线穿透、遮挡形成、道具接触或观众终于看清信息。必须写清结尾画面，而不是只写“逐渐结束”。

## 十二、动态时间控制等级

### RELATIVE_PHASE

使用“前段稳定—中段发展—后段收住”的相对阶段。适用于呼吸、抬眼、轻微转头、缓慢走动、衣料与环境微动等低风险镜头。

仍需写清顺序、幅度、因果和尾态，但不机械设置多个绝对秒点。

### ABSOLUTE_EVENT_ANCHOR

关键接触、冲击、揭示、转身、道具状态改变、焦点切换，或摄影机与人物需要同步响应时，使用绝对时间锚点。

```yaml
timing_control:
  mode: ABSOLUTE_EVENT_ANCHOR
  duration:
  pre_event_hold:
  event_anchors:
    - event_id:
      exact_time_or_window:
      preparation_start:
      trigger_action:
      exact_contact_or_change:
      actor_response:
      prop_response:
      environment_and_material_response:
      camera_response:
      focus_response:
      lighting_and_exposure_response:
      sound_sync_point:
      response_delay:
      amplitude_numeric:
      amplitude_visible_result:
      decay_or_rebound:
      settle_time:
      forbidden_desynchronization: []
  final_hold:
```

数值必须与可见结果同时出现，例如：

```text
茶杯震起约2厘米，杯底清楚离开桌面但不倾倒、不破裂；
摄影机下沉约10厘米，只改变一个手掌宽度的观察高度，不形成大幅俯冲。
```

### SPLIT_EXECUTION

当同一镜头需要多人精确交互、复杂手部接触、多个道具连锁反应、人物与摄影机同时大幅运动，或多个绝对锚点争夺执行能力时，不继续增加Prompt长度。

改用首尾帧、Bridge CF、两段生成、抽尾帧续拍、遮挡切换、不同路线子Shot或分层合成。

## 十三、时间轴动作编译

动作必须按镜头时长写成可执行时间段。示例：

```text
0.0—0.8秒：保持开始状态，只有呼吸和衣料微动；
0.8—3.4秒：右手以受控速度移动8厘米，手腕保持水平；
3.4—4.2秒：道具落入支架，产生一次轻微承重震动；
4.2—5.0秒：双手松开并停住，保持尾态不少于0.5秒。
```

### 起始状态

写清：身体姿态、头部朝向、视线落点、左右手、道具接触点、重心、脚部、呼吸、环境和摄影机起点。

### 起势

写清动作前的微小准备：视线、呼吸、手指收紧、重心转移或肩部发力。普通动作不需要夸张蓄力。

### 过程

按时间顺序写1—3个动作节点，量化方向、距离、角度、速度和接触。

### 收住

写清最终姿态、手的位置、道具状态、视线、呼吸、背景和稳定停留。不能在动作中间随机结束。

### 关键事件因果同步

```text
人物起势
→ 接触、释放或状态变化
→ 道具受力或改变
→ 环境与材质响应
→ 摄影机、焦点、灯光或声音按导演设计响应
→ 惯性、余震或情绪残留衰减
→ 停在结束帧合同
```

明确哪些响应同时发生、哪些延迟多少，以及哪些元素保持静止。禁止摄影机提前震动、物体无接触自行运动、冲击后持续漂浮、动作自动重复或灯光无动机闪烁。

## 十四、动作物理

- 重物明确重量感、双手分工、肩臂受力和重心；
- 手与道具写明接触点、握持位置和移动路径；
- 脚部接地或按当前媒介的悬浮规则执行，禁止无设定滑行；
- 布料、头发和饰物只产生由动作或环境引起的运动；
- 速度使用匀速、缓入缓出、先慢后停、过冲回弹等具体曲线；
- 幅度尽量量化为厘米、角度或画面比例；
- 每个数值同时说明观众可见结果；
- 风格化动画可以夸张动作曲线，但接触、因果和状态变化必须清楚。

## 十五、人物表演合同

```yaml
performance_contract:
  scene_objective:
  immediate_intention:
  inner_emotion:
  outer_strategy:
  emotional_contradiction:
  intensity_start:
  intensity_end:
  gaze_and_eyelids:
  eyebrows_and_forehead:
  mouth_jaw_and_swallow:
  breathing:
  posture_and_weight:
  hands_and_fingers:
  emotion_beats: []
  forbidden_overacting: []
  end_performance_state:
```

要求：

- 情绪转化成可见线索，不得只写标签；
- 4—6秒镜头默认一个主要情绪转折、1—3个微动作和一次呼吸变化；
- 眼、嘴、肩、手和头部不同时进行高幅度动作；
- 镜头距离、焦点和灯光必须让关键表演可读；
- 结束表演状态进入结束帧合同和下一镜继承；
- 风格化角色仍需表演，不得只靠大眼、夸张嘴形和预设动漫表情替代。

## 十六、摄影机合同

```yaml
camera_contract:
  medium_translation:
  lens_or_equivalent:
  camera_height:
  camera_distance:
  shot_size:
  angle:
  axis_and_screen_direction:
  start_position:
  movement_type:
  movement_start_time:
  movement_end_time:
  event_sync_relation:
  direction:
  speed_curve:
  amplitude:
  amplitude_visible_result:
  endpoint:
  movement_motivation:
  stabilization:
```

要求：

- 固定镜头写明无平移、摇镜、旋转和数字变焦；
- 推进、横移和升降尽量量化；
- 写明运动何时开始和结束；
- 关键事件写清摄影机提前蓄势、同时响应、延迟跟随或始终静止；
- 一个短镜头只使用一种主要运镜；
- 环境宏大运动时摄影机更克制；
- 运镜必须服务揭示、压迫、空间确认、动作跟随或情绪距离；
- 二维、绘画和定格项目将焦段翻译为构图压缩、视差、分层和画面移动，不机械套真人参数。

## 十七、焦点、景深和曝光合同

```yaml
optical_contract:
  medium_translation:
  depth_of_field_or_layer_separation:
  focus_at_start:
  focus_transition:
  focus_event_sync:
  focus_at_end:
  lens_breathing_or_equivalent:
  exposure_or_value_state:
  white_balance_or_color_baseline:
  highlight_protection:
  shadow_detail:
  motion_blur_or_medium_equivalent:
```

- 焦点落在具体对象；
- 转移时写清起点、终点和时间；
- 关键揭示写清焦点与事件同步关系；
- 不用浅景深掩盖身份和手部错误；
- 高光不能掩盖角色表面和关键道具；
- 暗部保留空间和材质层次；
- 风格化动画、二维和绘画项目使用项目媒介等效表达。

## 十八、逐镜灯光合同

每条最终视频Prompt都必须包含当前镜头具体灯光，不能只引用全局视觉圣经。

```yaml
lighting_contract:
  render_medium_reference:
  key_source_or_value_origin:
  key_direction:
  key_height:
  key_softness_or_edge_language:
  key_color_temperature_or_relation:
  key_intensity_or_value_priority:
  fill_source:
  fill_intensity:
  practical_lights:
  rim_or_separation_light:
  background_light:
  lighting_ratio_or_value_relation:
  illuminated_areas:
  shadow_areas:
  shadow_direction:
  highlight_control:
  atmospheric_light:
  motivated_change_time:
  motivated_change_trigger:
  continuity_with_previous_and_next:
  forbidden_light_changes:
```

最低要求：

1. 主光或主明暗来源是什么；
2. 来自画面哪一侧、人物前后关系和高度；
3. 冷暖、色温或颜色关系；
4. 软硬、边缘和强弱；
5. 照亮哪些区域；
6. 哪些区域保持阴影且不死黑；
7. 辅光、实景灯和背景光；
8. 光比或明度层级；
9. 高光和暗部策略；
10. 整段视频中不得无因闪烁和漂移；
11. 需要变化时写明时间、触发、幅度和尾态。

真实光源不等于真人写实。风格化3D、二维、绘画和定格项目按各自媒介翻译。

## 十九、画面空间、色彩、材质与着色

最终Prompt必须形成明确画面：

- 前景、中景和背景；
- 主体位置、构图重心、留白和视觉路径；
- 固定地标和空间纵深；
- 当前媒介中的角色表面、头发、服装、道具和环境着色；
- 材质类别、纹理、折痕、磨损、反射、笔触、线条或实体材料；
- 雨雾、尘埃、烟和体积光的范围与强度；
- 哪些元素完全不动；
- 哪些变化必须保持媒介一致。

必须继承同一场景的主光、屏幕方向、色彩基准、阴影、白平衡或媒介等效关系、黑位、高光、材质和着色语言。

禁止模型自行变亮、变暗、闪烁、改变主色或增加无来源轮廓光；也禁止风格化3D在运动中突然真人化、塑料化或游戏截图化。

## 二十、结束帧合同

每一个镜头都必须设计结束状态，即使没有预先生成尾帧。

```yaml
end_frame_contract:
  exact_time:
  character_pose:
  face_and_gaze:
  hands_and_contact:
  prop_position_and_state:
  environment_state:
  render_medium_state:
  camera_position_and_framing:
  focus_target:
  foreground_midground_background:
  lighting_state:
  color_material_and_shading_state:
  allowed_residual_motion:
  stable_hold_frames:
  next_shot_inheritance:
```

要求：

- 结束状态可见、可截图、可验证；
- 明确手脚、道具、视线和背景；
- 明确镜头和焦点终点；
- 明确灯光、色彩、材质、着色和媒介状态；
- 结尾通常稳定停留12—24帧，除非明确运动中切断；
- 下一镜依赖尾态时，必须使用尾帧、抽取稳定尾帧或其他准确控制，不能让模型自由结束。

## 二十一、声音字段

按工具能力写环境音、呼吸、衣料、道具接触、台词、音乐和沉默。关键动作需要声音同步时，写明发生秒点以及与接触、摄影机和环境响应的同步关系。

不支持原生声音时明确转入后期，不假装模型一定生成。

## 二十二、路线专属完整公式

### PURE_T2V

```text
当前渲染媒介
+ 主体与准确起始状态
+ 唯一核心视觉事件
+ 场景空间、景别、构图与视觉动线
+ 时间阶段或关键秒点
+ 关键姿势、动作曲线、接触与重心
+ 材质和环境的分层运动
+ 背景事件形成、扩大、高潮与收住
+ 摄影机起点、响应时机、运动曲线与终点
+ 焦点、明暗、灯光、色彩和着色
+ 精确结束状态与稳定停留
+ 声音、下一镜连续性和禁止漂移
```

### REFERENCE_T2V

```text
真实参考图职责
+ 当前渲染媒介
+ 主体与准确起始状态
+ 唯一核心视觉事件
+ 完整空间、动作、材质、摄影机、灯光、尾态与连续性
```

### IMAGE_TO_VIDEO

```text
输入首帧保护
+ 当前渲染媒介和连续性起态
+ 唯一核心视觉事件
+ 时间轴动作与分层响应
+ 摄影机、焦点、灯光、色彩、材质和精确尾态
```

### FIRST_LAST_FRAME

```text
首帧与尾帧职责及静态一致性
+ 当前媒介和主体起始状态
+ 唯一核心视觉事件
+ 准确接触、释放、揭示或状态切换时间
+ 中间动作、材质因果、摄影机响应与稳定终点
```

### TAIL_FRAME_CONTINUATION

从上一镜尾态继续，只推进尚未完成的动作，不重新起情绪、不重置状态、不改变媒介。

## 二十三、最终Prompt写作标准

最终可复制Prompt必须是完整、具体、具有画面顺序的自然语言，不得只输出字段清单。

每镜至少写清：

- 与路线匹配的首句前置核心块；
- 当前渲染媒介与禁止漂移；
- 实际输入媒体或明确无输入；
- 画面空间和构图；
- 导演意图、观众位置和揭示顺序；
- 起始姿态与表演基线；
- 人物目标、内外矛盾和情绪节拍；
- 可见微表情、呼吸、身体语言和手部变化；
- 动画项目的关键姿势、动作曲线和次级动作；
- 时间控制模式；
- 分秒动作过程或相对阶段；
- 关键事件锚点、因果同步、延迟、幅度与衰减；
- 动作物理；
- 摄影机、事件同步和终点；
- 焦点、景深或层级、曝光或明度；
- 逐镜灯光及有动机变化；
- 色彩、材质、着色和环境动态；
- 精确结束状态；
- 下一镜继承；
- 声音和负面约束。

不得为了方便复制压缩成几句通用话，也不得为了突出时间轴、媒介或前置权重而删除完整画面和导演设计。

## 二十四、输出格式

每镜使用`templates/video-shot-prompt-block.md`或当前任务指定的等效模板。完整正向Prompt、负面Prompt、输出规则、尾态、衔接和失败修复必须位于同一镜头块。

用户复制到模型的内容只取`【视频正向Prompt】`字段；该字段不得以项目名、Shot标题、版本号或解释性语句开头。

## 二十五、视频Prompt硬失败

以下任一情况直接FAIL：

- 未继承`RENDER_MEDIUM_LOCK`；
- 把电影感自动编译为真人写实；
- 用户要求风格化3D动画，Prompt仍以真人毛孔、真人写真或真实演员为核心；
- 路线与输入媒体不匹配；
- PURE_T2V伪造首帧、尾帧或参考绑定；
- 需要精确身份、手部或尾态却无理由使用PURE_T2V；
- 只写动作和运镜，没有画面、光线、焦点和尾态；
- 只有情绪标签，没有人物目标、内外矛盾和可见表演；
- 五秒内安排多个主要情绪转折或无事件强度跳级；
- 微表情在当前景别、焦点、遮挡或灯光下不可读；
- 无台词人物嘴部持续说话或出现随机夸张表情；
- 每镜没有结束帧合同；
- 只写真实光照、电影感、动漫感或冷色调；
- 未写主光来源、方向、照亮区域和暗部；
- 光源和色彩在同一镜头或相邻镜头中漂移；
- 未写焦点、层级和信息优先级；
- 运镜没有开始、结束、方向、幅度和终点；
- 一个短镜头包含过多动作与运镜；
- 没有可见尾态或稳定停留；
- 视频Prompt重新设计人物、服装、场景、媒介或光源；
- 首尾帧差异过大却强迫平滑变换；
- 声音与工具能力不匹配且未转后期；
- IMAGE_TO_VIDEO没有首帧保护；
- 只重复静态画面，没有时间发展；
- 只写人物起舞、衣袂飘动、海浪翻涌、镜头推进等摘要；
- 没有唯一核心视觉事件；
- 背景只有名词，没有形成、高潮和尾态；
- 头发、内外衣料、道具、雾和背景以同一方向、速度和幅度运动；
- 时间轴从头到尾均匀漂动，没有视觉峰值和收住；
- 动画项目没有关键姿势和剪影控制，所有元素同时无因飘动；
- 用增加形容词代替运动因果；
- 为加入绝对秒点删除景别、构图、焦点、灯光、色彩、材质、表演、环境、声音和连续性；
- 关键接触没有统一事件锚点；
- 只给厘米、角度和秒数，不说明画面可见结果；
- 普通低风险镜头被机械拆成过多绝对秒点；
- 超过单次模型能力却不改路线、不拆段、不使用控制帧或分层；
- 把作品名、Shot ID、文件名、版本号、导演解释或主题说明放在模型执行Prompt开头；
- 前置核心块只有电影感、震撼、治愈、史诗、动漫风等抽象词；
- 把动漫、真人、二维、三维或游戏CG写成通用负面项；
- 用一条Prompt代替多个Shot并声称完整长片段必然稳定；
- 为追求前置权重而删除后续导演设计。
