# Frame Clarity & Density Controller V4.5

## 目标

本模块控制单张控制帧、剧情关键帧、氛围图和视觉概念图的：

- 视觉层级；
- 画面清洁度；
- 结构化华丽；
- 焦点统一；
- 缩略图可读性；
- 动作阶段语义；
- 关系残留；
- 原创视觉语法；
- 材质语义漂移；
- 画幅适配。

它不规定固定美学，不把所有画面变成极简或华丽，也不替代摄影、灯光、表演和图片Prompt编译器。它负责防止：

- 华丽被错误翻译成满屏细碎元素；
- 干净被错误翻译成空洞；
- 关键动作在静态帧中被误读；
- 画面最亮处、色彩锚点和叙事中心互相分离；
- 抽象结构回落成高频AI模板；
- 指定材质被模型替换为玻璃、冰、塑料等常见材质；
- 横竖画幅只改比例、不重建构图。

## 启用范围

### 必须启用

- 剧情关键帧；
- 分镜START / END / BRIDGE CF；
- 视觉概念图；
- 氛围叙事图；
- 用户明确要求华丽、震撼、共鸣、悬疑、抽象或电影关键帧；
- 实测后出现噪点、密集小物、动作误读、海报化或材质漂移。

### 简化启用

人物身份板、三视图、道具结构板和场景布局板只使用清洁度、材质和结构可读性部分，不强制奇观、大形冲击或缩略图叙事。

## 一、视觉层级：大形、中形、小形

每帧必须先定义视觉层级，不能直接堆细节。

```yaml
visual_hierarchy:
  core_macro_shapes: []
  supporting_medium_structures: []
  micro_detail_zones: []
  clean_silhouette_zones: []
  visual_rest_zones: []
  detail_attenuation:
```

### 大形

决定第一眼关系的1—4个宏观形体，例如：

- 人物轮廓；
- 建筑或环境主结构；
- 巨型曲面、光带、阴影、道路或空间分界；
- 人物与环境的尺度关系。

大形必须能够用一句话说明。若一句话无法说清第一视觉关系，说明元素可能过多或结构不明确。

### 中形

承担空间层次、秩序、结构华丽和叙事机制，例如：

- 柱廊、肋架、台阶、门框、轨道、衣片；
- 受控装饰带、结构脊、嵌饰、窗格；
- 主要道具群或环境节奏。

中形不是越少越好。华丽项目不能只剩极简大形；但中形必须具有结构或叙事功能，不能平均铺满所有区域。

### 小形

只集中在需要近距离读取的位置：

- 面部；
- 手部；
- 核心道具；
- 服装重点纹样；
- 关键损伤、裂口、文字区域或状态标记。

禁止皮肤、服装、建筑、天空和空气同时拥有同等高频纹理。

## 二、主体清洁区与视觉休息区

### 主体清洁区

必须明确哪些区域不能被微粒、雾点、花瓣、裂纹、背景线条、衣摆或装饰穿过，通常包括：

- 面部与头肩轮廓；
- 双手和关键接触点；
- 核心道具；
- 主要动作轮廓；
- 唯一色彩锚点。

清洁区不是把背景删除，而是降低局部纹理、亮点和竞争性线条。

### 视觉休息区

每帧至少保留一处低信息区域。复杂或华丽画面通常需要两至三处。休息区通过降低纹理、局部对比度、锐度和装饰密度产生，不等于空白无内容。

## 三、结构化华丽

华丽感优先来自：

1. 空间尺度；
2. 大形与中形的秩序；
3. 材质差异；
4. 光线层次；
5. 受控装饰；
6. 运动痕迹；
7. 单一或少量视觉锚点。

禁止默认使用：

- 漫天金粉；
- 无数花瓣；
- 密集羽毛；
- 随机碎片；
- 满屏光点；
- 所有表面密集刺绣或裂纹；
- 过度锐化和高微对比。

一个镜头原则上只设：

- 一个主要流动元素；
- 最多一个辅助环境流动元素；
- 一个主要视觉锚点。

项目确有多元素形式规则时可以突破，但必须证明层级、方向和功能，不得随机增加。

## 四、微粒、噪点与颗粒策略

```yaml
particle_and_noise_policy:
  primary_flow_element:
  secondary_environment_element:
  particles_allowed:
  particle_type:
  particle_zone:
  particle_scale_and_density:
  grain_mode: NONE | CLEAN_DIGITAL_BASE | SUBTLE_POST_GRAIN | INTENTIONAL_HEAVY_GRAIN
  noise_risks: []
```

