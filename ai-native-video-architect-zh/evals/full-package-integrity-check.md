# Full Package Integrity Check V4.5

## 用途

在交付完整制作提示词包前，检查`NARRATIVE_LOCK`、项目视觉策略、资产、Shot、`CONTINUITY_LEDGER`、CF、图片Prompt、视频Prompt、导演执行、画面沟通和可生成性是否形成同一闭环。

本检查保留V4.4的完整制作能力，并与`evals/frame-communication-check.md`并行执行。它只核验当前制作包，不重新创作第二套策略、镜头或连续状态。

## 一、NARRATIVE_LOCK

检查是否保留：

- 主角或主体；
- 核心关系与处境；
- 世界规则或主要机制；
- 关键选择；
- 高潮行动者与不可逆变化；
- 结尾及开放程度；
- 主题意义；
- 用户授权边界。

为了风格、资产、场景功能、生成便利或单镜奇观擅自改变上述事实，直接`REPAIR`。

## 二、项目视觉策略

完整项目必须有`PROJECT_VISUAL_STRATEGY`，并满足：

- `scope: PROJECT_ONLY`；
- 生成于`NARRATIVE_LOCK`之后；
- 引用当前剧本证据；
- 定义Style DNA、背景职责、视觉张力、原创视觉语法、视觉密度、清洁度、材质语义、画幅影响、连续性锚点、允许变化和禁止漂移；
- 资产、Shot、CF、图片Prompt和视频Prompt能够追溯到该策略；
- 镜头允许有叙事驱动差异，不机械相同；
- 没有把当前项目的配色、摄影、材质、表演温度、背景功能和画幅写成Skill默认。

单图或单镜任务只能使用局部视觉合同。

## 三、场景功能与导演执行

每个正式Shot必须：

- 有且只有一个主场景功能；
- 次功能为空或最多一个；
- 有剧本证据；
- 明确信息、情绪、奇观优先级和观众第一眼、第二眼、最终理解；
- 把功能传递到导演意图、摄影、灯光、表演、背景、CF和Prompt；
- 写明不得牺牲项和冲突/拆镜判定。

以下直接`REPAIR`：

- 功能标签只存在于Shot表；
- 一个短Shot有三个以上同权功能；
- 功能冲突却未拆镜；
- 为追求震撼、共鸣、反转或治愈改写剧情事实。

## 四、资产覆盖

逐项检查实际镜头是否有足够依据：

- 面部近景身份；
- 正面、严格侧面、背面、转身和离场背影；
- 全身、俯身、跪姿、走动和复杂身体方向；
- 发型、服装和配饰前后结构；
- 精确手部与道具交互；
- 污染、伤损、湿水、变装、体力等状态进程；
- 场景正反方向、关键局部、时间状态和世界光源；
- 道具结构、尺寸、页面、开合、破损、消耗和阶段变化；
- 每项资产的必要性、使用Shot与缺失风险。

缺少实际镜头所需依据不得`PASS`；没有Shot使用的冗余资产应删除。

## 五、唯一连续性台账

完整项目必须只有一个`CONTINUITY_LEDGER`。第一镜引用`PROJECT_INITIAL_STATE`，后续镜头引用上一镜唯一`End State ID`。

每个Shot必须具有：

```yaml
continuity_reference:
  ledger_id:
  source_end_state_id:
  inherited_facts_used:
  new_change_in_this_shot:
  current_end_state_id:
  next_shot_required_inheritance: []
```

台账至少覆盖：

- 人物知识、目的和决定；
- 动作阶段与完成度；
- 位置、朝向、姿态、视线、呼吸、重心、手部与接触；
- 道具状态与归属；
- 伤损、污渍、湿水、服装、体力与其他累积状态；
- 场景地理、地标、轴线与屏幕方向；
- 摄影、焦点、灯光、天气、时间与声音状态；
- 情绪和关系残留；
- 本镜新增变化与精确尾态。

禁止Shot卡、CF、图片Prompt、视频Prompt或最终模板建立竞争版本的`input_state / continuity_in / continuity_out`。

以下直接`REPAIR`：

- `source_end_state_id`不存在；
- 上一镜End State没有成为下一镜起态；
- Shot、CF和Prompt引用不同版本状态；
- 已完成动作重新开始；
- 人物忘记信息或恢复旧目的；
- 道具、伤损、湿水、服装、体力或接触状态被重置；
- 换机位后改变了空间事实；
- 情绪每镜从零重新起步；
- 只保持配色相似，却丢失剧情因果。

