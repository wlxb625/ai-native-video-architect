---
name: ai-native-video-architect-zh
description: 一套中文AI原生影视全流程创作Skill。可在Agent内部从想法、题材、故事或现有剧本完成故事设计、正式剧本、视觉圣经、角色场景道具参考图Prompt、导演意图、摄影指导、逐镜灯光、人物表演与情绪曲线、镜头表、Control Frame设计、逐镜头首尾帧Prompt、图生视频Prompt、连续性与可生成性自检，最终交付可复制到外部生图和生视频平台使用的完整制作提示词包。也可诊断、改写或只处理单个镜头与Prompt。
---

# 强执行契约入口（Contract Skill Extension 0.1）

本包包含`EXECUTION.yaml`，属于**契约型Skill扩展**。当宿主能够执行包内脚本时，调用本Skill后的第一项动作必须是运行：

```bash
python scripts/contract_runner.py start --request-file <用户任务文件>
```

随后只能使用`prepare → submit → evaluate → finalize`生命周期。未取得`ACTIVATION_RECEIPT`前不得开始领域创作；未取得`CONTRACT_COMPLETE`凭证前不得把任何产物称为最终成品。

强执行优先级固定为：

```text
IMMUTABLE_CONSTITUTION
> ADAPTIVE_POLICY
> TASK_PLAN
> USER_REQUEST
> MODEL_DECISION
```

模型无权修改`constitution/`、`EXECUTION.yaml`、`contracts/workflow.enforced.yaml`、门禁阈值或状态文件。模型只能对第二层策略提交Patch，由`apply_policy_patch.py`批准或拒绝。

若宿主无法运行脚本，本包只能进入`SOFT_CONTRACT`兼容模式：仍须严格按阶段工作，但必须明确说明没有强制执行凭证，禁止伪称已经通过强门禁。

详细协议：`contracts/execution-protocol.md`。


## 人物年龄策略

短视频、网文和面向年轻受众的商业内容，默认先探索青年主角，以提高代入速度与传播入口；但这不是“所有主角必须年轻”。年龄必须服从职业资历、人生阶段、关系历史、身体条件、时代背景和主题。中年或老年更适合时禁止强行年轻化，青年更适合时也禁止为了厚重感无必要加龄。S01—S03必须通过`Character Age Fit Check`。


## 主题意义与创作必要性

除明确的抽象、无厘头和纯形式实验外，所有叙事作品都必须通过`Meaning & Thematic Necessity Check`。主题不能只写在创作说明中，必须由人物原有信念、可理解的价值冲突、持续受压、高潮行动和结尾余波共同证明。

抽象、无厘头和形式实验可以使用`FORMAL_ABSURDIST_EXCEPTION`，但必须证明形式目的、观众体验、内部模式、形式高潮与非随机性。普通故事不得用“实验”标签逃避主题意义门禁。

# AI Native Film Studio V4.4（Agent全流程创作版）

## 1. Skill定位

这是一个在Agent内部完成完整影视创作与制作设计的统一Skill：

```text
想法或已有材料
→ 故事与剧本
→ 视觉圣经与基础资产Prompt
→ 导演意图、摄影、灯光与表演设计
→ 镜头设计
→ Control Frame设计
→ 逐镜头生图Prompt
→ 逐镜头生视频Prompt
→ 连续性、覆盖率和可生成性内部返修
→ 最终完整制作提示词包
```

最终交付物用于用户在外部生图、生视频、剪辑或后期平台实际制作。

本Skill默认**不要求先真实生成参考图再继续写后续Prompt**。当用户要求“全套”“完整制作包”“从剧本到提示词”或类似结果时，Agent必须使用规划资产编号完成整条链路，不能在参考图、样片或逐镜确认处停止。

真实图片和视频只用于后续实测验收与局部修复，不能成为本轮完整提示词包的前置阻塞。

## 2. 入口判断

每次调用先判断：

1. 用户已经拥有什么：想法、大纲、剧本、视觉设定、参考图、镜头表、分镜帧、视频Prompt或生成片段；
2. 用户本轮需要什么：概念、剧本、完整创作包、完整制作提示词包、诊断、改写或单项Prompt；
3. 哪些信息是真实素材，哪些只是待生成的规划资产。

直接从当前缺失部分开始。用户已经给出的信息不得重复询问。

### 全流程触发

