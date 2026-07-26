# Asset Readiness Score V4.0

## 使用方式

本评分器用于两种情况：

1. 用户明确请求助手审核资产；
2. S11核心样片失败，需要定位身份、结构或状态问题。

默认流程为`USER_SELF_AUDIT`，不得在用户没有请求时强迫逐图评分或逐张上传。

## 评分

总分100：

- Character Identity：20；
- Costume and Character States：15；
- Environment Structure and Multi-Angle：20；
- Prop Identity and State Chain：15；
- Frame Readiness：15；
- Continuity and Versioning：15。

## 检查项

### Character Identity

- 正、严格侧面、背面是否为同一人物；
- 年龄、骨相、发际线和稳定标记是否一致；
- 是否避免网红脸、塑料皮肤和随机美化。

### Costume and States

- 内外层、领口、袖口、下摆和鞋履是否清楚；
- 污渍、湿度、破损和剧情状态是否有固定版本。

### Environment

- 主布局、出入口、固定地标和轴线是否清楚；
- 无人物空镜与多机位是否对应同一空间；
- 时间、天气、主光方向和色调六轴是否稳定。

### Props

- 尺寸、人体比例、结构、材料和独特标记是否稳定；
- 左右手、握持、放置和状态链是否清楚。

### Frame Readiness

- 需要的首帧与尾帧是否定义准确静态瞬间；
- 复杂变化是否拆为首尾帧、硬切或分层；
- 是否为动作留下空间。

### Continuity and Versioning

- 资产ID、版本、文件命名和批准状态是否可追踪；
- 镜头是否引用批准资产；
- 动作完成百分比、视线、站位和背景地标是否可继承。

## 状态

- 85—100：PASS；
- 70—84：CONDITIONAL，可继续做Core Sample；
- 0—69：FAIL；
- 任一硬失败存在：FAIL。

评分结果用于帮助用户定位问题，不取代用户最终选择。

## 硬失败

- 三视图明显不是同一人物；
- 核心服装结构或颜色在资产板中已经漂移；
- 同一场景多机位无法对应同一布局；
- 核心道具尺寸、结构或独特标记改变；
- 故事依赖状态变化却没有状态链；
- 每镜重新发明人物、场景或道具；
- 首尾帧改变禁止变化项；
- 已批准版本无编号覆盖，无法回滚。

## 输出

```yaml
status: PASS | CONDITIONAL | FAIL
applicability: HIGH | MEDIUM | LOW | NOT_APPLICABLE
review_mode: ASSISTED_AUDIT
score:
dimensions:
  character_identity:
  costume_states:
  environment_structure:
  prop_identity_states:
  frame_readiness:
  continuity_versioning:
hard_failures: []
evidence: []
must_fix: []
user_final_decision_required: true
```
