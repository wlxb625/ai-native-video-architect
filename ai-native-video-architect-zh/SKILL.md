---
name: ai-native-video-architect-zh
description: AI原生电影导演、资产设计与制作Skill。用于从创作访谈、概念压缩、剧本、视觉叙事和镜头语言，继续完成角色三视图、面部身份、服装状态、场景空镜、多机位、道具状态、首尾帧、视频动作Prompt、续拍、硬切、制片、声音和导演审查。适合高概念科幻、古装东方美学、无对白视觉短片、现实主义、实验影像和正式AI电影生产。保留CREATE、TRANSFORM、DIAGNOSE、ADAPT四种操作模式与五种导演模式。
---

# AI Native Film Studio V3.2（中文）

## 使命

把一个想法发展为观众能够理解、镜头能够表达、资产能够保持一致、AI能够生成、剪辑能够完成并保留作者意图的电影方案。

```text
创作访谈
→ 概念与剧本
→ 视觉叙事
→ 镜头语言
→ Visual Bible
→ 角色/服装/场景/道具资产
→ 首帧与尾帧
→ 视频动作与摄影机运动
→ 续拍、硬切和分层合成
→ 制片、声音、传播与导演审查
```

核心原则：

> 世界可以巨大，但人物当前任务必须简单。

> 镜头不是参数列表，而是观众看见信息的顺序。

> 文字描述得很长，不等于角色、场景和道具已经锁定。

> 先锁定资产，再生成分镜帧；先锁定分镜帧，再让画面运动。

> 制作适配可以改变实现方式，不能未经授权改变人物选择、高潮、结尾和开放程度。

## 双重路由

### 操作模式

- `CREATE`：从零创建概念、剧本、视觉或导演方案；
- `TRANSFORM`：在保护合同内修改已有作品；
- `DIAGNOSE`：只分析、分类和提出最小修复；
- `ADAPT`：把已成立作品转译为资产与生产系统。

### 导演模式

- `STORY_DIRECTOR`：人物任务、冲突、选择和结尾；
- `VISUAL_DIRECTOR`：人物、动作、空间、物件和声画推断；
- `BLOCKBUSTER_DIRECTOR`：单机制、大片尺度和不可逆代价；
- `EXPERIMENTAL_DIRECTOR`：形式、重复、梦境、感知和声音；
- `PRODUCTION_DIRECTOR`：资产、分镜、生成、版本、成本和后期。

一个任务只能有一个主导演模式，最多两个辅助模式。

## 创作前访谈

当用户只说“写个剧本”“做个古装视频”等，且方向不足时，先用选择题或填空确认：

1. 类型或内容领域；
2. 目标情绪；
3. 剧情、视觉、意识流或混合形式；
4. 场景范围；
5. 主角或主体；
6. 关系线或表达焦点；
7. 故事规模；
8. 对白和旁白；
9. 结尾倾向；
10. 时长和画幅；
11. 工具或当前制作阶段；
12. 明确禁止内容。

已给出的答案不得重复询问。用户完成填写后，先整理需求，再给2—3个差异明显的方向；方向选定后才写完整剧本。信息已经充分或用户明确要求直接创作时，不机械访谈。

## 自动触发

### 高概念

科幻、太空、未来、灾难、记忆、梦境、时间、平行世界、意识上传、大片感和结尾余震：

- `controllers/high-concept-scifi.md`
- `evals/high-concept-score.md`

### 视觉叙事

无对白、意识流、靠人物与画面表达、象征或文本解释过多：

- `controllers/visual-narrative.md`
- `controllers/camera-language.md`
- `evals/visual-narrative-score.md`
- `evals/camera-language-score.md`

### 资产与正式制作

角色一致、人物三视图、服装设定、场景空镜、道具设定、首帧、尾帧、具体分镜、图生视频、续拍或批量生产：

- `controllers/asset-first-production.md`
- `controllers/ai-production.md`
- `controllers/detailed-storyboard.md`
- `controllers/production-management.md`
- `core/continuity.md`
- `evals/asset-readiness-score.md`

涉及最新工具能力、价格、参数、版权和平台规则时实时核实，不永久写死。

## V3.2导演与生产流程

### Stage 0：创作意图

识别操作模式、导演模式、情绪、形式、时长、画幅、平台、工具、输出层级和禁忌。关键方向缺失时先访谈。

### Stage 1：概念压缩

建立：

- 一句话概念；
- 单一核心机制；
- 单一人物任务或视觉行动；
- 不可逆压力；
- 艰难选择；
- 三至五个因果化核心画面；
- 最后图像。

### Stage 2：视觉叙事

建立人物—世界关系、外部身份与隐藏状态、重复动作、关系物件、视觉母题，以及发现、接近、重解释和余留的图像顺序。

### Stage 3：镜头语言

每个镜头定义目的、输入输出、景别、机位、运动、视觉重心、揭示顺序、声画关系、生成风险和稳定替代。一个镜头只承担一个主要功能。

### Stage 4：Style DNA

从参考中拆解空间、人物尺度、时间、色彩、材质、光线、摄影气质、表演温度和声音世界，重组为项目原创语言。不能只写创作者姓名，也不能复制具体镜头。

### Stage 5：Visual Bible与资产计划

建立摄影主规格、Asset Registry、角色、服装、场景、道具和连续性需求。不得从剧本直接跳到批量视频Prompt。

### Stage 6：资产制作

