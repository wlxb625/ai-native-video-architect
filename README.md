# AI 视频剧本架构师 V2

一套面向 **AI 短片、短剧、叙事视频、广告概念片、MV 与实验影像** 的中文 Skill。

它不只是生成故事梗概或视频提示词，而是把灵感、人物处境、已有剧本、热点或粗剪，转化为一套完整的 AI 视频创作与制作系统：

```text
创作定位
→ 人物、关系与结构
→ 对白、反转与机制
→ 传播和平台文化
→ 资产与镜头拆解
→ 制作风险与备用方案
→ 粗剪和成片回归
```

显式调用名称：

```text
$ai-native-video-architect-zh
```

## 它能做什么

### 1. 从零创作 AI 视频

你可以只提供一句想法、一个人物、一种情绪、一个场景或一个视觉规则，Skill 会逐步完成：

- 项目定位与主要创作路径；
- 一句话概念和核心体验；
- 人物、关系、阻力与能动性；
- 商业、文学或实验结构；
- 中段变化、高潮和结尾；
- 对白、视觉和声音策略；
- 热梗与平台文化判断；
- 初步制作风险和落地方案。

示例：

```text
使用 $ai-native-video-architect-zh，
帮我设计一个90秒现实主义竖屏短片：
一个员工被要求签署一份不属于自己的责任确认。
不要爽文式反击，结尾只取得有限结果。
```

### 2. 优化或改编已有剧本

Skill 使用五级改写体系：

| 等级 | 主要用途 |
|---|---|
| Level 0 | 错字、标点和格式校对 |
| Level 1 | 语言自然化、压缩和轻度优化 |
| Level 2 | 信息顺序、场景和中段结构优化 |
| Level 3 | 商业、文学、实验、类型或热梗方向增强 |
| Level 4 | 获得明确授权后的深度改编 |

改写前会区分：

- 必须保留；
- 允许调整；
- 明确允许改变；
- 明确禁止；
- 变化预算；
- 改写后的收益与损失。

### 3. 诊断概念、剧本或成片

诊断统一分为：

- `BUG`：真实错误或失控；
- `RISK`：目前成立但存在失败风险；
- `CHOICE`：有意创作选择；
- `OPPORTUNITY`：可选增强方向；
- `PREFERENCE`：审美或市场偏好。

可检查：

- 事实和人物知识是否矛盾；
- 人物是否真正参与变化；
- 中段是否只是重复；
- 反转是否公平；
- 开放结尾是否真正完成了某些内容；
- 对白是否符合人物和言语行为；
- 机制是否替代人物行动；
- 热梗是否符合人物与当前语境；
- 制作和剪辑是否改变原作含义。

### 4. 转译为可制作的 AI 视频方案

当剧本已经成立时，Skill 可以进入制作适配：

- 角色、场景、道具、文字与声音资产；
- 镜头和动作拆分；
- 多人同框与口型处理；
- 关键文字后期方案；
- 允许漂移与禁止漂移；
- 高风险镜头和核心样片；
- 理想、稳定、最低成本三档方案；
- 单点失败与备用镜头；
- 粗剪、声音、字幕和结尾回归。

## 四种工作模式

Skill 会根据自然语言自动判断模式，用户不需要记住命令。

- `CREATE`：从主题、人物、情绪或视觉概念开始，建立概念、节拍和剧本。
- `TRANSFORM`：润色、压缩、扩写、结构优化、方向增强或深度改编。
- `DIAGNOSE`：只分析不重写，诊断剧本、版本、粗剪和成片。
- `ADAPT`：拆解资产、镜头、声音、后期和制作风险。

混合任务通常按以下顺序执行：

```text
DIAGNOSE → TRANSFORM → ADAPT
```

## 四种创作路径

- `COMMERCIAL`：行动、因果、类型回报、留存、高潮和最后一拍。
- `LITERARY`：人物状态、关系、生活细节、潜台词、克制和余味。
- `EXPERIMENTAL`：形式规则、重复、变奏、声画关系、感知变化和结尾重构。
- `HYBRID`：允许多条路径共同存在，但必须明确各自职责。

## 核心原则

> 规则用于防止作品无意失控，而不是阻止创作者有意选择开放、被动、反高潮、非线性、梦境逻辑或形式实验。

因此，以下设计不会被自动判错：

- 开放结尾；
- 有意被动；
- 现实主义有限结果；
- 反高潮；
- 多义反转；
- 弱情节；
- 日常对白和沉默；
- 非线性与碎片化；
- 梦境、象征或形式因果；
- 视觉、声音、字幕或空间成为主体。

系统真正检查的是：

```text
这项规则是否被建立？
是否被持续执行或有意打破？
预期效果是否真正实现？
```

## 热梗与平台文化

Skill 支持把热梗、热门音频和平台文化用于：

- 标题或包装；
- 人物语言和动作；
- 情境与关系；
- 结构回调；
- 主题、机制或形式。

涉及当前热梗时，应实时确认原始语境、目标平台、生命周期、饱和风险、人物适配和版权风险。通常还会准备一个 `TIMELESS_VERSION`。

## 安装

### 克隆仓库

```bash
git clone https://github.com/wlxb625/ai-native-video-architect.git
cd ai-native-video-architect/ai-native-video-architect-zh
```

### Windows

复制整个 `ai-native-video-architect-zh` 目录到：

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

复制到项目目录：

```text
<项目根目录>/.agents/skills/ai-native-video-architect-zh
```

安装完成后重新开启 Agent 会话，并使用显式调用进行第一次测试。

## 快速调用

### 从零创作

```text
使用 $ai-native-video-architect-zh，
根据“一个人每天都在群里回复，却越来越像没有参与过项目”
设计一个两分钟AI短片。
```

### 只诊断

```text
使用 $ai-native-video-architect-zh，
只诊断下面的剧本，不要替我重写。
请区分真实错误、有意选择和可选增强项。
```

### 剧本优化

```text
使用 $ai-native-video-architect-zh，
保留人物关系、高潮主体和开放结尾，
只优化下面剧本的中段与对白。
```

### 制作适配

```text
使用 $ai-native-video-architect-zh，
不要改变人物选择、高潮和结尾，
把这个剧本拆成可生成镜头，
并为多人同框、中文文字和连续动作提供稳定替代方案。
```

## 输出模板

- `templates/concept-brief.md`：概念简报；
- `templates/beat-sheet.md`：节拍表；
- `templates/standard-script.md`：标准剧本；
- `templates/diagnosis-report.md`：诊断报告；
- `templates/transform-contract.md`：改写保护合同；
- `templates/production-pack.md`：完整制作包。

## 项目结构

```text
ai-native-video-architect-zh/
├── SKILL.md
├── AGENT.md
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

## 验证

```bash
python scripts/validate_package.py
```

验证内容包括必需文件、Markdown 文件、内部路径和 Skill 元数据。

## 当前边界

本项目是一套创作与制作规范，不会永久写死：

- 某个视频模型的最新参数；
- 平台当前算法规则；
- 当前热梗榜单；
- 热门音频的实时版权状态。

这些信息在实际任务中需要根据最新公开资料确认。
