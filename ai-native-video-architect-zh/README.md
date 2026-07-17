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

---

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

示例：

```text
使用 $ai-native-video-architect-zh，
保留人物关系、最后一句台词和开放结尾，
把下面的剧本压缩到两分钟，并让对白更自然。
```

### 3. 诊断概念、剧本或成片

诊断不会把所有非常规设计都当成问题，而是统一分为：

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
- 开放结尾是否真的完成了某些内容；
- 对白是否符合人物和言语行为；
- 机制是否替代人物行动；
- 热梗是否符合人物与当前语境；
- 制作和剪辑是否改变原作含义。

示例：

```text
使用 $ai-native-video-architect-zh，
只诊断下面的剧本，不要替我重写。
请区分真正的错误、有意选择和可选增强项。
```

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

示例：

```text
使用 $ai-native-video-architect-zh，
不要改变人物选择、高潮和结尾，
把这个剧本拆成可生成镜头，
并为多人同框、中文文字和连续动作提供稳定替代方案。
```

---

## 四种工作模式

Skill 会根据自然语言自动判断模式，用户不需要记住命令。

### CREATE｜从零创作

适用于：

- 从主题、人物、情绪或视觉概念开始；
- 建立概念简报、节拍表或完整剧本；
- 生成多个真实不同的创作方向。

### TRANSFORM｜优化与改编

适用于：

- 润色、压缩、扩写；
- 对白自然化；
- 结构优化；
- 商业、文学、实验或类型增强；
- 热梗融合和深度改编。

### DIAGNOSE｜诊断与评分

适用于：

- 只分析不重写；
- 找出剧本为什么失效；
- 比较多个版本；
- 检查改写是否越界；
- 诊断粗剪和成片问题。

### ADAPT｜制作适配

适用于：

- 资产、镜头和生成任务拆解；
- 制作风险控制；
- AI 视频模型稳定性适配；
- 核心样片和三档方案；
- 粗剪与成片回归。

混合任务通常按以下顺序执行：

```text
DIAGNOSE → TRANSFORM → ADAPT
```

---

## 四种创作路径

### COMMERCIAL｜商业路径

关注行动、因果、类型回报、留存、高潮和最后一拍。

### LITERARY｜文学路径

关注人物状态、关系、生活细节、潜台词、克制和余味。

### EXPERIMENTAL｜实验路径

关注形式规则、重复、变奏、声画关系、感知变化和结尾重构。

### HYBRID｜混合路径

允许商业、文学和实验共同存在，但必须明确每条路径分别负责什么，避免平均堆叠。

---

## 设计原则

本项目的核心原则是：

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

---

## 热梗与平台文化

Skill 支持把热梗、热门音频和平台文化用于：

- 标题或包装；
- 人物语言和动作；
- 情境与关系；
- 结构回调；
- 主题、机制或形式。

涉及当前热梗时，应实时确认：

- 原始语境；
- 目标平台和社群；
- 生命周期；
- 饱和与过期风险；
- 人物和类型适配；
- 版权或直接模仿风险。

通常还会准备一个 `TIMELESS_VERSION`，在具体热梗失效后继续保留相同的场景和结构功能。

---

## 安装

### 方法一：克隆仓库

```bash
git clone https://github.com/wlxb625/ai-native-video-architect.git
cd ai-native-video-architect/ai-native-video-architect-zh
```

### Windows 用户级安装

将整个 `ai-native-video-architect-zh` 目录复制到：

```text
%USERPROFILE%\.agents\skills\ai-native-video-architect-zh
```

或者在 Skill 目录运行：

```powershell
.\scripts\install_windows.ps1
```

### macOS / Linux 用户级安装

复制到：

```text
$HOME/.agents/skills/ai-native-video-architect-zh
```

或者运行：

```bash
bash scripts/install_unix.sh
```

### 项目级安装

复制到项目目录：

```text
<项目根目录>/.agents/skills/ai-native-video-architect-zh
```

安装完成后重新开启 Agent 会话，并使用显式调用进行第一次测试。

---

## 快速调用

### 从零创作

```text
使用 $ai-native-video-architect-zh，
根据“一个人每天都在群里回复，却越来越像没有参与过项目”
设计一个两分钟AI短片。
```

### 文学短片

```text
使用 $ai-native-video-architect-zh，
设计一个克制的文学短片。
允许人物被动和开放结尾，不要强行反转或和解。
```

