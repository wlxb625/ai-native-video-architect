# AI Production Controller V4.4

## 目标

把已成立剧本、资产和分镜转译为可生成、可连续、可剪辑、可修复和可追踪版本的AI电影生产系统。

核心原则：

> 先锁资产，再锁分镜帧；先锁分镜帧，再让画面运动。

## 必读

- `controllers/post-script-production.md`
- `controllers/asset-first-production.md`
- `controllers/detailed-storyboard.md`
- `controllers/camera-director.md`
- `controllers/lighting-director.md`
- `controllers/performance-director.md`
- `references/emotion-library.md`
- `prompt-engineering/performance-prompt-compiler.md`
- `prompt-engineering/image-prompt-compiler.md`
- `prompt-engineering/storyboard-frame-system.md`
- `prompt-engineering/video-prompt-compiler.md`
- `prompt-engineering/camera-movement-library.md`
- `prompt-engineering/continuity-repair-system.md`
- `core/continuity.md`

## 生产阶段

```text
P0 保护合同
P1 Visual Bible、色调与光影
P2 Asset Registry和参考职责
P3 整批资产Prompt与外部资产制作
P4 用户自审和资产确认
P5 分镜设计与整批首尾帧Prompt
P6 核心样片视频Prompt
P7 整批视频Prompt、续拍和硬切
P8 剪辑、声音、调色和交付
```

不得从P1跳到P6。

## 保护合同

```yaml
production_protection:
  must_preserve: []
  allowed_implementation_changes: []
  forbidden_changes: []
  allowed_visual_drift: []
  forbidden_visual_drift: []
  delivery:
  budget_level:
```

制作难度不能成为改变人物选择、高潮、结尾或开放程度的理由。

## Visual Bible

除画幅和风格外，必须锁定：

- 主色、辅助色、点缀色；
- 色温、饱和度、对比度和白平衡；
- 黑位、高光和肤色关系；
- 主光方向、光色和照亮对象；
- 材质和禁止风格。

## 图片Prompt

基础结构：

```text
参考职责
+ 主体和静态瞬间
+ 可见微表情、视线、姿态、重心和手部状态
+ 场景空间
+ 服饰道具
+ 景别机位构图
+ 光线色调材质
+ 输出规则
+ 负面约束
```

静态图片不描述完整连续动作。

## 视频Prompt

基础结构：

```text
唯一首帧
+ 起始状态
+ 人物目标、内外矛盾和起始表演基线
+ 一个主要动作和一个主要情绪转折
+ 起势、微表情与情绪过程、收住
+ 速度方向幅度重心
+ 运镜起点方向速度终点
+ 允许环境动态
+ 指定结束状态
+ 声音
+ 禁止变化
```

视频Prompt主要描述运动与表演随时间的变化，不重新定义人物和场景。

## 首尾帧

优先用于外观变化、道具变化、环境变化、指定动作终点和高风险镜头。首帧留动作空间，尾帧锁定最终姿态和下一镜继承。

## 镜头策略

- Establishing：空间建立；
- Performance：人物目标、内外矛盾、微表情、呼吸、身体语言和反应；
- Interaction：人物与道具/人物；
- Spectacle：前兆、发生、结果分层；
- Symbol：低动作、高构图和声音；
- Connector：视线、脚步、手部、门、光和道具连接。

## 导演、摄影、灯光和表演

先建立导演意图和观众位置，再选择摄影参数。运镜必须有动机和终点，调用`camera-director.md`与`camera-movement-library.md`。逐镜灯光必须让关键表演区域可读。人物表演调用`performance-director.md`和`performance-prompt-compiler.md`，禁止只写情绪标签。固定镜头是合法且常用选择。

## 续拍

提取上一段稳定尾帧作为下一段唯一首帧，只继续剩余动作。

## 硬切

可换景别和机位，必须保持身份、服装、道具、动作进度、站位、空间、光线和色调。复杂硬切优先生成两段后剪辑。

## Core Sample

先测试核心角色、主场景、核心道具、高风险变化、一个衔接和主要运镜。用户自行生成并确认；回复“下一步”即通过。

## 批量生产

按复用率和风险排序，不按剧情顺序盲目生成。S/A镜头有稳定替代。

## 失败恢复

优先局部修复、图生图、重做单帧、重做单镜，再返回资产。禁止一个局部错误推翻整片。
