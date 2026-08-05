# Shot–CF–Prompt Binding System V4.5

## 目标

消除“有Shot但没有参考、控制帧或可执行Prompt”的断层，并确保项目视觉策略、场景功能、动作阶段、关系残留、画面控制和跨镜状态沿同一绑定链传递。

本系统不建立第二套连续性记录。所有跨镜剧情事实统一引用`CONTINUITY_LEDGER`。

## 一、ID规范

```text
Scene: SC-01
Shot: SH-01-03
Continuity Entry: CL-SH01-03
Source End State: ES-SH01-02
Current End State: ES-SH01-03
Start CF: CF-SH01-03-S
End CF: CF-SH01-03-E
Bridge CF: CF-SH01-03-B1
```

ID在Shot表、连续性台账、CF包、图片Prompt包、视频Prompt包和参考矩阵中必须一致。

## 二、唯一绑定链

```text
NARRATIVE_LOCK
→ PROJECT_VISUAL_STRATEGY
→ CONTINUITY_LEDGER起态
→ Shot场景功能与导演设计
→ Asset references
→ CF
→ Image Prompt / Video Prompt / Post Plan
→ Shot精确尾态
→ 新End State写回CONTINUITY_LEDGER
→ 下一Shot继承
```

对象关系：

```text
Asset ──references──> CF
CF ──belongs_to──> Shot
Continuity Entry ──defines_start_and_end_state──> Shot
Previous End State ──hands_off──> Next Continuity Entry
Shot ──carries──> Scene Function / Director / Camera / Lighting / Performance
CF ──carries──> Visible State / Visual Hierarchy / Gesture Semantics / Focal Alignment
Shot ──compiles_to──> Image Prompt / Video Prompt / Post Plan
```

CF不能脱离Shot；Shot不能引用不存在的CF、资产、台账条目或End State。场景功能、连续性和画面控制不能只停留在分析表中，必须进入最终Prompt。

## 三、Shot最小完整单元

```yaml
shot_binding:
  shot_id:
  scene_id:
  narrative_purpose:
  visual_description:
  project_visual_strategy_reference:
  continuity:
    ledger_id:
    source_end_state_id:
    inherited_facts_used:
    new_change_in_this_shot:
    current_end_state_id:
    next_shot_required_inheritance: []
  scene_function:
    primary:
    secondary:
    script_evidence: []
    audience_immediate_effect:
    audience_delayed_effect:
    information_emotion_spectacle_priority:
    first_read:
    second_read:
    final_reveal:
    must_not_sacrifice: []
    conflict_and_split_decision:
  director_intent:
  orchestration_required: REQUIRED | SIMPLIFIED | NOT_REQUIRED
  camera_direction:
  lighting_direction:
  performance_direction_or_non_character_performance:
  emotion_curve_or_environment_rhythm:
  action_semantics:
    intended_action:
    phase:
    relation_to_previous_phase:
    contact_state:
    weight_or_force_transfer:
    direction_and_visible_result:
    misread_risks: []
  relationship_residue_or_not_applicable:
  references:
    character: []
    location: []
    prop: []
    state: []
    previous_cf: []
  frame_source_mode:
  start_cf:
  end_cf:
  bridge_cfs: []
  image_prompt_delivery:
  video_prompt_delivery:
  post_delivery:
  risk_and_fallback:
```

不得再同时维护`input_state`、`continuity_in`、`continuity_out`等竞争字段。需要展示起态和尾态时，从对应`source_end_state_id`和`current_end_state_id`展开。

## 四、CF绑定

每个生成CF必须绑定：

```yaml
cf_binding:
  cf_id:
  shot_id:
  cf_type: START | END | BRIDGE | TEXT_CONTRACT_ONLY
  continuity_ledger_id:
  represented_state_id:
  reference_assets: []
  project_visual_strategy_reference:
  scene_function_reference:
  action_phase:
  exact_visible_state:
  frame_communication:
    visual_hierarchy:
    clean_subject_zones:
    visual_rest_zones:
    detail_attenuation:
    particle_and_noise_policy:
    focal_alignment:
    thumbnail_readability:
    prop_naturalism:
    original_visual_grammar:
    material_semantic_drift:
    posterization_risk:
    aspect_ratio_execution:
```

