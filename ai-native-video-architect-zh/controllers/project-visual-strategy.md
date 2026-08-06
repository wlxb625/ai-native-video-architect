# Project Visual Strategy Controller V4.7

## 目标

在剧本或视觉脚本成立并进入制作阶段后，根据当前项目的主题、人物、空间、动作、时长、画幅、平台和生成条件，推导只对该项目生效的视觉制作策略，并在资产规划前完成：

1. `RENDER_MEDIUM_LOCK`：作品以什么视觉媒介存在；
2. `GENERATION_ROUTE_PLAN`：哪些Shot使用纯文生视频、参考文生视频、图生视频、首尾帧或后期主导。

本模块负责统一项目级视觉世界、渲染媒介、生成路线和后续制作边界，不替代Shot场景功能、摄影、灯光、表演、CF画面控制或Prompt编译，也不为整个Skill预设固定审美。

本阶段必须读取：

- `prompt-engineering/render-medium-generation-route-contract.md`。

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

单张图片、单镜视频、图生图、纯文生视频、续拍和局部修复只建立：

```text
LOCAL_IMAGE_VISUAL_CONTRACT
或
LOCAL_SHOT_VISUAL_CONTRACT
```

局部合同仍应明确当前媒介与生成路线，但不能伪称已经锁定整部作品。

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

视觉制作可以改变实现方式、渲染媒介、机位、镜头数量、资产和生成方法，但不得为了风格改变叙事事实。

## 三、创作中立

Skill统一推导方法和制作质量，不统一视觉结果。

禁止把以下内容设为全局默认：

- 冷灰、低饱和、暖金或任何固定配色；
- 写实、诗性、克制、宏大、东方、华丽或任何固定风格；
- 真人实拍、照片写实CG、风格化3D动画、二维动画、2.5D、游戏电影CG、水墨、定格或任何固定媒介；
- 浅景深、慢推、对称构图、手持或固定运镜习惯；
- 背景必须压迫、托举或响应人物；
- 青年主角、古典服装、雾、水、废墟、花瓣、粒子等固定元素；
- 固定禁止喜剧、明亮色彩、夸张表演或快速剪辑；
- 固定使用图生视频、首尾帧或纯文生视频。

同一Skill必须能够为现实主义、喜剧、恐怖、广告、MV、古典、科幻、无厘头和形式实验生成明显不同的项目策略、媒介合同和生产路线。

## 四、从剧本推导

每条视觉规则必须有当前项目证据，并回答：

1. 人物在什么处境中行动；
2. 观众需要靠近、疏离、误判、等待还是见证；
3. 冲突通过人物、空间、物件、时间还是形式发生；
4. 高潮依赖什么可见行动与状态变化；
5. 结尾需要留下什么视觉余波；
6. 哪些元素承担主题，哪些只是装饰；
7. 平台、时长、画幅和模型允许怎样的制作复杂度；
8. 哪种渲染媒介最能放大当前项目的角色、空间、情绪与动作优势；
9. 哪些镜头需要精确身份、构图和尾态，哪些镜头更需要文生视频的动态创造力。

不能只写“电影感、高级感、东方美学、赛博朋克、治愈、压迫、动漫风、3D感”。

## 五、方向探索与锁定

用户没有成熟视觉方向时，内部探索2—4个真正不同的方案。差异应来自：

- 渲染媒介与风格化程度；
- 角色面部、身体、头发和服装的设计语言；
- 环境形体与人物是否共用同一套视觉语法；
- 空间与人物尺度；
- 写实程度和媒介感；
- 摄影距离与运动方式；
- 色彩与世界内部成立的光源；
- 材质与着色系统；
- 表演与动画运动语言；
- 背景职责；
- 纯文生、参考文生、图生、首尾帧与后期方法。

不得只做同一真人写实方案的轻微配色变化，也不得只把“3D动漫”作为一句风格标签贴在真人摄影合同上。

选择主方向时评估：

- 是否支持主题、人物和关键选择；
- 观众体验是否清楚；
- 是否保留原创性；
- 是否适合时长和画幅；
- 是否适合当前模型和后期条件；
- 是否能形成稳定资产和跨镜连续性；
- 角色、环境、材质、灯光和运动是否属于同一媒介；
- 是否给需要自由动态的镜头保留文生视频空间；
- 是否给需要精确控制的镜头安排了足够参考或控制帧。

