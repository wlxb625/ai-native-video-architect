# Temporal Visual Orchestration Integration Gate V4.5

## 目的

控制`temporal-visual-orchestration.md`何时进入正式制作流程，避免因为一个参考项目就把实验性结论写成所有项目的硬规则。

## 一、状态

```yaml
module_status: EXPERIMENTAL_CORE_CANDIDATE
current_validation:
  uploaded_reference_case: 1
  synthetic_cross_project_cases: 5
  internal_full_pipeline_benchmarks: 1
  externally_generated_benchmarks: 0
  real_cross_project_cases_required_before_hard_gate: 3
```

已完成内部完整流程基准：

- `benchmarks/temporal-orchestration-benchmark-001-slow-one-second.md`；
- `evals/temporal-orchestration-benchmark-001-report.md`。

该基准验证了同一现实主义项目内可根据不同Shot切换摄影机、环境、灯光和声音关系，但尚未通过外部视频生成验证。

当前模块可以用于：

- 条件化导演规划；
- 视觉序列、梦境、MV、抽象段落和多系统运动镜头；
- 诊断人物、环境、摄影机、灯光和声音各自随机运动的问题；
- 生成测试和横向压力测试。

当前模块暂不应：

- 成为所有Shot必须完整填写的硬字段；
- 用单一参考项目决定默认时序；
- 把某一种耦合关系写进全局视觉策略；
- 因字段完整而让简单镜头过度设计。

## 二、当前接入方式

### 条件启用

出现以下任一条件时读取完整模块：

- 同镜头两个以上系统明显变化；
- 用户强调画面流畅融合、人物与背景统一、材质和空间共同变化；
- 当前段落为`VISUAL_SEQUENCE_DRIVEN`或`HYBRID`；
- 相邻镜头需要形状、运动、节奏、声音、语义或情绪接力；
- 实测出现随机独立运动、自动跟随、无原因灯光变化或无意义背景动态。

### 简化启用

普通叙事镜头只填写：

- 主导系统；
- 摄影机角色；
- 环境关系；
- 灯光是否变化及原因；
- 初始关系、主要变化和结束关系；
- 切镜连续通道或硬切理由。

### 不启用完整块

- 静态资产板；
- 纯结构参考图；
- 没有时间变化的单张图片；
- 简单字幕、纯后期或无需生成的视频段落。

## 三、升级为正式硬门禁的条件

必须同时满足：

1. 至少三个真实且类型差异明显的项目完成测试；
2. 每个项目形成`test_learning_report`；
3. 没有把案例具体手法写成默认；
4. 能在叙事、悬疑、喜剧、动作、抽象或广告中得到不同合法答案；
5. 与摄影、灯光、表演、连续性和视频Prompt编译器没有字段冲突；
6. 简单镜头可以简化，不因模块增加而过度复杂；
7. `temporal-visual-orchestration-check.md`能够发现真实失败而不是只检查填表；
8. 至少完成一轮外部视频生成验证。

满足后再修改：

- `SKILL.md`全流程必读列表；
- `post-script-production.md`正式步骤；
- `shot-production-card.md`强制字段；
- `full-package-integrity-check.md`硬性计数；
- `full-creation-package.md`最终交付结构。

## 四、当前实验工作流

```text
用户参考或当前项目
→ test-learning-abstraction-protocol
→ 选择是否启用时空视觉编排
→ 使用temporal-visual-orchestration
→ 编译进视频Prompt扩展
→ 运行orchestration check
→ 生成真实视频测试
→ 形成新的test_learning_report
→ 横向汇总
```

没有额外真实参考时，可先执行内部完整流程基准，但其结果只能记为`DESIGN_PASS_EXTERNAL_GENERATION_PENDING`，不能计入真实跨项目案例数量。

## 五、防止过度膨胀

新增字段必须证明它控制了以下至少一项：

- 可见先后关系；
- 主次与注意力；
- 运动或信息因果；
- 摄影、灯光、环境或声音的角色；
- 峰值和结束状态；
- 跨镜头连续或有意断裂。

只重复原有动作、摄影、灯光或表演描述的字段应删除或合并。

## 六、当前结论

现阶段将本模块保留为“可调用、可测试、尚未全局强制”的导演层候选，是比立即改写所有核心模板更安全的做法。

当前已通过：

- 单一外部参考的案例抽象；
- 五类合成横向压力测试；
- 一个完整现实主义项目的设计态端到端基准。

当前仍缺：

- 外部生成后的镜头执行验证；
- 两个以上差异明显的真实项目；
- 对实际模型失败类型的修正规则。