### 实验影像

```text
使用 $ai-native-video-architect-zh，
设计一个固定机位、重复与变奏驱动的实验短片。
明确哪些画面变化是有意的，哪些必须保持稳定。
```

### 剧本优化

```text
使用 $ai-native-video-architect-zh，
保留高潮主体和结尾，只优化下面剧本的中段与对白。
```

### 热梗融合

```text
使用 $ai-native-video-architect-zh，
为这个职场喜剧增加当前平台网感，
但热梗必须符合人物，并同时输出去时效版本。
```

### 制作拆解

```text
使用 $ai-native-video-architect-zh，
把下面剧本转成9:16 AI视频制作包，
包含资产表、镜头表、高风险样片和三档制作方案。
```

---

## 输出深度

- `STANDARD`：概念、单场戏或单条短视频；
- `PROFESSIONAL`：完整剧本、正式发布或制作前；
- `FULL_SYSTEM`：复杂混合路径、多重现实、系列项目；
- `AUDIT`：压力测试、多版本比较和一致性审计。

根据任务，Skill 可以输出：

- Concept Brief；
- Beat Sheet；
- Standard Script；
- Diagnosis Report；
- Transform Contract；
- Production Pack。

---

## 统一评估协议

所有评估使用统一结果：

```yaml
status: PASS | CONDITIONAL | FAIL
design_tags: []
applicability: HIGH | MEDIUM | LOW | NOT_APPLICABLE
evidence: []
risks: []
must_fix: []
should_strengthen: []
must_protect: []
```

有意的高风险或实验设计通常使用：

```yaml
status: PASS
design_tags:
  - HIGH_RISK_WORTH_PRESERVING
  - OPEN_ENDING
  - INTENTIONAL_PASSIVITY
```

而不是因为“不常规”被降级为失败。

---

## 项目目录

```text
ai-native-video-architect-zh/
├── SKILL.md
├── AGENT.md
├── README.md
├── agents/
│   └── openai.yaml
├── modes/
│   ├── create.md
│   ├── transform.md
│   ├── diagnose.md
│   └── adapt.md
├── core/
│   ├── story.md
│   ├── continuity.md
│   ├── dialogue.md
│   ├── transform.md
│   └── production.md
├── controllers/
│   ├── short-video.md
│   ├── comedy.md
│   ├── suspense.md
│   ├── horror.md
│   ├── emotion.md
│   ├── realism.md
│   ├── visual.md
│   └── trend-culture.md
├── evals/
│   ├── semantic-hard-gate.md
│   ├── drama-score.md
│   ├── propagation-score.md
│   ├── character-agency-check.md
│   ├── twist-legality-check.md
│   ├── dialogue-check.md
│   ├── mechanism-overuse-check.md
│   ├── production-score.md
│   └── transform-fidelity-score.md
├── templates/
│   ├── concept-brief.md
│   ├── beat-sheet.md
│   ├── standard-script.md
│   ├── diagnosis-report.md
│   ├── transform-contract.md
│   └── production-pack.md
├── references/
├── tests/
├── audit/
└── scripts/
```

---

## 验证 Skill 包

进入 Skill 目录后运行：

```bash
python scripts/validate_package.py
```

验证脚本会检查：

- `SKILL.md` 元信息；
- 必需目录和文件；
- 四种模式；
- 九项评估；
- 六个模板；
- 安装脚本和清单。

---

## 适合的项目

- 60秒至数分钟的AI短片；
- 竖屏短剧和信息流叙事；
- 现实主义、喜剧、悬疑、恐怖和情感短片；
- 文学性、开放式和弱情节作品；
- 意识流、非线性和形式实验；
- AI原生机制设计；
- 热梗、平台文化和去时效版本；
- 已有剧本的优化与改编；
- 图生视频前的生产规划；
- 粗剪、字幕、声音和成片回归。

它不以单纯生成一条图像提示词、普通文案润色或实时模型参数查询为主要用途。

---

## 当前状态

项目已经完成：

- 四种工作模式；
- 商业、文学、实验和混合路径；
- 核心叙事与制作模块；
- 类型和热梗控制器；
- 九项专项评估；
- 六个正式模板；
- 静态压力测试与一致性审计。

实际输出质量仍会受到所使用模型、上下文长度和制作工具能力影响。涉及当前平台规则、热门音频、模型参数或热梗状态时，应以实时资料为准。