用户已有明确成熟方向时优先忠实实现；只有内部冲突、不可生成或会破坏叙事时才修正。

策略锁定后只对当前项目生效，新项目必须重新推导。

## 六、渲染媒介锁定

项目进入资产规划前必须建立：

```yaml
render_medium_lock:
  evidence: []
  medium:
  stylization_level:
  character_rendering:
  facial_design:
  skin_or_surface_shading:
  hair_rendering:
  costume_rendering:
  environment_rendering:
  material_language:
  lighting_language:
  camera_and_optical_translation:
  animation_language:
  compositing_language:
  target_visual_finish:
  allowed_medium_variation: []
  forbidden_medium_drift: []
```

媒介可以是真人实拍、照片写实CG、高端风格化3D动画、2.5D、二维动画、绘画动画、定格、水墨、游戏电影CG、混合媒介或项目自定义媒介。

“真实光源、真实材质、摄影机、焦段、景深、物理因果”必须按当前媒介翻译。它们要求世界内部逻辑清楚，不自动等于真人照片。

当前项目若锁定风格化3D动画，必须进一步说明角色建模、面部风格化、皮肤或表面着色、发束造型、服装大形、环境形体、动画电影灯光、关键姿势和次级动作，禁止退回真人写真、真人CG替身或普通游戏截图。

## 七、生成路线计划

媒介锁定后、资产规划前建立：

```yaml
generation_route_plan:
  evidence: []
  project_default:
  route_reasoning:
  model_and_platform_conditions:
  direct_t2v_eligible_shots: []
  reference_t2v_shots: []
  image_to_video_shots: []
  first_last_frame_shots: []
  post_only_shots: []
  route_decision_rules:
  asset_implications:
  control_frame_implications:
  fallback_order: []
```

允许的主路线：

- `PURE_T2V`；
- `REFERENCE_T2V`；
- `IMAGE_TO_VIDEO`；
- `FIRST_LAST_FRAME`；
- `HYBRID`；
- `POST_LED`。

正式Shot仍需逐镜选择，不因项目默认路线而机械统一。

路线判断必须考虑：

- 身份和服装是否必须稳定；
- 首帧构图是否必须准确；
- 尾态是否必须精确抵达；
- 是否有精确手部、接触、开合或状态变化；
- 画面价值是否主要来自宏观空间、材质和抽象运动；
- 是否已有真实可用参考；
- 平台支持的参考与控制方式；
- 失败后的稳定降级路线。

## 八、最小字段

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
  render_medium_lock:
    evidence: []
    medium:
    stylization_level:
    character_rendering:
    facial_design:
    skin_or_surface_shading:
    hair_rendering:
    costume_rendering:
    environment_rendering:
    material_language:
    lighting_language:
    camera_and_optical_translation:
    animation_language:
    compositing_language:
    target_visual_finish:
    allowed_medium_variation: []
    forbidden_medium_drift: []
  generation_route_plan:
    evidence: []
    project_default:
    route_reasoning:
    model_and_platform_conditions:
    direct_t2v_eligible_shots: []
    reference_t2v_shots: []
    image_to_video_shots: []
    first_last_frame_shots: []
    post_only_shots: []
    route_decision_rules:
    asset_implications:
    control_frame_implications:
    fallback_order: []
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
    render_medium:
    light_world_positions:
    color_progression:
    material_progression:
  allowed_variation: []
  forbidden_drift: []
  production_implications:
    route_driven_asset_requirements:
    shot_design_implications:
    cf_implications:
    generation_and_post_implications:
