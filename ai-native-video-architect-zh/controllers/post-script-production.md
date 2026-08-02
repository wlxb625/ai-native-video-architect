# Post-Script Production Orchestrator V4.4

## 目标

剧本或视觉脚本成立后，在Agent内部完成外部平台制作所需的全部设计内容：

```text
NARRATIVE_LOCK
→ 剧本制作拆解
→ PROJECT_VISUAL_STRATEGY与视觉圣经
→ 镜头需求预分析
→ 规划资产与资产Prompt
→ 完整Shot表
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
- 时间、天气、灯光和色调变化；
- 声音与剪辑连接；
- 必须继承的结束状态；
- 需要后期的精确文字、镜面和效果；
- 预期出现的正侧背角度、景别、全身动作、手部交互与反向机位。

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

## S08 完整Shot表与导演设计

一次性完成所有Shot，不只做关键镜头。每镜一个主要任务和一个主要动作或揭示。

必须有`visual_description`，不能用主题词代替可见画面。每镜同时建立：`project_visual_strategy_reference`、`director_intent`、`camera_direction`、`lighting_direction`、`performance_direction`和`emotion_curve`。空镜使用环境节奏与观看关系替代表演字段，但不得留空。

## S09 Shot–CF绑定

对每个Shot选择：

- `NEW_START_FRAME`；
- `PREVIOUS_TAIL_INHERITANCE`；
- `FIRST_LAST_FRAME`；
- `EXISTING_USER_FRAME`；
- `TEXT_TO_VIDEO`；
- `POST_ONLY`。

建立Start CF、End CF和必要Bridge CF。CF必须属于当前Shot，并引用项目视觉策略和覆盖该角度、交互、状态的资产。

## S10 图片Prompt

图片Prompt默认执行视觉密度要求：剧情关键帧必须明确主体视觉状态、主要张力来源、当前项目规定的背景职责与大形、前中后景、冻结运动痕迹、光色和材质；技术型资产板保持中性、清晰和可复用，不做无意义电影化。

- 新首帧：交付完整Prompt；
- 首尾帧：交付两条完整Prompt；
- 继承上一镜：写明CF来源和备用首帧Prompt；
- 不预制尾帧：交付文字版结束帧合同；
- POST_ONLY：写明素材和后期操作。

任何Shot不得留空。

## S11 视频Prompt

图生视频必须先保护首帧身份、美术、构图与光线，再围绕唯一核心视觉事件编排身体部位动作、材质速度差、背景事件、镜头响应、时间高潮和结束状态。用户无需额外调用“强化模式”。

每个生成型Shot编写完整、独立、可复制的视频正向Prompt和负面Prompt。Prompt必须编译人物目标、内外矛盾、可见微表情、呼吸、身体语言、情绪节拍、摄影可读性、灯光可读性和项目视觉策略。

一个短镜头只有一个主要动作、一个主要情绪转折和一种主要运镜。复杂镜面、文字、雾气和多层状态使用硬切、遮挡或分层。

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
9. 相邻镜头连续性；
10. 摄影—灯光—表演一致性；
11. 情绪强度与相邻镜头连续性；
12. Prompt冲突；
13. 生成可行性；
14. 最终包ID一致性。

最多两轮返修。

## S13 最终交付

使用`templates/full-creation-package.md`输出：

- 剧本与`NARRATIVE_LOCK`摘要；
- 项目视觉策略与视觉圣经；
- 全片导演、摄影、灯光和人物表演基准；
- 资产覆盖矩阵与资产Prompt；
- Shot总表；
- 全部逐镜头制作卡；
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
