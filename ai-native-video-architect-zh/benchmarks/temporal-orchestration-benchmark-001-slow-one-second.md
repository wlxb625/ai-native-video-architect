# Temporal Visual Orchestration Benchmark 001｜《慢一秒》

## 定位

本文件是内部完整项目基准，不是项目模板，也不向核心Skill输入固定美学。它用于验证：同一现实主义项目中，不同Shot是否能根据叙事任务切换主导权、耦合方式、摄影机、灯光、环境和声音关系，同时保持整体风格、空间事实和情绪连续。

## 项目概览

- 片名：《慢一秒》
- 时长：约30秒
- 类型：当代现实主义 / 短时动作悬疑 / 克制情绪
- 画幅：16:9，仅为本测试参数
- 场景：雨夜城市路口
- 人物：外卖骑手、带孩子过街的母亲、儿童、远处货车司机
- 导演形式：`HYBRID`，叙事事实优先，局部使用感知与时序编排强化危险认知
- 核心命题：真正改变结局的不是英雄姿态，而是一个人在极短时间里决定停下来。

## NARRATIVE_LOCK

```yaml
protagonist: 夜间送单的年轻骑手
core_situation: 他在雨夜赶时间通过路口
inciting_visible_event: 儿童手中的纸风车被风卷入车道
critical_choice: 骑手在时间与安全之间选择急停
irreversible_change: 他失去本可通过路口的时机，但避免事故
ending: 绿灯再次亮起，儿童捡回纸风车，骑手安静等待下一次通行
meaning: 克制与停下同样是一种行动
forbidden_change:
  - 不改成追车英雄救人
  - 不制造撞击或受伤
  - 不让环境奇迹般响应人物情绪
```

## PROJECT_VISUAL_STRATEGY摘要

- 现实主义数字电影质感，雨夜但关键动作可读；
- 街灯、车辆灯、信号灯均来自真实世界位置；
- 色彩以湿冷灰蓝、道路钠灯中性暖色、交通信号色构成；
- 画面不使用神圣逆光、夸张慢动作、粒子奇观和情绪化天气突变；
- 环境大多数时间保持中性或构成真实阻力；
- 流畅感来自时序、信息、动作和声音关系，而不是材质变形；
- 摄影机可领先、保持或抵抗，不设固定跟随规则。

## 序列级编排

```yaml
sequence_orchestration:
  sequence_id: SEQ-01
  directing_form: HYBRID
  governing_relation: 现实环境持续运行，人物在极短窗口内读取危险并作出选择
  density_curve: [2, 2, 3, 5, 4, 2, 1]
  motion_energy_curve: [2, 2, 3, 5, 4, 1, 1]
  information_curve: [1, 2, 3, 5, 4, 3, 2]
  emotional_curve: [1, 1, 2, 4, 3, 2, 1]
  breathing_points: [SH-06, SH-07]
  final_residual_state: 雨和城市继续，人物因选择停下获得短暂秩序
```

## Shot表与时空视觉编排

| Shot | 时长 | 主功能 | 主导权 | 耦合方式 | 摄影机 | 环境 | 灯光 | 声音 | 主要任务 |
|---|---:|---|---|---|---|---|---|---|---|
| SH-01 | 4s | ATMOSPHERIC_IMMERSION | ENVIRONMENT | INDEPENDENT | HOLD | REMAIN_NEUTRAL | STABILIZE | BRIDGE | 建立雨夜路口与空间事实 |
| SH-02 | 3s | NARRATIVE_ADVANCE | OBJECT | CAUSAL | REVEAL | INITIATE | IGNORE | FOLLOW | 纸风车脱手滚入车道 |
| SH-03 | 4s | HOOK_REVERSAL | CAMERA | ANTICIPATORY | LEAD | REMAIN_NEUTRAL | REVEAL | LEAD | 观众先发现侧后方货车逼近 |
| SH-04 | 5s | SUSPENSE_OPPRESSION | GROUP | RESISTANT | RESIST | OPPOSE | STABILIZE | SYNCHRONIZE | 骑手制动、货车接近、道路形成阻力 |
| SH-05 | 4s | CATHARTIC_RELEASE | CHARACTER | CAUSAL | FOLLOW | REMAIN_NEUTRAL | REVEAL | FOLLOW | 骑手停住，危险窗口结束 |
| SH-06 | 5s | EMOTIONAL_RESONANCE | CHARACTER | COUNTERPOINT | HOLD | IGNORE | STABILIZE | WITHHOLD | 骑手与儿童隔着车道短暂对视 |
| SH-07 | 5s | HEALING_SOOTHING | ENVIRONMENT | INDEPENDENT | HOLD | REMAIN_NEUTRAL | STABILIZE | BRIDGE | 绿灯重新亮起，日常继续 |

