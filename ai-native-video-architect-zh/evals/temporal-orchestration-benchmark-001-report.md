# Temporal Visual Orchestration Benchmark 001 Report

## 测试对象

- 基准项目：`benchmarks/temporal-orchestration-benchmark-001-slow-one-second.md`
- 项目类型：当代现实主义 / 短时动作悬疑 / 克制情绪
- 与外部参考的主要差异：无奇观、无材质变形、无仪式人物、环境多数保持中性或构成阻力
- 测试性质：内部完整流程设计验证，尚未进行外部视频生成

## 测试问题

1. 同一项目是否可以在不同Shot中切换主导权，而不破坏整体风格？
2. 摄影机是否可以根据镜头任务领先、保持、抵抗和跟随，而不是机械采用一种角色？
3. 灯光与环境是否可以保持稳定、忽视人物或构成阻力，同时仍形成连贯镜头？
4. 流畅是否可以通过信息、空间、声音、视线和节奏建立，而不依赖流体或材质转化？
5. 新控制器是否产生不必要的字段重复或改变`NARRATIVE_LOCK`？

## 结果

```yaml
status: DESIGN_PASS_EXTERNAL_GENERATION_PENDING
narrative_lock_preserved: true
project_visual_strategy_preserved: true
scene_function_compatibility: true
multiple_agency_modes_supported: true
multiple_coupling_modes_supported: true
camera_temporal_role_variation: true
light_event_role_variation: true
environment_relation_variation: true
sound_temporal_role_variation: true
perceptual_continuity_without_material_morphing: true
intentional_neutrality_supported: true
intentional_resistance_supported: true
case_specific_reference_leakage: false
fixed_fluid_aesthetic_leakage: false
fixed_camera_follow_rule: false
fixed_light_follow_rule: false
field_duplication_risks:
  - shot_orchestration中的动作细节不得重复performance_direction完整内容
  - camera_temporal_role只定义摄影机与事件时序，不重复焦段、机位和完整运镜参数
  - light_event_relation只定义灯光与事件关系，不重复完整逐镜灯光合同
  - environment_relation只定义环境角色，不替代背景大形和环境物理细节
external_generation_pending: true
```

## Shot级检查

| Shot | 选择是否有证据 | 是否产生固定模板 | 是否与摄影/灯光/表演冲突 | 结果 |
|---|---|---|---|---|
| SH-01 | 有：先建立客观城市 | 否 | 否 | PASS |
| SH-02 | 有：道具引发事件 | 否 | 否 | PASS |
| SH-03 | 有：观众先知位置 | 否 | 否 | PASS |
| SH-04 | 有：阻力与危险空间 | 否 | 否 | PASS |
| SH-05 | 有：结果先于情绪 | 否 | 否 | PASS |
| SH-06 | 有：世界不替人物煽情 | 否 | 否 | PASS |
| SH-07 | 有：客观秩序恢复 | 否 | 否 | PASS |

## 主要发现

### 1. 流畅不等于同向运动

SH-04中人物、道路阻力、货车和摄影机形成对抗关系。统一来自清楚的空间目标、危险节点和声音汇合，而不是所有元素朝同一方向运动。

### 2. 环境中性同样是导演选择

SH-01、SH-06和SH-07中，环境不主动回应人物。雨、信号灯和交通按自身规律运行，这种稳定反而强化现实主义和人物选择。

### 3. 摄影机角色可以在同一项目内变化

- SH-01保持；
- SH-03领先揭示；
- SH-04抵抗并维持空间；
- SH-05在结果形成后跟随；
- SH-06再次保持。

变化由观众位置和信息任务决定，没有造成风格随机。

### 4. 连续通道不必依赖材质变形

本项目主要使用：

- 空间位置；
- 运动方向；
- 声音桥；
- 亮度信息；
- 视线；
- 呼吸；
- 语义母题；
- 情绪能量。

因此验证了`perceptual_continuity_channels`不应固定为形状和材质继承。

## 未通过真实验证的内容

以下结论仍需外部生成：

- 视频模型能否准确执行摄影机`RESIST`而不变成随机后退；
- 湿路面制动能否保持真实且不生成夸张漂移；
- 货车、骑手、纸风车三者能否稳定维持安全空间；
- 声音与视频后期是否能实现设计中的先行、同步与留白；
- 连续七镜的身份、车辆、天气和空间是否稳定。

## 对核心模块的影响

### 保留

- 主导权选择；
- 耦合方式；
- 摄影机、灯光、环境和声音时序角色；
- 感知连续通道；
- 项目证据和冲突处理；
- 简单镜头简化启用。

### 不新增

- 不新增“现实主义环境必须中性”；
- 不新增“摄影机在动作场面必须抵抗”；
- 不新增“灯光必须稳定”；
- 不新增雨夜、骑手、纸风车等项目内容；
- 不把本基准的七镜结构设为标准。

## 下一验证建议

不再继续扩展核心字段。下一步从本基准中选择三个相邻高价值镜头执行外部生成：

```text
SH-03 摄影机领先揭示
→ SH-04 多系统对抗与急停
→ SH-05 危险结束后的摄影机跟随
```

这组三镜可以验证：摄影机角色是否能在同一空间内从领先转为抵抗，再转为跟随，并检查切换是否自然。
