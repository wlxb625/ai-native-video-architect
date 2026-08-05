# Full Creation Package Template V4.5

## 1. 项目总览

- 片名：
- 一句话故事：
- 核心机制：
- 类型与情绪：
- 时长与画幅：
- 当前任务：ADAPT / FULL_CREATION_PACKAGE
- 制作策略：

## 2. 完整剧本或视觉脚本

按场次输出，包含时间地点、人物状态、可见动作、对白或无对白设计、道具与环境变化、声音和场次退出状态。

## 3. NARRATIVE_LOCK

- 主角或主体：
- 核心关系与处境：
- 世界规则或主要机制：
- 关键选择：
- 高潮行动者与不可逆变化：
- 结尾及开放程度：
- 主题意义：
- 用户授权改动范围：

制作阶段不得为了视觉风格、生成便利或单镜奇观改变以上事实。

## 4. 项目视觉策略

必须标记`scope: PROJECT_ONLY`，并包含：

- 当前项目剧本证据；
- 观众体验；
- 视觉方向探索与最终选择；
- 视觉论点与Style DNA；
- 背景职责与视觉张力；
- 原创视觉语法；
- 视觉密度与清洁度原则；
- 材质语义与常见漂移风险；
- 画幅对人物占比、负空间和动势的影响；
- 连续性锚点；
- 允许变化与禁止漂移；
- 对资产、Shot、CF和生成后期的影响。

不得把当前项目的视觉值描述成Skill通用默认。

## 5. 视觉圣经

人物、场景、道具、色彩、真实光源、摄影、材质、表演、声音、背景职责、视觉密度、画幅适配、连续性锚点和禁止漂移。

## 6. 导演与表演圣经

- 全片观众关系与镜头距离策略；
- 摄影基准、景别、焦段感和运镜限制；
- 主要场景灯光母合同、可读性和情绪功能；
- 人物表演基线、动作习惯、情绪强度范围和禁止夸张方式；
- 全片情绪曲线与关键表演峰值；
- 动作阶段、接触、重量和人物关系残留原则；
- 时空视觉编排的项目级使用范围；
- 目标平台观看距离和缩略图可读性原则。

## 7. 资产覆盖矩阵

先列实际镜头需求，再列资产，不以“最少”为目标，也不机械全做。

| 主体 | 实际镜头需求 | 景别/角度/交互/状态 | 对应资产 | 缺少依据的风险 | 覆盖结果 |
|---|---|---|---|---|---|

至少检查面部近景、正侧背、全身动作、服装和发型结构、精确手部交互、状态累积、场景正反方向、环境状态以及道具结构与阶段。

## 8. 规划资产与生图Prompt

逐项使用`asset-prompt-block.md`，注明`PLANNED_REFERENCE`或`ACTUAL_REFERENCE`，并包含：

- 项目视觉策略引用；
- 必要性证据；
- 覆盖的镜头需求；
- 使用Shot；
- 完整正向Prompt；
- 针对性负面Prompt；
- 输出规则。

技术资产板以结构、身份、材质、角度和清晰度优先，不机械使用剧情帧的奇观强化。

## 9. Shot总表

| Shot | 场景 | 时长 | 剧情作用 | Ledger ID | Source End State | Current End State | 主功能 | 次功能 | 观众位置 | 可见画面 | 本镜唯一变化 | 动作阶段 | 表演强度起→止 | 摄影策略 | 灯光功能 | 帧来源 | 视频模式 |
|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## 9A. Shot功能与画面执行矩阵

| Shot | 剧本证据 | 观众即时体验 | 观众延迟体验 | 信息/情绪/奇观优先级 | 第一眼 | 第二眼 | 最终揭示 | 不得牺牲 | 功能冲突/拆镜 |
|---|---|---|---|---|---|---|---|---|---|

主功能必须且只能一个；次功能可为空且最多一个。功能必须进入摄影、灯光、表演、CF与Prompt。

## 10. 唯一 CONTINUITY_LEDGER

此节是全片跨镜剧情与状态的唯一事实源。后续Shot卡、CF和Prompt只引用或更新这里的条目，不另建`continuity_in / continuity_out`。

```yaml
continuity_ledger_entry:
  ledger_id:
  shot_id:
  source_end_state_id:
  inherited_story_facts:
  character_knowledge_and_intention:
  action_phase_and_completion:
  visible_character_state:
  prop_state_and_ownership:
  costume_damage_wetness_stamina_and_accumulation:
  scene_geography_axis_and_screen_direction:
  camera_focus_light_weather_time_and_sound_state:
  emotional_and_relationship_residue:
  new_change_in_this_shot:
  facts_that_must_not_reset: []
  exact_end_state:
  end_state_id:
  next_shot_required_inheritance: []
  intentional_discontinuity:
  discontinuity_reason:
```

