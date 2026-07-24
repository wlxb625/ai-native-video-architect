# AI Native Film Studio V3.0

## AI原生电影导演工作室

一套面向 **AI短片、叙事视频、无对白视觉电影、高概念科幻、广告概念片、MV、实验影像和AI电影生产** 的中文Skill。

显式调用：

```text
$ai-native-video-architect-zh
```

它不只生成剧本或提示词，而是把一个想法逐步转化为：

```text
概念
→ 人物与世界关系
→ 视觉叙事
→ 镜头语言
→ Style DNA
→ 视觉、角色与场景锁定
→ AI生成方案
→ 制片管理
→ 声音设计
→ 传播适配
→ 导演审查
```

## V3解决什么

很多AI视频的问题不是没有漂亮画面，而是：

- 世界很大，但人物不知道要做什么；
- 画面很强，但观众看不出人物关系；
- 分镜写了景别和运镜，却没有观看目的；
- 角色、场景和道具在镜头之间漂移；
- 高难度镜头失败后没有替代方案；
- 声音只是铺音乐；
- 传播优化改变了原本的主题和结尾。

V3把这些问题拆成独立但可协同的导演模块。

## 双重路由

### 四种操作模式

- `CREATE`：从零创造概念、结构、剧本或导演包；
- `TRANSFORM`：在保护合同内修改已有作品；
- `DIAGNOSE`：只诊断，不默认重写；
- `ADAPT`：把已成立作品转译为生产方案。

### 五种导演模式

- `STORY_DIRECTOR`：人物任务、冲突、选择和结尾；
- `VISUAL_DIRECTOR`：用人物、动作、空间、物件和声画表达；
- `BLOCKBUSTER_DIRECTOR`：高概念、大片尺度和不可逆代价；
- `EXPERIMENTAL_DIRECTOR`：形式、重复、梦境、感知和声音；
- `PRODUCTION_DIRECTOR`：资产、镜头、生成、成本和后期。

用户不需要记住模式名称，Skill会根据自然语言自动选择。

## 九阶段导演工作流

1. 创作意图和目标输出层级；
2. 一句话概念、单一机制、人物任务和最后图像；
3. 人物—世界关系、重复动作和视觉母题；
4. 镜头目的、揭示顺序和声画关系；
5. 原创Style DNA；
6. 视觉圣经、角色锁定和环境锁定；
7. 镜头优先级、成本、生成顺序和失败恢复；
8. 世界声、人物声、声音母题和沉默；
9. 传播适配和导演审查。

完整流程定义在：

- `config/modes.yaml`
- `config/workflow.yaml`
- `config/scoring.yaml`

## 核心能力

### 高概念压缩

在展开世界观前，先确认：

- 一句话概念；
- 单一核心机制；
- 单一人物任务；
- 不可逆压力；
- 艰难选择；
- 三至五个因果化核心画面；
- 最后一幅画面。

世界可以巨大，但故事不能依赖一串术语才能理解。

### 视觉叙事

视觉叙事不是没有故事，而是让故事进入：

- 人物重复动作；
- 物件状态；
- 空间被使用的痕迹；
- 人物与世界的关系；
- 图像在后段被重新理解；
- 声音的提前、延后、缺席和余留。

核心控制器：`controllers/visual-narrative.md`。

### 镜头语言

每个正式镜头定义：

- 镜头目的；
- 输入状态和输出状态；
- 景别、机位、运镜和时长；
- 第一视觉重心；
- 揭示顺序；
- 情绪和声音；
- AI生成风险；
- 稳定替代。

核心控制器：`controllers/camera-language.md`。

### AI生产与制片

先锁定：

- Visual Bible；
- Character Lock；
- Environment Lock；
- Shot Contract；
- Sound Bible。

再按S/A/B/C管理镜头价值和资源，优先制作标志镜头、高潮、高风险镜头和核心样片。

核心控制器：

- `controllers/ai-production.md`
- `controllers/production-management.md`

### Style DNA

参考作品会被拆成空间、人物尺度、时间感、色彩、材质、摄影气质和声音参数，再组合为项目自己的原创语言。

不会只用创作者姓名替代设计，也不会复制具体镜头、角色、场景或台词。

### 声音设计

声音分为：

