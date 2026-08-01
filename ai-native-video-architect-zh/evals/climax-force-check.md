# Climax Force Check V0.2

## 职责

独立检查高潮是否真正形成戏剧峰值，而不是把象征性收束、告别仪式、一次不可逆动作或母题回收误判为高潮。

该检查不要求所有作品都“爆炸式”升级，但必须按照任务声明的`climax_profile`验证对应峰值。默认使用`STRONG_DRAMATIC_PEAK`。

## 输出

```yaml
evaluator: climax_force_check
status: PASS | CONDITIONAL | FAIL
score: 0-100
subscores:
  pressure_and_escalation: 0-20
  value_collision: 0-20
  audience_uncertainty: 0-20
  action_cost_and_irreversibility: 0-20
  audiovisual_peak_and_state_change: 0-20
counterfactual_challenges:
  removable_without_changing_ending: true | false
  choice_has_obvious_correct_answer: true | false
  cost_paid_on_screen: true | false
  climax_distinct_from_resolution: true | false
  pressure_escalates_before_action: true | false
  post_climax_state_cannot_return: true | false
evidence: []
hard_failures: []
must_fix: []
must_protect: []
```

## STRONG_DRAMATIC_PEAK通过条件

1. 高潮前至少存在两次同一冲突引擎的升级，不是只在高潮前增加说明。
2. 人物必须在两个都具有真实价值的方向之间选择；不能是一边明显正确、一边只是拖延或违规。
3. 存在主动压力源、期限或不可逆触发点，使人物不能无限等待。
4. 观众在行动发生前不能完全确定人物会怎么选。
5. 代价必须在画面中被支付，并改变现实、关系、身份、承诺或未来可能性。
6. 高潮动作不能删除后仍保持相同结尾；删除后若故事仍能自然收束，判为伪高潮。
7. 高潮后的状态必须不能恢复到高潮前。
8. 摄影、表演、声音、空间或动作密度必须形成可感知级差；克制不等于平铺。

## 常见硬失败

- `EMOTIONAL_RESOLUTION_MISLABELED_AS_CLIMAX`：真正的决定早已完成，所谓高潮只是把情绪收好。
- `CLIMAX_IS_ONLY_CLOSING_RITUAL`：动作主要承担告别、清理、覆盖、焚烧、离开等仪式，没有新的冲突结果。
- `VALUES_NOT_COMPARABLE`：一边是明显合理行为，另一边只是违规、执念或无现实价值。
- `NO_ESCALATING_PRESSURE`：没有逐步缩短选择空间的压力。
- `OUTCOME_PREDETERMINED`：观众从概念建立后就知道人物必然会做出该动作。
- `COST_ONLY_STATED_NOT_PAID`：文本声称有代价，但镜头中没有失去任何具体东西。
- `CLIMAX_REMOVABLE_WITHOUT_ENDING_CHANGE`：删掉高潮，结尾关系和状态仍然成立。
- `NO_POST_CLIMAX_STATE_DELTA`：高潮后没有新的现实或关系状态。

## 反例

人物最后覆盖一枚旧脚印，如果此前没有真正升级的对抗、保留脚印也不存在同等价值、覆盖结果早已确定，那么它可以是优秀的视觉收束，却不能被评为强戏剧高潮。
