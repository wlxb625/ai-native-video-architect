# Production Runbook Template

该模板用于Prompt完成后的实际生产组织。没有实际图片或视频证据时，只填写计划字段，不得把计划状态写成已通过。

```yaml
project:
  title:
  duration:
  aspect_ratio:
  current_status: DESIGN_READY | PROMPT_READY | REFERENCE_READY | SAMPLE_VALIDATED | BATCH_GENERATION_READY | EDIT_READY | DELIVERY_READY
  status_evidence: []
  target_platform_or_model:
  known_model_limits: []

canonical_references:
  - id:
    type: CHARACTER | ENVIRONMENT | PROP | SPECIAL_STATE
    selected_file:
    source_prompt_version:
    locked_features: []
    approved_uses: []
    known_limitations: []
    supersedes:

reference_candidate_selection:
  generated_candidates: []
  selected_candidate:
  rejected_candidates:
    - file:
      reason:
  selection_checks:
    identity_or_structure:
    visible_errors:
    shot_coverage:
    lighting_and_material_fit:
    reference_readability:

representative_tests:
  normal_shot:
    shot_id:
    reason:
    start_frame:
    end_frame:
    prompt_version:
    generated_versions: []
    selected_version:
    acceptance_score:
    status: PLAN | PASS | CONDITIONAL | FAIL
    evidence:
    must_fix: []
  high_risk_shot:
    required:
    shot_id:
    risk:
    generation_mode:
    bridge_or_layers: []
    generated_versions: []
    selected_version:
    acceptance_score:
    status: PLAN | PASS | CONDITIONAL | FAIL
    evidence:
    must_fix: []

sample_gate:
  normal_shot_passed:
  high_risk_shot_passed_or_not_required:
  end_frame_reachability_verified:
  identity_prop_continuity_verified:
  camera_focus_lighting_verified:
  edit_connection_verified:
  batch_generation_allowed:

failure_diagnosis:
  layer: REFERENCE_FAILURE | CONTROL_FRAME_FAILURE | PROMPT_FAILURE | MODEL_CAPABILITY_FAILURE | POST_PRODUCTION_FAILURE
  observed_problem:
  repeated_across_versions:
  smallest_effective_repair:
  new_asset_required:
  reason:

production_dependency_graph:
  canonical_references: []
  sample_control_frames: []
  representative_clips: []
  dependent_control_frames: []
  continuous_story_shots: []
  independent_insert_or_end_shots: []
  post_only_layers: []

shot_queue:
  - shot_id:
    narrative_order:
    production_order:
    dependency:
    mode:
    start_frame:
    end_frame:
    bridge_or_layers: []
    prompt_version:
    target_candidate_count:
    status: NOT_STARTED | GENERATING | REVIEW | PASS | CONDITIONAL | FAIL

shot_ledger:
  - shot_id:
    generated_candidates:
      - file:
        prompt_version:
        acceptance_score:
        result: PASS | CONDITIONAL | FAIL
        failed_dimensions: []
    selected_candidate:
    selected_in_point:
    selected_out_point:
    end_hold_frames:
    next_shot_connection:
    repair_action:

asset_upgrade_log:
  - trigger_failure:
    repeated_evidence:
    added_reference:
    expected_reuse_shots: []
    why_prompt_or_post_was_not_enough:

editing_plan:
  timeline_order: []
  shot_versions: []
  transitions:
    - from:
      to:
      method: HARD_CUT | ACTION_MATCH | GAZE_MATCH | SOUND_BRIDGE | OCCLUSION_SWITCH | CUT_TO_BLACK
      exact_cut_point:
  layered_composites:
    - shot_id:
      base_plate:
      subject_layer:
      effect_layer:
      mask_or_track:
  post_text:
    - shot_id:
      content:
      perspective_and_tracking:
      depth_and_blur:
  sound:
    ambience: []
    foley: []
    dialogue_or_voice: []
    music: []
    silence_design: []
  color_and_finish:
    exposure_continuity:
    white_balance:
    contrast_and_saturation:
    grain_or_texture:

final_quality_control:
  script_fidelity:
  identity_and_costume:
  environment_and_props:
  camera_and_focus:
  lighting_and_exposure:
  edit_continuity:
  text_and_graphics:
  sound_and_music:
  duration_and_pacing:
  export_settings:
  unresolved_issues: []
  final_status: EDIT_READY | DELIVERY_READY | CONDITIONAL | FAIL
```

## 使用规则

- `selected_file`和`selected_candidate`必须指向真实存在并已选择的文件；
- 未看到实际样片时，代表性测试状态只能写`PLAN`；
- `batch_generation_allowed`只有普通样片和必要高风险样片通过后才能为`true`；
- 每个镜头只保留一个进入剪辑的主版本，备选版本可以记录但不能混乱使用；
- 新增资产必须在`asset_upgrade_log`记录实际失败依据；
- 最终交付前必须填写`final_quality_control`。