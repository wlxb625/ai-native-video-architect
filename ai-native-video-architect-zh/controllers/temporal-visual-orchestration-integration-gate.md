# Temporal Visual Orchestration Integration Gate V4.5

## 目的

控制`temporal-visual-orchestration.md`何时参与项目制作，并确保Skill最终生成的各镜头提示词在剧情、人物状态、动作、道具、空间和情绪上能够连续衔接。

核心原则：

> 不要求为了新模块重写现有提示词写法；要求生成出来的提示词不能把每个镜头写成彼此独立、状态重置的小片段。

## 一、状态

```yaml
module_status: EXPERIMENTAL_CORE_CANDIDATE
prompt_style_policy: KEEP_EXISTING_WHEN_EFFECTIVE
generated_prompt_continuity: REQUIRED
current_validation:
  uploaded_reference_case: 1
  synthetic_cross_project_cases: 5
  internal_full_pipeline_benchmarks: 1
  externally_generated_benchmarks: 0
```

本模块目前用于导演设计、镜头关系设计和提示词生成前的连续性约束，尚不作为所有Shot必须完整填写的硬表格。

## 二、启用范围

完整启用：

- 同镜头两个以上系统明显变化；
- 视觉序列、梦境、MV、奇观、动作高潮或复杂转场；
- 人物、环境、摄影机、灯光、声音之间存在明确先后、响应、对抗或脱节；
- 相邻镜头依赖动作、视线、道具、空间、声音、情绪或视觉母题接力；
- 当前项目容易出现镜头漂亮但剧情断开的风险。

普通叙事镜头简化启用，只检查前态、当前变化、尾态和下一镜继承。

## 三、提示词生成连续性合同

Skill生成任何Shot的视频提示词前，必须读取：

```yaml
prompt_continuity_input:
  previous_shot_end_state:
  current_story_task:
  current_character_knowledge:
  current_character_intention:
  current_action_phase:
  current_pose_gaze_hand_contact:
  current_prop_state_and_ownership:
  current_costume_damage_wetness_or_accumulation:
  current_scene_geography:
  current_screen_direction_and_axis:
  current_camera_start_relation:
  current_light_weather_time_state:
  current_emotional_residual_state:
  next_shot_required_start_state:
```

然后输出：

```yaml
prompt_continuity_output:
  inherited_state:
  new_change_in_this_shot:
  facts_that_must_not_reset: []
  exact_end_state:
  next_shot_handoff: []
```

这些字段不要求机械显示在最终提示词中，但必须被转译为可执行内容。

## 四、剧情连续性要求

生成的连续Shot提示词必须保证：

- 人物不会忘记上一镜已经知道的信息；
- 已经完成的决定不会无原因重新犹豫或重新执行；
- 动作按准备、接触、进行、完成、完成后残留自然推进；
- 人物姿势、视线、手部、呼吸、重心和接触状态不会无原因重置；
- 道具位置、归属、开合、破损、湿水和消耗状态持续累积；
- 伤口、污渍、服装变化和环境影响不会下一镜自动消失；
- 场景地理、入口出口、人物方位、屏幕方向和轴线保持可理解；
- 时间、天气、光源和亮度变化有原因；
- 情绪从上一镜尾态继续，而不是每镜从同一强度重新开始；
- 上一镜结束状态能够自然进入下一镜开始状态。

镜头可以跳切、省略、错位或故意断裂，但必须是导演选择，不能是提示词遗漏造成的事故。

## 五、镜头设计必须保留

为了连续，不能把视频提示词压缩成简单剧情摘要。最终提示词仍应保留当前项目需要的：

- 导演意图和观众位置；
- Shot场景功能和剧情任务；
- 构图、景别、主体位置、视觉路径和前中后景；
- 机位、焦段感、摄影机运动起止和终点；
- 灯光来源、照明区域、阴影与环境关系；
- 人物表演、视线、呼吸、重心和手部动作；
- 背景职责、空间大形、材质和环境物理；
- 动作发展、峰值、收束和结果；
- 首帧保护、结束帧合同与下一镜继承；
- 足够详细且具有可见控制作用的描述。

连续性是增加镜头之间的逻辑，不是删除镜头内部的设计。

## 六、提示词生成流程

```text
读取剧本与NARRATIVE_LOCK
→ 确认当前Shot的场景功能和导演意图
→ 读取上一镜精确尾态
→ 设计当前镜头的摄影、灯光、表演、环境和动作
→ 决定谁主导、谁响应、谁保持或对抗
→ 确认当前镜头只推进本镜应发生的变化
→ 写出精确尾态
→ 检查能否无重置进入下一镜
→ 生成最终视频提示词
```

现有提示词风格和详细度可以继续使用，只要完成以上连续性传递。

## 七、硬失败

- 每个镜头都重新介绍人物和环境，像独立短片；
- 人物知识、目的或情绪无原因回到前一状态；
- 道具、伤损、服装、湿水或接触状态被重置；
- 上一镜动作已经完成，下一镜又从准备阶段开始；
- 人物位置、屏幕方向、道路或房间布局突然变化；
- 灯光、天气或时间无原因重新建立；
- 镜头切换只保持相似色彩，却丢失剧情因果；
- 为追求单镜奇观而破坏前后剧情；
- 提示词写了很多镜头细节，却没有上一镜尾态和下一镜交接。

## 八、当前边界

- 不把参考视频的具体运动、材质、灯光或摄影机顺序设为默认；
- 不新增独立Skill；
- 不改变`NARRATIVE_LOCK`；
- 不要求所有镜头复杂运动；
- 不因为强调连续性就牺牲构图、摄影、灯光、表演和画面设计；
- 当前仍需通过真实连续镜头生成验证执行效果。