## 六、硬性计数

以下数量必须与适用Shot总数一致：

```text
镜头制作卡
可见画面描述
项目视觉策略引用
有效CONTINUITY_LEDGER条目
有效source_end_state_id
已登记current_end_state_id
主场景功能与剧本证据
导演意图
摄影方向
逐镜灯光方向
人物镜头的表演方向与情绪曲线
空镜的NON_CHARACTER_PERFORMANCE与环境节奏
动作阶段语义
适用关系镜头的关系残留
参考绑定
完整S10控制帧Prompt块
生成型Shot的图像来源
视频Prompt或POST_ONLY方案
风险与稳定备用
```

简单镜头可以不启用完整时空编排，但必须记录`REQUIRED / SIMPLIFIED / NOT_REQUIRED`及理由，不能以不启用为由省略导演、摄影、灯光、连续性或Prompt。

## 七、ID与绑定完整性

- 所有Scene、Shot、CF、Asset、Ledger Entry和End State ID唯一；
- 每个CF只属于一个Shot；
- 每个引用对象真实存在；
- Shot表、台账、CF表、图片Prompt、视频Prompt和参考矩阵编号一致；
- START CF对应台账起态；
- END CF或结束帧合同对应当前End State；
- Bridge CF不改变未授权剧情事实；
- 继承上一镜尾帧时写明CF、End State和备用方案。

短编号不能成为删字段或缩短Prompt的理由。

## 八、Shot内容完整性

每个Shot必须有：

- `narrative_purpose`；
- `visual_description`；
- `project_visual_strategy_reference`；
- `continuity_ledger_reference`；
- `source_end_state_id`；
- `new_change_in_this_shot`；
- `current_end_state_id`；
- `scene_function`及证据；
- `director_intent`；
- `camera_direction`；
- `lighting_direction`；
- `performance_direction`或`NON_CHARACTER_PERFORMANCE`；
- `emotion_curve`或`environment_rhythm`；
- `action_semantics`；
- `relationship_residue`或不适用原因；
- `reference_bindings`；
- `frame_source_mode`；
- `control_frames`；
- `generation_mode`；
- `image_prompt`或继承说明；
- `video_prompt`或`POST_ONLY`说明；
- `risk_and_fallback`。

时空视觉编排只在条件满足时完整填写，并只记录系统关系，不重复摄影、灯光、表演和台账参数。

## 九、S10控制帧与图片Prompt

每个需要生成CF的Shot必须完整实例化`templates/storyboard-frame-prompt-block.md`，至少检查：

- Shot、Scene、CF、类型、时间和时长；
- 镜头唯一任务、主次场景功能与观众阅读顺序；
- 项目视觉策略与参考资产职责；
- `ledger_id`、`represented_state_id`和上一镜End State；
- 帧来源与生成模式；
- 前中后景、背景职责、大形、方向、局部高潮与冻结运动痕迹；
- 核心大形、中尺度结构、细节集中区、主体清洁区、视觉休息区与衰减；
- 焦点、最亮区、最高对比、色彩锚点和世界变化起点；
- 动作阶段、接触、重量、手部趋势、可见结果与防误读线索；
- 适用时的关系残留和道具自然化；
- 人物表演或环境节奏；
- 构图、景别、焦段、机位、轴线和动作空间；
- 焦点、景深、曝光、白平衡、高光与暗部；
- 真实光源、世界位置、方向、软硬、色温、光比、照亮区域和阴影；
- 原创视觉语法、材质可观察属性和语义漂移反制；
- 缩略图可读性、海报化风险和画幅执行；
- 完整正向Prompt、针对性负面Prompt和输出规则；
- END CF或`TEXT_CONTRACT_ONLY`的精确尾态；
- 图生图、局部修复和稳定降级。

每个生成CF必须独立可复制：禁止公共视觉前缀、“同上”“沿用前面”“Prompt略”和只列资产ID。静态Prompt只能描述一个瞬间。

以下直接`REPAIR`：

- START CF不符合台账起态；
- END CF与当前End State不一致；
- 下一镜依赖准确尾态却无预生成尾帧或完整文字合同；
- Prompt缺少项目视觉、场景功能、背景、构图、表演、动作阶段、焦点曝光、灯光、材质、画幅或连续性；
- 负面Prompt是无针对性的万能词；
- 输出规则缺少比例、方向、不可裁切区、文字规则、优先级或文件名；
- 缺少局部修复与稳定备用。