```

## 九、背景策略

背景职责由当前项目决定，可以：

- 提供真实空间与行动条件；
- 对抗、压迫、托举、隔离、吞没或揭示人物；
- 通过状态变化承担叙事；
- 作为喜剧反应空间；
- 保持克制中性；
- 承担形式、图形、节奏或声音结构。

剧情关键帧和背景承担变化的项目，需要定义背景大形、近中远层次、方向、局部高潮和主体关系。身份板、商品结构图和技术资产板使用低干扰背景，不机械影视化。

背景设计必须继承当前媒介。风格化3D角色不能被贴进一套完全不同语言的写实场景；二维角色、定格模型和真人实拍也必须拥有各自成立的空间与材质关系。

## 十、视觉密度、原创结构与材质

项目策略只定义全片范围与边界，不逐帧填写CF控制表。

至少明确：

- 华丽或简洁由什么空间、结构、材质、着色和光影产生；
- 哪些区域允许高密度，哪些区域必须保持清洁；
- 大形、中尺度结构和小细节的总体比例；
- 微粒、数字噪点、胶片颗粒、笔触或动画纹理的项目原则；
- 当前项目的原创形状、连接、受力、重复和变化规则；
- 重要材质在当前媒介中的可观察属性与模型常见替代风险；
- 人物、服装和环境是否共享曲线、折面、连接、纹理或受力语言；
- 横竖画幅变化会如何影响人物占比、负空间和动势。

不得把“极致华丽”翻译成满屏粒子、花瓣和碎片，也不得把“干净”翻译成删除中尺度结构后的空洞画面。

## 十一、路线驱动的资产规划接口

策略和Shot路线预判完成后，再根据实际需求规划资产。必要性由以下两类证据共同决定：

### 镜头覆盖证据

- 人物景别、正侧背角度和身体动作；
- 重要面部近景；
- 全身、转身、背影、俯身、跪姿和复杂姿态；
- 服装、发型和配饰前后结构；
- 精确手部与道具交互；
- 污染、伤损、湿水、变装和其他累积状态；
- 正反打、反向机位、局部空间与时间状态；
- 道具结构、尺寸、页面、开合、破损与阶段变化；
- 跨镜需要保持的视觉锚点。

### 生成路线证据

- `PURE_T2V`是否真的需要角色、风格、材质或世界参考；
- `REFERENCE_T2V`需要哪些可被平台实际读取的参考；
- `IMAGE_TO_VIDEO`需要哪些母参考来生成准确首帧；
- `FIRST_LAST_FRAME`需要哪些起点、终点和桥接依据；
- `POST_LED`需要哪些底板、前景层、遮罩和后期素材。

缺少依据会导致身份、结构、交互、状态、空间或媒介漂移的资产属于必要资产；没有实际Shot和路线使用的资产应删除。

禁止在生成路线尚未确定时机械规划固定十项、六宫格、所有机位或所有状态资产。

## 十二、阶段加载与职责边界

本模块在S05只完成项目级视觉策略、媒介锁定和项目级路线计划，不提前重做全部Shot和Prompt。

后续按阶段读取：

### 资产阶段

读取：

- `prompt-engineering/render-medium-generation-route-contract.md`；
- `prompt-engineering/asset-prompt-system.md`；
- 当前媒介需要的材质与设计模块。

资产必须继承媒介，并由Shot路线决定是否需要。

### Shot阶段

读取：

- `prompt-engineering/render-medium-generation-route-contract.md`；
- `references/scene-function-taxonomy.md`；
- `controllers/scene-function-router.md`；
- 当前镜头需要的摄影、灯光和表演模块。

每个Shot在导演设计前先锁定本镜生成路线及其控制边界。

### CF与图片阶段

剧情关键帧、START / END / BRIDGE CF、概念图或氛围图需要时读取：

- `prompt-engineering/render-medium-generation-route-contract.md`；
- `controllers/frame-clarity-density-controller.md`；
- `prompt-engineering/image-prompt-compiler-v4.5-extension.md`；
- `templates/scene-function-frame-control-block.md`。

`PURE_T2V`镜头没有实际控制帧需求时，不得为了填模板而生成伪首帧。技术资产板只使用必要的结构、清洁度和当前媒介材质部分。

### 视频Prompt阶段

读取：

- `prompt-engineering/render-medium-generation-route-contract.md`；
- `prompt-engineering/video-prompt-compiler.md`；
- 当前Shot已批准的导演、摄影、灯光、表演和连续性设计。

Prompt结构必须随`PURE_T2V / REFERENCE_T2V / IMAGE_TO_VIDEO / FIRST_LAST_FRAME / POST_LED`改变。

### 最终检查阶段

读取：

- `evals/frame-communication-check.md`；
- `evals/full-package-integrity-check.md`。

检查模块不得在S05反向生成另一套项目视觉策略、媒介合同或生成路线。

## 十三、Shot级场景功能接口

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

并在Shot卡中记录：

```yaml
shot_generation_route:
  route:
  reason:
  actual_inputs: []
  exact_start_required:
  exact_end_required:
  identity_lock_required:
  fallback_route:
