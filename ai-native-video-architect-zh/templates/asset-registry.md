# Asset Registry

## 项目信息

- 项目名：
- 版本：
- 画幅：
- 总时长：
- 当前阶段：概念 / 资产 / 分镜帧 / 视频 / 后期
- 主导演模式：
- 主要工具类别：

## Asset Readiness Gate

| 类别 | 状态 | 证据 | 必须修复 |
|---|---|---|---|
| Visual Bible | PASS / CONDITIONAL / FAIL |  |  |
| Character Identity | PASS / CONDITIONAL / FAIL / N/A |  |  |
| Costume States | PASS / CONDITIONAL / FAIL / N/A |  |  |
| Environment Layout | PASS / CONDITIONAL / FAIL |  |  |
| Empty Plates | PASS / CONDITIONAL / FAIL |  |  |
| Props and States | PASS / CONDITIONAL / FAIL / N/A |  |  |
| Continuity Registry | PASS / CONDITIONAL / FAIL |  |  |
| Reference Quality | PASS / CONDITIONAL / FAIL |  |  |

- ready_for_storyboard_frames：true / false
- ready_for_video_generation：true / false

## 角色资产

| ID | 名称 | 类型 | 状态 | 当前选中版本 | 引用镜头 | 风险 |
|---|---|---|---|---|---|---|
| CHAR_C01 |  | Identity |  |  |  |  |
| FACE_C01 |  | Face Board |  |  |  |  |
| HAIR_C01 |  | Hair Board |  |  |  |  |
| POSE_C01_P01 |  | Pose |  |  |  |  |

## 服装资产

| ID | 所属角色 | 状态名称 | 首次出现 | 产生变化的镜头 | 后续继承 | 选中版本 |
|---|---|---|---|---|---|---|
| COST_C01_A |  |  |  |  |  |  |

## 场景资产

| ID | 名称 | 类型 | 时间/天气 | 主光方向 | 固定地标 | 选中版本 |
|---|---|---|---|---|---|---|
| SCENE_S01 |  | Master |  |  |  |  |
| PLATE_S01_WIDE |  | Empty Plate |  |  |  |  |
| ANGLE_S01_L01 |  | Multi-angle |  |  |  |  |

## 道具资产

| ID | 名称 | 状态 | 尺寸 | 默认位置/持有者 | 产生变化的镜头 | 选中版本 |
|---|---|---|---|---|---|---|
| PROP_P01_A |  |  |  |  |  |  |

## 镜头帧资产

| 镜头 | 首帧ID | 尾帧ID | 参考角色 | 服装 | 场景 | 道具 | 生成方法 | 当前版本 |
|---|---|---|---|---|---|---|---|---|
| SH01 | FRAME_SH01_IN | FRAME_SH01_OUT |  |  |  |  |  |  |

## 资产依赖

```yaml
shot_dependencies:
  SH01:
    characters: []
    costumes: []
    environments: []
    props: []
    start_frame:
    end_frame:
    audio: []
```

## 禁止覆盖

- 已选中的角色身份图不得被新尝试直接覆盖；
- 已使用的道具状态不得无版本号修改；
- 场景布局和光源方向变更必须生成新场景版本；
- 首帧或尾帧变化必须同步更新镜头依赖和连续性台账。
