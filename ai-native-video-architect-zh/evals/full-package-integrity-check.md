# Full Package Integrity Check V4.4

## 用途

在Agent交付完整制作提示词包前，检查所有Shot、CF、资产、导演字段、表演和Prompt是否真正闭环。

## 硬性计数

以下数量必须相等：

```text
Shot总数
镜头制作卡数量
有可见画面描述的Shot数量
有导演意图的Shot数量
有摄影方向的Shot数量
有逐镜灯光方向的Shot数量
人物镜头中有表演方向与情绪曲线的数量
有参考绑定的Shot数量
有开始状态的Shot数量
有结束状态的Shot数量
有图像来源的生成型Shot数量
有视频Prompt或POST_ONLY方案的Shot数量
```

空镜、纯道具和环境镜头不得用空白绕过表演字段，应标记`NON_CHARACTER_PERFORMANCE`并给出环境节奏、观看关系和运动强度。

## ID完整性

- 所有Shot ID唯一；
- 所有CF ID唯一；
- 每个CF只属于一个Shot；
- 每个引用CF都存在；
- 每个资产ID已定义；
- 镜头表、CF表、图片Prompt和视频Prompt编号一致。

## 内容完整性

每个Shot必须有：

- narrative_purpose；
- visual_description；
- director_intent；
- camera_direction；
- lighting_direction；
- performance_direction或NON_CHARACTER_PERFORMANCE；
- emotion_curve或environment_rhythm；
- input_state；
- primary_action；
- exact_end_state；
- reference_bindings；
- frame_source_mode；
- control_frames；
- generation_mode；
- image_prompt或继承说明；
- video_prompt或POST_ONLY说明；
- continuity_in与continuity_out；
- risk_and_fallback。

## 导演一致性

读取`evals/directing-coherence-check.md`和`evals/performance-direction-score.md`，检查：

- 情绪目标是否由可见表演实现；
- 观众位置是否由机位、距离和揭示顺序实现；
- 镜头与灯光是否让关键表演可读；
- 表演强度是否符合事件、时长和相邻镜头；
- 灯光变化是否有真实原因；
- 结尾表演状态是否写入End CF和下一镜开始状态。

## 连续性

逐对检查：

- 人物位置、朝向、视线；
- 左右手、道具和接触；
- 动作完成百分比；
- 表演强度、呼吸、嘴、肩膀、手指和重心；
- 屏幕方向与轴线；
- 场景地标；
- 光源方向、白平衡、曝光；
- 声音和剪辑连接。

## Prompt一致性

Shot、CF、图片Prompt和视频Prompt不能在动作、表演、情绪强度、机位、运镜、焦点、灯光和尾态上互相矛盾。

## 结果

```yaml
status: PASS | REPAIR
shot_count:
coverage_ratio:
missing_fields: []
orphan_cf_ids: []
missing_cf_ids: []
undefined_asset_ids: []
continuity_conflicts: []
emotion_intensity_conflicts: []
directing_coherence_conflicts: []
prompt_conflicts: []
repair_actions: []
```

只有`PASS`才能输出`PROMPT_PACKAGE_READY`。