- 世界声音；
- 人物声音；
- 主题声音母题。

同时设计音乐进入与退出、空间层级、主动沉默和必要的Voice Bible。

### 传播优化

按需提供前三秒钩子、标志镜头、一句话复述、讨论空间、二刷证据和多时长版本。

传播优化不得改变人物选择、事实、现实主义有限结果或结尾开放程度。

## 输出层级

- `CONCEPT_DIRECTION`：适合早期判断方向；
- `DEVELOPMENT_PACKAGE`：概念、视觉圣经、人物、母题和结构；
- `DIRECTOR_PACKAGE`：完整镜头、声音、风格和导演审查；
- `PRODUCTION_PACK`：资产、逐镜头Prompt、生成顺序、风险、替代和后期。

Skill默认输出当前真正需要的最小层级，不会第一次就机械展开全部文档。

## 快速使用

### 高概念科幻

```text
使用 $ai-native-video-architect-zh，
帮我设计一个3分钟科幻短片：飞船必须燃烧人的记忆才能跃迁。
先给概念方向和最后图像，不要直接写完整剧本。
```

### 视觉叙事

```text
使用 $ai-native-video-architect-zh，
设计一个无对白视觉短片，用一个角色、一个空间和三个重复物件表达等待。
不要抽象概念图，要让人物行动和画面自己讲故事。
```

### 剧本视觉化改写

```text
使用 $ai-native-video-architect-zh，
保留人物关系、高潮和开放结尾，
把下面这份解释性对白过多的剧本改成视觉叙事版本。
先列出哪些信息可以转成动作、物件、空间和声音。
```

### 逐镜头制作

```text
使用 $ai-native-video-architect-zh，
不要改变人物选择和结尾，
把这个剧本做成Director Package和Production Pack。
为每个S/A镜头提供稳定替代。
```

### 只诊断

```text
使用 $ai-native-video-architect-zh，
只诊断这个分镜，不要重写。
重点检查视觉壁纸、无动机运镜、揭示顺序、连续性和AI生成风险。
```

## 模板

- `templates/concept-brief.md`
- `templates/visual-bible.md`
- `templates/visual-narrative-board.md`
- `templates/camera-shot-plan.md`
- `templates/director-package.md`
- `templates/production-pack.md`
- `templates/standard-script.md`
- `templates/diagnosis-report.md`
- `templates/transform-contract.md`

## 示例

- `references/examples/high-concept-scifi-memory-fuel.md`
- `references/examples/visual-narrative-last-gardener.md`
- `references/examples/commercial-workplace.md`
- `references/examples/literary-open-ending.md`
- `references/examples/experimental-corridor.md`

## 安装

### 克隆仓库

```bash
git clone https://github.com/wlxb625/ai-native-video-architect.git
cd ai-native-video-architect/ai-native-video-architect-zh
```

### Windows

复制整个目录到：

```text
%USERPROFILE%\.agents\skills\ai-native-video-architect-zh
```

或运行：

```powershell
.\scripts\install_windows.ps1
```

### macOS / Linux

复制到：

```text
$HOME/.agents/skills/ai-native-video-architect-zh
```

或运行：

```bash
bash scripts/install_unix.sh
```

### 项目级安装

复制到：

```text
<项目根目录>/.agents/skills/ai-native-video-architect-zh
```

安装后重新开启Agent会话，并通过显式调用进行第一次测试。

## 验证

```bash
python scripts/validate_package.py
```

验证包括：必需文件、V3版本、导演模式、核心控制器、评估器、模板、示例、清单和编码。

## 项目结构

```text
ai-native-video-architect-zh/
├── SKILL.md
├── AGENT.md
├── config/
├── modes/
├── core/
├── controllers/
├── evals/
├── templates/
├── references/
├── tests/
├── audit/
└── scripts/
```

## 当前边界

本项目保存创作和制作原则，不永久写死：

- 视频模型最新能力和参数；
- 工具价格和额度；
- 平台当前算法；
- 热梗生命周期；
- 热门音频和参考素材的实时版权状态。

实际任务中应根据最新公开信息进行核实。

## 一句话定位

> 从一个想法开始，建立一个观众能够经历、AI能够制作、剪辑能够完成，并且只属于这个项目的电影世界。
