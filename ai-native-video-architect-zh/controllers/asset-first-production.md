# Asset-First Production Controller

## 目标

在进入详细分镜、首帧图或视频Prompt前，先建立可复用、可编号、可追踪状态的角色、服装、场景、道具与镜头帧资产。

本控制器解决一个常见误区：

> 文字写得很长，不等于资产已经稳定。

当每个镜头都重新描述人物、场景和道具时，模型仍会重新设计它们，造成换脸、换衣、建筑漂移、道具变形和光线跳变。

## 触发条件

当用户要求以下任一内容时，必须读取本文件：

- 具体分镜、逐镜头、分镜图、首帧、尾帧；
- 角色一致、场景一致、道具一致；
- 人物三视图、角色板、服装设定、道具三视图；
- 图生视频、首尾帧视频、抽尾帧续拍；
- 可直接生成、正式制作包、批量生成；
- 同一角色跨多个镜头、同一场景多机位或道具存在状态变化。

同时读取：

- `controllers/ai-production.md`
- `controllers/detailed-storyboard.md`
- `core/continuity.md`
- `templates/asset-registry.md`

## 核心顺序

```text
剧本锁定
→ 视觉圣经
→ 资产需求清单
→ 角色资产
→ 服装状态资产
→ 场景空镜与空间主图
→ 道具资产与状态版本
→ 资产审核
→ 分镜首帧/尾帧
→ 视频动作Prompt
→ 生成、续拍、硬切与回归
```

不得从剧本直接跳到批量视频Prompt。

## 资产编号协议

每项资产必须有稳定ID：

```text
CHAR_C01          角色身份
FACE_C01          面部身份板
HAIR_C01          发型结构
COST_C01_A        角色C01的服装状态A
POSE_C01_P03      角色C01的姿态03
SCENE_S01         场景主空间
PLATE_S01_WIDE    场景S01无人物宽景空镜
ANGLE_S01_L03     场景S01第3个机位
PROP_P01          核心道具
PROP_P01_B        道具P01状态B
FRAME_SH03_IN     镜头03首帧
FRAME_SH03_OUT    镜头03尾帧
SHOT_SH03_V04     镜头03第4版视频
```

Prompt优先引用资产ID与参考图，不在每个镜头中重新发明资产。

## Asset Readiness Gate

进入正式分镜图前检查：

```yaml
asset_readiness:
  visual_bible: PASS | CONDITIONAL | FAIL
  character_identity: PASS | CONDITIONAL | FAIL | NOT_APPLICABLE
  costume_states: PASS | CONDITIONAL | FAIL | NOT_APPLICABLE
  environment_layout: PASS | CONDITIONAL | FAIL
  empty_plates: PASS | CONDITIONAL | FAIL
  props_and_states: PASS | CONDITIONAL | FAIL | NOT_APPLICABLE
  continuity_registry: PASS | CONDITIONAL | FAIL
  reference_quality: PASS | CONDITIONAL | FAIL
  ready_for_storyboard_frames: true | false
```

以下情况必须`ready_for_storyboard_frames: false`：

- 角色正面、侧面和背面明显不是同一人；
- 服装结构或颜色在参考板中已经不一致；
- 场景没有固定布局或光线方向；
- 核心道具没有尺寸、结构或状态定义；
- 故事依赖道具变化，但没有状态时间线；
- 资产图被艺术排版遮挡，无法作为生产参考；
- 只有文字设定，没有至少一张可用参考资产，且任务要求稳定制作。

## 角色资产包

正式角色至少包含：

### 1. Production Turnaround

- 正面全身；
- 严格90度侧面全身；
- 背面全身；
- 同一站姿、光线、比例和服装状态；
- 头顶到脚底完整，不裁切；
- 纯色或中性背景，无场景干扰。

三视图是生产资产，不等同于艺术角色板。

### 2. Face Identity Board

- 正面无表情；
- 左右四分之三侧脸；
- 标准侧脸；
- 眼睛、鼻翼、嘴唇、皮肤、发际线和鬓角细节；
- 2—4个与作品相关的细微表情；
- 普通真实演员质感，避免精修模特脸。

### 3. Hair Structure Board

- 正面、侧面和背面；
- 发髻、分缝、饰物插入位置、碎发分布；
- 湿润、风吹或受损状态需要单独版本。

### 4. Costume Pack

每套服装记录：

- 内层、中层、外层；
- 领口、袖口、腰带、下摆、鞋履；
- 布料、缝线、纹样和做旧位置；
- 穿戴逻辑与开合结构；
- 允许变化和禁止变化。

若服装在剧情中变化，必须建立`COST_A → COST_B → COST_C`状态链，不能只写“逐渐变红”或“越来越破旧”。

### 5. Hand and Interaction Board

当手部或持物重要时，记录：

- 左右手分工；
- 握持位置和方向；
- 手掌与道具尺寸比例；
- 指甲、皮肤、手套或伤痕；
- 常用接触动作和禁止穿模关系。

### 6. Pose and Motion Language

至少建立与作品相关的标准姿态：

- 自然站立；
- 行走；
- 坐、跪或俯身；
- 持物；
- 情绪停顿；
- 高潮动作。

复杂连续动作才使用4—9格动作故事板；普通静态场景不机械使用九宫格。

## 艺术角色板与生产角色板

艺术身份板可用于探索气质、轮廓和表情范围，但不能单独承担生产锁定。

如果艺术板存在：

- 不对称排版；
- 多种姿态；
- 局部裁切；
- 强光影或复杂构图；

则仍需补充标准三视图和面部身份板。

## 场景资产包

每个主场景至少包含：