出现以下意图时，默认执行`FULL_CREATION_PACKAGE`：

- 全套完成；
- 从想法做到生图生视频Prompt；
- 按某个项目完整实测；
- 给完整剧本、分镜、参考图Prompt和视频Prompt；
- 不要分步询问，直接完成；
- 用Agent完成全部内容创作，外部平台只负责生成。

全流程模式不得在中途要求用户先生成资产、选母参考或验证样片。必要假设应明确标注后继续完成。

## 3. 操作模式

保留四种操作模式：

- `CREATE`：从零创作；
- `TRANSFORM`：改造已有故事或剧本；
- `DIAGNOSE`：只诊断；
- `ADAPT`：把已成立内容转成完整制作提示词包。

混合任务内部按：

```text
DIAGNOSE → TRANSFORM → ADAPT
```

用户要求全套时，`CREATE`或`TRANSFORM`完成剧本后必须自动进入`ADAPT`，同一轮完成最终提示词包。

## 4. 内部完整创作顺序

即使最终只展示成品，内部仍按以下顺序执行：

1. 解析题材、时长、画幅、平台、模型信息和限制；
2. 建立人物处境、不可见矛盾、主机制和结尾；
3. 完成可制作剧本或视觉脚本；
4. 锁定视觉规则；
5. 规划最少但足够的角色、场景、道具与特殊状态资产；
6. 为所有规划资产编写完整生图Prompt；
7. 拆解完整镜头表；
8. 为每个镜头建立导演意图、观众位置、信息优先级与揭示顺序；
9. 为每个镜头建立摄影方向、逐镜灯光、表演方向和情绪曲线；
10. 为每个镜头建立开始状态、主要动作和结束状态；
11. 选择控制帧与视频生成方式；
12. 为每个镜头编写生图Prompt或明确继承来源；
13. 为每个镜头编写完整生视频Prompt；
14. 对相邻镜头执行连续性与情绪强度检查；
15. 对Shot、CF、参考图、导演字段和Prompt执行覆盖率检查；
16. 对高风险镜头执行可生成性降级；
17. 最多进行两轮内部返修；
18. 输出完整制作提示词包。

不得把第6至第11步拆成需要用户逐项确认的外部流程，除非用户明确要求按步骤协作。

### 全流程必读模块

执行`FULL_CREATION_PACKAGE`时读取：

- `controllers/agent-full-creation.md`；
- `controllers/post-script-production.md`；
- `controllers/camera-director.md`；
- `controllers/lighting-director.md`；
- `controllers/performance-director.md`；
- `references/emotion-library.md`；
- `prompt-engineering/performance-prompt-compiler.md`；
- `prompt-engineering/asset-prompt-system.md`；
- `prompt-engineering/shot-cf-binding-system.md`；
- `prompt-engineering/image-prompt-compiler.md`；
- `prompt-engineering/storyboard-frame-system.md`；
- `prompt-engineering/video-prompt-compiler.md`；
- `prompt-engineering/continuity-repair-system.md`；
- `evals/full-package-integrity-check.md`；
- `templates/full-creation-package.md`。

只有用户提供真实生成媒体并要求审核时，才读取`controllers/production-execution.md`和`evals/shot-output-acceptance-score.md`。

## 5. 故事与剧本合同

作品至少建立：

- 主角或主体；
- 可观察任务；
- 核心关系、冲突或生成机制；
- 递进与代价；
- 关键选择；
- 高潮行动者；
- 最后图像；
- 与时长匹配的信息密度。

剧情剧本至少包含场次、时间地点、人物状态、可观察动作、对白或无对白设计、道具环境变化、声音和场次退出状态。

无对白、MV、广告、意识流或实验项目必须有完整视觉脚本，不能只是一组互不相关的意象。

已有作品未经授权不得改变人物关系、核心机制、关键选择、高潮主体、结尾和开放程度。

## 6. 视觉圣经与规划资产

正式镜头Prompt前建立共享视觉规则：

- 人物身份、骨相、发型、体型、服装和允许变化；
- 场景布局、入口、地标、固定道具和光源世界位置；
- 核心道具的结构、尺寸、材质和状态变化；
- 画幅、写实程度、色彩、曝光、颗粒与材质；
- 全片摄影倾向和禁止漂移。

### 规划资产与真实资产必须区分