## 逐镜关键编排

### SH-01｜城市先存在

```yaml
shot_orchestration:
  initial_relation: 雨夜路口按自身节奏运行，人物尚未成为中心
  initiating_system: ENVIRONMENT
  first_change: 远处信号灯由绿转黄
  camera_temporal_role: HOLD
  light_event_relation: STABILIZE
  environment_relation: REMAIN_NEUTRAL
  sound_temporal_role: BRIDGE
  development: 骑手从左后方进入，但环境不为其让路或响应
  peak: 信号灯进入黄灯末段
  settling_or_cut: 骑手接近停止线时切入下一镜
  handoff_channels: [spatial_position, rhythm, sound]
```

目的：证明流畅不必依靠人物驱动环境。城市可以先存在，人物只是进入它。

### SH-02｜物件发起事件

```yaml
shot_orchestration:
  initiating_system: OBJECT
  first_change: 儿童手中纸风车脱落
  coupling_mode: CAUSAL
  camera_temporal_role: REVEAL
  environment_relation: INITIATE
  light_event_relation: IGNORE
  sound_temporal_role: FOLLOW
  development: 风车先落地，再被路面横风推入车道；摄影机只小幅横移保持其轨迹可读
  peak: 风车进入骑手预计通过路径
  exact_end_relation: 风车停在湿路面，骑手尚未完全察觉
  handoff_channels: [object_motion, screen_direction, sound]
```

目的：主导者可以是道具，不默认人物或环境。

### SH-03｜摄影机先于人物知道

```yaml
shot_orchestration:
  initiating_system: CAMERA
  coupling_mode: ANTICIPATORY
  camera_temporal_role: LEAD
  environment_relation: REMAIN_NEUTRAL
  light_event_relation: REVEAL
  sound_temporal_role: LEAD
  development: 摄影机从骑手前方视线区缓慢侧移，先露出侧后方货车灯光；低频轮胎声先进入
  peak: 观众同时看清风车、骑手运动方向和货车逼近关系
  exact_end_relation: 骑手还未转头，观众已经知道危险
  handoff_channels: [attention, brightness, sound, spatial_relation]
```

目的：允许摄影机领先，而不是机械跟随主体。

### SH-04｜多系统对抗

```yaml
shot_orchestration:
  initiating_system: GROUP
  coupling_mode: RESISTANT
  camera_temporal_role: RESIST
  environment_relation: OPPOSE
  light_event_relation: STABILIZE
  sound_temporal_role: SYNCHRONIZE
  response_order:
    - 骑手右手收紧刹车
    - 前轮减速并偏离原路线少量
    - 后轮在湿地面短暂侧滑
    - 货车灯光快速接近但不越过安全边界
  development: 摄影机向后保持距离，不追求英雄式贴身；道路摩擦和车身惯性构成真实阻力
  peak: 刹车声、轮胎水声和货车喇叭在同一危险节点汇合
  settling_or_cut: 骑手与风车之间保留安全距离，车辆均未发生接触
  handoff_channels: [motion_energy, sound, spatial_distance]
```

目的：统一可以来自对抗和阻力，而非同向融合。

### SH-05｜结果先于情绪

```yaml
shot_orchestration:
  initiating_system: CHARACTER
  coupling_mode: CAUSAL
  camera_temporal_role: FOLLOW
  environment_relation: REMAIN_NEUTRAL
  light_event_relation: REVEAL
  sound_temporal_role: FOLLOW
  development: 骑手停稳后，摄影机才小幅靠近；货车从背景安全通过，前灯短暂扫过湿路面
  peak: 骑手确认儿童仍在路边安全区域
  exact_end_relation: 身体仍紧张，但危险事实已结束
  handoff_channels: [gaze, breath, brightness_decay]
```

目的：摄影机跟随是本镜选择，不是项目默认。

### SH-06｜世界不替人物煽情