默认剧情母图优先`CLEAN_DIGITAL_BASE`。明显胶片颗粒、旧片划痕、漏光和特殊噪声优先留到后期，除非它们本身承担项目叙事或媒介表达。

必须区分：

- 数字噪点与暗部彩色斑点；
- 有意胶片颗粒；
- 空气微粒；
- 视觉噪音；
- 高频纹理堆积；
- AI伪文字与重复纹样。

不能仅写“no noise”。负面Prompt需针对当前画面的高频风险。

## 五、焦点统一

每帧检查以下区域是否互相支持：

```yaml
focal_alignment:
  narrative_action_area:
  brightest_area:
  highest_local_contrast_area:
  strongest_saturation_area:
  sharpest_detail_area:
  world_change_origin:
  aligned:
  intentional_misalignment_reason:
```

叙事关键帧默认要求动作区、局部最亮区、最高对比区和主要色彩锚点尽量对齐。若故意错开，必须有清楚的揭示或误导理由。

常见硬失败：

- 人物动作在暗处，最亮区域在无关天空；
- 唯一高饱和色出现在无关装饰；
- 世界变化与人物动作没有可见起点；
- 背景奇观比剧情事件更清楚。

## 六、缩略图与观看距离可读性

短视频、封面和移动端画面必须进行缩略图检查：

```yaml
thumbnail_readability:
  primary_shape_readable:
  protagonist_or_subject_readable:
  key_action_readable:
  key_prop_readable:
  cause_and_effect_readable:
  emotional_relation_readable:
  depends_on_micro_detail:
```

缩小后应至少保留主场景功能所需的第一层信息。不能要求观众放大后才能知道：

- 谁在做什么；
- 关键物件在哪里；
- 奇观与动作有什么关系；
- 两个人处于怎样的关系；
- 威胁从哪里来。

缩略图检查不要求所有微表情清楚，而是确保核心关系不被误读。

## 七、动作阶段语义

静态帧必须明确动作处于哪个阶段：

```text
PREPARATION：动作发生前的准备
CONTACT：刚接触或刚开始施力
TRANSITION：动作正在发生
COMPLETION：动作结果刚形成
AFTERMATH_RESIDUE：动作已经完成，但身体仍保留残留姿态或关系余温
```

每个关键动作填写：

```yaml
gesture_semantics:
  intended_action:
  action_phase:
  actor_goal:
  contact_state:
  weight_or_force_transfer:
  hand_and_body_direction:
  visible_result:
  preparation_pose_risk:
  alternate_misread_risks: []
  disambiguation_cues: []
```

必须区分：

- 递出与接取；
- 松手与伸手；
- 剪断与激活；
- 推开与扶住；
- 即将离开与刚刚回来；
- 躲避与攻击；
- 安慰与控制。

不能只写手的位置。必须写手掌方向、手指残留形态、肘部趋势、重心、接触是否存在、重量由谁承担和动作后的可见结果。

## 八、关系残留

情绪共鸣、治愈和人物关系镜头需要检查动作完成后是否仍有关系痕迹：

```yaml
relationship_residue:
  previous_contact_or_shared_action:
  current_distance:
  tactile_memory_visible:
  uncompleted_gesture:
  avoided_or_shifted_gaze:
  involuntary_emotional_leak:
  personal_history_trace:
  residue_preserved:
```

关系残留不是要求人物靠得越近越好，而是让观众看见刚刚发生过什么：

- 手指已经分开但姿态仍保留握持形状；
- 身体正在离开，视线仍停在对方动作上；
- 道具已经交接，但重量和褶皱显示刚刚发生过转移；
- 话没有说出口，却通过嘴唇、吞咽、呼吸或手指泄漏。

动作语义准确与情绪残留必须同时成立，不能为了避免误读把关系距离拉得过远。

## 九、道具自然化与商业化风险

情绪或叙事道具必须服从人物动作和重力，不得自动成为商品陈列。

```yaml
prop_naturalism:
  narrative_role:
  owner_and_weight_holder:
  contact_and_gravity:
  wear_and_irregularity:
  framing_prominence:
  commercial_display_risk:
  correction:
```

检查：

