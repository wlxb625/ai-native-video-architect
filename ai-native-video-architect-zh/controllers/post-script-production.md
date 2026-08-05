# Post-Script Production Orchestrator V4.5

## 目标

剧本或视觉脚本成立后，在Agent内部完成外部平台制作所需的全部设计内容：

```text
NARRATIVE_LOCK
→ 剧本制作拆解
→ PROJECT_VISUAL_STRATEGY与视觉圣经
→ 镜头需求与资产规划
→ 完整Shot表
→ CONTINUITY_LEDGER
→ CF设计
→ 图片Prompt
→ 视频Prompt
→ 内部闭环返修
→ PROMPT_PACKAGE_READY
```

真实图片、样片和视频不是设计态完整包的前置条件。

本控制器只在用户要求进入制作时启用。只写剧本、诊断剧本或修改文本时，不得强制执行S04—S13。

## 必读模块

- `controllers/agent-full-creation.md`；
- `controllers/project-visual-strategy.md`；
- `controllers/camera-director.md`；
- `controllers/lighting-director.md`；
- `controllers/performance-director.md`；
- `references/emotion-library.md`；
- `prompt-engineering/performance-prompt-compiler.md`；
- `prompt-engineering/visual-style-color-light.md`；
- `prompt-engineering/asset-prompt-system.md`；
- `prompt-engineering/shot-cf-binding-system.md`；
- `prompt-engineering/image-prompt-compiler.md`；
- `prompt-engineering/storyboard-frame-system.md`；
- `prompt-engineering/video-prompt-compiler.md`；
- `prompt-engineering/camera-movement-library.md`；
- `prompt-engineering/continuity-repair-system.md`；
- `evals/prompt-production-readiness-score.md`；
- `evals/full-package-integrity-check.md`；
- `templates/full-creation-package.md`。

时空视觉编排只在项目或镜头满足启用条件时读取，不作为所有Shot的固定必填模块。

## S04 NARRATIVE_LOCK与制作拆解

先确认剧本通过叙事门禁，并记录：

- 主角或主体；
- 核心关系与处境；
- 世界规则或主要机制；
- 关键选择；
- 高潮行动者与不可逆变化；
- 结尾及开放程度；
- 主题意义；
- 用户允许改动范围。

随后提取：

- 人物、服装和可见状态变化；
- 场景、空间地标和光源位置；
- 核心道具及状态变化；
- 每场和每镜的可见动作；
- 人物在各节点知道、误判和决定什么；
- 动作准备、接触、进行、完成和残留；
- 时间、天气、灯光、色调和声音变化；
- 必须继承的结束状态；
- 伤损、污渍、湿水、变装、体力和其他累积变化；
- 后期精确文字、镜面和效果；
- 实际Shot需要的角度、景别、全身动作、手部交互与反向机位。

不能只列“每镜发生什么”，还要明确状态在哪里改变、之后由哪些镜头继续继承。

## S05 项目视觉策略与视觉圣经

读取`controllers/project-visual-strategy.md`。

视觉策略必须从当前剧本证据推导，只对当前项目生效。用户没有成熟视觉方向时，内部探索2—4个真正不同的方案，再锁定一个主方向。

至少包含：

- `scope: PROJECT_ONLY`；
- `narrative_lock_reference`；
- 剧本证据与观众体验；
- 视觉论点和Style DNA；
- 人物、空间、道具、色彩、真实光源、材质、摄影、表演和声音规则；
- 背景职责和视觉张力；
- 允许变化与禁止漂移；
- 对资产、Shot、CF和生成后期的影响。

视觉制作不得为追求风格改变`NARRATIVE_LOCK`。

## S06 镜头覆盖型资产规划

根据S04拆解和实际Shot需求建立覆盖矩阵，再注册`PLANNED_REFERENCE`资产ID。

判断标准不是默认最少，也不是机械做全套，而是实际镜头中的身份、角度、结构、交互、状态和空间是否有充分视觉依据。

重要面部近景、严格侧背面、全身动作、精确手部交互、伤损湿水状态、反向空间和道具阶段变化，必须有对应资产或等效依据。

每项资产写明必要性、覆盖范围、使用Shot和缺失风险。

## S07 资产Prompt

一次性交付全部必要资产的：

- 资产ID和职责；
- 使用Shot；
- 项目视觉策略继承；
- 身份、结构、角度、交互或状态覆盖；
- 完整正向Prompt；
- 针对性负面Prompt；
- 输出规则与连续性优先级。

## S08 完整Shot表、导演设计与连续性台账

一次性完成所有Shot，不只做关键镜头。每镜只有一个主要任务和一个主要动作或揭示。

每镜必须有：

- `visual_description`；
- `project_visual_strategy_reference`；
- `scene_function`；
- `director_intent`；
- `camera_direction`；
- `lighting_direction`；
- `performance_direction`或`NON_CHARACTER_PERFORMANCE`；
- `emotion_curve`或环境节奏；
- 动作阶段和精确结束状态。