### 1. Environment Lock

- 时代与地点；
- 场景功能；
- 空间布局；
- 出入口；
- 固定地标；
- 地面、墙体、顶部和远景；
- 核心道具的位置；
- 主光、辅光和环境光来源；
- 时间、天气、空气状态；
- 主色、辅色、点缀色、色温、饱和度和对比度；
- 禁止出现的时代错误与现代物件。

### 2. Empty Plate

先生成无人物空镜，用于锁定：

- 建筑结构；
- 透视；
- 材质；
- 光源方向；
- 道具位置；
- 空间纵深。

人物分镜图应引用角色资产与空镜资产共同生成，不凭文字重新生成整个空间。

### 3. Master Layout

用平面图、俯视图或清楚的文字台账记录：

- 门、窗、柱、桌、楼梯和主要道具；
- 人物进入、离开和可走路线；
- 轴线和屏幕方向；
- 可用机位区与不可穿越区域。

### 4. Multi-Angle Environment Board

当同一场景有三个以上机位时，补充：

- 正面宽景；
- 左侧、右侧；
- 侧后方；
- 低机位；
- 高机位或俯视；
- 关键道具对应方向。

所有机位只改变观看角度，不改变建筑、光线、地面和道具布局。

## 道具资产包

核心道具必须记录：

```yaml
prop_asset:
  id:
  name:
  narrative_function:
  era_and_culture:
  dimensions:
  silhouette:
  front_side_back:
  materials:
  construction_logic:
  colors:
  wear_and_patina:
  unique_marks:
  storage_or_carry_method:
  hand_relationship:
  default_location:
  states: []
  forbidden_changes: []
```

需要三视图的道具：武器、工具、乐器、法器、容器、面具、交通工具和反复出现的标志物。

状态变化例：

```text
PROP_P01_A 完整
PROP_P01_B 沾水
PROP_P01_C 断裂
PROP_P01_D 被遗留
```

每个状态明确由哪个镜头产生、后续哪些镜头继承。

## 图片Prompt与视频Prompt分离

### 图片Prompt负责

- 当前资产版本；
- 静态姿态和物件位置；
- 前景、中景、背景；
- 画幅、构图、景别和机位；
- 光线、色彩、材质和空间；
- 首帧或尾帧的准确状态。

### 视频Prompt负责

- 使用哪张图作为唯一首帧；
- 起始状态；
- 唯一主要动作；
- 起势、过程、收住；
- 动作方向、速度、幅度和重心；
- 摄影机运动起点、终点、速度与动机；
- 环境中允许运动的元素；
- 结束状态；
- 禁止变化项。

视频Prompt不应被重复的外貌和风格形容词淹没。稳定身份由参考资产承担。

## 首帧与尾帧协议

对以下镜头优先制作首尾帧：

- 角色服装或外观状态变化；
- 道具打开、破裂、燃烧、消失或变形；
- 建筑或环境发生结构变化；
- 画面从一种空间状态过渡到另一种；
- 动作必须准确停在指定姿态；
- 单首帧生成经常偏离目标终点。

```yaml
frame_pair:
  shot_id:
  start_frame_asset:
  end_frame_asset:
  invariant_assets: []
  allowed_changes: []
  transformation_path:
  camera_path:
  final_hold:
  fallback_composite:
```

复杂变化若首尾帧仍不稳定，拆成前兆、发生和结果，不强迫一个镜头完成全部变化。

## 尾帧续拍

同一动作、同一场景或同一运镜需要继续时：

1. 提取上一段最终稳定帧；
2. 将其登记为下一镜或下一段的首帧资产；
3. 继承人物位置、姿态、服装、道具、背景、光线、色调和机位；
4. 只描述尚未完成的动作；
5. 禁止模型重新设计场景或让人物突然换动作。

尾帧续拍不等于所有镜头都做伪一镜到底。正常电影剪辑优先使用有动机的硬切。

## 硬切连续性

换景别或换机位时，记录：

- 切点动作节点；
- 人物位置和朝向；
- 道具在哪只手；
- 视线方向；
- 动作已完成百分比；
- 主光方向；
- 背景地标；
- 下一镜需要保留的运动空间。

硬切可以改变景别和角度，不能改变事实和空间布局。

## 生成批次原则

不一次性批量生成整片。推荐：

1. 完成一名角色与一个主场景的资产闭环；
2. 选择一个同时包含角色、场景、道具和动作的Core Sample；
3. 验证资产能否在两个不同机位中保持稳定；
4. 验证首尾帧或硬切能否连接；
5. 通过后再扩展其他镜头。

## 项目目录与版本

推荐：

```text
PROJECT/
├── 01_script/
├── 02_visual_bible/
├── 03_characters/
├── 04_costumes/
├── 05_environments/
├── 06_props/
├── 07_storyboard_frames/
├── 08_video_clips/
├── 09_audio/
├── 10_post/
└── 11_delivery/
```

命名示例：

```text
CHAR_C01_FACE_FRONT_V03.png
SCENE_S02_EMPTY_WIDE_V02.png
PROP_P01_STATE_B_SIDE_V01.png
FRAME_SH07_OUT_V04.png
SHOT_SH07_VIDEO_V06.mp4
```

不得覆盖已选中的生产版本；新尝试使用新版本号。

## 输出要求

资产制作任务至少输出：

1. 资产需求清单；
2. 资产ID与状态版本；
3. 每项资产的文字定义；
4. 可直接生成的中文Prompt；
5. 必要时的英文Prompt；
6. 负面约束；
7. 资产审核标准；
8. 资产之间的引用关系；
9. 建议生成顺序；
10. 失败恢复方案。