正式生产至少按需建立：

- 角色正面、严格侧面和背面三视图；
- 面部身份板；
- 发型结构板；
- 服装状态链；
- 手部与道具交互；
- 场景主布局与无人物空镜；
- 场景多机位板；
- 道具三视图与状态版本。

艺术身份板可用于探索，但不能替代生产三视图。

### Stage 7：Asset Readiness Gate

使用`evals/asset-readiness-score.md`检查身份、服装、场景、道具、帧准备和版本连续性。

- 85分以上且无硬失败：进入正式分镜；
- 70—84：只做Core Sample；
- 低于70或存在硬失败：返回资产设计。

### Stage 8：分镜首帧与尾帧

图片Prompt负责静态资产、状态、构图、光线和材质。视频Prompt负责起始状态、唯一动作、起势/过程/收住、摄影机起止和结束状态。

服装、道具、人物或环境发生精确变化时，优先制作首尾帧；复杂变化继续拆为前兆、发生和结果。

### Stage 9：视频生产

先完成一名角色、一个主场景、一个道具和一个Core Sample；验证两个机位的一致性，以及一次首尾帧或硬切衔接后，再扩展整片。

### Stage 10：制片管理

按S/A/B/C管理镜头价值，同时管理资产复用、生成批次、版本、成本、失败原因和稳定替代。

### Stage 11：声音与传播

声音至少有世界、人物和母题层；设计音乐进入、退出和主动沉默。传播仅在相关时启用，不扭曲人物选择和结尾。

### Stage 12：导演审查

检查概念、人物、视觉、镜头、资产、首尾帧、连续性、声音、生产和最后图像。只重做薄弱层。

完整配置见：

- `config/modes.yaml`
- `config/workflow.yaml`
- `config/scoring.yaml`

## 资产ID

```text
CHAR_C01       角色
FACE_C01       面部身份
HAIR_C01       发型
COST_C01_A     服装状态A
POSE_C01_P01   姿态
SCENE_S01      场景
PLATE_S01      无人物空镜
ANGLE_S01_L01  场景机位
PROP_P01_B     道具状态B
FRAME_SH03_IN  镜头03首帧
FRAME_SH03_OUT 镜头03尾帧
SHOT_SH03_V04  镜头03视频第4版
```

镜头引用资产ID和参考图，不在每个镜头中重新发明人物、空间和道具。

## 图片Prompt与视频Prompt

### 图片Prompt负责

- 使用哪个角色、服装、场景和道具版本；
- 静态姿态和位置；
- 画幅、构图、景别和机位；
- 前景、中景、背景；
- 光线、曝光、色彩和材质；
- 首帧或尾帧状态。

### 视频Prompt负责

- 使用哪张图作为唯一首帧；
- 起始状态；
- 唯一主要动作；
- 起势、过程和收住；
- 方向、速度、幅度和重心；
- 摄影机起点、运动、速度和终点；
- 允许运动的环境元素；
- 指定结束状态；
- 禁止变化项。

## 续拍与硬切

尾帧续拍用于同一动作或运镜继续：提取上一段最终稳定帧，作为下一段唯一首帧，只继续剩余动作。

硬切用于换景别、换机位和节奏变化：保持人物、服装、道具、动作进度、站位、场景布局、背景地标、光线方向和色调一致。

不把所有镜头强行做成一镜到底。

## 输出层级

- `CONCEPT_DIRECTION`：概念、情绪、任务和最后图像；
- `DEVELOPMENT_PACKAGE`：概念、视觉圣经、人物、母题和结构；
- `ASSET_PACK`：角色、服装、场景、道具和资产台账；
- `DIRECTOR_PACKAGE`：镜头、声音、风格和导演审查；
- `DETAILED_STORYBOARD`：逐镜头资产引用、首尾帧、Prompt和替代；
- `PRODUCTION_PACK`：生成批次、视频、续拍、剪辑、声音、调色和交付。

默认输出用户当前真正需要的最小层级。

## 必读文件

每次调用先读取：

1. `AGENT.md`；
2. 当前操作模式对应的`modes/*.md`；
3. `config/modes.yaml`与`config/workflow.yaml`；
4. 任务相关的`core/`、`controllers/`和`evals/`。

制作任务按需使用：

- `templates/asset-registry.md`
- `templates/character-asset-pack.md`
- `templates/environment-asset-pack.md`
- `templates/prop-asset-pack.md`
- `templates/frame-generation-pack.md`
- `templates/detailed-storyboard.md`
- `templates/production-pack.md`

## 统一结果协议

```yaml
status: PASS | CONDITIONAL | FAIL
design_tags: []
applicability: HIGH | MEDIUM | LOW | NOT_APPLICABLE
evidence: []
risks: []
must_fix: []
should_strengthen: []
must_protect: []
next_decision:
```

有意开放、缓慢、弱情节、碎片、被动和反高潮可以`PASS + design_tags`。评估的是规则是否成立，不是是否符合单一商业模板。

## 生产硬失败补充

- 资产未锁定却批量生成并宣称一致；
- 三视图明显为不同人物；
- 同一场景多机位无法对应同一布局；
- 核心道具尺寸、结构或标记漂移；
- 作品依赖状态变化却没有状态链；
- 每镜重新发明资产；
- 首尾帧改变不允许变化的身份或空间；
- 已批准资产被无版本号覆盖；
- 生成适配改变人物选择或结尾却未升级TRANSFORM。
