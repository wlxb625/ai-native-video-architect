# AI Native Film Studio V4.1

## 从创意、剧本到生图、分镜和视频Prompt的完整中文Skill

显式调用：

```text
$ai-native-video-architect-zh
```

这个Skill同时负责两部分工作：

```text
创意、故事与剧本创作
+
剧本确认后的AI图片与视频Prompt生产
```

用户不需要在剧本完成后切换到另一个Skill。

## 能力入口

### 从零创作

从想法、人物、题材或情绪开始，完成故事方案、人物关系、完整剧本或视觉脚本，然后继续后续制作。

### 使用已有作品

已有大纲、剧本或视觉脚本时，保护用户明确要求保留的内容，直接进行诊断、改写或AI制作适配。

### 使用已有参考图

已有角色图、场景图、道具图或分镜图时，直接作为参考继续生成缺失的分镜帧Prompt、视频Prompt或修复方案。

### 单独调用某项能力

用户只需要角色板、场景空镜、某个分镜、首尾帧或单个视频Prompt时，直接处理该任务，不要求补做无关步骤。

## 故事与剧本模块

故事创作会根据项目类型建立：

- 一句话故事；
- 主角目标；
- 核心关系、规则或冲突；
- 递进方式；
- 关键选择；
- 高潮；
- 最后图像；
- 与目标时长匹配的节奏。

支持：

- 对白剧情片；
- 无对白视觉短片；
- 广告和MV；
- 意识流和实验影像；
- 已有剧本改写；
- 现有作品AI制作适配。

剧本确认后，继续调用下游Prompt工程模块。

## 剧本后生产模块

### 1. 剧本制作拆解

从剧本提取真正影响生成的内容：

- 主要人物；
- 可见服装与状态变化；
- 主要场景和空间锚点；
- 核心道具和状态；
- 镜头主要动作；
- 光线、天气和色调；
- 声音、剪辑连接和高风险内容。

不为了显示专业而增加剧本不需要的资产。

### 2. 视觉设定

统一：

```text
整体风格
+ 主色、辅助色、点缀色
+ 色温、饱和度、对比度
+ 真实光源和方向
+ 人物、场景和道具材质
+ 摄影与构图倾向
+ 禁止风格
```

### 3. 核心参考图Prompt

普通短片默认只制作最必要的参考图：

- 每名主要角色一张综合角色板或三视图；
- 每个主要场景一张无人物空镜；
- 必须稳定的核心道具结构或状态板；
- 剧情必须控制的特殊变化状态板。

独立面部、发型、服装、手部、多机位和技术测试均为按需升级内容。

角色和场景Prompt优先采用用户提供资料中的原始模板结构，再填入当前项目设定。

### 4. 分镜设计

一次性完成整片镜头表，每个镜头明确：

- 镜头目的；
- 一个主要动作；
- 景别、角度和构图；
- 运镜及其动机；
- 输入和输出状态；
- 时长、声音和剪辑连接；
- 角色、场景和道具参考。

### 5. 分镜帧Prompt

第一张分镜：

```text
角色参考 + 场景空镜 + 道具参考 + 当前镜头要求
```

后续分镜：

```text
角色参考 + 场景空镜 + 上一张满意分镜 + 当前镜头要求
```

图片Prompt只描述一个准确静态瞬间：

```text
主体 + 场景 + 静态动作瞬间 + 服饰道具
+ 景别 + 机位 + 构图 + 光线色调
+ 材质真实度 + 风格 + 比例 + 负面约束
```

只有动作终点、状态变化或生成模型需要时才增加尾帧。

### 6. 图生视频Prompt

视频Prompt负责：

```text
唯一首帧
+ 起始状态
+ 一个主要动作
+ 动作方向、速度和幅度
+ 一种主要运镜
+ 场景稳定要求
+ 结束状态
+ 声音
+ 负面约束
```

图片决定画面是什么，视频Prompt决定人物和摄影机怎么动。

### 7. 连续性与修复

保持：

- 人物身份、年龄、发型和服装；
- 场景布局和主光方向；
- 道具结构、位置和状态；
- 左右手、屏幕方向和动作进度；
- 上一镜结束状态与下一镜开始状态。

失败时优先局部修复、简化动作、固定机位、缩短片段、增加尾帧或硬切，最后才新增参考资产。

## 用户资料优先规则

当用户提供Prompt工程资料、教程或模板时：

- 必须先读取相关原文；
- 原资料结构、主体Prompt、负面约束和输出方式优先；
- 当前项目设定用于填充模板；
- 自行补充内容必须与原资料区分；
- 不得把自由扩写冒充原资料内容。

## 内部文件

### 剧本后编排

- `controllers/post-script-production.md`

### 图片与资产Prompt

- `prompt-engineering/image-prompt-compiler.md`
- `prompt-engineering/visual-style-color-light.md`
- `prompt-engineering/asset-prompt-system.md`

### 分镜与视频Prompt

- `prompt-engineering/storyboard-frame-system.md`
- `prompt-engineering/video-prompt-compiler.md`
- `prompt-engineering/camera-movement-library.md`
- `prompt-engineering/continuity-repair-system.md`

### 输出模板

- `templates/asset-prompt-block.md`
- `templates/storyboard-frame-prompt-block.md`
- `templates/video-shot-prompt-block.md`

## 交付方式

Skill会根据用户当前拥有的成果，直接输出所需内容：

- 创意方向；
- 故事方案；
- 剧本或视觉脚本；
- 视觉设定；
- 参考图Prompt包；
- 分镜镜头表；
- 分镜帧Prompt包；
- 视频Prompt包；
- 修复和后期方案。

内部可以记录项目位置，但不会把阶段编号和进度卡强制展示给用户。用户要求按步骤推进或询问进度时才显示。

## 安装

```bash
git clone https://github.com/wlxb625/ai-native-video-architect.git
cd ai-native-video-architect/ai-native-video-architect-zh
```

复制到：

```text
Windows: %USERPROFILE%\.agents\skills\ai-native-video-architect-zh
macOS/Linux: $HOME/.agents/skills/ai-native-video-architect-zh
```

## 验证

```bash
python scripts/validate_package.py
```

## 当前边界

Skill负责创作、导演设计和Prompt生产，不直接替代外部生图、视频生成、剪辑和声音软件。具体模型版本、价格、额度和平台规则不会永久写死，涉及当前工具能力时需要实时核实。