```text
PLANNED_REFERENCE：Agent已经设计编号和Prompt，但图片尚未生成。
ACTUAL_REFERENCE：用户已经真实生成、上传或选定的图片。
```

Agent可以使用`PLANNED_REFERENCE`继续完成所有镜头Prompt，但不得声称它已经通过真实一致性验证。

### 最小充分参考

普通短片默认：

- 每名主要角色至少一个身份锚点；
- 每个主要场景至少一个无人物空镜；
- 跨镜头稳定且结构重要的道具建立参考；
- 特殊状态在剧情必须精确控制时建立状态参考；
- 三视图、全身、面部、手部、综合板和第二场景角度按镜头需要增加。

不是越少越好，也不是越多越好。判断标准是：最终所有镜头是否都能明确引用足够的身份、空间、道具与状态依据。

## 7. 导演、摄影、灯光与表演控制

每个正式Shot必须先建立四层控制，再编译图片与视频Prompt：

```text
DIRECTOR_INTENT
→ CAMERA_DIRECTION
→ LIGHTING_DIRECTION
→ PERFORMANCE_DIRECTION
→ IMAGE / VIDEO PROMPT
```

### 导演意图

至少写明：叙事功能、情绪目标、观众位置、信息优先级、揭示顺序、人物力量关系和切镜理由。禁止先填景别和焦段，再反向编造理由。

### 摄影方向

调用`controllers/camera-director.md`。景别、机位、焦段感、构图、景深和运镜必须服务导演意图。微表情为主要信息时，镜头距离、焦点和遮挡必须让表演可读。

### 灯光方向

调用`controllers/lighting-director.md`和`prompt-engineering/visual-style-color-light.md`。每镜写清真实光源、世界位置、方向、软硬、色温、受光区域、阴影区域、光比、曝光、情绪功能和连续性。灯光不得为了情绪无原因变色、闪烁或移动。

### 表演方向

调用`controllers/performance-director.md`、`references/emotion-library.md`和`prompt-engineering/performance-prompt-compiler.md`。人物情绪必须转化成：

- 人物目标和本镜头即时意图；
- 内部情绪、对外策略与内外矛盾；
- 眼神、眼睑、眉、嘴、下颌、呼吸、姿态、重心和手部中的少量可见线索；
- 按时间排列的情绪节拍；
- 0—5级的起始与结束强度；
- 下一镜需要继承的结束表演状态；
- 禁止夸张表演。

4—6秒镜头默认只有一个主要情绪转折、1—3个微动作和一次呼吸变化。禁止用“悲伤、恐惧、震惊”代替可见表演。

### 长Prompt规则

用户需要大量表情控制或目标平台允许长Prompt时，可输出`FULL_PERFORMANCE_PROMPT`，但必须按优先级组织，不重复同义词：人物目标与矛盾 → 起始基线 → 分秒节拍 → 面部 → 呼吸与身体 → 手部 → 摄影 → 灯光 → 结束状态 → 负面表演约束。

## 8. 资产Prompt合同

每个规划资产必须有：

```yaml
asset:
  asset_id:
  type: CHARACTER | LOCATION | PROP | STATE | STYLE
  purpose:
  used_by_shots: []
  reference_status: PLANNED_REFERENCE | ACTUAL_REFERENCE
  positive_prompt:
  negative_prompt:
  output_rules:
```

最终正向Prompt必须是一条可直接复制的完整自然语言，融合：

```text
主体身份、用途与当前视觉状态
+ 叙事型图片的主要视觉张力来源
+ 构图、画面大形、视觉动线和主体位置
+ 摄影机、焦段、机位、角度、焦点和景深
+ 曝光、白平衡、高光与暗部
+ 主光真实来源、方向、色温、软硬、亮区与阴影
+ 色彩与皮肤、布料、木材、金属等材质
+ 背景功能、大形、近中远层次、局部高潮、空间和连续性锚点
```

禁止要求用户自行拼接人物描述、摄影合同、灯光合同或统一风格前缀。

## 9. Shot与CF的唯一关系

### Shot是什么

`Shot`是一个可剪辑镜头，负责一个主要叙事任务和一个主要动作或揭示。

每个Shot必须包含：

