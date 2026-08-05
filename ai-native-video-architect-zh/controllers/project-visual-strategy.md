# Project Visual Strategy Controller V4.5

## 目标

在剧本或视觉脚本成立并进入制作阶段后，根据当前项目的主题、人物、空间、动作、时长、画幅、平台和生成条件，推导只对该项目生效的视觉制作策略。

本模块负责统一项目级视觉世界和后续制作边界，不替代Shot场景功能、摄影、灯光、表演、CF画面控制或Prompt编译，也不为整个Skill预设固定审美。

## 一、启用边界

### 完整项目策略

仅在以下任务进入制作阶段时启用：

- `ADAPT`；
- `FULL_CREATION_PACKAGE`；
- 用户明确要求视觉圣经、资产、Shot、CF、图片Prompt、视频Prompt或完整制作包。

### 不启用完整策略

以下任务不得被强制视觉锁定：

- 只创作故事、剧本或视觉脚本；
- 只诊断或改写文本；
- 纯概念讨论、题材探索和多候选方向。

### 局部视觉合同

单张图片、单镜视频、图生图、续拍和局部修复只建立：

```text
LOCAL_IMAGE_VISUAL_CONTRACT
或
LOCAL_SHOT_VISUAL_CONTRACT
```

局部合同不能伪称已经锁定整部作品。

## 二、前置条件

完整项目视觉策略只能在`NARRATIVE_LOCK`之后生成，并引用其中的：

- 主角或主体；
- 人物关系与核心处境；
- 世界规则或主要表达机制；
- 关键选择；
- 高潮行动者与不可逆变化；
- 结尾及开放程度；
- 主题意义；
- 用户允许改动范围。

视觉制作可以改变实现方式、机位、镜头数量、资产和生成方法，但不得为了风格改变叙事事实。

## 三、创作中立

Skill统一推导方法和制作质量，不统一视觉结果。

禁止把以下内容设为全局默认：

- 冷灰、低饱和、暖金或任何固定配色；
- 写实、诗性、克制、宏大、东方、华丽或任何固定风格；
- 浅景深、慢推、对称构图、手持或固定运镜习惯；
- 背景必须压迫、托举或响应人物；
- 青年主角、古典服装、雾、水、废墟、花瓣、粒子等固定元素；
- 固定禁止喜剧、明亮色彩、夸张表演或快速剪辑。

同一Skill必须能够为现实主义、喜剧、恐怖、广告、MV、古典、科幻、无厘头和形式实验生成明显不同的项目策略。

## 四、从剧本推导

每条视觉规则必须有当前项目证据，并回答：

1. 人物在什么处境中行动；
2. 观众需要靠近、疏离、误判、等待还是见证；
3. 冲突通过人物、空间、物件、时间还是形式发生；
4. 高潮依赖什么可见行动与状态变化；
5. 结尾需要留下什么视觉余波；
6. 哪些元素承担主题，哪些只是装饰；
7. 平台、时长、画幅和模型允许怎样的制作复杂度。

不能只写“电影感、高级感、东方美学、赛博朋克、治愈、压迫”。

## 五、方向探索与锁定

用户没有成熟视觉方向时，内部探索2—4个真正不同的方案。差异应来自：

- 空间与人物尺度；
- 写实程度和媒介感；
- 摄影距离与运动方式；
- 色彩与真实光源；
- 材质系统；
- 表演温度；
- 背景职责；
- 生成与后期方法。

不得只做同一方案的轻微配色变化。

选择主方向时评估：

- 是否支持主题、人物和关键选择；
- 观众体验是否清楚；
- 是否保留原创性；
- 是否适合时长和画幅；
- 是否适合当前模型和后期条件；
- 是否能形成稳定资产和跨镜连续性。

用户已有明确成熟方向时优先忠实实现；只有内部冲突、不可生成或会破坏叙事时才修正。

策略锁定后只对当前项目生效，新项目必须重新推导。

## 六、最小字段

```yaml
project_visual_strategy:
  project_id:
  scope: PROJECT_ONLY
  activated_by:
  narrative_lock_reference:
  script_evidence: []
  audience_experience:
  visual_thesis:
  rejected_directions_and_reasons: []
  style_dna:
    spatial_logic:
    human_scale:
    time_feeling:
    color_system:
    material_system:
    lighting_logic:
    camera_temperament:
    performance_temperature:
    sound_world:
    graphic_and_text_rules:
    original_signature:
  background_strategy:
  visual_tension_sources: []
  visual_density_range:
  cleanliness_principle:
  material_semantic_boundaries:
  original_visual_grammar:
  aspect_ratio_implications:
  continuity_anchors:
    character:
    environment:
    props:
    light_world_positions:
    color_progression:
    material_progression:
  allowed_variation: []
  forbidden_drift: []
  production_implications:
    asset_requirements:
    shot_design_implications:
    cf_implications:
    generation_and_post_implications:
```

## 七、背景策略

背景职责由当前项目决定，可以：

- 提供真实空间与行动条件；
- 对抗、压迫、托举、隔离、吞没或揭示人物；
- 通过状态变化承担叙事；
- 作为喜剧反应空间；
- 保持克制中性；
- 承担形式、图形、节奏或声音结构。

剧情关键帧和背景承担变化的项目，需要定义背景大形、近中远层次、方向、局部高潮和主体关系。身份板、商品结构图和技术资产板使用低干扰背景，不机械影视化。

## 八、视觉密度、原创结构与材质

项目策略只定义全片范围与边界，不逐帧填写CF控制表。

