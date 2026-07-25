# ADAPT Mode

把已成立作品转译为可执行的AI电影生产系统。ADAPT优先改变实现方式，不改变作品核心。

## 三级变化

- A：表现替换，如正反打、画外对白、文字后期、局部动画、首尾帧或声音补充。
- B：局部场景功能、镜头和资产方案调整，需要语义、人物和连续性回归。
- C：改变人物目标、高潮、结尾、开放或形式核心，必须升级TRANSFORM。

## Production Protection Contract

```yaml
production_protection:
  must_preserve: []
  allowed_implementation_changes: []
  forbidden_changes: []
  allowed_visual_drift: []
  forbidden_visual_drift: []
  allowed_sound_changes: []
  target_delivery:
  budget_level:
```

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

## V3.2工作流

1. 建立Production Protection Contract。
2. 创建Visual Bible和Cinematic Master Spec。
3. 根据剧本建立Asset Registry，不立即批量写视频Prompt。
4. 创建核心角色的生产三视图、面部身份板、发型、服装状态和动作语言。
5. 创建主场景的空间布局、无人物空镜和必要多机位板。
6. 创建核心道具三视图、尺寸、交互关系和状态时间线。
7. 运行Asset Readiness Gate。
8. 通过后，将场景拆为有输入状态、单一动作和输出状态的镜头。
9. 为需要精确变化的镜头制作首帧和尾帧。
10. 分离图片Prompt和视频动作Prompt。
11. 选择单首帧、首尾帧、尾帧续拍、硬切、局部动画、分层合成、实拍或后期组合。
12. 按S/A/B/C评价镜头价值和风险。
13. 先做Core Sample与不同机位一致性测试。
14. 对S/A和CRITICAL/HIGH风险镜头提供Ideal/Stable/Minimum三档方案。
15. 按资产批次和镜头价值生产，不按剧情顺序盲目批量生成。
16. 粗剪后运行事实、人物、道具、空间、视觉叙事、镜头、声音、传播和结尾回归。

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
  ready_for_storyboard_frames:
```

若用户只需要概念草案，可跳过完整资产生产；若用户要求“可直接生成”，不能跳过关键资产。

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

## 逐镜头生产协议

```yaml
shot_production:
  id:
  priority: S | A | B | C
  narrative_function:
  asset_dependencies:
    character:
    costume:
    environment:
    environment_angle:
    props: []
  input_state:
  start_frame:
  primary_action:
  camera_plan:
  reveal_order:
  output_state:
  end_frame:
  sound_relation:
  generation_method:
  continuity_anchors: []
  forbidden_drift: []
  ideal_execution:
  stable_execution:
  minimum_execution:
  single_point_of_failure:
  test_clip:
  edit_connection:
```

## 图片与视频Prompt

### 图片Prompt

负责静态身份、当前状态、构图、机位、光线、材质和首尾帧。

### 视频Prompt

负责：指定首帧、起始状态、唯一主要动作、起势/过程/收住、速度与方向、摄影机起止、环境可动元素和结束状态。

视频Prompt不重复整套人物与场景说明，引用已批准资产。

## 首尾帧策略

以下镜头优先首尾帧：

- 人物、服装或道具状态变化；
- 打开、断裂、燃烧、消失或变形；
- 环境结构变化；
- 精确动作终点；
- 单首帧多次无法抵达目标。

复杂变化仍失败时，拆为前兆、发生和结果，并准备分层合成。

## 尾帧续拍与硬切

### 尾帧续拍

适合同一动作、同一运镜或同场景继续。抽取上一段稳定尾帧作为下一段唯一首帧，只继续尚未完成的动作。

### 硬切

适合换景别、换机位和节奏变化。切前切后保持：人物、服装、道具、动作进度、站位、背景地标、光源方向和色调。

不要把所有镜头强行做成一镜到底。

## 高概念大片适配

先锁定3—5个HERO_SHOT：

- HOOK_SHOT；
- RULE_SHOT；
- ESCALATION_SHOT；
- CLIMAX_SHOT；
- AFTERIMAGE_SHOT。

先验证高潮选择、规则展示和最后残像能否由资产与镜头稳定完成，再制作世界观空镜。

## 视觉叙事适配

必须保留：

- 人物重复动作；
- 关系物件；
- 母题的建立、变义和回收；
- 发现、接近、重解释和余留顺序；
- 最后画面的停留和声音关系。

关系物件必须建立道具资产和状态时间线，不能在镜头中随意变化。

## 稳定降级

1. 修复资产，而不是继续堆Prompt；
2. 减少人群，保留尺度和关系；
3. 从全景改为局部、倒影、阴影或结果；
4. 连续变形改为首尾帧、匹配剪辑或分层合成；
5. 多人同框改为视线、声音和反打；
6. 保留人物动作、选择和不可逆结果；
7. 最后才缩小世界规模。

不得降级为系统自动替人物行动、旁白解释核心规则、删除标志物或改变结尾开放程度。

## 生产管理输出

至少输出：

- 保护合同；
- Visual Bible与摄影主规格；
- Asset Registry；
- 角色、服装、场景和道具资产包；
- Asset Readiness Gate；
- Core Sample；
- 分镜首帧/尾帧需求；
- 视频动作Prompt；
- 生成批次与版本命名；
- S/A镜头和风险矩阵；
- 稳定替代、后期需求和交付版本。

## 制作底线

资产、首尾帧和三档方案可以降低规模或改变实现方式，不能改变单一核心机制、人物主任务、艰难选择双方、私人不可逆代价、标志物新含义、最后图像，以及作品完成与开放的边界。
