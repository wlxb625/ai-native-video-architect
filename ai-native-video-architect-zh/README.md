# AI Native Film Studio V4.0

## 从剧本到生图、图生视频和成片的完整中文Skill

显式调用：

```text
$ai-native-video-architect-zh
```

V4.0保留原有故事、剧本、导演、资产与分镜能力，并把用户提供的专业AI生图和视频Prompt工程规范整理成可调用模块，正式覆盖剧本确认后的全部生产步骤。

## 完整流程

```text
S00 创作需求
→ S01 创意方向
→ S02 故事方案
→ S03 剧本或视觉脚本
→ S04 剧本拆解
→ S05 视觉圣经
→ S06 资产计划
→ S07 整批资产Prompt与资产制作
→ S08 用户自审与资产确认
→ S09 分镜设计
→ S10 整批分镜帧Prompt
→ S11 核心样片
→ S12 整批视频生产与后期
→ S13 导演审查与交付
```

## V4.0解决了什么

### 1. 不再凭通用经验自由写Prompt

剧本完成后必须读取内置Prompt工程模块：

- 图片Prompt基础公式；
- 主色、辅助色、点缀色、色温、饱和度和对比度；
- 光源、方向、光色、受光对象和暗部；
- 角色板、三视图、面部、服装和交互；
- 场景主布局、空镜和多机位；
- 道具结构、尺寸和状态链；
- 图生图、局部修改、降噪和4K增强；
- 首帧、尾帧、图生视频和硬切；
- 动作、环境、台词和声音；
- 固定、推、拉、摇、移、跟拍、环绕、升降、FPV、焦点转移等运镜；
- 抽尾帧续拍、多角度防穿帮和失败修复。

### 2. 阶段一次性交付

默认批次单位是阶段，不是单张图片：

- S07一次性给完全部资产Prompt；
- S09一次性给完整镜头表；
- S10一次性给完全部首尾帧Prompt；
- S11一次性给核心样片测试包；
- S12一次性给完整视频Prompt和后期包。

内容很长时可以分章节，但在同一轮完整交付，不要求用户每生成一张图就回来。

### 3. 单资产一块完整复制

每个资产块同时包含：

- 资产用途；
- 前置参考图和参考职责；
- 必须保持和允许变化；
- 完整正向Prompt；
- 针对性负面Prompt；
- 输出规则；
- 稳定生成方案；
- 修改与修复Prompt；
- 文件命名和后续依赖。

不会把全局Prompt、负面Prompt和输出规则拆散后让用户自行拼接。

### 4. 用户默认自行审核

S08默认为`USER_SELF_AUDIT`。用户在外部软件里生成、筛选和修改，完成后回复：

```text
下一步
```

Skill就把当前阶段视为用户已确认并进入下一阶段。

只有用户明确说“帮我审核这张图”时，才由Skill辅助检查候选图。

### 5. “下一步”表示下一个阶段

当当前阶段已经整批交付时，“下一步”不会被理解成下一个资产或下一张图。

只有用户明确说“逐项来”“下一个资产”时，才在同一阶段内部继续。

## 图片Prompt公式

```text
主体 + 场景环境 + 静态动作瞬间 + 服饰道具
+ 景别 + 机位 + 构图 + 光线色调
+ 材质真实度 + 风格 + 比例 + 负面约束
```

图片只负责一个准确瞬间，不负责完整动作过程。

## 视频Prompt公式

```text
唯一首帧 + 视频类型 + 场景 + 主体 + 起始状态
+ 动作过程 + 运镜 + 光线色调 + 风格
+ 稳定要求 + 结尾 + 声音 + 负面约束
```

短镜头只保留一个主要动作和一种主要运镜。

## 色调与光影

色调不是单一滤镜。每个项目锁定：

```text
主色 + 辅助色 + 点缀色 + 色温 + 饱和度 + 对比度
```

光影锁定：

```text
真实光源 + 方向 + 光色 + 照亮对象 + 暗部层次 + 情绪目的
```

## 新增核心文件

### 编排

- `controllers/post-script-production.md`

### Prompt工程

- `prompt-engineering/image-prompt-compiler.md`
- `prompt-engineering/visual-style-color-light.md`
- `prompt-engineering/asset-prompt-system.md`
- `prompt-engineering/storyboard-frame-system.md`
- `prompt-engineering/video-prompt-compiler.md`
- `prompt-engineering/camera-movement-library.md`
- `prompt-engineering/continuity-repair-system.md`

### 模板

- `templates/asset-prompt-block.md`
- `templates/storyboard-frame-prompt-block.md`
- `templates/video-shot-prompt-block.md`

### 评估和测试

- `evals/prompt-production-readiness-score.md`
- `tests/post-script-prompt-pipeline-stress-tests.md`

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

Skill保存长期稳定的创作、图片和视频Prompt工程原则，不永久写死具体模型版本、价格、额度和平台规则。涉及当前工具能力时需要实时核实。
