# Drama Score

## 职责
按COMMERCIAL、LITERARY、EXPERIMENTAL分别评价完成度；HYBRID不默认平均。

## 统一输出
```yaml
status: PASS | CONDITIONAL | FAIL
design_tags: []
applicability: HIGH | MEDIUM | LOW | NOT_APPLICABLE
evidence: []
risks: []
must_fix: []
should_strengthen: []
must_protect: []
```

## 评估维度
- 进入与核心承诺
- 主体及其限制
- 中段变化
- 高潮/峰值/反高潮
- 结尾完成与开放
- 路径一致性

## 合法设计标签
- `COMMERCIAL_PATH`
- `LITERARY_PATH`
- `EXPERIMENTAL_PATH`
- `ANTI_CLIMAX`
- `WEAK_PLOT_BY_DESIGN`

## 硬失败
- 1. 未识别路径就评分
- 2. 中段完全重复
- 3. 高潮依赖临时规则
- 4. 结尾既未完成也未有意开放
- 5. 实验无规则
- 6. 文学无人物/关系/意义变化

## 条件通过
- 1. 核心成立但中段偏弱
- 2. 结尾成立但准备不足
- 3. 路径职责重叠
- 4. 峰值存在但表现不够清楚

## 评分
商业、文学、实验各自100分。只报告主要路径分数；辅助路径注明适用性。