START CF必须表现台账起态；END CF必须表现当前`End State ID`；BRIDGE CF只能处理镜头内部生成分段，不能悄悄改变剧情事实。

## 五、图片来源决策

### NEW_START_FRAME

交付完整首帧Prompt，并从当前台账起态重新构图。换机位可以改变观看角度，不能改变人物知识、动作完成度、道具归属、累积状态和空间事实。

### FIRST_LAST_FRAME

交付完整首帧和尾帧Prompt。尾帧必须对应当前`End State ID`，包含动作结果、关系残留、道具状态、构图终点、灯光尾态和下一镜继承。

### PREVIOUS_TAIL_INHERITANCE

必须交付：

- `source_end_state_id`；
- 继承的CF或稳定尾帧ID；
- 继续使用的资产；
- 允许变化和禁止变化；
- 尾帧不可用时的备用首帧Prompt。

### EXISTING_USER_FRAME

写明用户图片与台账起态的一致和冲突之处，以及当前动作阶段、视觉密度、焦点、身份、空间或状态需要补足的内容。

### TEXT_TO_VIDEO

写明无需静态参考的理由，并明确台账起态、唯一变化、精确尾态、场景功能、动作阶段和连续性边界。

### POST_ONLY

写明素材来源、后期操作、起态和尾态，不得因不生成视频而省略剧情与连续性。

## 六、空值处理

禁止输出：

```text
参考图：无
描述词：无
Prompt：略
同上
沿用前面
功能：默认
动作：自然
画面：干净
连续性：保持一致
```

必须转换为具体绑定，例如：

```text
引用CL-SH01-03；从ES-SH01-02继承人物右手已握住钥匙、门仍上锁和受伤右腕状态。
首帧使用CF-SH01-02-E；继续使用CHAR-01、LOC-01和PROP-KEY-01。
本镜只推进“钥匙插入锁孔”，结束于ES-SH01-03；不重新取钥匙，不恢复右腕动作能力。
```

## 七、跨对象一致性

逐项检查：

- Shot引用的`source_end_state_id`真实存在；
- START CF与台账起态一致；
- 本镜只推进台账登记的新增变化；
- Shot动作阶段与START / END CF一致；
- 接触、重量、手部、道具和累积状态进入图片Prompt；
- 视频Prompt从起态发展到当前`End State ID`，不重启动作；
- END CF、结束帧合同和台账精确尾态一致；
- 下一Shot引用正确的End State；
- 场景功能与CF视觉重点一致；
- 焦点、灯光、色彩锚点与镜头任务一致；
- 画幅与平台比例在Shot、CF和输出规则中一致；
- 原创结构、材质和项目视觉策略没有在编译时丢失。

## 八、覆盖率检查

```yaml
coverage_report:
  shot_count:
  shot_cards:
  shots_with_visual_description:
  shots_with_project_visual_strategy_reference:
  shots_with_continuity_ledger_reference:
  shots_with_valid_source_end_state:
  shots_with_registered_current_end_state:
  shots_with_primary_scene_function:
  shots_with_scene_function_script_evidence:
  shots_with_director_intent:
  shots_with_camera_direction:
  shots_with_lighting_direction:
  character_shots_with_performance_direction:
  shots_with_action_semantics:
  relationship_shots_with_residue_control:
  shots_with_reference_binding:
  shots_with_image_source:
  shots_with_video_prompt_or_post_plan:
  generated_frames_with_visual_hierarchy:
  generated_frames_with_focal_alignment:
  generated_frames_with_thumbnail_readability:
  generated_frames_with_material_drift_control:
  generated_frames_with_aspect_ratio_execution:
  orphan_cf_ids: []
  missing_cf_ids: []
  undefined_asset_ids: []
  missing_ledger_entries: []
  missing_end_state_ids: []
  broken_end_state_handoffs: []
  inconsistent_shot_ids: []
  function_binding_conflicts: []
  action_phase_binding_conflicts: []
  relationship_residue_binding_conflicts: []
  aspect_ratio_binding_conflicts: []
```

所有数量必须与适用Shot或CF数量一致，异常数组必须为空，才能标记`PROMPT_PACKAGE_READY`。
