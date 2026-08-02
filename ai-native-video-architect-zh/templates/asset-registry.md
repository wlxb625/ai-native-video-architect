# Asset Registry

## 项目信息

- 项目名：
- 版本：
- 画幅：
- 总时长：
- 当前阶段：项目视觉策略 / 资产 / 分镜帧 / 视频 / 后期
- 项目视觉策略ID：
- NARRATIVE_LOCK引用：
- 资产工作等级：EXPLORATION / NARRATIVE_PRODUCTION / STUDIO
- 主要工具类别：

## Shot需求预分析

| 角色/场景/道具 | 实际镜头需求 | 景别/角度/交互/状态 | 缺少依据的风险 | 对应资产ID |
|---|---|---|---|---|
|||||

## Asset Readiness Gate

| 类别 | 状态 | 证据 | 必须修复 |
|---|---|---|---|
| Narrative Lock Preservation | PASS / CONDITIONAL / FAIL |  |  |
| Project Visual Strategy | PASS / CONDITIONAL / FAIL |  |  |
| Character Face Identity | PASS / CONDITIONAL / FAIL / N/A |  |  |
| Character Front-Side-Back | PASS / CONDITIONAL / FAIL / N/A |  |  |
| Full Body & Costume Structure | PASS / CONDITIONAL / FAIL / N/A |  |  |
| Hand & Prop Interaction | PASS / CONDITIONAL / FAIL / N/A |  |  |
| Character State Progression | PASS / CONDITIONAL / FAIL / N/A |  |  |
| Environment Master Layout | PASS / CONDITIONAL / FAIL |  |  |
| Environment Reverse/Detail Angles | PASS / CONDITIONAL / FAIL / N/A |  |  |
| Environment State Progression | PASS / CONDITIONAL / FAIL / N/A |  |  |
| Props and States | PASS / CONDITIONAL / FAIL / N/A |  |  |
| Continuity Registry | PASS / CONDITIONAL / FAIL |  |  |
| Reference Quality | PASS / CONDITIONAL / FAIL |  |  |

- ready_for_storyboard_frames：true / false
- ready_for_video_generation：true / false

## 角色资产

| ID | 名称 | 类型 | 状态 | 覆盖镜头需求 | 引用镜头 | 风险 |
|---|---|---|---|---|---|---|
| CHAR_C01_FACE |  | Face Identity |  |  |  |  |
| CHAR_C01_TURN |  | Front-Side-Back |  |  |  |  |
| CHAR_C01_FULL |  | Full Body Costume |  |  |  |  |
| CHAR_C01_HAIR |  | Hair & Costume Structure |  |  |  |  |
| CHAR_C01_HAND |  | Hand & Prop Interaction |  |  |  |  |
| STATE_C01_A |  | State Progression |  |  |  |  |

## 服装与状态资产

| ID | 所属角色 | 状态名称 | 首次出现 | 产生变化的镜头 | 后续继承 | 选中版本 |
|---|---|---|---|---|---|---|
| COST_C01_A |  |  |  |  |  |  |

## 场景资产

| ID | 名称 | 类型 | 对应机位/局部/状态 | 主光方向 | 固定地标 | 引用镜头 |
|---|---|---|---|---|---|---|
| LOC_S01_MASTER |  | Master |  |  |  |  |
| LOC_S01_REVERSE |  | Reverse Angle |  |  |  |  |
| LOC_S01_DETAIL |  | Detail Plate |  |  |  |  |
| STATE_S01_A |  | State Progression |  |  |  |  |

## 道具资产

| ID | 名称 | 类型/状态 | 尺寸 | 默认位置/持有者 | 产生变化的镜头 | 引用镜头 |
|---|---|---|---|---|---|---|
| PROP_P01_MASTER |  |  |  |  |  |  |
| PROP_P01_STATE_A |  |  |  |  |  |  |

## 镜头帧资产

| 镜头 | 首帧ID | 尾帧ID | 项目策略 | 角色身份/结构 | 场景机位 | 道具/状态 | 生成方法 |
|---|---|---|---|---|---|---|---|
| SH01 | CF-SH01-S | CF-SH01-E |  |  |  |  |  |

## 资产依赖

```yaml
shot_dependencies:
  SH01:
    project_visual_strategy:
    character_face: []
    character_structure: []
    costumes: []
    character_states: []
    environments: []
    environment_states: []
    props: []
    prop_states: []
    start_frame:
    end_frame:
    audio: []
```

## 资产充分性结论

- 是否覆盖全部重要面部近景：
- 是否覆盖正侧背和复杂身体动作：
- 是否覆盖服装与发型前后结构：
- 是否覆盖精确手部交互：
- 是否覆盖人物状态累积：
- 是否覆盖场景正反方向和关键局部：
- 是否覆盖环境与道具状态变化：
- 是否存在没有镜头使用的冗余资产：
- 最终结论：PASS / REPAIR

## 禁止覆盖

- 已选中的角色身份图不得被新尝试直接覆盖；
- 已使用的道具状态不得无版本号修改；
- 场景布局和光源方向变更必须生成新场景版本；
- 首帧或尾帧变化必须同步更新镜头依赖和连续性台账；
- EXPLORATION级参考不得伪称为正式成片一致性资产包。
