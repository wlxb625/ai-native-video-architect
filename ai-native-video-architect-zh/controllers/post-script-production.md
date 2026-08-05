# Post-Script Production Orchestrator V4.5

## 目标

剧本或视觉脚本成立后，在Agent内部完成外部平台制作所需的全部设计内容：

```text
NARRATIVE_LOCK
→ 剧本制作拆解
→ PROJECT_VISUAL_STRATEGY与视觉圣经
→ 镜头需求预分析
→ 规划资产与资产Prompt
→ 完整Shot表
→ 跨镜剧情与状态传递
→ CF设计
→ 图片Prompt
→ 视频Prompt
→ 内部连续性、风格和覆盖率返修
→ PROMPT_PACKAGE_READY
```

真实图片、样片和视频不是设计态完整包的前置条件。

本控制器只在用户要求进入制作时启用。只写剧本、只诊断剧本或只改写文本时，不得强制执行S04—S13。

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

用户提供AIGC教程、模板或资料时，读取与当前任务有关的原文并保留其成熟制作方法。

## S04 NARRATIVE_LOCK与剧本制作拆解

先确认当前剧本已经通过叙事门禁，并记录`NARRATIVE_LOCK`：

- 主角或主体；
- 核心关系与处境；
- 世界规则或主要机制；
- 关键选择；
- 高潮行动者与不可逆变化；
- 结尾及开放程度；
- 主题意义；
- 用户允许改动范围。

随后提取：

- 主要人物、服装和可见状态变化；
- 主要场景、空间地标和光源位置；
- 核心道具及状态变化；
- 每场和每镜的可见动作；
- 人物在每个节点知道什么、误判什么、决定什么；
- 动作准备、接触、进行、完成和完成后残留；
- 时间、天气、灯光和色调变化；
- 声音与剪辑连接；
- 必须继承的结束状态；
- 伤损、污渍、湿水、变装、体力和其他累积变化；
- 需要后期的精确文字、镜面和效果；
- 预期出现的正侧背角度、景别、全身动作、手部交互与反向机位。

制作拆解不能只列“每镜发生什么”，还要明确每个状态从哪里继承、在哪一镜改变、改变后由哪些后续镜头继续使用。

## S05 项目视觉策略与视觉圣经

读取`controllers/project-visual-strategy.md`。

视觉策略必须从当前剧本证据推导，只对当前项目生效，不能把固定的冷灰、诗性、写实、浅景深或慢镜头当成Skill默认。

用户没有明确成熟视觉方向时，内部探索2—4个真正不同的方案，再锁定一个主方向。输出至少包含：

- `scope: PROJECT_ONLY`；
- `narrative_lock_reference`；
- 剧本证据与观众体验；
- 视觉论点和Style DNA；
- 人物、空间、道具、色彩、真实光源、材质、摄影、表演和声音规则；
- 当前项目的背景职责；
- 视觉张力来源；
- 允许变化与禁止漂移；
- 对资产、Shot、CF和生成后期的影响。

视觉制作不得为追求风格改变`NARRATIVE_LOCK`。

## S06 镜头覆盖型规划资产

先根据S04的制作拆解和预期Shot需求建立覆盖矩阵，再注册`PLANNED_REFERENCE`资产ID。

资产规划不使用“默认尽量少”的原则，也不机械要求所有项目固定做全套。判断标准是：全部实际镜头中的身份、角度、结构、交互、状态和空间是否有充分视觉依据。

以下情况出现时必须增加对应资产：

- 重要面部近景：面部身份主参考；
- 正面、严格侧面、背面、转身或离场背影：标准三视图或等效结构参考；
- 全身、走动、俯身、跪姿或服装前后结构：全身服装与发型结构参考；
- 精确手部叙事动作：手部与核心道具交互参考；
- 污染、伤损、湿水、变装或累积变化：状态进程参考；
- 正反打、反向机位、关键局部空间：对应环境机位参考；
- 道具页面、开合、破损、尺寸或阶段变化：道具结构与状态参考。

每个资产必须列明必要性证据、覆盖的角度或状态、使用Shot和未建立该资产会产生的风险。

## S07 资产Prompt

一次性交付所有必要资产的完整正向Prompt、负面Prompt和输出规则。每个资产列出：

- 资产ID和职责；
- 使用Shot；
- 项目视觉策略继承；
- 身份、结构、角度、交互或状态覆盖；
- 完整可复制正向Prompt；
- 针对性负面Prompt；
- 输出规则和连续性优先级。

## S08 完整Shot表、导演设计与连续状态链

一次性完成所有Shot，不只做关键镜头。每镜一个主要任务和一个主要动作或揭示。

必须有`visual_description`，不能用主题词代替可见画面。每镜同时建立：`project_visual_strategy_reference`、`director_intent`、`camera_direction`、`lighting_direction`、`performance_direction`和`emotion_curve`。空镜使用环境节奏与观看关系替代表演字段，但不得留空。

在Shot表完成后，按叙事顺序建立连续状态链。第一镜使用`PROJECT_INITIAL_STATE`，其余每镜必须记录：

```yaml
shot_continuity:
  previous_shot_end_state:
  inherited_story_facts:
  character_knowledge_and_intention:
  action_phase_and_completion:
  pose_gaze_breath_weight_and_hands:
  prop_state_contact_and_ownership:
  costume_damage_wetness_and_accumulation:
  scene_geography_axis_and_screen_direction:
  camera_light_weather_time_and_sound_state:
  emotional_and_relationship_residue:
  new_change_in_this_shot:
  exact_end_state:
  next_shot_required_start_state:
  facts_that_must_not_reset: []
```

要求：

