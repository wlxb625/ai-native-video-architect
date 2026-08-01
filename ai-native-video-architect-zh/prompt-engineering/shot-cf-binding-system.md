# Shot–CF–Prompt Binding System V4.4

## 目标

消除“有Shot但没有描述词、参考图或可执行Prompt”的断层。

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
Shot ──compiles_to──> Image Prompt / Video Prompt / Post Plan
```

CF不能脱离Shot独立存在；Shot不能只引用CF名称而没有对应定义。

## 三、Shot最小完整单元

```yaml
shot_binding:
  shot_id:
  scene_id:
  narrative_purpose:
  visual_description:
  director_intent:
  camera_direction:
  lighting_direction:
  performance_direction_or_non_character_performance:
  emotion_curve_or_environment_rhythm:
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

## 四、图片来源决策

### NEW_START_FRAME

交付完整首帧Prompt。

### FIRST_LAST_FRAME

交付完整首帧Prompt和尾帧Prompt。

### PREVIOUS_TAIL_INHERITANCE

必须交付：

- 继承CF ID；
- 继续使用的基础资产；
- 对继承帧允许和禁止的变化；
- 上一镜尾帧不可用时的备用首帧Prompt。

### EXISTING_USER_FRAME

写明用户图片职责以及需要补充的身份、场景或风格参考。

### TEXT_TO_VIDEO

写明无需静态参考的充分理由，并仍明确视觉描述和连续性边界。

### POST_ONLY

写明不生成的原因和完整后期操作。

## 五、空值处理

禁止输出：

```text
参考图：无
描述词：无
Prompt：略
同上
沿用前面
```

必须转换为可执行说明，例如：

```text
参考来源：继承CF-SH01-02-E；继续使用CHAR-01锁定身份、LOC-01锁定空间。
本镜无需新首帧；若继承尾帧不稳定，使用下列备用首帧Prompt重新生成。
```

## 六、覆盖率检查

```yaml
coverage_report:
  shot_count:
  shot_cards:
  shots_with_visual_description:
  shots_with_director_intent:
  shots_with_camera_direction:
  shots_with_lighting_direction:
  character_shots_with_performance_direction:
  shots_with_reference_binding:
  shots_with_start_state:
  shots_with_end_state:
  shots_with_image_source:
  shots_with_video_prompt_or_post_plan:
  orphan_cf_ids: []
  missing_cf_ids: []
  undefined_asset_ids: []
  inconsistent_shot_ids: []
```

所有数量必须与`shot_count`一致，所有异常数组必须为空，才能标记`PROMPT_PACKAGE_READY`。
