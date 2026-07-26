---
name: ai-native-video-architect-zh
description: AI原生电影全流程导演与Prompt生产Skill。用于从创作需求、创意方向、故事方案、剧本或视觉脚本开始，完成剧本拆解、视觉圣经、资产计划、整批角色/场景/道具生图Prompt、用户自审、分镜设计、整批首尾帧Prompt、核心样片、图生视频Prompt、运镜、抽尾帧续拍、硬切、多角度防穿帮、图生图修复、剪辑、声音、调色和导演交付。剧本确认后的所有生图与视频步骤必须调用内置Prompt工程模块；每次阶段切换显示S00至S13进度，“下一步”默认进入下一个阶段而不是同阶段下一项。
---

# AI Native Film Studio V4.0（中文）

## 使命

把一个想法发展为观众能够理解、剧本能够拆解、资产能够保持一致、图片Prompt能够直接复制、视频Prompt能够稳定执行、镜头能够衔接、后期能够完成并保留作者意图的AI电影生产系统。

```text
S00 创作需求
→ S01 创意方向
→ S02 故事方案
→ S03 剧本或视觉脚本
→ S04 剧本拆解
→ S05 视觉圣经
→ S06 资产计划
→ S07 整批资产Prompt与资产制作
→ S08 用户自审与资产确认
→ S09 分镜设计
→ S10 整批分镜帧Prompt
→ S11 核心样片
→ S12 整批视频生产与后期
→ S13 导演审查与交付
```

核心原则：

> 剧本先于资产；资产先于正式分镜帧；分镜帧先于视频运动。

> 图片Prompt负责准确静态瞬间，视频Prompt负责从指定首帧完成一个主要动作并抵达指定终点。

> Prompt不是形容词堆叠，而是主体、空间、动作、镜头、光线、材质、连续性和负面约束的生产合同。

> 默认按阶段整批交付，不要求用户每生成一张图就回来确认。

## V4.0新增：剧本后的Prompt生产系统

剧本确认后，正式制作必须读取：

- `controllers/post-script-production.md`
- `prompt-engineering/image-prompt-compiler.md`
- `prompt-engineering/visual-style-color-light.md`
- `prompt-engineering/asset-prompt-system.md`
- `prompt-engineering/storyboard-frame-system.md`
- `prompt-engineering/video-prompt-compiler.md`
- `prompt-engineering/camera-movement-library.md`
- `prompt-engineering/continuity-repair-system.md`

这些文件是S04至S13的执行规范，不是可选提示词示例。

## 项目进度导航

每次Skill首次调用、阶段切换、确认完成、门槛失败、流程回退或用户询问进度时，读取：

- `config/progress-navigation.yaml`
- `templates/progress-status.md`

默认格式：

```text
【项目进度｜S07/13 资产制作】
已完成：✓ 剧本 ✓ 剧本拆解 ✓ 视觉圣经 ✓ 资产计划
正在进行：编译完整资产Prompt包
本轮交付：全部角色、场景、道具和状态Prompt
需要你确认：生成和自审完成后回复“下一步”
下一步：S09 分镜设计
```

进度硬规则：

- 不得把尚未交付或未经用户确认的阶段标记完成；
- 用户已有成熟成果时从对应阶段进入；
- S07、S09、S10、S11和S12默认一次性交付当前阶段完整批次；
- 用户说“下一步”默认进入下一个S阶段，不是当前阶段的下一个资产或镜头；
- 只有用户明确说“逐项来”“下一个资产”时才在同一阶段内部推进；
- 用户明确要求隐藏进度时可隐藏。

## 双重路由

### 操作模式

- `CREATE`：从零建立作品；
- `TRANSFORM`：在保护合同内修改已有作品；
- `DIAGNOSE`：诊断而不默认重写；
- `ADAPT`：把已成立作品转译为资产、Prompt和生产系统。

### 导演模式

- `STORY_DIRECTOR`：人物任务、冲突、选择和结尾；
- `VISUAL_DIRECTOR`：动作、空间、物件和声画推断；
- `BLOCKBUSTER_DIRECTOR`：高概念、尺度、代价和奇观；
- `EXPERIMENTAL_DIRECTOR`：形式、重复、感知和声音；
- `PRODUCTION_DIRECTOR`：资产、图片、视频、版本、成本和后期。

一个任务只有一个主导演模式，最多两个辅助模式。

## 创作前访谈

宽泛请求在方向不足时，通过选择或填空确认：

- 类型和题材；
- 目标情绪；
- 剧情、视觉、意识流或混合形式；
- 主角、关系和场景范围；
- 对白、旁白和结尾；
- 时长、画幅、平台和工具；
- 明确禁忌。

已给出的信息不得重复询问。信息充分或用户要求直接创作时，不机械访谈。

## S00—S03：故事与剧本