- 上一镜已经完成的行为不得在下一镜重新开始；
- 人物已经知道的信息、作出的决定和关系变化必须持续；
- 道具、伤损、服装、湿水、体力和环境影响持续累积；
- 换景别、换角度和正反打只能改变观看位置，不能改变故事事实；
- 有意跳切、时间省略或断裂必须写明导演理由和断裂后仍保留的事实。

## S09 Shot–CF绑定

对每个Shot选择：

- `NEW_START_FRAME`；
- `PREVIOUS_TAIL_INHERITANCE`；
- `FIRST_LAST_FRAME`；
- `EXISTING_USER_FRAME`；
- `TEXT_TO_VIDEO`；
- `POST_ONLY`。

建立Start CF、End CF和必要Bridge CF。CF必须属于当前Shot，并引用项目视觉策略和覆盖该角度、交互、状态的资产。

当下一镜依赖准确姿势、视线、手部、道具、伤损、空间或灯光尾态时，优先使用上一镜稳定尾帧、首尾帧或完整文字尾帧合同。不能每镜重新文生首帧后只靠相似配色假装连续。

## S10 图片Prompt

图片Prompt默认执行视觉密度要求：剧情关键帧必须明确主体视觉状态、主要张力来源、当前项目规定的背景职责与大形、前中后景、冻结运动痕迹、光色和材质；技术型资产板保持中性、清晰和可复用，不做无意义电影化。

- 新首帧：交付完整Prompt；
- 首尾帧：交付两条完整Prompt；
- 继承上一镜：写明CF来源和备用首帧Prompt；
- 不预制尾帧：交付文字版结束帧合同；
- POST_ONLY：写明素材和后期操作。

任何Shot不得留空。

连续镜头的首帧Prompt必须从上一镜精确尾态出发；即使摄影角度改变，也要保留人物知识、动作完成度、道具归属、累积状态和空间事实。

## S11 视频Prompt

图生视频必须先保护首帧身份、美术、构图与光线，再围绕唯一核心视觉事件编排身体部位动作、材质速度差、背景事件、镜头响应、时间高潮和结束状态。用户无需额外调用“强化模式”。

每个生成型Shot编写完整、独立、可复制的视频正向Prompt和负面Prompt。这里的“独立可复制”只表示Prompt无需用户手工拼接外部段落，不表示镜头可以脱离前后剧情重新开始。

每条视频Prompt必须：

1. 读取上一镜精确结束状态或项目初始状态；
2. 明确本镜继承的人物知识、目的、动作阶段、姿态、视线、手部、道具、空间、光线和情绪；
3. 只推进本镜应发生的一个主要剧情变化；
4. 编译人物目标、内外矛盾、可见微表情、呼吸、身体语言、情绪节拍、摄影可读性、灯光可读性和项目视觉策略；
5. 写出可见、可截图、可验证的精确结束状态；
6. 把该尾态交给下一镜，不让下一镜无原因重置。

一个短镜头只有一个主要动作、一个主要情绪转折和一种主要运镜。复杂镜面、文字、雾气和多层状态使用硬切、遮挡或分层。

现有视频Prompt的详细镜头写法可以保留。连续性是在原有构图、摄影、灯光、表演、环境和动作设计之间建立状态传递，不是把Prompt压缩成剧情摘要。

## S12 内部闭环验证

执行：

1. `NARRATIVE_LOCK`是否被保留；
2. 项目视觉策略是否只作用于当前项目；
3. 项目视觉策略是否有剧本证据；
4. 资产是否覆盖全部镜头角度、近景、交互、状态和反向空间；
5. Shot完整性；
6. CF绑定；
7. 图片来源覆盖；
8. 视频Prompt覆盖；
9. 相邻镜头是否从上一镜精确尾态进入，而不是重新初始化；
10. 人物知识、目的、决定和剧情因果是否持续推进；
11. 动作阶段、手部接触、道具归属和完成度是否连续；
12. 伤损、污渍、湿水、服装、体力和其他累积状态是否保留；
13. 人物位置、场景地理、轴线、屏幕方向和地标是否可理解；
14. 摄影—灯光—表演一致性；
15. 情绪强度、呼吸和关系残留是否从上一镜继续；
16. 时间、天气、光源、声音桥和环境状态是否有原因地变化；
17. 每镜精确尾态是否能够进入下一镜；
18. Prompt冲突；
19. 生成可行性；
20. 最终包ID一致性。

以下直接REPAIR：

- 每个镜头像独立短片一样重新介绍人物和环境；
- 已完成动作在下一镜再次从准备阶段开始；
- 人物忘记已知信息或无原因恢复旧目的；
- 道具、伤损、湿水、服装或接触状态被重置；
- 只保持相似色彩和风格，却丢失剧情因果与空间关系；
- 为追求单镜奇观破坏前后剧情；
- 结束帧合同存在，但没有进入下一镜开始状态。

最多两轮返修。

## S13 最终交付

使用`templates/full-creation-package.md`输出：

- 剧本与`NARRATIVE_LOCK`摘要；
- 项目视觉策略与视觉圣经；
- 全片导演、摄影、灯光和人物表演基准；
- 资产覆盖矩阵与资产Prompt；
- Shot总表；
- 全部逐镜头制作卡；
- 全片跨镜剧情与状态传递表；
- CF和图片Prompt；
- 全部视频Prompt；
- 参考矩阵；
- 连续性传递；
- 剪辑声音后期；
- 高风险备用；
- 外部生成顺序；
- 完整性检查摘要。

状态为`PROMPT_PACKAGE_READY`。

## 实际生成后的后续

用户提供真实媒体后，才读取`controllers/production-execution.md`执行实际验收和修复。该步骤是后续能力，不得阻塞设计态完整包。
