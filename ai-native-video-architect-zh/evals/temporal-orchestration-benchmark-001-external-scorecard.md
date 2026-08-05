# Temporal Visual Orchestration Benchmark 001｜外部生成评分卡

## 1. 使用说明

本评分卡只用于《慢一秒》SH-03～SH-05三镜外部生成测试。

必须基于真实生成视频、真实抽取帧和最终无声/有声拼接结果评分。未生成时所有字段保持`PENDING`，不得根据Prompt文本预判通过。

```yaml
test_status: PENDING_EXTERNAL_MEDIA
strong_gate_result: NOT_EVALUATED
```

---

## 2. 测试记录

```yaml
execution_record:
  date:
  platform_or_model:
  model_version:
  generation_mode:
  aspect_ratio:
  output_resolution:
  fps:
  SH03_seed_or_job_id:
  SH04_seed_or_job_id:
  SH05_seed_or_job_id:
  number_of_attempts:
  reference_assets_used: []
  post_processing_used: []
  evaluator:
```

每次重试单独记录，不得只保留最好的一次而删除失败样本。

---

## 3. 评分原则

每项使用0—4分：

- `0`：完全失败或与导演意图相反；
- `1`：勉强可辨，但存在严重漂移或误读；
- `2`：部分成立，需要明显返修；
- `3`：基本成立，只有局部问题；
- `4`：清楚成立，可作为验证证据。

以下任一硬失败出现时，即使总分较高，也不能判定PASS。

---

# 4. SH-03评分｜摄影机LEAD

## 4.1 信息与摄影机角色

| 检查项 | 0-4 | 证据时间码 | 备注 |
|---|---:|---|---|
| 摄影机先于人物揭示货车 |  |  |  |
| 侧移平滑、低幅、无甩镜 |  |  |  |
| 骑手在结尾前尚未完全反应 |  |  |  |
| 风车、骑手方向、货车关系同时可读 |  |  |  |
| 货车揭示来自空间变化而非突然弹出 |  |  |  |
| 灯光变化只由货车进入角度引起 |  |  |  |

## 4.2 SH-03硬失败

```yaml
SH03_hard_failures:
  camera_whip_pan_or_random_orbit: false
  rider_reacts_before_reveal: false
  truck_teleports_or_changes_lane: false
  spatial_triangle_unreadable: false
  child_enters_road: false
  unexplained_light_flash: false
  identity_or_vehicle_drift: false
```

### SH-03结果

```yaml
SH03_score:
SH03_result: PENDING
SH03_primary_failure_source:
  DIRECTING_CHOICE | CONTROL_FRAME | PROMPT | MODEL_EXECUTION | ASSET_CONTINUITY | UNKNOWN
```

---

# 5. SH-04评分｜摄影机RESIST与多系统对抗

## 5.1 动作与空间

| 检查项 | 0-4 | 证据时间码 | 备注 |
|---|---:|---|---|
| 制动从手部准备开始，动作顺序可读 |  |  |  |
| 电动车减速、轻微偏转和重心修正真实 |  |  |  |
| 后轮侧滑短促受控，没有夸张漂移 |  |  |  |
| 货车保持车道和安全距离 |  |  |  |
| 前轮、纸风车、儿童安全区关系清楚 |  |  |  |
| 结尾人物与车辆稳定停住 |  |  |  |

## 5.2 摄影机、灯光与声音关系

| 检查项 | 0-4 | 证据时间码 | 备注 |
|---|---:|---|---|
| 摄影机后撤是为了维持空间，而非随机运动 |  |  |  |
| 摄影机没有贴脸、环绕或英雄化主体 |  |  |  |
| 雨、路灯和信号灯保持稳定 |  |  |  |
| 制动、轮胎水声和喇叭峰值可对齐 |  |  |  |
| 动作高潮后声音和运动能够分离收束 |  |  |  |

## 5.3 SH-04硬失败

```yaml
SH04_hard_failures:
  collision_or_contact: false
  child_in_danger_center: false
  heroic_jump_or_rescue: false
  exaggerated_drift_or_crash: false
  truck_lane_or_scale_drift: false
  camera_aggressive_push_or_orbit: false
  random_weather_or_light_change: false
  pinwheel_crushed_or_disappears: false
  rider_or_vehicle_identity_drift: false
  end_state_unstable: false
```

### SH-04结果

```yaml
SH04_score:
SH04_result: PENDING
SH04_primary_failure_source:
  DIRECTING_CHOICE | CONTROL_FRAME | PROMPT | MODEL_EXECUTION | ASSET_CONTINUITY | MULTI_OBJECT_COMPLEXITY | UNKNOWN
```

---

# 6. SH-05评分｜摄影机FOLLOW

## 6.1 时序与表演