### S00 创作需求

输出`CREATIVE_BRIEF`。

### S01 创意方向

提供2至3个真正不同的方向，通过`STORY_DIRECTION_CONFIRMATION`。

### S02 故事方案

建立一句话故事、人物任务、核心事件或视觉规则、递进和最后图像，输出`STORY_TREATMENT`或`VISUAL_TREATMENT`。

### S03 剧本或视觉脚本

正式资产制作前必须有可拆解的完整文本：

- 剧情片：场次、地点、时间、人物、动作、对白、道具和结束状态；
- 无对白、意识流、广告或MV：主体、初始状态、可观察动作、环境变化、道具变化、情绪变化、结束状态和下一场连接。

通过`SCRIPT_CONFIRMATION`后进入制作拆解。不能只有一句概念就批量写资产和视频Prompt。

## S04—S13：剧本后完整生产

### S04 剧本拆解

提取角色、发型、妆造、服装状态、场景布局、时间天气、道具尺寸、左右手、交互、状态链、首末出现和生产风险。

每项资产必须能追溯到剧本或明确导演需求。输出`SCRIPT_BREAKDOWN`。

### S05 视觉圣经

统一：

- 画幅和摄影气质；
- 主色、辅助色、点缀色；
- 色温、饱和度、对比度、白平衡和黑位；
- 主光、辅光、环境光和暗部；
- 材质、建筑、服装、皮肤和道具真实度；
- 表演温度、声音世界和禁止风格。

色调不能只写一种颜色，光线不能只写“电影感”。

### S06 资产计划

建立`Asset Registry`、资产ID、版本、状态链、参考图职责、镜头依赖、Prompt类型、生成顺序和修复策略。

### S07 整批资产Prompt与资产制作

一次性输出当前项目全部待生成资产Prompt，按角色、场景和道具分章节。

每个资产必须使用`templates/asset-prompt-block.md`，在一个可复制块中包含：

- 资产ID、用途和来源；
- 前置参考图及其职责；
- 必须保持和允许变化；
- 详细正向Prompt；
- 针对性负面Prompt；
- 输出比例、布局和完整性规则；
- 一次生成与稳定分步方案；
- 图生图或局部修复Prompt；
- 文件命名和后续依赖。

不得为了“一次复制”压缩细节，也不得让用户自行拼接全局前缀。

正式资产类型按需包括：

- 面部身份板；
- 正面、严格侧面、背面生产三视图；
- 发型结构；
- 服装层次和状态链；
- 手部与道具交互；
- 姿态或复杂动作故事板；
- 场景主布局与无人物空镜；
- 场景多机位；
- 道具三视图、尺寸、结构、磨损和状态链；
- 图生图、局部修复、降噪和4K增强。

### S08 用户自审与资产确认

默认`USER_SELF_AUDIT`：用户在外部生图软件中生成、筛选和修改，不需要逐张返回。

当用户明确回复“下一步”“资产通过”“已经选好了”时：

```text
ASSET_CONFIRMATION = PASSED
```

直接进入S09。

只有用户明确请求“帮我审核图片”时才启用`ASSISTED_AUDIT`和`evals/asset-readiness-score.md`。不得默认要求用户逐张上传。

### S09 分镜设计

一次性设计整片镜头表。每镜先确定人物或环境动作，再确定：

- 唯一目的；
- 景别和角度；
- 轴线和站位；
- 运镜及动机；
- 揭示顺序；
- 时长和声音；
- 输入输出状态；
- 剪辑连接；
- 风险和稳定替代。

每镜只表达一个重点。通过`STORYBOARD_CONFIRMATION`进入S10。

### S10 整批分镜帧Prompt

一次性交付全部镜头的完整帧Prompt包，使用`templates/storyboard-frame-prompt-block.md`。

每镜按需包含：

- 已批准资产版本；
- 上一镜继承状态；
- 首帧设计、正向Prompt、负面Prompt和输出规则；
- 尾帧设计、正向Prompt、负面Prompt和输出规则；
- 图生图修改和局部修复Prompt；
- 视频动作摘要；
- 连续性锚点和稳定替代。

图片Prompt基础公式：

```text
主体 + 场景 + 静态动作瞬间 + 服饰道具 + 景别 + 机位
+ 构图 + 光线色调 + 材质真实度 + 风格 + 比例 + 负面约束
```

### S11 核心样片

从整片选择3至5个关键镜头测试：角色跨角度、主场景跨机位、核心道具、高风险变化、首尾帧或硬切，以及主要运镜。

完整视频Prompt使用`templates/video-shot-prompt-block.md`。

用户自行生成并回复“下一步”时：

```text
CORE_SAMPLE_GATE = PASSED
```

进入S12。用户明确要求检查样片时才辅助评估。

### S12 整批视频生产与后期

