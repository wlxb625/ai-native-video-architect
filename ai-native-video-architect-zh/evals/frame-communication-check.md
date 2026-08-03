# Frame Communication Check V4.5

## 用途

本检查用于评估Shot与Control Frame是否真正把场景功能、动作、关系、焦点、视觉层级、材质和画幅转化为可读画面。它与`full-package-integrity-check.md`并行，不替代原有剧本、资产、连续性和Prompt完整性检查。

## 1. 场景功能

每个正式Shot必须：

- 有且只有一个主场景功能；
- 次功能为空或最多一个；
- 有本镜事件、人物状态或信息释放作为证据；
- 明确观众即时体验、延迟体验与信息/情绪/奇观优先级；
- 让功能进入摄影、灯光、表演、背景与Prompt；
- 不改变`NARRATIVE_LOCK`；
- 发现功能冲突时拆镜或重新排序。

标签只存在于表格、没有进入执行时，判定`REPAIR`。

## 2. 视觉层级与密度

每个生成型CF检查：

- 1—4个核心大形是否明确；
- 是否存在承担结构、秩序或叙事职责的中尺度结构；
- 微小细节是否集中在面部、手部、道具或局部状态；
- 是否有主体清洁区和视觉休息区；
- 前中远景细节、锐度与对比是否衰减；
- 主要流动元素、辅助环境元素、微粒和颗粒策略是否受控。

华丽不能主要依赖密集金粉、花瓣、羽毛、碎片和满屏光点；干净也不能删除中尺度结构，导致画面空洞。两种情况都判定`REPAIR`。

## 3. 焦点统一

检查叙事动作区、局部最亮区、最高局部对比区、主要高饱和区、最高锐度区和世界变化起点是否共同服务主场景功能。

以下情况判定`REPAIR`：

- 核心动作在暗处，最亮处位于无关背景；
- 唯一高饱和色用于无关装饰；
- 背景奇观比人物事件更清楚；
- 世界变化看不出起点；
- 焦点与景深使关键表演或道具不可读。

故意错开时必须有揭示、误导或观看关系理由。

## 4. 缩略图可读性

按手机短视频或封面观看距离检查：

- 主大形是否可读；
- 主体或人物关系是否可读；
- 关键动作与核心道具是否可读；
- 因果是否可读；
- 是否依赖放大后的微表情、细线、裂纹或小字才能理解。

不要求所有微表情在缩略图中清楚，但主场景功能不能被误读。

## 5. 动作阶段语义

每个关键动作必须明确属于：

```text
PREPARATION / CONTACT / TRANSITION / COMPLETION / AFTERMATH_RESIDUE
```

检查接触状态、重量或力量承担者、手掌与手指方向、手腕与肘部趋势、身体重心和可见结果。

必须防止：

- 松手被看成伸手接取；
- 剪断被看成激活或连接；
- 推开被看成扶住；
- 递出与接取方向相反；
- 离开被看成返回；
- 安慰被看成阻拦。

只写“手在哪里”而没有动作阶段、方向与结果，判定`REPAIR`。

## 6. 关系残留

适用于情绪共鸣、治愈和重要人物关系镜头。检查：

- 刚刚发生的接触或共同动作是否保留残留姿态；
- 人物距离是否符合当前时间点；
- 视线、手指、呼吸或道具是否保留关系余温；
- 是否为了纠正动作误读，把人物拉得过远或完全切断联系；
- 是否存在至少一个非自愿情绪泄漏和生活历史痕迹。

动作阶段正确但关系残留完全消失时，判定`REPAIR`。

## 7. 道具自然化

检查关键道具的持有者、承重者、接触、重力、褶皱、变形和使用痕迹。若道具过度居中、正面、完整、鲜亮、排列完美，导致商品广告或公益宣传感，判定`REPAIR`。

## 8. 原创视觉语法

检查：

- 是否只删除常见符号，却没有建立替代结构；
- 大形为何存在、如何连接和受力；
- 重复结构是否有变化；
- 环境变化是否与人物行动有因果；
- 是否回落成通用莲花、光环、仙山、传送门、巨兽、帆片、工业吊具或抽象白片模板。

出现模板风险时，应补充正向形状、结构、受力和材质规则，不能只增加负面词。

## 9. 材质语义漂移

检查目标材质是否被模型替换：

- 薄瓷变成冰、玻璃或水晶；
- 黑漆变成水面、镜子或湿柏油；
- 螺钿变成霓虹亮片；
- 旧金变成廉价亮金或发光塑料；
- 薄纱变成烟雾或塑料膜；
- 丝绸变成橡胶、皮革或亮片布。

正向Prompt必须包含哑光程度、反射粗糙度、透明度、重量、边缘、受光、重力和使用痕迹等可观察属性。

## 10. 海报化与摆拍

根据镜头目的检查无意发生的：

- 人物居中、正面、直视镜头；
- 背景形成标准光环；
- 服装左右完整展开；
- 所有大形完整收进画框；
- 动作被姿势展示替代；
- 道具变成商品陈列；
- 现实主义镜头像公益广告或宣传照。

海报或广告任务可以有意使用，但电影事件帧无意海报化时判定`REPAIR`。

## 11. 画幅执行

检查当前指定比例、横竖方向、外部平台实际比例参数、人物占比、负空间、主要动势与不可裁切区。横竖比例改变后必须重建构图，不能只替换Prompt里的比例文字，也不能把本轮测试比例写成Skill默认。

## 12. 结果

```yaml
status: PASS | REPAIR
scene_function_coverage:
scene_function_execution_consistency:
function_conflicts: []
visual_hierarchy_coverage:
structured_richness:
visual_cleanliness:
macro_shape_failures: []
medium_structure_voids: []
micro_detail_overload_frames: []
particle_overload_frames: []
uniform_sharpness_frames: []
subject_contamination_frames: []
focal_alignment_coverage:
focal_misalignment_frames: []
thumbnail_readability_coverage:
thumbnail_misread_frames: []
gesture_semantics_coverage:
action_phase_misread_frames: []
relationship_residue_coverage:
relationship_residue_loss_frames: []
prop_naturalism_coverage:
commercialized_prop_frames: []
original_visual_grammar_coverage:
generic_visual_template_frames: []
material_semantic_drift_coverage:
material_drift_frames: []
posterization_control:
unintended_poster_frames: []
aspect_ratio_conformance:
aspect_ratio_conflicts: []
repair_actions: []
```

只有原有完整性检查通过，并且本检查为`PASS`，才能标记`FRAME_COMMUNICATION_PASS`。