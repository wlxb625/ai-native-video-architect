# Asset Readiness Score

## 适用性

当任务要求角色一致、场景一致、道具一致、具体分镜、首尾帧、图生视频、批量生成或正式Production Pack时，适用性为HIGH。

概念探索、纯文字剧本或一次性无角色环境镜头可为LOW或NOT_APPLICABLE。

## 评分

总分100。

### 1. Character Identity — 20

- 正、侧、背是否同一人物；
- 面部不同角度是否保持年龄、骨相和辨识特征；
- 发型和身体比例是否清楚；
- 是否避免过度美颜和AI标准脸。

### 2. Costume and Character States — 15

- 服装内外层、袖口、下摆和鞋履是否清楚；
- 剧情变化是否建立状态版本；
- 磨损、湿度、伤痕和污渍是否有连续性。

### 3. Environment Structure — 20

- 是否有主布局、出入口和固定地标；
- 是否有无人物空镜；
- 多机位是否对应同一空间；
- 主光、时间和天气是否稳定。

### 4. Prop Identity and States — 15

- 核心道具是否有尺寸、结构、材质和独特标记；
- 是否有合理持有和使用逻辑；
- 状态变化是否建立版本与产生镜头。

### 5. Frame Readiness — 15

- 关键镜头是否定义首帧和结束状态；
- 需要精确变化的镜头是否准备尾帧；
- 首帧是否为动作留下空间；
- 视频Prompt是否只承担运动。

### 6. Continuity and Versioning — 15

- 是否有资产ID与版本；
- 镜头是否引用明确资产；
- 左右手、方向、道具位置和动作进度是否可追踪；
- 已批准版本是否避免被覆盖。

## 状态

- 85—100：PASS，可进入正式分镜帧或视频生成；
- 70—84：CONDITIONAL，可做Core Sample，不可批量生产；
- 0—69：FAIL，返回资产设计；
- 任一硬失败存在：FAIL。

## 硬失败

- AF1：三视图明显为不同人物；
- AF2：核心服装在资产板中结构或颜色已漂移；
- AF3：同一场景不同机位无法对应同一布局；
- AF4：核心道具在不同图中尺寸、结构或独特标记改变；
- AF5：作品依赖状态变化，却没有状态时间线；
- AF6：没有资产参考却批量生成多镜头并声称角色/场景已锁定；
- AF7：每个镜头重新描述资产，未引用固定版本；
- AF8：首尾帧之间改变了不允许变化的人物、场景或道具；
- AF9：艺术角色板被误当成唯一生产三视图，关键结构被裁切或遮挡；
- AF10：已批准资产被无版本号覆盖，无法回滚。

## 输出

```yaml
status: PASS | CONDITIONAL | FAIL
applicability: HIGH | MEDIUM | LOW | NOT_APPLICABLE
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
ready_for_storyboard_frames: true | false
ready_for_video_generation: true | false
```