- 是否正面、端正、居中展示；
- 颜色是否过度鲜亮；
- 数量和排列是否过于完美；
- 使用痕迹是否符合人物生活；
- 是否遮挡人物关系；
- 是否让画面像广告或公益宣传照。

## 十、原创视觉语法

禁止只列“不要莲花、不要光环、不要仙山”等负面词，而不定义新的结构。

```yaml
original_visual_grammar:
  project_specific_core_relation:
  shape_language:
  structural_rules:
  material_rules:
  repetition_and_variation:
  common_cliche_risks: []
  replacement_structure:
  generic_concept_art_risk:
```

抽象结构至少说明：

- 为什么存在；
- 如何受力或连接；
- 各大形承担什么职责；
- 哪些结构重复，如何变化；
- 与人物行动如何产生因果；
- 为什么属于当前项目，而不是通用AI素材库。

## 十一、材质语义漂移

图片模型常把复杂材质替换为常见高反射材质。必须预判：

```yaml
material_semantic_drift:
  intended_material:
  observable_properties:
  likely_model_substitutions: []
  silhouette_or_light_causing_misread:
  positive_counter_description:
  negative_constraints:
```

例如：

- 乳白半透瓷 → 容易漂移成冰、玻璃、水晶；
- 黑漆 → 容易漂移成镜子、水面、湿柏油；
- 螺钿 → 容易漂移成霓虹亮片；
- 旧金 → 容易漂移成廉价亮金或发光塑料；
- 薄纱 → 容易漂移成烟雾或塑料膜。

正向Prompt必须写可观察属性：哑光或反射粗糙度、透明程度、重量、边缘、受光方式、重力和使用痕迹。负面约束只能辅助，不能代替正向定义。

## 十二、海报化与摆拍风险

剧情关键帧检查：

```yaml
posterization_risk:
  centered_character:
  perfect_symmetry:
  direct_camera_gaze:
  costume_display_pose:
  complete_world_inside_frame:
  action_replaced_by_pose:
  controlled_imbalance:
```

海报化不是绝对禁止。广告、角色海报和仪式性场景可以有意使用；但电影事件帧若要求正在发生，必须避免：

- 人物正面居中站立；
- 左右服装完全展开；
- 背景形成标准光环；
- 所有元素完整收进画框；
- 道具只是拿在手上展示；
- 动作被英雄姿势替代。

## 十三、画幅适配

```yaml
aspect_ratio_execution:
  requested_ratio:
  orientation:
  platform_parameter_required:
  composition_rebuilt:
  subject_scale:
  negative_space_function:
  motion_direction:
  crop_protection:
```

画幅是当前任务参数，不是固定美学。

- 16:9适合横向关系、并置、对峙、环境延展和宽银幕空间；
- 9:16适合垂直压迫、高低关系、手机占屏和纵向动作；
- 同一场景切换比例时必须重新设计人物占比、视线空间、主要动线、负空间和超框结构；
- 不得只替换Prompt中的“16:9/9:16”；
- 外部平台的实际宽高比参数优先于文字描述，最终交付需注明参数要求。

## 十四、输出到Prompt

以上判断不能只留在分析或表格中。最终正向Prompt至少直接写入：

- 核心大形与中尺度结构；
- 细节集中区、主体清洁区和视觉休息区；
- 主要流动元素与微粒策略；
- 动作阶段、接触、重量和可见结果；
- 焦点、最亮处、最高对比和色彩锚点；
- 画幅下的人物占比与空间功能；
- 材质可观察属性；
- 原创替代结构；
- 针对性高频污染与误读负面约束。

禁止把这些内容压缩为“画面干净、电影感、高级、动作自然”。

## 十五、硬失败

以下任一情况必须REPAIR：

- 第一视觉关系无法一句话说明；
- 画面所有区域同等复杂或同等锐利；
- 华丽主要依靠密集粒子和随机碎片；
- 主体面部、手部或关键道具被高频背景穿过；
- 最亮处、唯一高饱和色与叙事动作互相分离且无意图；
- 核心动作在缩略图中被误读；
- 静态姿态无法区分动作前与动作后；
- 道具重量、接触和持有者不清；
- 关系镜头动作正确但关系残留完全消失；
- 只删除常见符号，没有建立替代结构；
- 材质被模型常见替代物吞没；
- 剧情帧回落成角色海报或商品广告且无意图；
- 横竖画幅改变后仍沿用原构图；
- Prompt只写抽象控制词，没有可见实现方式。