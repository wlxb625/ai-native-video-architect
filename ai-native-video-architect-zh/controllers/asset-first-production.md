# Asset-First Production Controller V4.0

## 目标

在正式分镜帧和视频生成前，建立可复用、可编号、可追踪状态的角色、服装、场景和道具资产，并编译为整批可复制Prompt。

资产先行建立在已确认剧本之上。

## 必读

- `controllers/post-script-production.md`
- `prompt-engineering/image-prompt-compiler.md`
- `prompt-engineering/visual-style-color-light.md`
- `prompt-engineering/asset-prompt-system.md`
- `templates/asset-prompt-block.md`
- `core/continuity.md`

## 核心顺序

```text
剧本确认
→ 剧本拆解
→ Visual Bible
→ Asset Registry
→ 完整资产Prompt包
→ 用户外部生成与自审
→ ASSET_CONFIRMATION
→ 分镜设计
```

不得从剧本直接跳到批量视频Prompt。

## 资产ID

```text
CHAR_C01
FACE_C01
HAIR_C01
COST_C01_A
POSE_C01_P01
SCENE_S01
PLATE_S01_WIDE
ANGLE_S01_L01
PROP_P01_A
FRAME_SH03_IN
FRAME_SH03_OUT
SHOT_SH03_V01
```

镜头引用资产ID和参考图，不在每个镜头中重新设计。

## 角色生产资产

- 面部身份板；
- 正面、严格90度侧面、背面三视图；
- 发型正侧背；
- 服装层次、材质和状态；
- 手部与核心道具交互；
- 常用姿态；
- 复杂动作故事板（仅在必要时）。

艺术身份板可以探索气质，不能替代生产三视图。

## 场景生产资产

- Environment Lock；
- Master Layout；
- 无人物Empty Plate；
- 正面、左右、侧后、低机位和高机位；
- 出入口、人物路线和轴线；
- 主光、辅光、天气和色调；
- 场景状态版本。

同一场景多机位只改变摄影机，不改变布局和光源。

## 道具生产资产

记录：尺寸、人体比例、正侧背、材质、工艺、磨损、独特标记、持有与收纳、左右手、默认位置和状态链。

核心道具必须能够单独完整显示，不能被艺术排版遮挡。

## S07整批输出

S07必须一次性交付Asset Registry中全部Prompt。每项使用完整复制块并内含正向、负面和输出规则。

不得一次只输出一个资产并要求用户生成后返回。

## S08用户确认

默认用户自行生成和审核。用户明确说“下一步”“资产通过”时记录`ASSET_CONFIRMATION = PASSED`。

只有明确请求时才运行助手审核。评分器用于自检或辅助，不是强制用户逐图上传的理由。

## Asset Readiness自检

正式分镜前，Skill内部检查：

- 人物身份和三视图是否可锁定；
- 服装状态是否清楚；
- 场景布局和光源是否固定；
- 道具尺寸和状态是否定义；
- 参考图是否无遮挡、可复用；
- Prompt是否含完整正向、负面和输出规则；
- 用户是否明确确认资产阶段完成。

## Prompt分离

图片负责静态身份、位置、构图、光影、材质和状态。视频负责指定首帧后的运动。

## 失败恢复

- 换脸：返回FACE；
- 换衣：返回COST；
- 场景漂移：返回PLATE和布局；
- 道具变形：返回PROP结构和比例；
- 手部失败：局部修复或返回交互板；
- 色调跳变：返回Visual Bible的色调合同；
- 多视图不稳：改为分张生成后排版。