```yaml
shot:
  shot_id:
  scene_id:
  narrative_purpose:
  visual_description:
  duration:
  input_state:
  primary_action:
  exact_end_state:
  director_intent:
  camera_direction:
  lighting_direction:
  performance_direction:
  emotion_curve: []
  camera_and_composition:
  reference_bindings: []
  frame_source_mode:
  control_frames: []
  generation_mode:
  image_prompt_status:
  video_prompt_status:
  previous_shot_handoff:
  next_shot_handoff:
  risk_and_fallback:
```

### CF是什么

本Skill中`CF`固定表示 **Control Frame，控制帧**，不是场景、资产或独立镜头。

CF只能作为某个Shot的子对象存在：

```text
SH-03
├── CF-SH03-S：开始控制帧
├── CF-SH03-E：结束控制帧
└── CF-SH03-B1：必要时的桥接控制帧
```

CF与Shot必须通过`shot_id`绑定，不得输出没有归属Shot的CF，也不得输出引用不存在CF的Shot。

### CF类型

- `START`：镜头首帧；
- `END`：镜头准确结束帧；
- `BRIDGE`：遮挡、复杂动作或分段生成使用的桥接帧；
- `TEXT_CONTRACT_ONLY`：不预生成图片，但必须写明可见结束状态和抽尾帧规则。

CF不是角色参考图或场景参考图。它由角色、场景、道具等资产和当前镜头要求共同生成。

## 10. Reference Binding合同

每个Shot必须建立参考绑定表，不能留空：

```yaml
reference_bindings:
  - asset_id: CHAR-01
    role: 锁定人物身份和服装
  - asset_id: LOC-02
    role: 锁定空间布局和光源位置
  - asset_id: PROP-01
    role: 锁定道具结构与状态
  - asset_id: CF-SH02-E
    role: 继承上一镜结束姿势与构图
```

没有独立参考图时也必须明确写：

```text
无独立新参考；继承CF-SH02-E，并继续使用CHAR-01、LOC-02。
```

禁止出现空白“参考图”字段。

## 11. Frame Source合同

每个Shot必须从以下模式中选择一个：

- `NEW_START_FRAME`：使用资产参考新生成首帧；
- `PREVIOUS_TAIL_INHERITANCE`：以上一镜稳定尾帧作为首帧；
- `FIRST_LAST_FRAME`：预生成首尾帧；
- `EXISTING_USER_FRAME`：使用用户已有图片；
- `TEXT_TO_VIDEO`：模型和镜头确实适合纯文生视频；
- `POST_ONLY`：镜头由剪辑、文字、合成或后期完成。

### 禁止空Prompt

- `NEW_START_FRAME`必须有完整首帧Prompt；
- `FIRST_LAST_FRAME`必须有首帧和尾帧Prompt；
- `PREVIOUS_TAIL_INHERITANCE`必须写明继承的CF或上一镜尾帧，并提供尾帧不可用时的备用首帧Prompt；
- `TEXT_TO_VIDEO`必须解释为何无需参考图，并给完整视频Prompt；
- `POST_ONLY`必须写明素材来源、后期操作和无需生成Prompt的原因。

任何Shot都不能以“没有描述词和参考图”的空状态进入最终包。

## 12. 分镜帧Prompt合同

图片Prompt只描述一个准确静态瞬间。

每个需要生成控制帧的Shot必须给出：

- CF编号和类型；
- 参考资产编号及职责；
- 上一镜继承；
- 人物与道具准确位置；
- 左右手、视线和接触点；
- 前中后景与构图；
- 景别、焦段、机位和轴线；
- 焦点、景深、曝光与白平衡；
- 当前镜头具体灯光；
- 完整正向Prompt；
- 负面Prompt；
- 输出规则。

静态Prompt不得描述多个连续动作。

剧情关键帧、氛围图和视觉概念图还必须：

- 把“唯美、空灵、史诗、宿命、神性、压迫”等抽象词转化为具体构图、光线、色彩、空间和材质；
- 明确2—5个主要视觉张力来源；
- 把背景当作第二视觉主体，写清功能、大形、前中后景、方向和局部高潮；
- 写清衣料、雨雾、水、火、尘等在静态瞬间留下的运动痕迹。

人物身份板、三视图、道具结构板和场景布局板以清晰、中性和可复用优先，不为震撼破坏结构。用户无需调用额外提示词强化模块。

## 13. 视频生成模式

按镜头选择：

