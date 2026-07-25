# Production Management Controller

## 目标

把导演方案转为可排期、可分配资源、可控制成本、可追踪资产与版本、可恢复失败的生产计划。

生产管理的最小单位不仅是镜头，还包括：

- 角色、面部、发型和姿态资产；
- 服装状态；
- 场景空镜、布局和机位资产；
- 道具与状态版本；
- 分镜首帧和尾帧；
- 视频片段、声音和后期版本。

## 镜头价值评估

```yaml
shot_value:
  story_value: 0-5
  visual_value: 0-5
  emotional_value: 0-5
  propagation_value: 0-5
  continuity_value: 0-5
  generation_difficulty: 0-5
  asset_dependency_count: 0-20
  postproduction_difficulty: 0-5
  priority: S | A | B | C
```

- S：作品标志、高潮、核心规则或传播镜头；
- A：人物选择、关系变化和关键情绪；
- B：必要信息、空间建立与连接；
- C：可替代过渡或装饰。

默认资源分配：S+A约70%，B约20%，C约10%。C镜头成本超过价值时合并或删除。

## 资产价值评估

```yaml
asset_value:
  asset_id:
  type: character | costume | environment | prop | frame | audio
  reused_by_shots: []
  identity_importance: 0-5
  continuity_importance: 0-5
  generation_cost: 0-5
  replacement_difficulty: 0-5
  approval_status: DRAFT | REVIEW | APPROVED | REJECTED
```

高复用角色、主场景和核心道具资产应优先投入，不在低质量基础资产上批量生成镜头。

## 资产清单

至少跟踪：

- 生产三视图、面部身份板、发型板和姿态；
- 每个角色的服装状态链；
- 场景主布局、无人物空镜、多机位和光照状态；
- 核心道具三视图、尺寸、独特标记和状态版本；
- 每镜首帧、尾帧、源图、生成版本、选中版本和失败原因；
- 字幕、界面、标识和后期文字；
- 环境声、声音母题、配音和音乐。

使用 `templates/asset-registry.md`。

## 生产顺序

不要按剧情顺序盲目生成。推荐：

1. Production Protection Contract；
2. Visual Bible和摄影主规格；
3. Asset Registry和需求清单；
4. 核心角色三视图、面部和服装状态；
5. 主场景布局、无人物空镜和多机位；
6. 核心道具三视图与状态链；
7. Asset Readiness Gate；
8. 一个包含角色、场景、道具和动作的Core Sample；
9. 两个不同机位的一致性测试；
10. 一次首尾帧或硬切衔接测试；
11. S/A镜头；
12. B连接镜头；
13. C镜头、补镜和后期元素；
14. 粗剪、声音、调色和连续性回归。

Core Sample失败时先修资产或设计，不继续批量抽卡。

## 生成批次

推荐按资产依赖分批，而不是一次铺满全部节点：

### Batch 1：Identity

- 一名核心角色；
- 一套初始服装；
- 一个面部身份板；
- 一套基本姿态。

### Batch 2：World

- 一个主场景；
- 一张宽景空镜；
- 两个关键机位；
- 一个核心道具。

### Batch 3：Proof

- 一个稳定首帧；
- 一个稳定尾帧；
- 一个3—8秒测试视频；
- 一个硬切或尾帧续拍测试。

通过后再扩展。

## Asset Readiness Gate

正式批量生产前检查：

- 角色不同角度是否同一身份；
- 服装和发型结构是否稳定；
- 场景是否有固定布局和光源方向；
- 核心道具是否有尺寸、结构和状态；
- 资产图是否清楚、无遮挡、可引用；
- 连续性台账是否能回答每镜使用哪个版本；
- 首帧、尾帧和硬切策略是否可行。

任一核心项FAIL时暂停批量生产。

## 工具匹配原则

不把工具名称和版本永久写死。根据当前能力选择：

- 概念探索与角色设定；
- 身份或场景一致性生成；
- 图像编辑和局部重绘；
- 单首帧图生视频；
- 首尾帧视频；
- 视频续拍或扩展；
- 分层合成、剪辑、调色和声音。

涉及最新模型能力、价格、参数和版权时实时核实。

## 成本与规模

### 低成本

- 1名主要角色；
- 1个主场景；
- 1—2个核心道具；
- 4—8个镜头；
- 低动作复杂度；
- 使用空镜、特写和声音扩展世界。

### 中等成本

- 完整核心角色资产；
- 2—3个主场景；
- 服装和道具状态链；
- 5—10个核心镜头；
- 少量首尾帧和分层合成。

### 高质量

- 完整角色、服装、场景、道具资产库；
- 多轮Core Sample；
- 首尾帧、续拍、分层合成；
- 系统版本管理、统一调色和声音设计。

## 失败恢复

每个S/A镜头必须有稳定替代：

- 换景别或使用遮挡；
- 把连续动作拆为起点、接触和结果；
- 多人同框改为视线、声音和反打；
- 奇观改为环境反应、局部证据和结果镜头；
- 精确口型改为背影、画外音、设备播放或后期；
- 环境变形改为稳定底板和效果层；
- 服装或道具变化改用首尾帧；
- 同场续拍使用上一段稳定尾帧；
- 硬切补充新首帧，但保持动作、空间和光线连续。

不得通过删除人物选择或改变事实来“降低难度”。

## 目录与命名

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

命名：

```text
PROJECT_ASSET_OR_SCENE_SHOT_STATE_STAGE_VERSION
```

示例：

```text
PROJECT_CHAR_C01_FACE_FRONT_V03.png
PROJECT_SCENE_S02_EMPTY_WIDE_V02.png
PROJECT_PROP_P01_STATE_B_SIDE_V01.png
PROJECT_FRAME_SH07_OUT_V04.png
PROJECT_SHOT_SH07_VIDEO_V06.mp4
```

已批准版本不得覆盖；新尝试递增版本号。

## 输出要求

```yaml
production_plan:
  duration:
  shot_count:
  asset_registry:
  readiness_gate:
  core_sample:
  s_shots: []
  a_shots: []
  high_risk_shots: []
  generation_batches: []
  tool_categories: []
  budget_level:
  fallback_matrix:
  version_naming:
  postproduction_needs: []
  delivery_versions: []
```
