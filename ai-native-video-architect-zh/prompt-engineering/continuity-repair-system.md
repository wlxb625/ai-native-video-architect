# Continuity and Repair System

## 目标

在视频Prompt生成前保护剧情与镜头连续性，并在真实生成后解决上下视频不连贯、多角度穿帮、人物变脸、场景重建、道具消失、手部错误、色调跳变和画质问题。

本系统不是只在出错后调用。连续Shot进入Prompt编译前，必须先完成状态传递，避免每个镜头被写成彼此独立、重新开始的小片段。

## 生成前连续性传递

每个Shot生成Prompt前，读取上一镜精确尾态，并只推进本镜应发生的新变化。

```yaml
continuity_ledger:
  previous_shot_id:
  inherited_story_facts:
  character_knowledge:
  character_intention:
  action_phase:
  character_positions_and_orientations:
  pose_gaze_breath_and_weight:
  hands_contacts_and_ownership:
  prop_states:
  costume_damage_wetness_and_accumulation:
  scene_geography_and_landmarks:
  screen_direction_and_axis:
  camera_end_state:
  lighting_weather_and_time_state:
  emotional_residual_state:
  unresolved_action_or_question:
  facts_that_must_not_reset: []
```

当前镜头必须输出：

```yaml
continuity_handoff:
  inherited_state_used:
  new_change_completed_in_this_shot:
  exact_story_result:
  exact_character_end_state:
  exact_prop_and_contact_state:
  exact_space_camera_and_light_state:
  emotional_residual_state:
  next_shot_required_start_state:
```

这些字段可以保留在制作卡和内部记录中，不要求机械复制为最终Prompt标题；但其内容必须进入最终Prompt的首帧保护、动作起点、结束帧合同和下一镜继承。

## 剧情状态不得重置

连续镜头必须保证：

- 人物不会忘记已经知道的信息；
- 已经作出的决定不会无原因重新犹豫或重新执行；
- 动作按准备、接触、进行、完成、完成后残留继续推进；
- 已经拿起、放下、打开、破坏或交付的道具不会恢复旧状态；
- 伤损、污渍、湿水、服装变化和体力消耗持续累积；
- 人物站位、朝向、视线、手部接触和重心不会无原因回到初始值；
- 场景入口出口、地标、轴线、屏幕方向和光源位置保持可理解；
- 情绪从上一镜尾态继续，不在每镜重新从同一强度开始；
- 上一镜尾态能够直接进入下一镜首态，或明确说明省略、跳切和有意断裂。

可以改变摄影角度、景别和构图，不能因此改变故事事实。

## 抽尾帧续拍

适用于：

- 同一动作未完成；
- 人物继续行走、转身或说话；
- 运镜继续推进；
- 同一场景需要接近一镜到底。

步骤：

1. 导出上一段；
2. 提取最后一个稳定帧，不使用运动模糊或形变帧；
3. 将其作为下一段唯一首帧；
4. 保持人物位置、姿势、服装、道具、背景、光线、色调和机位；
5. 读取`continuity_ledger`，只描述剩余动作，不重新介绍或重启已完成动作；
6. 指定下一段结束状态和继续传出的剧情状态。

## 硬切新镜头

适用于换景别、换机位、换角度、切人物反应或道具特写。

新首帧必须基于上一镜结尾记录：

```yaml
hard_cut_anchor:
  inherited_story_facts:
  character_knowledge_and_intention:
  character_positions:
  body_orientations:
  screen_direction:
  action_completion_percent:
  gaze:
  prop_state_and_hand:
  costume_damage_wetness_and_accumulation:
  background_landmarks:
  light_direction:
  color_state:
  emotional_residual_state:
  next_action_space:
```

可以改变观看角度，不能改变空间事实、人物知识、动作完成度和累积状态。

## 多角度防穿帮

- 第一个空间锚定镜头优先全景或中远景；
- 画面同时保留人物、地面、背景建筑和关键道具；
- 角色背后有可识别地标；
- 多人场景先锁定站位图；
- 换角度时写“只改变摄影机，不改变站位、动作完成度和布局”；
- 避免连续极近特写后突然切到没有空间依据的新角度；
- 正反打必须保持视线方向、道具归属、说话顺序和人物已知信息一致。

## 人物变脸

不要继续往镜头Prompt中堆外貌词。返回面部身份资产：

- 使用批准正面图；
- 图生图修复面部；
- 保留发际线和骨相；
- 重新输出单帧；
- 再做视频。

## 服装漂移

返回服装状态板，锁定领口、袖口、颜色、层次和固定污渍。使用图生图只修服装区域。

服装已有湿水、破损、血迹、灰尘或变装进程时，必须继承当前阶段，不能返回初始洁净状态。

## 场景漂移

- 回到无人物空镜；
- 使用主布局和正确机位；
- 角色与场景分层或共同引用；
- 减少自由背景描述；
- 硬切镜头保留背景地标；
- 检查入口出口、人物方位、屏幕方向、天气、时间和世界光源是否与上一镜一致。

## 道具变形

- 使用道具三视图和尺寸；
- 加入与手掌或身体的比例参考；
- 使用交互板；
- 将道具单独生成后合成；
- 状态变化使用首尾帧；
- 同时检查道具当前归属、开合、破损、消耗、湿水和与手部接触状态。

## 手部错误

优先局部重绘或切到更稳定景别。不要为修手重生成整张已稳定画面。

修复手部时不得改变已经成立的道具归属、接触关系、动作阶段和下一镜所需尾态。

## 图生图修改模板原则

```text
保持原图构图、人物、背景、光线、色调和质感不变。
只修改指定区域：原内容 → 新内容。
新内容的光线、透视、材质和边缘必须与原图融合。
其他区域零变化。
```

## 局部标记法

用户可上传带红框、箭头或蒙版的图。Prompt必须说明只处理标记区域。完成后去除标记，不改变未标记区域。

## 夜景降噪

只修复：脏灰、噪点、压缩痕迹、彩色斑块、模糊边缘和低质量伪影。保持构图、人物、动作、场景、色调和光线不变。

## 4K增强

只增强毛孔、发丝、睫毛、布料、缝线和材质边缘，扩展动态范围。禁止重绘面孔、改变姿势、重新布光、改变白平衡和颜色关系。

## 台词错误

- 单镜只保留一个说话主体；
- 面部和嘴部清楚；
- 一次只说一句；
- 写明逐字台词和语气；
- 禁止增删改词；
- 其他人无台词；
- 背景音乐不盖人声；
- 复杂对话分人分句生成；
- 下一镜必须继承谁已经说过什么、谁听见了什么以及当前反应阶段。

## 连续性失败判定

以下任一情况不能只当作画面小瑕疵：

- 每镜重新介绍人物和场景，像独立短片；
- 已完成动作在下一镜重新开始；
- 人物知识、目的、关系或情绪无原因回退；
- 道具、伤损、服装、湿水或接触状态被重置；
- 镜头只保持相似颜色，却丢失事件因果；
- 为追求单镜奇观改变上一镜已经成立的事实；
- 上一镜结束帧合同没有进入下一镜首态。

发生时先回到Shot卡和连续性台账确认设计，再决定局部修复、重做控制帧或重做单镜，不直接推翻全片视觉策略。

## 修复优先级

```text
修正连续性台账或Shot继承关系
→ 局部修复
→ 图生图修复单帧
→ 重做单个首帧或尾帧
→ 重做单个视频镜头
→ 回到对应资产
→ 最后才回退场景或视觉圣经
```

不得因为一个手部错误推翻全部资产和分镜，也不得用后期硬掩盖已经破坏剧情因果的状态重置。
