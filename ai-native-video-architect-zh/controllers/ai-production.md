# AI Production Controller

## 目标

把已成立的概念、剧本、视觉叙事和镜头语言转译为可生成、可连续、可剪辑、可修复、可追踪版本的AI电影生产系统。

核心原则：

> 先锁定资产，再生成分镜帧；先锁定分镜帧，再让画面运动。

文字设定不能替代生产参考。用户要求正式制作、角色一致、场景一致、道具一致、具体分镜或批量Prompt时，必须先读取：

- `controllers/asset-first-production.md`
- `controllers/detailed-storyboard.md`
- `core/continuity.md`
- `templates/asset-registry.md`

## 生产阶段

```text
P0 作品与保护合同
P1 Visual Bible与摄影主规格
P2 Asset Registry与资产需求
P3 角色/服装/场景/道具资产
P4 Asset Readiness Gate
P5 分镜首帧与尾帧
P6 视频动作Prompt与生成方法
P7 续拍、硬切、分层合成与版本管理
P8 粗剪、声音、调色与连续性回归
```

不得从P1直接跳到P6。

## P0：保护合同

```yaml
production_protection:
  must_preserve: []
  allowed_implementation_changes: []
  forbidden_changes: []
  allowed_visual_drift: []
  forbidden_visual_drift: []
  target_delivery:
  budget_level:
```

制作难度不能成为未经授权改变人物选择、高潮、结尾或开放程度的理由。

## P1：视觉圣经与摄影主规格

```yaml
visual_bible:
  aspect_ratio:
  palette:
    primary: []
    secondary: []
    accent: []
  white_balance:
  saturation:
  contrast:
  lighting_rules:
  material_rules:
  atmosphere:
  spatial_scale:
  camera_temperament:
  texture_and_grain:
  forbidden_look: []
```

用户未指定且明确要求电影级横屏详细分镜时，可采用：

```yaml
cinematic_master_spec:
  aspect_ratio: 21:9
  camera_reference: ARRI Alexa 35 or ARRI Alexa LF
  lens_system: restrained anamorphic
  frame_rate: 24fps
  shutter_angle: 180deg
  dynamic_range: wide, natural exposure relationship
  highlight_rolloff: soft and gradual
  shadow_detail: preserved
  grain: subtle and fine
  sharpening: restrained
  actor_realism: ordinary real actor, natural unretouched skin
  material_realism: source-based wear and age
  movement_policy: motivated and physically plausible
```

摄影机名称不能代替具体光线、曝光、材质、构图和运动描述。

## P2：Asset Registry

为资产分配稳定ID：

- `CHAR_`：角色身份；
- `FACE_`：面部身份；
- `HAIR_`：发型结构；
- `COST_`：服装状态；
- `POSE_`：姿态和动作语言；
- `SCENE_`：场景主空间；
- `PLATE_`：无人物空镜；
- `ANGLE_`：场景多机位；
- `PROP_`：道具和状态；
- `FRAME_`：镜头首帧或尾帧；
- `SHOT_`：视频版本。

镜头Prompt引用资产ID和参考图，不为每个镜头重新定义人物与空间。

## P3：角色资产

角色正式生产至少需要：

1. 正面、严格侧面、背面全身三视图；
2. 正面、左右四分之三和侧脸面部身份板；
3. 发型正侧背结构；
4. 服装内外层、袖口、下摆、鞋履和材质板；
5. 与剧情相关的服装状态版本；
6. 手部与核心道具交互参考；
7. 常用姿态和动作语言。

艺术身份板可用于风格探索，但不能代替生产三视图。

角色应保留普通真实演员特征：毛孔、轻微不对称、自然泛红、细纹、眼袋、嘴唇纹理、眉毛、发际线、发丝和区域色差。禁止网红脸、明星脸、模特脸、塑料皮肤和商业精修。

## P3：场景资产

每个多镜头主场景至少建立：

- `Environment Lock`：布局、出入口、地标、道具位置和光源；
- `Empty Plate`：无人物宽景、中景和必要细节空镜；
- `Master Layout`：平面关系、轴线、人物路线和可用机位；
- `Multi-Angle Board`：同一场景的关键机位参考；
- 场景状态版本：初始、变化、结果。

人物分镜帧优先由角色资产与场景空镜共同生成，不凭文字重新生成整个背景。

## P3：道具资产

核心道具记录：

- 尺寸和人体比例；
- 正面、侧面、背面或底部结构；
- 材料、制作工艺和时代依据；
- 磨损、包浆、氧化和独特标记；
- 持有、佩戴、存放和使用逻辑；
- 状态版本及由哪个镜头产生。

反复出现或影响剧情的武器、工具、面具、乐器、容器、信物和标志物必须建立三视图或结构板。

## P4：Asset Readiness Gate

