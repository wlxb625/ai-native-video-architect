# Full Creation Package Template V4.4

## 1. 项目总览

- 片名：
- 一句话故事：
- 核心机制：
- 类型与情绪：
- 时长与画幅：
- 当前任务：ADAPT / FULL_CREATION_PACKAGE
- 制作策略：

## 2. 完整剧本或视觉脚本

按场次输出。

## 3. NARRATIVE_LOCK摘要

- 主角或主体：
- 核心关系与处境：
- 世界规则或主要机制：
- 关键选择：
- 高潮行动者与不可逆变化：
- 结尾及开放程度：
- 主题意义：
- 用户授权改动范围：

制作阶段不得为了视觉风格擅自改变以上事实。

## 4. 项目视觉策略

必须标记`scope: PROJECT_ONLY`，并包含：

- 当前项目剧本证据；
- 观众体验；
- 视觉方向探索与最终选择；
- 视觉论点；
- Style DNA；
- 背景职责；
- 核心视觉张力；
- 允许变化与禁止漂移；
- 对资产、Shot、CF和生成后期的影响。

不得把当前项目的视觉值描述成Skill通用默认。

## 5. 视觉圣经

人物、场景、道具、色彩、真实光源、摄影、材质、表演、声音、连续性和禁止漂移。

## 6. 导演与表演圣经

- 全片观众关系与镜头距离策略；
- 全片摄影基准、常用景别、焦段感和运镜限制；
- 每个主要场景的灯光母合同、可读性目标和情绪功能；
- 主要人物的表演基线、动作习惯、情绪强度范围和禁止夸张方式；
- 全片情绪曲线和关键表演峰值。

## 7. 资产覆盖矩阵

先列实际镜头需求，再列对应资产，不以“最少”为目标，也不机械全做。

| 主体 | 实际镜头需求 | 景别/角度/交互/状态 | 对应资产 | 缺少依据的风险 | 覆盖结果 |
|---|---|---|---|---|---|

至少检查：

- 面部近景；
- 正侧背与全身动作；
- 服装和发型前后结构；
- 精确手部交互；
- 人物状态累积；
- 场景正反方向和关键局部；
- 环境状态变化；
- 道具结构、页面和阶段状态。

## 8. 规划资产与生图Prompt

逐项使用`asset-prompt-block.md`，注明`PLANNED_REFERENCE`或`ACTUAL_REFERENCE`，并包含：

- 项目视觉策略引用；
- 必要性证据；
- 覆盖的镜头需求；
- 使用Shot；
- 完整正向Prompt；
- 负面Prompt；
- 输出规则。

## 9. Shot总表

| Shot | 场景 | 时长 | 剧情作用 | 项目视觉策略 | 情绪目标 | 观众位置 | 可见画面 | 主要动作 | 表演强度起→止 | 摄影策略 | 灯光功能 | 帧来源 | 视频模式 |
|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|

## 10. 逐镜头导演制作卡

每个Shot完整使用`shot-production-card.md`，禁止只输出部分镜头。人物镜头必须包含表演方向和情绪时间轴；空镜必须填写环境节奏与观看关系。每镜必须引用当前项目视觉策略。

## 11. CF清单

| CF ID | 所属Shot | 类型 | 项目策略 | 来源资产 | 表演/环境状态 | 是否预生成 | Prompt/合同 |
|---|---|---|---|---|---|---|---|

## 12. 参考图使用矩阵

| Shot | 面部/结构参考 | 场景机位 | 道具/状态参考 | 上一镜尾帧 | 新增参考需求 |
|---|---|---|---|---|---|

## 13. 连续性与情绪传递表

| 上一Shot | 结束位置/动作 | 结束表演与强度 | 状态进程 | 下一Shot | 开始状态 | 衔接方式 | 必须保持 |
|---|---|---|---|---|---|---|---|

## 14. 剪辑、声音和后期

镜头顺序、转场、声音桥、环境声、呼吸、对白、音乐、留白、字幕、分层合成和调色。

## 15. 高风险与备用

逐项给风险、首选方法和稳定降级方法。表演风险优先简化微动作和运镜；资产缺口应补足实际需要的面部、角度、交互、状态或空间依据，而不是增加无关参考图。

## 16. 外部平台生成顺序

项目视觉策略确认 → 面部/三视图/全身/手部/状态资产 → 场景主空镜与必要反向机位 → 道具及状态 → 独立首帧 → 首尾帧 → 依赖尾帧镜头 → 分层素材 → 视频 → 剪辑后期。

## 17. 内部完整性检查摘要

```yaml
status: PROMPT_PACKAGE_READY | NEEDS_REPAIR
narrative_lock_preserved:
project_visual_strategy_scope:
project_visual_strategy_conformance:
asset_angle_interaction_state_coverage:
shot_count:
shot_cards:
shots_with_project_visual_strategy_reference:
shots_with_director_intent:
shots_with_camera_direction:
shots_with_lighting_direction:
character_shots_with_performance_direction:
shots_with_reference_binding:
shots_with_image_source:
shots_with_video_prompt_or_post_plan:
missing_asset_coverage: []
redundant_assets: []
orphan_cf_ids: []
undefined_asset_ids: []
continuity_conflicts: []
emotion_intensity_conflicts: []
directing_coherence_conflicts: []
prompt_conflicts: []
high_risk_shots: []
```