## 十、V4.5画面沟通

必须通过`evals/frame-communication-check.md`：

### 视觉密度

- 华丽来自空间、结构、材质和光影，而不是随机碎屑；
- 画面不是所有区域同等复杂、锐利和装饰密集；
- 干净没有删除必要的中尺度结构；
- 面部、手部和核心道具不被背景污染。

### 焦点与缩略图

- 动作、最亮处、最高对比、色彩锚点、最高锐度和变化起点共同服务镜头任务；
- 目标观看距离下能读出主大形、主体关系、关键动作、道具和因果。

### 动作与关系

- 阶段、接触、重量、手部方向和结果一致；
- 不被误读为相反动作；
- 关系镜头同时保留动作准确和情绪余温。

### 原创、道具与材质

- 有正向替代结构，不只是禁止常见符号；
- 未回落为通用AI模板；
- 道具不被无意商品化或宣传化；
- 目标材质未被玻璃、冰、塑料或霓虹替代。

### 画幅

- 当前比例真实进入构图重建；
- Prompt与外部平台比例参数一致；
- 测试比例没有变成Skill默认。

## 十一、导演一致性

读取`evals/directing-coherence-check.md`和`evals/performance-direction-score.md`，检查：

- 情绪目标由可见表演实现；
- 观众位置由机位、距离、构图和揭示顺序实现；
- 摄影和灯光让关键表演与动作可读；
- 表演强度符合事件、时长和上一镜尾态；
- 灯光变化有真实光源或明确形式规则；
- 结束表演、动作阶段和关系残留进入当前End State；
- 时空编排只协调关系，没有与专业模块竞争；
- 所有变化符合当前项目视觉策略。

## 十二、视频Prompt一致性

每个生成型Shot的视频Prompt必须：

- 从台账起态开始；
- 保护首帧身份、美术、构图和光线；
- 只推进本镜唯一核心事件；
- 保留完整摄影、灯光、表演、环境和动作设计；
- 写清身体部位顺序、材质速度差、背景过程、摄影机起止和时间峰值；
- 抵达可见、可截图、可验证的当前End State；
- 把该End State交给下一镜；
- 具有针对身份、人体、动作、道具、空间、光色和状态重置的负面约束。

Shot、CF、图片Prompt和视频Prompt不能在剧情事实、项目策略、场景功能、动作阶段、关系残留、表演、机位、运镜、焦点、灯光、画幅和尾态上互相矛盾。

## 十三、制作包组成

完整制作包必须同时包含：

- 剧本与`NARRATIVE_LOCK`；
- `PROJECT_VISUAL_STRATEGY`；
- 资产覆盖矩阵与全部资产Prompt；
- 完整Shot总表与制作卡；
- 唯一`CONTINUITY_LEDGER`；
- 完整CF清单；
- 完整S10控制帧Prompt包；
- 完整S11视频Prompt包；
- 参考矩阵；
- 剪辑、声音与后期说明；
- 高风险备用与生成顺序。

CF清单不能替代控制帧Prompt，镜头摘要不能替代视频Prompt。最终的连续性表只能是台账的人类可读视图，不能成为第二事实源。

## 十四、结果

```yaml
status: PASS | REPAIR
narrative_lock_preserved:
project_visual_strategy_scope:
project_visual_strategy_conformance:
scene_function_coverage:
scene_function_execution_consistency:
asset_angle_interaction_state_coverage:
continuity_ledger_present:
continuity_ledger_single_source:
shot_count:
shot_card_coverage:
valid_source_end_state_coverage:
registered_current_end_state_coverage:
end_state_handoff_coverage:
frame_prompt_full_template_coverage:
standalone_frame_prompt_coverage:
action_semantics_coverage:
relationship_residue_coverage:
visual_hierarchy_coverage:
focal_alignment_coverage:
thumbnail_readability_coverage:
original_visual_grammar_coverage:
material_semantic_drift_coverage:
aspect_ratio_conformance:
end_frame_contract_coverage:
frame_prompt_repair_coverage:
missing_fields: []
missing_asset_coverage: []
redundant_assets: []
orphan_cf_ids: []
missing_cf_ids: []
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
repair_actions: []
```

只有本检查和`frame-communication-check.md`均为`PASS`，才能标记`PROMPT_PACKAGE_READY`。没有真实媒体时不得声称已通过实际样片验收。