只有以下内容通过，才能开始正式分镜帧：

- 角色不同角度身份一致；
- 服装结构和状态链清楚；
- 场景布局、地标和主光方向稳定；
- 核心道具尺寸、结构和状态定义完整；
- 连续性台账已建立；
- 参考图清楚、无遮挡、能用于后续生成。

若任务仅为概念探索，可使用`CONDITIONAL`资产；若声称“可直接生产”，关键资产必须`PASS`。

## P5：首帧与尾帧

### 首帧负责

- 当前资产版本；
- 人物和道具准确位置；
- 静态姿态；
- 构图、景别和机位；
- 前景、中景、背景；
- 光线、材质和色彩；
- 为动作预留的运动空间。

### 尾帧负责

- 动作完成后的准确姿态；
- 人物与道具最终位置；
- 场景最终状态；
- 摄影机和焦点终点；
- 下一镜要继承的状态。

以下镜头优先使用首尾帧：外观或服装变化、道具打开/断裂/燃烧、建筑变化、空间转化、指定动作终点和单首帧难以稳定控制的变化。

## P6：图片Prompt与视频Prompt分离

### 图片Prompt

```text
固定视觉基准
+ 角色/服装/场景/道具资产引用
+ 当前静态姿态
+ 构图、景别、机位与空间层次
+ 光线、曝光、色彩和材质
+ 当前状态与下一动作空间
+ 禁止漂移
```

### 视频Prompt

```text
使用指定首帧
+ 保持哪些资产不变
+ 起始状态
+ 唯一主要动作
+ 起势、过程、收住
+ 方向、速度、幅度和重心
+ 摄影机起点、运动、速度和终点
+ 允许运动的环境元素
+ 指定结束状态
+ 禁止变化
```

视频Prompt主要描述运动，不重复整套人物外貌和风格词。身份稳定由资产参考承担。

## P6：镜头类型与策略

### Establishing

用空镜或角色进入场景的稳定关键帧建立空间。避免无目标飞行。

### Performance

人物反应、选择和微动作。优先参考图、短动作和清楚的收住姿态。

### Interaction

人物与道具或另一人物交互。先建立手部、尺寸、左右手和接触关系。

### Spectacle

核心奇观拆为前兆、发生、结果；人物底板、环境层和效果层可分开制作。

### Symbol

物件、重复动作和情绪回环。使用精确构图、低动作复杂度和声音强化。

### Connector

视线、脚步、手部、门、光线、道具位置和尾帧续拍连接。

## P7：续拍与硬切

### 尾帧续拍

适用于动作、运镜或同一场景继续。提取上一段稳定尾帧作为下一段唯一首帧，只描述剩余动作，不重新设计场景。

### 硬切

适用于换景别、换机位和提高节奏。允许改变观看角度，必须保持：人物身份、服装、道具、动作进度、站位关系、空间布局、光线方向和色调。

硬切记录切点、动作完成百分比、左右手、视线、背景地标和下一动作空间。

## P7：生成批次

不要一次性生成整片。推荐：

1. 一名核心角色；
2. 一个主场景；
3. 一个核心道具；
4. 一个同时包含角色、场景、道具和动作的Core Sample；
5. 两个不同机位的一致性测试；
6. 一次首尾帧或硬切测试；
7. 通过后扩展其他镜头。

## 一致性检查

- 画幅和安全构图；
- 脸、发型、身体比例和真实演员质感；
- 服装状态版本；
- 道具尺寸、结构、状态、位置和左右手；
- 场景布局、地标、轴线和光源方向；
- 人物出入方向、视线和动作结果；
- 色彩、曝光、颗粒、锐度和运动气质；
- 首帧、尾帧和下一镜继承状态。

## 失败恢复

- 换脸：回到FACE资产，不通过镜头Prompt继续堆外貌词；
- 服装漂移：建立或修复COST状态板；
- 场景漂移：使用空镜和多机位板，减少自由重建；
- 道具变形：使用三视图、尺寸和手部交互板；
- 手部失败：拆分接近、接触和结果，或使用遮挡与后期；
- 动作失败：减少同时动作，明确起势和收住；
- 变化失控：改用首尾帧或分层合成；
- 无法剪辑：补尾帧、硬切首帧和连接镜头；
- CG感：减少空泛质量词，强化真实曝光、材料历史和物理运动。

## 输出要求

正式PRODUCTION_PACK至少输出：

1. 保护合同；
2. Visual Bible与摄影主规格；
3. Asset Registry；
4. 角色、服装、场景、道具资产包；
5. Asset Readiness Gate；
6. 分镜首帧/尾帧资产需求；
7. 视频动作Prompt；
8. 生成方法与分层计划；
9. 版本命名和生成顺序；
10. 风险、稳定替代和连续性回归。
