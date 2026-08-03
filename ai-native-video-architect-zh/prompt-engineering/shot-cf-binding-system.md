# Shot–CF–Prompt Binding System V4.5

## 目标

消除“有Shot但没有描述词、参考图或可执行Prompt”的断层，并确保场景功能、动作阶段、视觉层级、关系残留、画幅与最终Prompt保持同一绑定链。

## 一、ID规范

```text
Scene: SC-01
Shot:  SH-01-03
Start CF:  CF-SH01-03-S
End CF:    CF-SH01-03-E
Bridge CF: CF-SH01-03-B1
```

ID在镜头表、CF包、图片Prompt包、视频Prompt包、连续性表和参考使用矩阵中必须完全一致。

## 二、绑定关系

```text
Asset ──references──> CF
CF ──belongs_to──> Shot
Previous Shot END CF ──hands_off──> Next Shot START
Shot ──carries──> Scene Function / Director / Camera / Lighting / Performance
CF ──carries──> Visual Hierarchy / Gesture Semantics / Focal Alignment / Aspect Ratio
Shot ──compiles_to──> Image Prompt / Video Prompt / Post Plan
```

CF不能脱离Shot独立存在；Shot不能只引用CF名称而没有对应定义。场景功能和V4.5画面控制不能只存在于分析表中，必须绑定到Shot、CF和最终Prompt。

## 三、Shot最小完整单元

```yaml
shot_binding:
  shot_id:
  scene_id:
  narrative_purpose:
  visual_description:
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
  camera_direction:
  lighting_direction:
  performance_direction_or_non_character_performance:
  emotion_curve_or_environment_rhythm:
  action_semantics:
    intended_action:
    phase:
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
  continuity_in:
  continuity_out:
```

每个生成CF还必须绑定：

```yaml
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

## 四、图片来源决策

### NEW_START_FRAME

交付完整首帧Prompt，并包含场景功能、视觉层级、动作阶段、焦点与画幅执行。

### FIRST_LAST_FRAME

交付完整首帧Prompt和尾帧Prompt。尾帧除动作结果外，还必须写关系残留、道具承重、焦点与下一镜继承。

### PREVIOUS_TAIL_INHERITANCE

必须交付：

- 继承CF ID；
- 继续使用的基础资产；
- 继承的场景功能与画面沟通状态；
- 对继承帧允许和禁止的变化；
- 上一镜尾帧不可用时的备用首帧Prompt。

### EXISTING_USER_FRAME

写明用户图片职责、当前动作阶段、画面已存在的视觉密度与焦点问题，以及需要补充的身份、场景或风格参考。

### TEXT_TO_VIDEO

写明无需静态参考的充分理由，并仍明确场景功能、视觉描述、动作阶段、缩略图可读性和连续性边界。

### POST_ONLY

写明不生成的原因和完整后期操作，包括是否由裁切、降噪、颗粒、分层合成或比例重构完成。

## 五、空值处理

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
```

必须转换为可执行说明，例如：

```text
参考来源：继承CF-SH01-02-E；继续使用CHAR-01锁定身份、LOC-01锁定空间。
主场景功能继续为EMOTIONAL_RESONANCE；本镜从上一镜COMPLETION进入AFTERMATH_RESIDUE。
本镜无需新首帧；若继承尾帧不稳定，使用下列备用首帧Prompt重新生成。
```

## 六、跨对象一致性

逐项检查：

- Shot主场景功能与CF视觉重点一致；
- Shot动作阶段与START / END CF一致；
- CF接触、重量、手部和道具状态进入图片Prompt；
- 视频Prompt从START阶段发展到END阶段，不重新设计动作含义；
- 关系残留从尾帧传入下一镜开始状态；
- 焦点、光色锚点与主场景功能一致；
- 当前画幅和平台比例参数在Shot、CF与输出规则中一致；
- 原创结构和材质规则没有在编译时丢失。

## 七、覆盖率检查

```yaml
coverage_report:
  shot_count:
  shot_cards:
  shots_with_visual_description:
  shots_with_primary_scene_function:
  shots_with_scene_function_script_evidence:
  shots_with_director_intent:
  shots_with_camera_direction:
  shots_with_lighting_direction:
  character_shots_with_performance_direction:
  shots_with_action_semantics:
  relationship_shots_with_residue_control:
  shots_with_reference_binding:
  shots_with_start_state:
  shots_with_end_state:
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
  inconsistent_shot_ids: []
  function_binding_conflicts: []
  action_phase_binding_conflicts: []
  relationship_residue_binding_conflicts: []
  aspect_ratio_binding_conflicts: []
```

所有数量必须与适用Shot或CF数量一致，所有异常数组必须为空，才能标记`PROMPT_PACKAGE_READY`。