```yaml
shot_orchestration:
  initiating_system: CHARACTER
  coupling_mode: COUNTERPOINT
  camera_temporal_role: HOLD
  environment_relation: IGNORE
  light_event_relation: STABILIZE
  sound_temporal_role: WITHHOLD
  development: 骑手和儿童隔着车道看向彼此；雨、信号和远处车辆继续正常运行
  peak: 儿童轻轻点头，骑手松开持续紧握的刹车
  exact_end_relation: 没有挥手、拥抱或环境回应
  handoff_channels: [gaze, gesture_residue, ambient_sound]
```

目的：情绪连贯可以来自世界的冷静和中性，而不是同步回应。

### SH-07｜秩序恢复但不是奖赏

```yaml
shot_orchestration:
  initiating_system: ENVIRONMENT
  coupling_mode: INDEPENDENT
  camera_temporal_role: HOLD
  environment_relation: REMAIN_NEUTRAL
  light_event_relation: STABILIZE
  sound_temporal_role: BRIDGE
  development: 行人绿灯按正常周期亮起，母亲带孩子捡回纸风车；骑手仍等待下一次机动车通行
  peak: 纸风车重新在儿童手中缓慢转动
  final_residual_state: 骑手没有获得英雄式凝视，只在雨中恢复呼吸
  handoff_channels: [semantic_motif, rhythm, emotional_energy]
```

目的：环境恢复是客观周期，不把绿灯写成世界奖励人物。

## 高风险视频Prompt编译测试｜SH-04

```text
保持首帧人物身份、车辆类型、湿路面、信号灯位置、道路透视和雨夜真实光源不变。本镜唯一核心事件是骑手在发现纸风车和侧后方货车后完成一次安全急停，所有动作必须服从真实惯性与空间距离。

0.0—0.6秒：骑手视线迅速落向前下方纸风车，右手手指先收紧刹车，肩部与躯干尚未剧烈摆动；摄影机保持在其前侧并轻微后撤，不迎面冲向人物。

0.6—2.2秒：前轮减速并向远离儿童的一侧偏转少量，后轮在湿路面发生短促、受控的侧滑，车身倾角有限，骑手通过髋部和左脚准备维持平衡。货车从侧后方接近但保持清楚安全距离，货车不会撞击、擦碰或突然变道。

2.2—3.8秒：制动力、路面阻力和身体重心共同让车辆停止。摄影机继续小幅后撤，以保持骑手、纸风车和货车三者空间关系可读。道路环境不随人物情绪产生超现实变化，雨量、街灯和信号灯保持稳定。

3.8—5.0秒：骑手完全停稳，双手仍握车把，胸腔出现一次急促呼吸；货车安全通过背景，喇叭声和轮胎水声逐渐远离。结尾保持骑手与纸风车无接触、与儿童有安全距离，稳定停留至少12帧。

禁止英雄式飞身、夸张漂移、慢动作爆炸水花、车辆擦碰、儿童进入危险中心、摄影机高速环绕、灯光随机闪烁、雨水突然增强、背景与人物同步夸张运动。人物、车辆、道路、灯光和声音通过对抗与阻力形成统一，而不是同方向一起运动。
```

## 预期检查

```yaml
expected_result:
  same_project_multiple_coupling_modes: true
  camera_roles_used: [HOLD, REVEAL, LEAD, RESIST, FOLLOW]
  light_roles_used: [STABILIZE, IGNORE, REVEAL]
  environment_roles_used: [REMAIN_NEUTRAL, INITIATE, OPPOSE, IGNORE]
  sound_roles_used: [BRIDGE, FOLLOW, LEAD, SYNCHRONIZE, WITHHOLD]
  fixed_reference_aesthetic_leakage: false
  fluid_or_material_transformation_required: false
  narrative_lock_preserved: true
  intentional_neutrality_supported: true
  intentional_resistance_supported: true
```

## 本基准不能升级为默认的内容

- 雨夜路口；
- 骑手、儿童、纸风车与货车；
- 16:9；
- 摄影机在SH-03领先、在SH-04抵抗；
- 灯光大部分时间稳定；
- 环境保持现实主义中性。

这些都属于本测试项目。能够进入核心判断的只有：同一项目可以根据镜头任务切换主导权、耦合方式、时序角色与连续通道，并且每种选择都必须有项目证据。