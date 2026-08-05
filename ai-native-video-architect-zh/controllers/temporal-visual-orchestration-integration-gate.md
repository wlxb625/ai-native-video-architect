# Temporal Visual Orchestration Integration Gate V4.5

## 定位

本文件是时空视觉编排模块的**开发验证记录与升级门禁**，不是普通项目的制作控制器，也不进入默认创作上下文。

正常项目是否启用时空编排，由以下文件决定：

- `controllers/post-script-production.md`的条件加载规则；
- `controllers/temporal-visual-orchestration.md`的启用判断；
- `templates/temporal-visual-orchestration-block.md`的完整、简化或不启用选项。

剧情与跨镜状态连续统一由`prompt-engineering/continuity-repair-system.md`中的`CONTINUITY_LEDGER`负责，本文件不再重复建立提示词连续性字段。

## 当前状态

```yaml
module_status: EXPERIMENTAL_CORE_CANDIDATE
normal_creation_default_load: false
conditional_project_use: true
current_validation:
  uploaded_reference_cases: 1
  synthetic_cross_project_cases: 5
  internal_full_pipeline_benchmarks: 1
  externally_generated_benchmarks: 0
```

当前结论只支持：

- 在复杂镜头中条件化选择主导权、耦合方式和相对时序角色；
- 统筹人物、环境、摄影机、灯光、声音、道具与剪辑的关系；
- 为跨镜感知接力选择通道或说明有意断裂；
- 简单镜头使用简化判断或明确不启用。

当前结论不支持：

- 把任何参考项目的运动顺序设为默认；
- 把摄影机领先、跟随、抵抗或环境中性写成类型固定答案；
- 成为所有Shot必须完整填写的硬表格；
- 重复摄影、灯光、表演或连续性模块的具体参数；
- 宣称已通过外部视频生成验证。

## 升级为正式核心硬门禁的条件

必须同时满足：

1. 至少三个真实且类型差异明显的项目完成测试；
2. 每个项目形成`test_learning_report`；
3. 至少完成一轮真实连续镜头外部生成；
4. 能在叙事、悬疑、喜剧、动作、抽象或广告中得到不同合法答案；
5. 没有把案例人物、色彩、材质、构图和运动顺序写成默认；
6. 与摄影、灯光、表演、声音和`CONTINUITY_LEDGER`无职责冲突；
7. 简单镜头能够简化或不启用；
8. `temporal-visual-orchestration-check.md`能发现真实失败，而不是奖励填表完整；
9. 多个项目反复出现的结构性问题才允许升级为核心规则。

满足前不得把该模块改成：

- 所有Shot的强制完整字段；
- 根`SKILL.md`的常驻专业模块；
- `full-package-integrity-check.md`对所有镜头的统一硬计数；
- 固定的视频Prompt运动公式。

## 开发验证资料

仅在开发Skill、复盘生成结果或决定是否升级规则时读取：

- `references/test-learning-abstraction-protocol.md`；
- `references/case-studies/`；
- `benchmarks/`；
- `evals/cross-project-orchestration-pressure-test.md`；
- `evals/temporal-orchestration-benchmark-*`。

案例是证据，不是模板。普通项目不得默认读取这些内容。

## 当前缺口

```yaml
remaining_validation:
  real_contrasting_projects_needed: 2
  external_continuous_shot_generation_needed: true
  prompt_execution_evidence_needed: true
  repeated_cross_project_failure_evidence_needed: true
```

在缺口补齐前，模块可条件使用、可测试、可局部修正，但不能宣称已经完成正式核心验证。
