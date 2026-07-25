# Continuity Core

## 职责

维护事实、人物知识、原话、文件、时间、空间、视角、现实层级，以及AI制作中的角色、服装、场景、道具、光线、镜头帧和版本状态。

连续性不只是“人物长得一样”，而是：

> 上一镜已经发生了什么，下一镜有权继承什么，哪些内容绝对不能被模型重新设计。

## 叙事台账

每场记录：

```yaml
story_continuity:
  confirmed_facts: []
  claims: []
  beliefs: []
  knowledge_source: []
  certainty:
  documents: []
  location:
  time:
  reality_layer:
  entry_state:
  exit_state:
```

人物不能因为观众知道就自动知道。生成、预测、发送、接收、执行和验证是不同状态。

## 生产连续性台账

```yaml
production_continuity:
  shot_id:
  character_ids: []
  face_asset:
  hair_asset:
  costume_state:
  pose_state:
  prop_states: []
  prop_hands: {}
  environment_state:
  environment_angle:
  character_positions: []
  screen_direction:
  eyelines: []
  camera_axis:
  light_direction:
  time_and_weather:
  start_frame:
  end_frame:
  inherited_by: []
  forbidden_drift: []
```

## 角色连续性

追踪：

- 面部身份与年龄；
- 发型结构和发饰位置；
- 身高、体型和身体比例；
- 服装状态ID；
- 污渍、伤痕、湿度和损伤；
- 左右手职责；
- 持物方式；
- 动作习惯和情绪基线。

服装或人物状态发生变化时，创建新状态ID，不覆盖旧版本。

## 场景连续性

追踪：

- 空间主布局；
- 门、窗、柱、桌、道路和楼梯；
- 固定地标；
- 人物进入和离开路线；
- 道具默认位置；
- 轴线和屏幕方向；
- 主光方向、时间、天气和空气状态；
- 场景状态版本。

换机位只能改变观看角度，不能让背景成为另一个地点。

## 道具连续性

每件核心道具记录：

```yaml
prop_continuity:
  prop_id:
  current_state:
  holder:
  hand:
  orientation:
  location:
  produced_by_shot:
  inherited_by_shots: []
  allowed_changes: []
  forbidden_changes: []
```

特别检查：

- 左右手突然交换；
- 道具尺寸变化；
- 独特标记消失；
- 道具在未发生动作时自动修复、变脏或破损；
- 道具从人物手中无原因回到场景默认位置。

## 首帧与尾帧

每个正式镜头至少记录：

- `input_state`：首帧之前已经成立的状态；
- `start_frame`：视频可见的第一帧；
- `output_state`：本镜真正改变了什么；
- `end_frame`：可用于续拍或硬切校验的最后稳定画面；
- `next_dependency`：下一镜必须继承什么。

尾帧续拍时，下一段首帧不得偏离上一段最终稳定帧。

## 硬切连续性

硬切允许改变景别和机位，但必须记录：

- 切点动作节点；
- 动作完成百分比；
- 人物位置、朝向和视线；
- 道具在哪只手；
- 背景地标；
- 主光方向；
- 下一动作所需空间。

## 特殊结构

不可靠叙述、梦境、记忆、循环和多现实必须定义：

- 主观范围；
- 信息互通规则；
- 稳定锚点；
- 允许漂移项；
- 禁止漂移项；
- 观众最终能确认的事实。

有意的不连续必须是设计规则，不能用来掩盖换脸、换衣、空间错误和道具漂移。

## 回归顺序

1. 事实与人物知识；
2. 角色身份；
3. 服装和伤痕状态；
4. 道具状态、位置和左右手；
5. 场景布局与地标；
6. 人物屏幕方向、轴线和视线；
7. 光线、天气和色调；
8. 首尾帧和动作进度；
9. 声音是否提前或延后改变事实。