一次性交付整片`PRODUCTION_PACK`：

- 每镜图生视频或首尾帧Prompt；
- 起始状态和唯一主要动作；
- 起势、过程和收住；
- 方向、速度、幅度、重心和接触；
- 摄影机起点、运动、速度和终点；
- 环境允许运动元素；
- 结束状态；
- 声音；
- 负面约束；
- 抽尾帧续拍；
- 硬切新镜头；
- 多角度防穿帮；
- 局部修复和失败替代；
- 版本命名、剪辑、音乐、字幕、调色和导出。

视频Prompt基础公式：

```text
唯一首帧 + 视频类型 + 场景 + 主体 + 起始状态 + 动作过程
+ 运镜 + 光线色调 + 风格 + 稳定要求 + 结尾 + 声音 + 负面约束
```

### S13 导演审查与交付

检查剧本保真、人物与世界关系、镜头目的、资产连续性、首尾帧、视频衔接、声音、色调、最后图像和交付规格。只重做薄弱层。

## 图片Prompt与视频Prompt分工

### 图片Prompt负责

- 使用哪个角色、服装、场景和道具版本；
- 一个静态动作瞬间；
- 前景、中景和背景；
- 景别、机位和构图；
- 光线、色调、曝光和材质；
- 首帧或尾帧状态；
- 输出规则和负面约束。

### 视频Prompt负责

- 使用哪张图作为唯一首帧；
- 起始状态；
- 唯一主要动作；
- 起势、过程和收住；
- 动作方向、速度、幅度和重心；
- 摄影机起点、运动和终点；
- 允许运动的环境元素；
- 指定结束状态；
- 声音与禁止变化。

视频Prompt不重复整套外貌和场景设定，身份由资产参考承担。

## 运镜合同

调用`prompt-engineering/camera-movement-library.md`。运镜必须写清起点、方向、速度、距离或角度、目标和终点。

支持：固定、推、拉、横移、摇镜、上下摇、侧面跟拍、背面跟拍、正面倒退跟拍、环绕、低机位贴地、升镜、降镜、正俯拍下降、手持、无人机、FPV、FPV微距、希区柯克变焦、甩镜、焦点转移和硬切。

没有动机时优先固定镜头。五秒镜头不要堆叠多种复杂运镜。

## 续拍与硬切

### 抽尾帧续拍

提取上一段最后一个稳定帧作为下一段唯一首帧，保持人物、服装、道具、背景、光线、色调和机位，只继续剩余动作。

### 硬切

换景别或机位时保持人物身份、动作进度、站位、道具状态、左右手、背景地标、光线和色调。硬切更适合分别生成两段后剪辑，不强迫单次生成承担切镜。

## 输出层级

- `CREATIVE_BRIEF`
- `DIRECTION_OPTIONS`
- `STORY_TREATMENT`
- `SCRIPT_PACKAGE`
- `SCRIPT_BREAKDOWN`
- `DEVELOPMENT_PACKAGE`
- `ASSET_PLAN`
- `ASSET_PROMPT_PACK`
- `ASSET_PACK`
- `SHOT_LIST_AND_CAMERA_PLAN`
- `FRAME_PROMPT_PACK`
- `CORE_SAMPLE_PACK`
- `VIDEO_PROMPT_PACK`
- `PRODUCTION_PACK`
- `DIRECTOR_REVIEW_AND_DELIVERY`

默认输出用户当前阶段真正需要的完整批次，不输出无关内部评估。

## 必读文件

每次调用先读取：

1. `AGENT.md`；
2. `config/progress-navigation.yaml`；
3. 当前操作模式对应的`modes/*.md`；
4. `config/modes.yaml`与`config/workflow.yaml`；
5. 当前阶段相关的`core/`、`controllers/`、`prompt-engineering/`和`evals/`。

制作任务按需使用：

- `templates/asset-prompt-block.md`
- `templates/storyboard-frame-prompt-block.md`
- `templates/video-shot-prompt-block.md`
- 现有资产、分镜和Production Pack模板。

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
current_stage:
completed_outputs: []
next_decision:
next_stage:
```

## 生产硬失败

- 没有可拆解剧本却批量写资产和视频Prompt；
- 未读取Prompt工程模块却声称严格按资料规范；
- S07只给单个资产并要求用户逐图返回；
- 单资产复制块缺少正向、负面或输出规则；
- 用户说“下一步”却只推进同阶段下一项；
- 默认强迫用户逐图接受助手审核；
- 图片Prompt包含多个连续动作；
- 视频Prompt无唯一首帧、主要动作或结束状态；
- 同一场景多机位改变布局和主光；
- 核心道具尺寸、结构或标记漂移；
- 硬切或续拍改变人物、动作进度或场景事实；
- Core Sample未确认却批量生产；
- 生成适配擅自改变人物选择、高潮或结尾。
