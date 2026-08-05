# Temporal Visual Orchestration Integration Gate V4.5

## 目的

控制`temporal-visual-orchestration.md`何时进入正式制作流程，避免因为一个参考项目就把实验性结论写成所有项目的硬规则；同时在设计整个Skill时持续检查现有视频Prompt能否承接剧情、动作、人物状态、空间和镜头关系的连续性。

核心原则：

> 现有视频Prompt是基线，不是不可修改的冻结层。能够保证剧情与镜头连续时保持不变；不能完整传递已经成立的导演和连续性设计时，才做有证据的最小修改。

## 一、状态

```yaml
module_status: EXPERIMENTAL_CORE_CANDIDATE
prompt_layer_status: CONDITIONAL_CONTINUITY_REVIEW
prompt_default_action: KEEP_CURRENT_BASELINE
current_validation:
  uploaded_reference_case: 1
  synthetic_cross_project_cases: 5
  internal_full_pipeline_benchmarks: 1
  externally_generated_benchmarks: 0
  real_cross_project_cases_required_before_hard_gate: 3
```

已完成内部完整流程基准：

- `benchmarks/temporal-orchestration-benchmark-001-slow-one-second.md`；
- `evals/temporal-orchestration-benchmark-001-report.md`。

该基准验证了同一现实主义项目内可以根据不同Shot切换摄影机、环境、灯光和声音关系，但尚未通过外部视频生成验证。

当前模块可以用于：

- 条件化导演规划；
- 视觉序列、梦境、MV、抽象段落和多系统运动镜头；
- 诊断人物、环境、摄影机、灯光和声音各自随机运动的问题；
- Shot级和Sequence级镜头关系设计；
- 检查现有视频Prompt是否完整传递剧情连续和镜头设计；
- 生成测试和横向压力测试。

当前模块暂不应：

- 成为所有Shot必须完整填写的硬字段；
- 用单一参考项目决定默认时序；
- 把某一种耦合关系写进全局视觉策略；
- 因字段完整而让简单镜头过度设计；
- 因为新增了导演关系字段，就自动重写所有视频Prompt；
- 未检查连续性风险便一律保留或一律修改现有Prompt；
- 为了理论完整而改变已经有效的镜头描述方法。

## 二、当前接入方式

### 条件启用

出现以下任一条件时读取完整模块：

- 同镜头两个以上系统明显变化；
- 用户强调画面流畅融合、人物与背景统一、材质和空间共同变化；
- 当前段落为`VISUAL_SEQUENCE_DRIVEN`或`HYBRID`；
- 相邻镜头需要形状、运动、节奏、声音、语义或情绪接力；
- 实测出现随机独立运动、自动跟随、无原因灯光变化或无意义背景动态；
- 当前视频Prompt可能遗漏剧情状态、动作尾态或下一镜继承关系。

### 简化启用

普通叙事镜头只检查：

- 当前镜头的主要剧情任务；
- 人物在镜头前后知道什么、决定什么、完成什么；
- 主导系统与摄影机角色；
- 环境和灯光是否变化以及为什么；
- 初始状态、主要变化和结束状态；
- 结束状态是否能无重置地进入下一镜。

### 不启用完整块

- 静态资产板；
- 纯结构参考图；
- 没有时间变化的单张图片；
- 简单字幕、纯后期或无需生成的视频段落。

## 三、剧情与镜头连续性审查

设计每个项目和序列时，先审查现有视频Prompt是否覆盖以下内容：

```yaml
continuity_support_audit:
  narrative_causality:
  event_order:
  character_knowledge_progression:
  character_intention_and_choice:
  action_phase_progression:
  pose_gaze_hand_and_contact_state:
  prop_state_and_ownership:
  costume_damage_wetness_and_other_accumulation:
  scene_geography_and_landmarks:
  screen_direction_and_axis:
  camera_start_end_and_cut_reason:
  lighting_weather_and_time_state:
  emotional_intensity_and_residual_state:
  sound_lead_bridge_decay_or_withhold:
  end_frame_to_next_start_inheritance:
```

检查重点不是让相邻镜头看起来颜色相似，而是确认：

- 上一镜发生的事情没有在下一镜被重置；
- 人物不会忘记已经知道的信息；
- 道具、伤损、湿水、服装和空间状态持续累积；
- 动作准备、接触、进行、完成和完成后残留顺序正确；
- 镜头切换改变观看角度，但不改变故事事实；
- 有意省略、跳切或断裂具有明确导演理由。

## 四、视频Prompt是否修改的决策顺序

### A｜现有Prompt已能承接

同时满足以下条件时保持现有写法：

- 剧情任务和信息揭示清楚；
- 人物、动作、道具、空间和情绪尾态已经写明；
- 首尾帧和下一镜继承成立；
- 摄影、灯光、表演和环境关系没有互相冲突；
- 没有为了单镜效果牺牲前后剧情。

结果：

```yaml
prompt_decision: KEEP_UNCHANGED
```

### B｜问题来自镜头设计或连续性设计

例如：

- 一个镜头承担过多动作和信息；
- 机位本身看不清关键动作；
- 首尾帧构图不具备继承条件；
- 下一镜轴线、视线或道具状态设计错误；
- 剧情缺少中间动作或状态过渡。

先修改Shot、CF、镜头数量、空间设计或连续性计划，不通过增加Prompt文字掩盖设计问题。

结果：

```yaml
prompt_decision: KEEP_COMPILER_REPAIR_DESIGN
```

### C｜导演设计成立，但现有Prompt没有传递关键连续关系

例如：