第一镜引用`PROJECT_INITIAL_STATE`，其余镜头必须引用上一镜唯一`End State ID`。

## 11. 逐镜头导演制作卡

每个Shot完整使用`shot-production-card.md`。每镜必须：

- 引用项目视觉策略；
- 引用对应`Continuity Ledger ID`和`Source End State ID`；
- 说明本镜唯一新增变化；
- 建立场景功能与观众效果；
- 完成导演、摄影、灯光、表演或环境节奏；
- 明确动作阶段与防误读；
- 适用时保留关系残留；
- 条件化使用时空视觉编排；
- 写出精确结束状态并登记`Current End State ID`；
- 完成缩略图、画幅、连续剧情和风险检查。

禁止只输出部分镜头。空镜使用`NON_CHARACTER_PERFORMANCE`和环境节奏，不留空。

## 12. CF清单

| CF ID | 所属Shot | 类型 | Ledger ID | 表现的State ID | 主场景功能 | 项目策略 | 来源资产 | 动作阶段 | 表演/环境状态 | 是否预生成 | Prompt/合同 |
|---|---|---|---|---|---|---|---|---|---|---|---|

CF清单只负责索引，不能替代完整控制帧Prompt。START CF表现台账起态；END CF表现当前End State。

## 13. 全部控制帧生图Prompt

逐镜完整使用`templates/storyboard-frame-prompt-block.md`，直接包含：

- Shot、Scene、CF、时间和时长；
- 镜头唯一任务、主次场景功能与观众阅读顺序；
- 项目视觉策略和参考图具体职责；
- `Ledger ID`与`represented_state_id`；
- 帧来源、生成模式和失败备用；
- 前中后景、背景职责、大形、方向、局部高潮和冻结运动痕迹；
- 核心大形、中尺度结构、细节集中区、主体清洁区和视觉休息区；
- 流动元素、微粒、噪点与颗粒策略；
- 焦点、最亮区、最高对比、色彩锚点与变化起点；
- 动作阶段、接触、重量、手部方向、可见结果与防误读；
- 适用时的关系残留与道具自然化；
- 原创视觉语法、模板风险与替代结构；
- 材质可观察属性与语义漂移反制；
- 缩略图可读性、海报化风险和画幅执行；
- 人物表演时点或`NON_CHARACTER_PERFORMANCE`；
- 构图、景别、焦段、机位、焦点、景深、曝光和白平衡；
- 真实光源、世界位置、方向、软硬、色温、光比、受光与阴影；
- 每个生成CF独立可复制的正向Prompt、负面Prompt和输出规则；
- END CF或`TEXT_CONTRACT_ONLY`的精确状态合同；
- 图生图修改、局部修复和稳定替代。

禁止只提供CF名称、公共视觉前缀、简短说明、“同上”或“Prompt略”。静态Prompt只描述一个瞬间。

## 14. 全部逐镜生视频Prompt

逐镜输出完整视频Prompt包，包括：

- 输入CF和`Source End State ID`；
- 继承的剧情事实、人物知识、动作阶段、道具、空间、灯光和情绪；
- 主场景功能、导演意图与视觉空间；
- 本镜唯一剧情变化和核心视觉事件；
- 表演合同与情绪时间轴；
- 分段动作、接触、重量和物理关系；
- 材质、衣料和环境分层运动；
- 摄影机运动起止、焦点、景深和曝光；
- 逐镜灯光与允许变化；
- 峰值、收束、稳定停留和精确结束状态；
- 新`Current End State ID`和下一镜继承；
- 完整正向Prompt；
- 针对性负面Prompt；
- `POST_ONLY`方案或稳定降级。

“独立可复制”不等于脱离前后剧情重新开场。镜头摘要不能替代完整视频Prompt。

## 15. 参考图使用矩阵

| Shot | 面部/结构参考 | 场景机位 | 道具/状态参考 | 上一镜CF/尾帧 | Source End State | 新增参考需求 |
|---|---|---|---|---|---|---|

## 16. 连续性台账可读视图

本节只把第10节`CONTINUITY_LEDGER`转成便于用户查看的表格，不能独立修改状态或成为第二事实源。