| 检查项 | 0-4 | 证据时间码 | 备注 |
|---|---:|---|---|
| 开头至少短暂保持SH-04停稳状态 |  |  |  |
| 摄影机在人物确认安全后才开始靠近 |  |  |  |
| 推进幅度克制，仍保留车把、风车和空间证据 |  |  |  |
| 骑手表演依靠视线、手指张力和呼吸 |  |  |  |
| 没有哭泣、微笑摆拍或英雄凝视 |  |  |  |
| 环境保持正常运行，不替人物煽情 |  |  |  |
| 货车灯光和声音自然衰减 |  |  |  |

## 6.2 SH-05硬失败

```yaml
SH05_hard_failures:
  camera_moves_before_stop_is_established: false
  push_becomes_face_closeup: false
  heroic_or_commercial_pose: false
  child_runs_to_rider: false
  rain_or_signal_changes_for_emotion: false
  truck_reappears_or_resets: false
  spatial_evidence_lost: false
  identity_or_costume_drift: false
```

### SH-05结果

```yaml
SH05_score:
SH05_result: PENDING
SH05_primary_failure_source:
  DIRECTING_CHOICE | CONTROL_FRAME | PROMPT | MODEL_EXECUTION | ASSET_CONTINUITY | UNKNOWN
```

---

# 7. 三镜连续性评分

| 检查项 | 0-4 | 证据 | 备注 |
|---|---:|---|---|
| 骑手身份、服装和电动车连续 |  |  |  |
| 路口、停止线、车道与光源位置连续 |  |  |  |
| 纸风车位置和状态连续 |  |  |  |
| 货车位置、方向和离场过程连续 |  |  |  |
| SH-03结尾动作准备无重置地进入SH-04 |  |  |  |
| SH-04停稳尾态无重置地进入SH-05 |  |  |  |
| 摄影机LEAD→RESIST→FOLLOW转换可感知 |  |  |  |
| 角色转换自然，不像三个独立随机镜头 |  |  |  |
| 声音桥支持信息和能量连续 |  |  |  |
| 整体节奏有建立、峰值和释放 |  |  |  |

## 三镜硬失败

```yaml
sequence_hard_failures:
  independent_scene_reconstruction: false
  screen_direction_reversal_without_reason: false
  vehicle_or_prop_reset: false
  camera_roles_indistinguishable: false
  camera_role_change_feels_random: false
  action_restarts_between_shots: false
  danger_state_reappears_after_resolution: false
  visual_continuity_only_from_color: false
```

---

# 8. 过拟合与规则污染检查

生成测试完成后必须回答：

```yaml
overfitting_check:
  did_result_prove_camera_must_lead_in_suspense: false
  did_result_prove_camera_must_resist_in_action: false
  did_result_prove_camera_must_follow_after_resolution: false
  did_result_prove_realism_requires_neutral_environment: false
  project_specific_findings: []
  transferable_mechanisms_supported: []
  mechanisms_not_supported: []
  new_conditional_options: []
  core_rule_changes_recommended: []
  case_library_only_findings: []
```

以上前四项原则上必须保持`false`。单个基准只能验证条件化选择是否可执行，不能证明该选择对同类项目普遍正确。

---

# 9. 诊断归因

出现失败时先归因，不直接增加Prompt长度。

```yaml
failure_diagnosis:
  director_choice_error:
  control_frame_error:
  temporal_prompt_error:
  model_capability_limit:
  multi_object_instability:
  identity_asset_error:
  spatial_layout_error:
  post_sound_or_edit_error:
  random_generation_variance:
  recommended_local_repair:
  should_core_skill_change: false
  reason:
```

核心Skill只有在多个差异项目出现相同结构性失败时才考虑修改。

---

# 10. 通过门槛

## 单镜PASS

每镜必须同时满足：

- 该镜平均分不低于3.0；
- 目标摄影机角色相关项目不低于3分；
- 无硬失败；
- 结束帧合同可截图验证；
- 失败不依赖剪辑掩盖。

## 三镜序列PASS

必须同时满足：

```yaml
sequence_pass_requirements:
  SH03_result: PASS
  SH04_result: PASS
  SH05_result: PASS
  continuity_average_minimum: 3.0
  camera_role_transition_score_minimum: 3
  hard_failures: 0
  stable_tail_inheritance_verified: true
  environment_and_light_randomness_absent: true
  case_specific_overgeneralization_absent: true
```

## 当前结果模板

```yaml
final_external_result:
  status: PENDING
  SH03:
  SH04:
  SH05:
  sequence_continuity:
  camera_role_transition:
  hard_failure_count:
  strongest_success:
  strongest_failure:
  local_repairs_needed: []
  core_skill_change_needed: false
  evidence_media: []
```

只有真实媒体完成并填写证据后，才能把`externally_generated_benchmarks`从0更新为1。
