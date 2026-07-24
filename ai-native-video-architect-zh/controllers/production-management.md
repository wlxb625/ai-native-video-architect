# Production Management Controller

## 目标

把导演方案转为可排期、可分配资源、可控制成本、可追踪版本和可恢复失败的生产计划。

## 镜头价值评估

```yaml
shot_value:
  story_value: 0-5
  visual_value: 0-5
  emotional_value: 0-5
  propagation_value: 0-5
  continuity_value: 0-5
  generation_difficulty: 0-5
  postproduction_difficulty: 0-5
  priority: S | A | B | C
```

优先级：

- S：代表作品的传播、高潮或规则镜头；
- A：人物选择、关系变化和关键情绪；
- B：必要信息、空间建立与连接；
- C：可替代过渡或装饰。

默认资源分配：S+A 70%，B 20%，C 10%。若C镜头消耗高于其价值，应合并或删除。

## 资产清单

至少跟踪：

- 角色参考、表情、服装和姿态；
- 场景主视图、结构图、光照和状态版本；
- 核心道具及其三次状态；
- 字幕、界面、标识和后期文字；
- 环境声、声音母题、配音和音乐；
- 每个镜头的源图、生成版本、选中版本和失败原因。

## 生成顺序

不要按剧情顺序盲目生成。推荐：

1. 视觉圣经与角色定稿；
2. 标志镜头和核心样片；
3. 高潮与高风险镜头；
4. 人物选择和情绪镜头；
5. 空间建立与连接镜头；
6. 补镜、转场和后期元素。

关键样片失败时，应先修改设计或工具路径，不继续批量生成同类镜头。

## 工具匹配原则

不把工具名称永久写死为唯一答案。根据当前可用能力选择：

- 概念图与视觉探索；
- 角色或场景一致性工作流；
- 图像转视频；
- 文生视频；
- 局部动画与重绘；
- 合成、剪辑、调色和声音。

涉及最新模型能力、价格、参数和版权限制时，需要实时核实。

## 成本与规模

### 低成本

少角色、少场景、强构图、短动作、声音承担空间，优先30—60秒。

### 中等成本

建立完整视觉圣经，集中5—10个核心镜头，允许少量合成和多轮生成。

### 高质量

完整角色与场景资产、多轮样片、分层合成、统一调色、声音设计和系统化版本管理。

## 失败恢复

每个S/A镜头必须至少有一个稳定替代：

- 改变景别或遮挡；
- 把连续动作拆为前因与结果；
- 把多人同框改为视线、声音和反打；
- 把复杂奇观改为环境反应和局部证据；
- 把精确口型改为背影、画外音、设备播放或后期；
- 用声音、字幕或物件补充，但不得改变事实。

## 版本命名

建议：

```text
PROJECT_SCENE_SHOT_VARIANT_STAGE_VERSION
```

示例：`ZERODREAM_S03_SH12_WIDE_VIDEO_V04`。

## 输出要求

```yaml
production_plan:
  duration:
  shot_count:
  s_shots:
  a_shots:
  high_risk_shots:
  asset_list:
  generation_order:
  tool_categories:
  budget_level:
  fallback_matrix:
  postproduction_needs:
  delivery_versions:
```