```

主场景功能必须且只能一个；次功能可为空且最多一个。标签不新增顶层模式，不绑定固定色彩、景别、题材、年龄、画幅或媒介。

流程为：

```text
PROJECT_VISUAL_STRATEGY
→ RENDER_MEDIUM_LOCK
→ GENERATION_ROUTE_PLAN
→ 路线驱动的资产规划
→ Shot拆解
→ SHOT_GENERATION_ROUTE
→ SCENE_FUNCTION_ROUTING
→ DIRECTOR_INTENT
→ CAMERA / LIGHTING / PERFORMANCE
→ 按路线生成CF与Prompt
```

## 十四、跨阶段一致性

资产、Shot、CF、图片Prompt和视频Prompt必须引用当前`PROJECT_VISUAL_STRATEGY`、`RENDER_MEDIUM_LOCK`和`GENERATION_ROUTE_PLAN`，但不得各自重写竞争版本。

检查：

- 是否仍服务`NARRATIVE_LOCK`；
- 是否继承视觉论点、Style DNA、媒介合同和连续性锚点；
- 镜头差异是否在允许变化范围内并有叙事理由；
- 是否出现上一项目、案例或模型默认风格污染；
- 是否把项目值误写成Skill全局规则；
- 场景功能、画幅和模型适配是否改变执行，而没有改变项目身份；
- 是否在风格化动画项目中突然出现真人照片、真人CG替身或不一致游戏截图；
- 是否为纯文生视频镜头虚构参考绑定；
- 是否为精确人物和手部镜头错误省略控制依据。

一致性不是要求每镜构图、色彩、景别和生成路线相同，而是要求它们仍属于同一个项目世界和媒介体系。

## 十五、真实生成与学习边界

真实媒体用于发现：

- 渲染媒介漂移；
- 生成路线选择错误；
- 跨场景共性缺口；
- 平台参数错误；
- 模型能力限制；
- Prompt、控制帧或资产问题；
- 适合局部修复或后期解决的缺陷。

单张图失败时，先区分：

```text
MEDIUM_SELECTION_FAILURE
PROMPT_TRANSLATION_FAILURE
ASSET_OR_CONTROL_FRAME_FAILURE
MODEL_CAPABILITY_FAILURE
```

不得因为一张图或一个视频无限扩展核心规则。案例学习必须区分项目专属手法、可迁移机制、条件化策略和不可迁移美学；多个差异项目重复出现的问题才考虑升级。

## 十六、硬失败

出现以下任一情况，项目视觉策略不得通过：

- 在剧本完成前用固定视觉模板限制故事探索；
- 文本任务被强制生成资产和完整视觉圣经；
- 没有`NARRATIVE_LOCK`就锁定项目视觉；
- 策略没有引用当前剧本证据；
- 完整制作项目没有`RENDER_MEDIUM_LOCK`；
- 只写风格名、导演名、滤镜、动漫风、3D感或抽象形容词；
- 把电影感、真实光源或真实材质自动解释为真人照片；
- 用户要求风格化3D动画，角色与环境仍按真人写真和现实摄影编译；
- 角色、服装、背景和材质不属于同一媒介语言；
- 在资产规划之后才决定生成路线；
- 所有Shot无理由统一为图生视频、首尾帧或纯文生视频；
- `PURE_T2V`镜头被迫生成伪首帧和伪参考图；
- 精确身份、手部、接触或尾态镜头无理由使用纯文生视频；
- 为追求风格改变人物关系、核心机制、关键选择、高潮或结尾；
- 把固定配色、摄影、材质、表演温度、背景职责、媒介或画幅设为Skill默认；
- 华丽依赖随机粒子、碎片和高频纹理；
- 为了干净删除中尺度结构；
- 只列禁止模板，没有建立正向原创结构；
- 材质边界不清，导致玻璃、冰、塑料、霓虹等替代目标材质；
- 资产规划没有覆盖实际角度、交互、状态、空间和路线；
- 生成无实际使用的冗余资产；
- 项目视觉策略阶段提前加载并重做全部Shot、CF、Prompt和评估工作；
- 局部图片或单镜任务伪称建立了全片视觉策略；
- 用户要求完善整体Skill时仍无限围绕同一张图微调。
