# Full Package Integrity Check V4.4

## 用途

在Agent交付完整制作提示词包前，检查剧本锁定、项目视觉策略、所有Shot、CF、资产、导演字段、表演和Prompt是否真正闭环。

## NARRATIVE_LOCK保留

检查制作阶段是否保留：

- 主角或主体；
- 核心关系与处境；
- 世界规则或主要机制；
- 关键选择；
- 高潮行动者和不可逆变化；
- 结尾及开放程度；
- 主题意义；
- 用户授权边界。

发现为了风格、资产或生成便利擅自改变上述事实，直接REPAIR。

## 项目视觉策略

完整制作包必须存在`PROJECT_VISUAL_STRATEGY`并满足：

- 标记`scope: PROJECT_ONLY`；
- 生成于`NARRATIVE_LOCK`之后；
- 引用当前剧本证据；
- 未把固定色彩、摄影、材质、表演温度或背景功能写成Skill通用默认；
- 定义Style DNA、背景职责、视觉张力、连续性锚点、允许变化和禁止漂移；
- 资产、Shot、CF、图片Prompt和视频Prompt均能追溯到该策略；
- 镜头之间允许有叙事驱动的差异，不要求机械相同。

单张图片或单镜头任务只能使用局部视觉合同，不能伪称完整项目策略。

## 资产角度、交互与状态覆盖

资产覆盖不能只统计是否存在一个角色图和一个场景图。逐项检查：

- 重要面部近景是否有面部身份依据；
- 正面、严格侧面、背面、转身和离场背影是否有结构依据；
- 全身、俯身、跪姿、走动和复杂身体方向是否有全身比例与服装结构依据；
- 发型、发饰、服装和配饰前后结构是否可见；
- 精确手部叙事是否有手型、尺寸、左右手分工和道具接触依据；
- 污染、伤损、湿水、变装等状态是否有进程依据；
- 场景正反方向、关键局部和时间状态是否有布局依据；
- 核心道具结构、页面、开合、破损、燃烧或阶段变化是否有依据；
- 每项资产是否有必要性证据和实际使用Shot；
- 是否存在只为显得专业、没有镜头使用的冗余资产。

缺少任何实际镜头所需依据，资产覆盖不得PASS。

## 硬性计数

以下数量必须相等：

```text
Shot总数
镜头制作卡数量
有可见画面描述的Shot数量
有项目视觉策略引用的Shot数量
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
- 每个资产有必要性证据和使用Shot；
- 镜头表、CF表、图片Prompt和视频Prompt编号一致。

## 内容完整性

每个Shot必须有：

- narrative_purpose；
- visual_description；
- project_visual_strategy_reference；
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
- 结尾表演状态是否写入End CF和下一镜开始状态；
- 变化是否符合当前项目视觉策略，而不是模型随机换风格。

## 连续性

逐对检查：

- 人物身份、比例、发型和服装结构；
- 人物位置、朝向、视线；
- 左右手、道具和接触；
- 动作完成百分比；
- 污染、伤损、湿水、变装等状态进程；
- 表演强度、呼吸、嘴、肩膀、手指和重心；
- 屏幕方向与轴线；
- 场景地标和反向空间；
- 光源方向、白平衡、曝光；
- 色彩与材质进程；
- 声音和剪辑连接。

## Prompt一致性

Shot、CF、图片Prompt和视频Prompt不能在剧本事实、项目视觉策略、动作、表演、情绪强度、机位、运镜、焦点、灯光和尾态上互相矛盾。

## 结果

```yaml
status: PASS | REPAIR
narrative_lock_preserved:
project_visual_strategy_scope:
project_visual_strategy_conformance:
asset_angle_interaction_state_coverage:
shot_count:
coverage_ratio:
missing_fields: []
missing_asset_coverage: []
redundant_assets: []
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