随后使用`prompt-engineering/continuity-repair-system.md`建立全片唯一`CONTINUITY_LEDGER`：

- 第一镜引用`PROJECT_INITIAL_STATE`；
- 其余镜头引用上一镜唯一`End State ID`；
- 每镜只记录本镜新变化，并把精确尾态写回台账；
- Shot卡、CF、图片Prompt、视频Prompt和评估只引用该台账，不复制多套状态表。

连续性必须覆盖人物知识、目的、动作完成度、姿态视线手部、道具归属、伤损湿水等累积状态、空间轴线、光线天气时间声音以及情绪和关系残留。

## S09 Shot–CF绑定

每个Shot选择：

- `NEW_START_FRAME`；
- `PREVIOUS_TAIL_INHERITANCE`；
- `FIRST_LAST_FRAME`；
- `EXISTING_USER_FRAME`；
- `TEXT_TO_VIDEO`；
- `POST_ONLY`。

建立Start CF、End CF和必要Bridge CF。CF属于当前Shot，并引用项目视觉策略、资产和对应`CONTINUITY_LEDGER`条目。

下一镜依赖准确姿势、视线、手部、道具、伤损、空间或灯光尾态时，优先使用上一镜稳定尾帧、首尾帧或完整文字尾帧合同。不能每镜重新文生首帧，再只靠相似配色假装连续。

## S10 图片Prompt

剧情关键帧必须明确主体状态、主要张力、背景职责与大形、前中后景、冻结运动痕迹、光色和材质。技术资产板保持中性、清晰和可复用。

- 新首帧：完整Prompt；
- 首尾帧：两条完整Prompt；
- 继承上一镜：CF来源和备用首帧Prompt；
- 不预制尾帧：完整文字结束帧合同；
- `POST_ONLY`：素材与后期操作。

连续镜头的首帧从台账起态建立。改变摄影角度时仍保留人物知识、动作完成度、道具归属、累积状态和空间事实。

## S11 视频Prompt

先保护首帧身份、美术、构图与光线，再围绕唯一核心视觉事件编排身体动作、材质速度差、背景事件、摄影机响应、时间高潮和结束状态。

每个生成型Shot交付独立可复制的正向Prompt和负面Prompt。“独立可复制”只表示无需用户拼接外部段落，不表示镜头可以脱离剧情重新开场。

每条视频Prompt必须：

1. 引用当前Shot的连续性台账起态；
2. 继承人物知识、目的、动作阶段、姿态、视线、手部、道具、空间、光线和情绪；
3. 只推进本镜唯一剧情变化；
4. 保留完整摄影、灯光、表演、环境和动作设计；
5. 抵达可见、可截图、可验证的精确尾态；
6. 将尾态登记为下一镜可引用的`End State ID`。

一个短镜头只有一个主要动作、一个主要情绪转折和一种主要运镜。复杂镜面、文字、雾气、多对象和多层状态优先硬切、遮挡或分层生成。

现有视频Prompt的详细写法可以保留。连续性是在完整镜头设计之间建立状态传递，不是把Prompt压缩成剧情摘要。

## S12 内部闭环验证

执行：

1. `NARRATIVE_LOCK`是否保留；
2. 项目视觉策略是否有剧本证据且只作用于当前项目；
3. 资产是否覆盖实际镜头需求；
4. Shot、CF、图片来源和视频Prompt是否完整；
5. 所有连续镜头是否引用唯一台账条目；
6. 上一镜`End State ID`是否成为下一镜起态；
7. 人物知识、目的、动作、道具、累积状态、空间、光线和情绪是否无重置；
8. 摄影—灯光—表演是否一致；
9. 时空编排启用时是否只统筹关系，没有重复专业模块；
10. Prompt是否存在冲突或超出模型可执行范围；
11. 最终包ID是否一致。

以下直接`REPAIR`：

- 每个镜头像独立短片一样重新介绍人物和环境；
- 已完成动作再次从准备阶段开始；
- 人物忘记信息或恢复旧目的；
- 道具、伤损、湿水、服装或接触状态被重置；
- 只保持相似风格却丢失剧情因果与空间；
- 为单镜奇观破坏前后剧情；
- 结束帧合同没有进入下一镜起态；
- 多个模块记录了互相冲突的连续状态。

最多两轮内部返修。

## S13 最终交付

使用`templates/full-creation-package.md`输出：

- 剧本与`NARRATIVE_LOCK`摘要；
- 项目视觉策略与视觉圣经；
- 全片导演、摄影、灯光和表演基准；
- 资产覆盖矩阵与资产Prompt；
- Shot总表和全部逐镜制作卡；
- 唯一`CONTINUITY_LEDGER`；
- CF与图片Prompt；
- 全部视频Prompt；
- 参考矩阵；
- 剪辑、声音与后期；
- 高风险备用和外部生成顺序；
- 完整性检查摘要。

状态为`PROMPT_PACKAGE_READY`。

## 实际生成后的后续

用户提供真实媒体后，才读取`controllers/production-execution.md`进行实际验收和修复。该步骤不得阻塞设计态完整包。