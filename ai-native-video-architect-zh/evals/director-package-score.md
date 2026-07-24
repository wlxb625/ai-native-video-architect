# Director Package Score

用于完整导演包和生产包的最终审查。满分100，低于85默认返回薄弱层修订。

|维度|权重|
|---|---:|
|概念统一性|20|
|视觉叙事|20|
|镜头语言|15|
|人物与情绪|15|
|AI生产可行性|15|
|声音设计|10|
|传播或艺术目标匹配|5|

## 必查问题

- 一句话概念、人物任务、视觉规则和结尾是否属于同一作品？
- 关键图像是否承载关系和历史，而不是壁纸？
- 镜头是否设计观看顺序，而非只列参数？
- 声音是否具有世界层、人物层和母题层？
- 角色、场景、道具和动作是否可以连续生成？
- S/A级镜头是否有稳定替代？
- 传播策略是否保护人物选择和结尾开放程度？

## 结果协议

```yaml
status: PASS | CONDITIONAL | FAIL
total_score:
layer_scores:
  concept:
  visual_narrative:
  camera_language:
  character_and_emotion:
  production:
  sound:
  target_fit:
hard_failures: []
weakest_layer:
minimal_revision:
must_protect: []
```
