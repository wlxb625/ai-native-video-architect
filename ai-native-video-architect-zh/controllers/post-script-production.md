# Post-Script Production Orchestrator V4.4

## 目标

剧本或视觉脚本成立后，在Agent内部完成外部平台制作所需的全部设计内容：

```text
剧本拆解
→ 视觉规则
→ 规划资产与资产Prompt
→ 完整Shot表
→ CF设计
→ 图片Prompt
→ 视频Prompt
→ 内部连续性和覆盖率返修
→ PROMPT_PACKAGE_READY
```

真实图片、样片和视频不是设计态完整包的前置条件。

## 必读模块

- `controllers/agent-full-creation.md`；
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

## S04 剧本制作拆解

提取：

- 主要人物、服装和可见状态变化；
- 主要场景、空间地标和光源位置；
- 核心道具及状态变化；
- 每场和每镜的可见动作；
- 时间、天气、灯光和色调变化；
- 声音与剪辑连接；
- 必须继承的结束状态；
- 需要后期的精确文字、镜面和效果。

## S05 视觉圣经

锁定身份、空间、道具、色彩、光线、摄影、材质和禁止漂移。

## S06 规划资产

建立`PLANNED_REFERENCE`资产ID。每名主要角色至少身份锚点，每个主要场景至少空镜，核心道具和特殊状态按镜头需求增加。

## S07 资产Prompt

一次性交付所有必要资产的完整正向Prompt、负面Prompt和输出规则。每个资产列出使用Shot。

## S08 完整Shot表与导演设计

一次性完成所有Shot，不只做关键镜头。每镜一个主要任务和一个主要动作或揭示。

必须有`visual_description`，不能用主题词代替可见画面。每镜同时建立：`director_intent`、`camera_direction`、`lighting_direction`、`performance_direction`和`emotion_curve`。空镜使用环境节奏与观看关系替代表演字段，但不得留空。

## S09 Shot–CF绑定

对每个Shot选择：

- `NEW_START_FRAME`；
- `PREVIOUS_TAIL_INHERITANCE`；
- `FIRST_LAST_FRAME`；
- `EXISTING_USER_FRAME`；
- `TEXT_TO_VIDEO`；
- `POST_ONLY`。

建立Start CF、End CF和必要Bridge CF。CF必须属于当前Shot。

## S10 图片Prompt

图片Prompt默认执行视觉密度要求：剧情关键帧必须明确主体视觉状态、主要张力来源、背景功能与大形、前中后景、冻结运动痕迹、光色和材质；技术型资产板保持中性、清晰和可复用，不做无意义电影化。

- 新首帧：交付完整Prompt；
- 首尾帧：交付两条完整Prompt；
- 继承上一镜：写明CF来源和备用首帧Prompt；
- 不预制尾帧：交付文字版结束帧合同；
- POST_ONLY：写明素材和后期操作。

任何Shot不得留空。

## S11 视频Prompt

图生视频必须先保护首帧身份、美术、构图与光线，再围绕唯一核心视觉事件编排身体部位动作、材质速度差、背景事件、镜头响应、时间高潮和结束状态。用户无需额外调用“强化模式”。

每个生成型Shot编写完整、独立、可复制的视频正向Prompt和负面Prompt。Prompt必须编译人物目标、内外矛盾、可见微表情、呼吸、身体语言、情绪节拍、摄影可读性和灯光可读性。

一个短镜头只有一个主要动作、一个主要情绪转折和一种主要运镜。复杂镜面、文字、雾气和多层状态使用硬切、遮挡或分层。

## S12 内部闭环验证

执行：

1. 资产覆盖；
2. Shot完整性；
3. CF绑定；
4. 图片来源覆盖；
5. 视频Prompt覆盖；
6. 相邻镜头连续性；
7. 摄影—灯光—表演一致性；
8. 情绪强度与相邻镜头连续性；
9. Prompt冲突；
10. 生成可行性；
11. 最终包ID一致性。

最多两轮返修。

## S13 最终交付

使用`templates/full-creation-package.md`输出：

- 剧本；
- 视觉圣经；
- 全片导演、摄影、灯光和人物表演基准；
- 资产Prompt；
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