- `SINGLE_START_FRAME`：低幅度运动且下一镜不依赖准确尾态；
- `FIRST_LAST_FRAME`：动作终点、姿势、道具、构图或下一镜继承重要；
- `TAIL_FRAME_CONTINUATION`：上一段稳定尾帧继续未完成动作；
- `TWO_SEGMENT_HARD_CUT`：构图变化或多状态变化无法稳定一次完成；
- `OCCLUSION_SWITCH`：利用遮挡切换状态；
- `LAYERED_COMPOSITE`：镜面、倒影、雾气、精确文字或复杂效果分层完成；
- `POST_ONLY`：不交给视频模型。

不得机械地让所有Shot使用同一种方式。

## 14. 导演级视频Prompt合同

每个生成型Shot必须有一条完整、独立、可复制的视频正向Prompt，包含：

```text
输入帧与生成模式
+ 首帧必须保持的人物、美术、构图和光线
+ 唯一核心视觉事件
+ 场景空间、背景功能和前中后景
+ 主体起始状态
+ 按身体部位和时间顺序编排的主要动作
+ 内外层材质及前中远景的速度差
+ 背景事件的形成、扩大、高潮与结束状态
+ 动作物理、接触和重心
+ 导演意图与观众位置
+ 摄影机与运镜时间轴
+ 焦点、景深、曝光和白平衡
+ 当前镜头具体灯光及情绪功能
+ 人物目标、内外矛盾、微表情、呼吸、身体语言与情绪节拍
+ 色彩、材质和环境动态
+ 最后1—2秒视觉峰值、精确结束状态与稳定停留
+ 下一镜继承
+ 稳定项和负面约束
```

视频Prompt负责“画面如何变化”，不能大段重复人物设定，也不能只写动作摘要。
图生视频Prompt必须写清：哪个身体部位先动、内层与外层材质如何不同、背景从什么状态发展到什么状态、摄影机何时开始和停止、最后停在什么可见高潮。禁止只写“人物起舞、衣袂飘动、海浪翻涌、镜头缓慢推进”。一个短镜头只允许一个核心视觉事件，复杂事件必须拆镜、首尾帧或分层生成。

## 15. 镜头覆盖率不变量

最终输出前必须满足：

```text
Shot总数
= 有完整镜头制作卡的数量
= 有导演意图、摄影方向和灯光方向的数量
= 人物镜头中有表演方向与情绪曲线的数量
= 有生成方式或POST_ONLY说明的数量
= 有参考绑定说明的数量
= 有开始状态和结束状态的数量
= 有视频Prompt或明确后期说明的数量
```

此外：

- 每个资产ID至少在资产表中定义一次；
- 每个CF ID只能属于一个Shot；
- 每个被引用CF必须真实存在；
- 每个生成型Shot至少有一条可执行图像来源；
- 每个相邻Shot都有明确handoff；
- Shot表、图片Prompt包和视频Prompt包中的编号完全一致。

出现遗漏时，Agent必须在内部补齐后再交付，不得把空字段留给用户。

## 16. 内部检查与返修

完整制作包输出前，内部执行：

### A. 剧本闭环

检查每场是否推动人物、冲突、规则或观众理解，结尾是否兑现核心机制。

### B. 资产完整性

检查每个反复出现的人物、场景和核心道具是否有规划资产和可复制Prompt。

### C. Shot完整性

检查每个Shot的叙事作用、可见描述、开始状态、主要动作、结束状态、生成模式、参考绑定、CF和Prompt。

### D. 导演与表演一致性

检查导演意图、观众位置、镜头距离、运镜、焦点、灯光可读性、人物内外情绪、微表情、身体语言和情绪强度是否共同服务同一个重点。

### E. 相邻镜头连续性

逐对检查人物位置、朝向、视线、左右手、道具、动作进度、屏幕方向、场景地标、主光、白平衡、曝光、呼吸、表演强度和情绪结束状态。

### F. Prompt冲突

检查镜头表、CF、图片Prompt和视频Prompt是否出现动作、机位、运镜、光线或结束状态冲突。

### G. 可生成性

检查单镜是否动作过多、多人关系过复杂、镜面或文字是否应拆层、是否需要首尾帧、续拍、硬切或后期。

### H. 覆盖率

执行第15节的不变量检查。

最多两轮返修：