| Ledger ID | Shot | Source End State | 继承剧情事实 | 人物知识/目的 | 动作与接触 | 道具/累积状态 | 空间/光线/声音 | 本镜新增变化 | Current End State | 下一镜必须继承 |
|---|---|---|---|---|---|---|---|---|---|---|

如表格与第10节台账冲突，以台账为准并立即`REPAIR`表格。

## 17. 剪辑、声音和后期

镜头顺序、转场、声音桥、环境声、呼吸、对白、音乐、留白、字幕、分层合成、降噪、胶片颗粒与调色。明显颗粒和特殊媒介质感优先在后期控制，除非其本身承担叙事。

声音和剪辑必须引用台账中的听觉状态、事件顺序与跨镜接力，不能无原因重新建立。

## 18. 高风险与备用

逐项给出风险、首选方法和稳定降级。至少检查：

- 剧情或状态重置；
- End State交接断裂；
- 场景功能冲突；
- 动作阶段误读；
- 关系残留损失；
- 焦点与叙事动作错位；
- 缩略图不可读；
- 视觉密度过载或中尺度结构空洞；
- 通用AI模板回落；
- 材质语义漂移；
- 道具商品化；
- 无意海报化或公益广告感；
- 画幅与外部平台参数不一致；
- 多对象、手部、复杂物理、镜面或文字超出模型能力。

## 19. 外部平台生成顺序

项目视觉策略确认
→ Shot场景功能路由
→ 建立`CONTINUITY_LEDGER`
→ 面部/三视图/全身/手部/状态资产
→ 场景主空镜与反向机位
→ 道具与状态
→ 独立首帧
→ 首尾帧
→ 依赖上一镜End State的镜头
→ 分层素材
→ 视频
→ 剪辑后期。

外部平台若提供宽高比参数，必须按当前任务设置，不能只依赖Prompt中的比例文字。

## 20. 内部完整性检查摘要

```yaml
status: PROMPT_PACKAGE_READY | NEEDS_REPAIR
narrative_lock_preserved:
project_visual_strategy_scope:
project_visual_strategy_conformance:
scene_function_coverage:
scene_function_execution_consistency:
function_conflicts: []
asset_angle_interaction_state_coverage:
shot_count:
shot_cards:
continuity_ledger_present:
continuity_ledger_single_source:
shots_with_valid_ledger_reference:
shots_with_valid_source_end_state:
shots_with_registered_current_end_state:
end_state_handoff_coverage:
shots_with_project_visual_strategy_reference:
shots_with_primary_scene_function:
shots_with_scene_function_script_evidence:
shots_with_director_intent:
shots_with_camera_direction:
shots_with_lighting_direction:
character_shots_with_performance_direction:
shots_with_action_phase_semantics:
relationship_shots_with_residue_control:
shots_with_reference_binding:
shots_with_full_frame_prompt_block:
generated_cf_with_standalone_prompt:
frames_with_visual_hierarchy:
frames_with_clean_subject_zones:
frames_with_visual_rest_zones:
frames_with_focal_alignment:
frames_with_thumbnail_readability:
frames_with_original_visual_grammar:
frames_with_material_drift_control:
shots_with_end_frame_contract:
shots_with_frame_repair_plan:
shots_with_image_source:
shots_with_video_prompt_or_post_plan:
frame_prompt_pack_included:
video_prompt_pack_included:
aspect_ratio_conformance:
missing_asset_coverage: []
redundant_assets: []
orphan_cf_ids: []
undefined_asset_ids: []
missing_ledger_entries: []
missing_end_state_ids: []
broken_end_state_handoffs: []
competing_continuity_records: []
incomplete_frame_prompt_shots: []
shared_prefix_dependent_cf_ids: []
missing_end_frame_contracts: []
missing_repair_prompts: []
continuity_conflicts: []
emotion_intensity_conflicts: []
directing_coherence_conflicts: []
prompt_conflicts: []
action_phase_misread_frames: []
relationship_residue_loss_frames: []
micro_detail_overload_frames: []
medium_structure_voids: []
focal_misalignment_frames: []
thumbnail_misread_frames: []
generic_visual_template_frames: []
material_drift_frames: []
commercialized_prop_frames: []
unintended_poster_frames: []
aspect_ratio_conflicts: []
high_risk_shots: []
```

只有`evals/full-package-integrity-check.md`和`evals/frame-communication-check.md`同时通过，才能标记`PROMPT_PACKAGE_READY`。没有真实媒体时不得声称样片或成片已经通过。
