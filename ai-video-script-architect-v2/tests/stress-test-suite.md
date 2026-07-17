# Stress Test Suite

以下静态情境必须得到预期结果：

1. 商业职场短剧：主角拒绝签字，有限结果 → PASS。
2. 文学开放结尾：事实开放但人物状态完成 → PASS + OPEN_ENDING。
3. 被动现实主义人物：有限选择与边界行动 → PASS。
4. 固定走廊重复变奏 → PASS + FORM_DRIVEN。
5. 结尾突然宣布全部是模拟 → FAIL。
6. 两种监控解释均有线索 → PASS + MULTIVALENT_TWIST。
7. 字幕按规则提前 → PASS；随机字幕错误 → FAIL。
8. AI发现、选择、执行和处罚，人物只观看 → FAIL。
9. 机制本身为实验主体且规则清楚 → PASS。
10. 用户只要求压缩却新增第三者和复合 → FAIL，未经授权LEVEL_4。
11. 用户明确授权类型与结尾重构 → PASS + DEEP_ADAPTATION。
12. 三人同框改正反打且高潮主体不变 → PASS。
13. 因动作难做改成系统自动执行 → FAIL并升级TRANSFORM。
14. 当前热梗符合人物并有回调 → CONDITIONAL，需实时验证与去时效版。
15. 粗剪先反应后动作导致因果倒置 → FAIL，优先重剪。
16. 开放结尾被明确音乐关闭 → FAIL。
17. 文学片商业分低但适用性LOW → 不得否定作品。
18. 无反转作品 → Twist评估LOW/NOT_APPLICABLE，不强制添加。
19. 无对白作品 → Dialogue NOT_APPLICABLE。
20. 随机角色和背景漂移自称意识流 → FAIL。

## 验收
所有正式实现应将上述案例固化为自动化或人工回归用例。