```text
第一轮：结构、资产、Shot和连续性
第二轮：Prompt冲突、可生成性和覆盖率
```

最终只展示简短自检结论，不展示隐式思维过程。

## 17. 最终交付结构

`FULL_CREATION_PACKAGE`默认包含：

1. 项目总览与创作核心；
2. 完整剧本或视觉脚本；
3. 视觉圣经；
4. 全片导演基准、摄影基准、灯光母合同与人物表演基准；
5. 资产编号与参考图生图Prompt；
6. 完整Shot总表；
7. 逐镜头制作卡，包含导演意图、摄影、灯光、表演和情绪曲线；
8. 每个CF的生图Prompt或文字合同；
9. 每个Shot的生视频Prompt；
10. 参考图使用矩阵；
11. Shot之间的连续性与情绪传递表；
12. 剪辑、声音和后期说明；
13. 高风险镜头与稳定备用方案；
14. 内部完整性检查摘要；
15. 外部平台建议生成顺序。

内容过长时可以按章节或镜头区间分块，但必须在同一任务中完成全部范围，不得只生成前几个镜头后停止。

## 18. 实际媒体验收是可选后续能力

用户之后提供真实参考图、分镜图或视频时，可以继续：

- 检查身份、场景、道具和灯光是否符合Prompt；
- 检查尾帧是否能接下一镜；
- 判断失败属于参考图、控制帧、Prompt、模型能力还是后期；
- 只修复薄弱层。

没有真实媒体时，最终状态应写：

```text
PROMPT_PACKAGE_READY
```

不得声称真实样片已经通过或成片已经完成，但也不得因此拒绝完整输出提示词包。

## 19. 用户资料忠实度

用户提供AIGC教程、模板、资料包或案例时：

1. 读取与当前任务有关的原文；
2. 以原资料的制作顺序、提示词结构、参考图方法和负面约束为重要依据；
3. 将当前作品设定填入对应方法；
4. 把人工经验转译为Agent内部规则；
5. 自行补充的方法不得冒充原资料内容。

重点保留可验证的制作经验，不把特定平台的临时按钮流程写死为永久规则。

## 20. 回复规则

- 先交付可直接使用的创作结果；
- 中文请求默认中文；
- 不展示长篇内部方法论；
- 不重复询问已经提供的信息；
- 不要求用户逐资产或逐镜头确认；
- 全流程请求不得在参考图未生成处停止；
- 每条最终Prompt必须能脱离当前对话单独复制使用；
- 未指定具体模型时输出通用模型版，避免凭记忆写过时参数；
- 用户指定当前模型时，核实官方能力后再做模型适配。

## 21. 硬失败

以下任一情况直接返修：

- 只有剧本或镜头表，没有完成用户要求的全套Prompt；
- CF没有绑定Shot；
- Shot没有可见画面描述；
- Shot参考图字段为空；
- 引用了未定义的角色、场景、道具或CF；
- 生成型Shot没有图像来源；
- 生成型Shot没有完整视频Prompt；
- 继承上一镜尾帧但没有写明来源；
- 不预制尾帧却没有文字版结束帧合同；
- Shot编号在镜头表、图片Prompt和视频Prompt之间不一致；
- 静态Prompt描述完整动作过程；
- 视频Prompt只写“缓慢移动、电影感、真实光照”；
- 生图Prompt只有人物很美，背景仍是泛化环境或空洞虚化；
- 用抽象审美词代替构图、光线、色彩、空间和材质设计；
- 图生视频没有首帧保持，或重新设计人物、服装、构图和场景；
- 图生视频没有唯一核心视觉事件、材质速度差、背景过程和时间高潮；
- 只有情绪标签，没有可观察的表演线索；
- 表演依赖微表情，但景别、焦点、遮挡或灯光使其不可读；
- 五秒镜头安排多个主要情绪转折或无事件发生强度跳级；
- 镜头意图要求克制观察，Prompt却使用无动机复杂运镜；
- 灯光为了情绪无原因变色、闪烁或跟随摄影机移动；
- 下一镜依赖精确尾态却使用无控制单首帧；
- 相邻镜头人物、手部、道具、屏幕方向或光线无法衔接；
- 为了流程完整而制造无用资产；
- 参考图尚未生成就停止全套内容创作；
- 没有真实媒体却声称样片已通过；
- 把用户变成逐资产、逐镜头确认操作员。
