# CREATE Mode V4.1

从原始灵感建立故事、剧本或视觉脚本，并在剧本确认后继续完成AI生图、分镜帧、视频Prompt和后期方案。

## 启动协议

先判断用户已经提供：

- 模糊想法；
- 明确方向；
- 故事梗概；
- 完整剧本；
- 参考图；
- 分镜或视频片段。

只补齐当前真正缺失的内容。用户已有成熟成果时直接继续，不强制从头开始，也不默认显示阶段编号。

然后确定：

1. 操作模式：`CREATE`；
2. 主导演模式；
3. 创作路径：`COMMERCIAL` / `LITERARY` / `EXPERIMENTAL` / `HYBRID`；
4. 本轮需要交付的具体结果。

## 创意与故事

方向不足时，确认类型、情绪、形式、主角、关系、场景范围、时长、画幅、声音和禁忌。已经给出的信息不得重复询问。

需要探索时给出2至3个真正不同的方向，差异来自：

- 人物任务；
- 核心事件、冲突或视觉规则；
- 递进方式；
- 关键选择；
- 结尾；
- 制作难度。

不得只更换美术风格。

故事方案至少建立：

```yaml
story_treatment:
  one_sentence_story:
  protagonist_or_subject:
  primary_task_or_visual_action:
  central_event_or_rule:
  progression:
  key_choice:
  climax:
  emotional_arc:
  final_image:
```

高概念项目同时检查单一机制、不可逆压力、艰难选择和因果化核心画面。

## 剧本或视觉脚本

正式整片Prompt生产前必须有可制作文本。

### 剧情剧本

至少包含：

- 场次、时间和地点；
- 人物与当前状态；
- 可观察动作；
- 对白或无对白设计；
- 道具和环境变化；
- 场景结束状态；
- 下一场连接。

### 视觉脚本

至少包含：

```yaml
visual_scene:
  location_and_time:
  subject:
  initial_state:
  observable_action:
  environment_change:
  prop_change:
  emotional_change:
  final_state:
  next_scene_connection:
```

无对白不等于没有剧本。只有一句概念或互不相关的意象时，先补成完整视觉脚本。

## 剧本确认后的继续创作

剧本由CREATE模式完成并确认后，不结束任务，也不要求切换Skill。按需读取：

- `controllers/post-script-production.md`
- `prompt-engineering/image-prompt-compiler.md`
- `prompt-engineering/visual-style-color-light.md`
- `prompt-engineering/asset-prompt-system.md`
- `prompt-engineering/storyboard-frame-system.md`
- `prompt-engineering/video-prompt-compiler.md`
- `prompt-engineering/camera-movement-library.md`
- `prompt-engineering/continuity-repair-system.md`

然后继续完成用户需要的：

- 剧本制作拆解；
- 视觉设定；
- 核心参考图Prompt；
- 完整分镜镜头表；
- 分镜帧Prompt；
- 图生视频Prompt；
- 连续性、修复和后期方案。

## 核心参考原则

普通短片默认只做最必要参考：

- 每个主要角色一张三视图或综合角色板；
- 每个主要场景一张无人物空镜；
- 必须稳定的核心道具一张结构或状态板；
- 剧情必须控制的特殊变化一张状态板。

不默认拆分面部、发型、服装、鞋履、手部、动作和多机位空镜。只有实际失败后才补。

## 分镜与Prompt

先设计镜头，再写Prompt。

每镜明确：

- 镜头目的；
- 一个主要动作；
- 景别、角度、构图和轴线；
- 运镜及动机；
- 输入与输出状态；
- 时长、声音和剪辑连接；
- 参考图。

第一张分镜使用角色参考、场景空镜和当前镜头要求；后续分镜优先继承上一张满意分镜。

图片Prompt负责一个静态瞬间。视频Prompt负责唯一首帧、一个主要动作、一种主要运镜和明确结束状态。

不是每个镜头都需要尾帧。只有动作终点、状态变化或生成模型需要时才增加。

## 用户资料

用户提供Prompt教程、模板或资料包时，先读取原文并使用原模板结构。自行补充的稳定方法、修复方案和负面约束必须与原资料明确区分。

## 代表性测试

普通项目默认测试一个代表性普通镜头。确实存在复杂变形、多人交互、镜面、特殊动作或复杂运镜时，再增加一个高风险镜头测试。

不固定要求3至5个样片，也不要求角色和场景全部跨两个角度后才继续。

## CREATE禁止

- 用户已有成熟内容却强制从创意访谈开始；
- 剧本完成后停止，无法继续生成生图、分镜和视频Prompt；
- 只有概念就批量写整片视频Prompt；
- 普通短片默认建立完整影视资产库；
- 所有镜头强制首尾帧；
- 用户提供资料却凭经验自由改写并声称来自原资料；
- 强制所有作品反击、获胜、反转或封闭结尾；
- 把意识流理解为互不相关的超现实画面拼贴；
- 把用户变成逐资产、逐镜头确认操作员。
