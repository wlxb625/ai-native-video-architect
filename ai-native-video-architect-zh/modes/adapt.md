# ADAPT Mode V4.1

把已成立作品转译为可执行的AI图片与视频生产内容。ADAPT优先改变实现方式，不改变人物目标、关键选择、高潮主体、结尾和开放程度。

## 启动

先判断用户已经拥有：

- 故事梗概；
- 完整剧本或视觉脚本；
- 视觉设定；
- 角色、场景或道具参考图；
- 镜头表；
- 分镜帧；
- 已生成的视频片段。

直接从用户缺失的交付物开始，不要求重做已经成立的内容，也不把阶段编号作为进入门槛。

## Production Protection Contract

```yaml
production_protection:
  source_material:
  target_delivery:
  must_preserve: []
  allowed_implementation_changes: []
  forbidden_changes: []
  allowed_visual_drift: []
  forbidden_visual_drift: []
  production_constraints: []
```

至少保护：

- 人物任务和关系；
- 核心机制或视觉规则；
- 关键选择；
- 高潮由谁行动、谁承担代价；
- 结尾和开放程度；
- 用户明确要求保留的画面、声音或风格。

## 剧本门槛

整片分镜和视频Prompt前必须有完整传统剧本或可制作视觉脚本。

如果用户只要求：

- 单个角色Prompt；
- 单个场景Prompt；
- 单个镜头Prompt；
- 已有图片的视频Prompt；
- 某个失败片段的修复；

则可以直接处理该局部任务，不强制补齐整片剧本，但不得虚构缺失的作品事实。

## 剧本后必读

按任务需要读取：

- `controllers/post-script-production.md`
- `prompt-engineering/image-prompt-compiler.md`
- `prompt-engineering/visual-style-color-light.md`
- `prompt-engineering/asset-prompt-system.md`
- `prompt-engineering/storyboard-frame-system.md`
- `prompt-engineering/video-prompt-compiler.md`
- `prompt-engineering/camera-movement-library.md`
- `prompt-engineering/continuity-repair-system.md`

## ADAPT交付能力

根据用户现有内容，可以直接交付：

- 剧本制作拆解；
- 视觉规则；
- 核心参考图Prompt；
- 完整镜头表；
- 分镜帧Prompt；
- 视频Prompt；
- 抽尾帧续拍与硬切方案；
- 局部修复和后期方案。

不要求用户先完成一套固定网站式流程。

## 最小参考策略

普通短片默认：

```text
每名主要角色：一张综合角色板或三视图
每个主要场景：一张无人物空镜
核心道具：只有必须跨镜头稳定时才单独生成
特殊状态：只有剧情必须精确控制时才生成状态板
```

只有实际出现：

- 持续换脸；
- 服装或发型漂移；
- 场景布局变化；
- 道具结构变形；
- 手部和交互失败；
- 特殊状态无法控制；

才补充对应的细分参考资产。

## 用户资料优先

用户提供Prompt模板、教程或资料包时：

- 原资料中的角色板、三视图、场景空镜、道具结构、正面提示和负面约束优先；
- 当前项目内容用于填充模板；
- 自行补充的方法必须标记为补充；
- 不得把自由扩写冒充原资料原文。

## 图片与视频Prompt

图片Prompt负责一个静态瞬间、人物和道具状态、构图、机位、光线、色调、材质和输出规则。

视频Prompt负责：

- 指定首帧；
- 唯一主要动作；
- 起势、过程和收住；
- 一种主要运镜；
- 结束状态；
- 声音；
- 禁止变化。

后续分镜优先继承上一张满意分镜，不为每个角度预制独立场景空镜。

## 代表性测试

默认先测试一个普通镜头。项目确实存在复杂变形、多人交互、镜面、特殊道具或高难运镜时，再增加一个高风险镜头。

不固定要求完整核心样片矩阵，也不把测试通过设成单条Prompt任务的阻塞条件。

## 稳定降级

1. 先简化Prompt或局部修图；
2. 简化动作并优先固定镜头；
3. 缩短视频片段；
4. 使用尾帧或硬切；
5. 多人动作拆成反打、局部和结果镜头；
6. 大尺度奇观拆成前兆、发生和结果；
7. 最后才新增参考资产；
8. 保留人物行动、选择和不可逆结果。

## ADAPT禁止

- 用户已有剧本却重新改写故事；
- 用户已有参考图却强制重做完整资产计划；
- 普通短片默认拆出大量面部、发型、服装、手部和多机位资产；
- 所有镜头强制首尾帧；
- 视频Prompt重复大段人物外貌却不写动作终点；
- 为降低制作难度改变谁行动、谁选择或谁承担代价；
- 用旁白替代原作必须由画面表达的核心证据。
