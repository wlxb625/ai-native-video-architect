# ADAPT Mode

把已成立作品转译为可执行的AI电影生产系统。ADAPT优先改变实现方式，不改变作品核心。

## 启动进度

首次进入ADAPT时读取：

- `config/progress-navigation.yaml`
- `templates/progress-status.md`

先判断用户带来的成果属于哪一阶段：

```text
只有故事梗概 → S03 剧本或视觉脚本
已有完整剧本 → S04 剧本拆解
已有拆解与视觉圣经 → S06 资产计划
已有角色/场景/道具图 → S08 资产审核
已有镜头表但无稳定资产 → S06，保留镜头意图
已有资产和分镜帧 → S11 Core Sample
```

进度提示必须说明进入依据、跳过阶段、本轮交付、需要确认和下一步。用户自带材料不等于已通过对应门槛。

## 三级变化

- A：表现替换，如正反打、画外对白、文字后期、局部动画、首尾帧或声音补充；
- B：局部场景功能、镜头和资产方案调整，需要语义、人物和连续性回归；
- C：改变人物目标、高潮、结尾、开放或形式核心，必须升级TRANSFORM并返回S03重新确认剧本。

## Production Protection Contract

```yaml
production_protection:
  source_stage:
  return_stage:
  must_preserve: []
  allowed_implementation_changes: []
  forbidden_changes: []
  allowed_visual_drift: []
  forbidden_visual_drift: []
  allowed_sound_changes: []
  target_delivery:
  budget_level:
```

## 剧本门槛

ADAPT进入资产和分镜前必须存在：

- 已确认的传统剧本；或
- 已确认的完整视觉脚本。

若用户只有故事梗概、分散镜头想法或氛围图，当前阶段定位为S03，不得直接批量生成角色、场景、道具或分镜Prompt。

若用户提供剧本但未做拆解，从S04开始提取：

- 角色与状态；
- 发型妆造与服装状态；
- 场景、布局、时间、天气和变化；
- 道具、尺寸、持有者、左右手、交互和状态链；
- 首次/最后出现和依赖镜头。

## 强制路由

用户要求角色一致、场景一致、道具设定、三视图、首帧、尾帧、具体分镜、图生视频或正式生产包时，读取：

- `controllers/asset-first-production.md`
- `controllers/ai-production.md`
- `controllers/detailed-storyboard.md`
- `controllers/production-management.md`
- `core/continuity.md`
- `templates/asset-registry.md`
- `templates/character-asset-pack.md`
- `templates/environment-asset-pack.md`
- `templates/prop-asset-pack.md`
- `templates/frame-generation-pack.md`

## V3.3 ADAPT工作流

1. 显示当前进度和进入依据；
2. 建立Production Protection Contract；
3. 检查并补足S03剧本/视觉脚本；
4. S04完成Script Breakdown；
5. S05创建Visual Bible和Cinematic Master Spec；
6. S06根据拆解建立Asset Registry和版本计划；
7. S07创建角色、服装、场景空镜、多机位、道具和交互资产；
8. S08运行Asset Readiness Gate并完成资产确认；
9. S09将剧本拆成有输入状态、单一动作和输出状态的镜头，并完成分镜确认；
10. S10制作首帧、尾帧、图片Prompt和视频动作Prompt；
11. S11完成Core Sample、不同机位、首尾帧或硬切测试；
12. S12按资产批次和镜头价值生产，完成剪辑、声音、音乐和调色；
13. S13运行导演审查与交付检查。

## Asset Readiness Gate

进入正式分镜帧前至少检查：

```yaml
asset_readiness:
  visual_bible:
  character_identity:
  costume_states:
  environment_layout:
  empty_plates:
  props_and_states:
  continuity_registry:
  score:
  hard_failures: []
  ready_for_storyboard_frames:
```

- 85以上且无硬失败：进入S09；
- 70—84：仅允许进入S11制作Core Sample；
- 低于70或存在硬失败：返回S06/S07修复。

用户只需要概念草案时可停在S02—S05；用户要求“可直接生成”时不能跳过关键资产和门槛。

## 资产与分镜的边界

### 资产负责

- 角色长什么样；
- 服装如何分层和变化；
- 场景结构、光源和地标；
- 道具尺寸、结构和状态；
- 不同镜头引用哪个版本。

### 分镜负责

- 当前镜头为什么存在；
- 观众先看到什么；
- 人物和摄影机如何运动；
- 镜头如何结束；
- 下一镜继承什么。

不得在每个镜头中重新发明资产。

## S09分镜确认

先输出镜头表：

```yaml
shot_design:
  id:
  narrative_function:
  asset_dependencies:
  input_state:
  shot_size:
  angle_and_axis:
  primary_action:
  camera_plan:
  reveal_order:
  duration:
  output_state:
  sound_relation:
  edit_connection:
  risk:
  stable_alternative:
```

用户确认镜头数量、动作、构图、运镜和难度后，通过`STORYBOARD_CONFIRMATION`，再进入S10批量写帧Prompt。

## 图片与视频Prompt

### 图片Prompt

负责静态身份、当前状态、构图、机位、光线、材质和首尾帧。

### 视频Prompt

负责：指定首帧、起始状态、唯一主要动作、起势/过程/收住、速度与方向、摄影机起止、环境可动元素和结束状态。

视频Prompt不重复整套人物与场景说明，引用已批准资产。

## 首尾帧、续拍与硬切

以下镜头优先首尾帧：

- 人物、服装或道具状态变化；
- 打开、断裂、燃烧、消失或变形；
- 环境结构变化；
- 精确动作终点；
- 单首帧多次无法抵达目标。

尾帧续拍适合同一动作或运镜继续，只继续尚未完成的动作。

硬切适合换景别和机位，切前切后保持人物、服装、道具、动作进度、站位、背景地标、光源方向和色调。

不把所有镜头强行做成一镜到底。

## S11 Core Sample Gate

正式批量生产前至少验证：

- 一名核心角色跨两个角度一致；
- 一个主场景跨两个机位一致；
- 一个核心道具尺寸和状态稳定；
- 一次首尾帧或硬切连续；
- 一个3—8秒Core Sample。

未通过时，进度提示必须说明保留什么、修哪一层和返回哪一门槛。不得继续批量生产。

## 稳定降级

1. 修复剧本拆解或资产，不继续堆Prompt；
2. 减少人群，保留尺度和关系；
3. 从全景改为局部、倒影、阴影或结果；
4. 连续变形改为首尾帧、匹配剪辑或分层合成；
5. 多人同框改为视线、声音和反打；
6. 保留人物动作、选择和不可逆结果；
7. 最后才缩小世界规模。

不得降级为系统自动替人物行动、旁白解释核心规则、删除标志物或改变结尾开放程度。

## 生产管理输出

至少输出：

- 当前进度、进入依据与下一步；
- 保护合同；
- Script Breakdown；
- Visual Bible与摄影主规格；
- Asset Registry；
- 角色、服装、场景和道具资产包；
- Asset Readiness Report；
- 分镜设计与确认状态；
- 首帧/尾帧和视频动作Prompt；
- Core Sample结果；
- 生成批次与版本命名；
- S/A镜头和风险矩阵；
- 稳定替代、后期需求和交付版本。

## 制作底线

剧本、资产、首尾帧和实现方案可以降低规模或改变实现方式，不能未经授权改变单一核心机制、人物主任务、艰难选择双方、私人不可逆代价、标志物新含义、最后图像，以及作品完成与开放的边界。