至少明确：

- 华丽或简洁由什么空间、结构、材质和光影产生；
- 哪些区域允许高密度，哪些区域必须保持清洁；
- 大形、中尺度结构和小细节的总体比例；
- 微粒、数字噪点和胶片颗粒的项目原则；
- 当前项目的原创形状、连接、受力、重复和变化规则；
- 重要材质的可观察属性与模型常见替代风险；
- 道具是否需要生活化、磨损、不规则和非商业陈列；
- 横竖画幅变化会如何影响人物占比、负空间和动势。

不得把“极致华丽”翻译成满屏粒子、花瓣和碎片，也不得把“干净”翻译成删除中尺度结构后的空洞画面。

## 九、资产规划接口

策略完成后，根据实际Shot需求规划资产。必要性由以下覆盖决定：

- 人物景别、正侧背角度和身体动作；
- 重要面部近景；
- 全身、转身、背影、俯身、跪姿和复杂姿态；
- 服装、发型和配饰前后结构；
- 精确手部与道具交互；
- 污染、伤损、湿水、变装和其他累积状态；
- 正反打、反向机位、局部空间与时间状态；
- 道具结构、尺寸、页面、开合、破损与阶段变化；
- 跨镜需要保持的视觉锚点。

缺少依据会导致身份、结构、交互、状态或空间漂移的资产属于必要资产；没有实际Shot使用的资产应删除。

## 十、阶段加载与职责边界

本模块在S05只完成项目级视觉策略，不提前加载整个制作仓库。

后续按阶段读取：

### Shot阶段

读取：

- `references/scene-function-taxonomy.md`；
- `controllers/scene-function-router.md`；
- 当前镜头需要的摄影、灯光和表演模块。

项目策略决定“这是怎样的世界”，场景功能决定“这个Shot此刻主要给观众什么”。二者不能混为一谈。

### CF与图片阶段

剧情关键帧、START / END / BRIDGE CF、概念图或氛围图需要时读取：

- `controllers/frame-clarity-density-controller.md`；
- `prompt-engineering/image-prompt-compiler-v4.5-extension.md`；
- `templates/scene-function-frame-control-block.md`。

技术资产板只使用必要的结构、清洁度和材质部分，不强制复杂叙事画面控制。

### 最终检查阶段

读取：

- `evals/frame-communication-check.md`；
- `evals/full-package-integrity-check.md`。

检查模块不得在S05反向生成另一套项目视觉策略。

## 十一、Shot级场景功能接口

每个正式Shot建立：

```yaml
scene_function:
  primary:
  secondary:
  script_evidence: []
  audience_immediate_effect:
  audience_delayed_effect:
  information_emotion_spectacle_priority:
  first_read:
  second_read:
  final_reveal:
  execution_bias:
  must_not_sacrifice: []
  conflict_and_split_decision:
```

主功能必须且只能一个；次功能可为空且最多一个。标签不新增顶层模式，不绑定固定色彩、景别、题材、年龄、画幅或审美。

流程为：

```text
PROJECT_VISUAL_STRATEGY
→ Shot拆解
→ SCENE_FUNCTION_ROUTING
→ DIRECTOR_INTENT
→ CAMERA / LIGHTING / PERFORMANCE
→ CF与Prompt
```

## 十二、跨阶段一致性

资产、Shot、CF、图片Prompt和视频Prompt必须引用当前`PROJECT_VISUAL_STRATEGY`，但不得各自重写竞争版本。

检查：

- 是否仍服务`NARRATIVE_LOCK`；
- 是否继承视觉论点、Style DNA和连续性锚点；
- 镜头差异是否在允许变化范围内并有叙事理由；
- 是否出现上一项目、案例或模型默认风格污染；
- 是否把项目值误写成Skill全局规则；
- 场景功能、画幅和模型适配是否改变执行，而没有改变项目身份。

一致性不是要求每镜构图、色彩和景别相同，而是要求它们仍属于同一个项目世界。

## 十三、真实生成与学习边界

真实媒体用于发现：

- 跨场景共性缺口；
- 平台参数错误；
- 模型能力限制；
- Prompt、控制帧或资产问题；
- 适合局部修复的缺陷。

不得因为一张图或一个视频无限扩展核心规则。案例学习必须区分项目专属手法、可迁移机制、条件化策略和不可迁移美学；多个差异项目重复出现的问题才考虑升级。

## 十四、硬失败

出现以下任一情况，项目视觉策略不得通过：

- 在剧本完成前用固定视觉模板限制故事探索；
- 文本任务被强制生成资产和完整视觉圣经；
- 没有`NARRATIVE_LOCK`就锁定项目视觉；
- 策略没有引用当前剧本证据；
- 只写风格名、导演名、滤镜或抽象形容词；
- 为追求风格改变人物关系、核心机制、关键选择、高潮或结尾；
- 把固定配色、摄影、材质、表演温度、背景职责或画幅设为Skill默认；
- 华丽依赖随机粒子、碎片和高频纹理；
- 为了干净删除中尺度结构；
- 只列禁止模板，没有建立正向原创结构；
- 材质边界不清，导致玻璃、冰、塑料、霓虹等替代目标材质；
- 资产规划没有覆盖实际角度、交互、状态和空间；
- 生成无实际使用的冗余资产；
- 项目视觉策略阶段提前加载并重做Shot、CF、Prompt和评估工作；
- 局部图片或单镜任务伪称建立了全片视觉策略；
- 用户要求完善整体Skill时仍无限围绕同一张图微调。