- Prompt只写了当前动作，没有写上一镜尾态；
- 没有说明人物在什么状态下继续动作；
- 摄影机运动与人物动作的先后关系缺失；
- 道具和手部接触在镜头间被重置；
- 灯光、环境或声音在下一镜无原因重新开始；
- 结束帧合同存在，但没有进入生成Prompt。

此时允许修改视频Prompt，但优先采用当前项目或当前镜头的局部补丁，不立即升级为全局规则。

结果：

```yaml
prompt_decision: LOCAL_CONTINUITY_PATCH
```

### D｜相同结构性问题跨项目重复出现

只有多个类型明显不同的项目都出现同一种Prompt传递缺口，才考虑修改核心`video-prompt-compiler.md`。

结果：

```yaml
prompt_decision: CORE_COMPILER_CANDIDATE
```

### E｜问题来自平台或模型能力

例如：

- 多对象持续漂移；
- 不支持准确首尾帧；
- 无法执行复杂物理动作；
- 摄影机运动与人物动作同时生成不稳定；
- 长Prompt导致平台忽略后半段。

优先使用拆镜、抽尾帧续拍、首尾帧、分层生成、后期或平台适配，不把模型限制误写成导演通用规则。

结果：

```yaml
prompt_decision: GENERATION_METHOD_ADAPTATION
```

## 五、修改视频Prompt时必须保留的镜头设计

无论局部修改还是未来调整核心编译器，都不能牺牲已经成立的导演和镜头设计。以下内容必须保留：

- `DIRECTOR_INTENT`与观众位置；
- Shot场景功能和主要剧情任务；
- 构图、景别、主体位置、视觉路径和前中后景；
- 摄影机机位、焦段感、运动起止、幅度和终点；
- 逐镜灯光合同、真实光源、照明区域和阴影策略；
- 人物目标、表演、微表情、呼吸、重心和手部动作；
- 背景职责、空间大形、环境物理和材质差异；
- 动作起势、接触、发展、峰值、收束和结果；
- 首帧保护、结束帧合同和下一镜继承；
- 与前后剧情有关的人物知识、道具状态和累积变化；
- 需要详细控制时允许长Prompt，但每句话必须具有可见或可执行作用；
- 不压缩成简单动作摘要，也不靠重复形容词增加长度。

允许根据连续性需要修改的主要范围是：

- 上一镜尾态如何进入当前镜头；
- 谁先、谁后、谁保持或对抗的表达顺序；
- 不同系统之间的响应延迟和峰值关系；
- 人物知识、动作阶段、道具接触和情绪残留；
- 当前镜头的精确结束状态；
- 下一镜的继承通道和禁止重置项；
- 针对模型误读的局部负面约束；
- 必要时拆镜、首尾帧、抽尾帧续拍或分层生成。

## 六、升级为正式硬门禁的条件

必须同时满足：

1. 至少三个真实且类型差异明显的项目完成测试；
2. 每个项目形成`test_learning_report`；
3. 没有把案例具体手法写成默认；
4. 能在叙事、悬疑、喜剧、动作、抽象或广告中得到不同合法答案；
5. 与摄影、灯光、表演、连续性和现有视频Prompt编译器没有字段冲突；
6. 简单镜头可以简化，不因模块增加而过度复杂；
7. `temporal-visual-orchestration-check.md`能够发现真实失败而不是只检查填表；
8. 至少完成一轮外部视频生成验证；
9. 若提出核心视频Prompt修改，必须有跨项目重复失败证据和明确归因；
10. 修改后仍完整保留镜头设计和剧情连续性要求。

满足后再考虑修改：

- `SKILL.md`全流程必读列表；
- `post-script-production.md`正式步骤；
- `shot-production-card.md`强制字段；
- `full-package-integrity-check.md`硬性计数；
- `full-creation-package.md`最终交付结构；
- `video-prompt-compiler.md`的局部连续性编译规则。

## 七、当前实验工作流

```text
用户参考或当前项目
→ test-learning-abstraction-protocol
→ 完成导演、Shot、CF和连续性设计
→ 审查现有视频Prompt是否能承接剧情与镜头关系
→ 能承接：保持现有Prompt
→ 不能承接：先区分设计、Prompt、资产、平台或模型问题
→ 必要时做项目级最小Prompt补丁
→ 生成真实视频测试
→ 形成test_learning_report
→ 多项目横向汇总
→ 决定是否需要核心编译器修改
```

没有额外真实参考时，可以先执行内部完整流程基准，但其结果只能记为`DESIGN_PASS_EXTERNAL_GENERATION_PENDING`，不能计入真实跨项目案例数量。

## 八、防止过度膨胀

新增字段必须证明它控制了以下至少一项：

- 剧情因果和人物认知；
- 可见先后关系；
- 主次与注意力；
- 动作、道具和人物状态累积；
- 摄影、灯光、环境或声音的角色；
- 峰值和结束状态；
- 跨镜头连续或有意断裂。

只重复原有动作、摄影、灯光或表演描述的字段应删除或合并。一次项目的局部Prompt补丁不得自动升级为核心规则。

## 九、当前结论

现阶段将本模块保留为“可调用、可测试、尚未全局强制”的导演层候选。现有视频Prompt保持默认基线，但每个项目都要接受剧情与镜头连续性审查；审查通过便不改，发现真实传递缺口时再做最小、可归因、保留镜头设计的修改。

当前已通过：

- 单一外部参考的案例抽象；
- 五类合成横向压力测试；
- 一个完整现实主义项目的设计态端到端基准。

当前仍缺：

- 外部生成后的镜头执行验证；
- 两个以上差异明显的真实项目；
- 当前视频Prompt是否会造成剧情不连贯的真实证据；
- 是否存在需要升级到核心编译器的跨项目共性缺口。