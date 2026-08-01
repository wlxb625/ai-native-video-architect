# AI Native Film Studio V4.4

一套面向 AI Agent 的中文 AI 原生影视创作 Skill。

它不是单独写剧本的提示词，也不是只生成几条画面描述，而是让 Agent 在内部完成从故事设计到逐镜头制作提示词的整条链路，最后交付可以直接用于外部生图、生视频、剪辑和后期工具的制作包。

```text
$ai-native-video-architect-zh
```

## 这个项目能做什么

你可以从一句想法、一份大纲、一个已有剧本、一张参考图、一个镜头或一段已经生成的视频开始。

Skill会根据现有材料自动判断从哪里接手，主要能够完成：

- 从零设计故事、人物、冲突、主题、高潮与结尾；
- 把故事大纲扩展成可拍摄的正式剧本或视觉脚本；
- 诊断并改写已有剧本，使其更适合AI生成式影像；
- 建立统一的视觉圣经，包括人物、场景、道具、色彩、材质和摄影规则；
- 为角色、场景、道具与特殊状态编写参考图Prompt；
- 拆解完整Shot镜头表，明确每镜的开始状态、主要动作和结束状态；
- 为每个镜头设计导演意图、观众位置、摄影、灯光、人物表演和情绪曲线；
- 设计Control Frame，并建立Shot、控制帧和参考资产之间的绑定关系；
- 编写逐镜头生图Prompt、文生视频Prompt和图生视频Prompt；
- 检查人物身份、服装、空间、道具、动作、光线和情绪在相邻镜头中的连续性；
- 对过于复杂、难以生成的镜头进行内部降级和返修；
- 输出一套完整、可复制、可继续制作的AI影视提示词包。

## 四种工作模式

| 模式 | 适合什么任务 |
| --- | --- |
| `CREATE` | 从想法、题材或一句话开始完整创作 |
| `TRANSFORM` | 改造已有故事、小说片段或剧本 |
| `DIAGNOSE` | 只分析问题，不直接重写全部内容 |
| `ADAPT` | 把已经成立的内容转成镜头、控制帧和生成Prompt |

当你要求“全套完成”“从想法做到生图生视频Prompt”或“直接给我完整制作包”时，Skill默认进入：

```text
FULL_CREATION_PACKAGE
```

它会在同一轮中继续完成后续环节，不会在参考图、镜头表或样片处停下来等待逐项确认。

## 完整工作流程

```text
想法、题材或已有剧本
→ 故事结构与正式剧本
→ 视觉圣经
→ 角色、场景和道具资产Prompt
→ 完整Shot镜头表
→ 导演、摄影、灯光和表演设计
→ Control Frame设计与绑定
→ 逐镜头生图Prompt
→ 逐镜头生视频Prompt
→ 连续性、覆盖率和可生成性检查
→ 完整制作提示词包
```

外部生图和视频平台只负责实际生成，前面的创作与制作设计由Agent完成。

## 输入什么都可以开始

你不需要先准备完整剧本。以下任一种材料都可以作为入口：

- 一句话创意或题材；
- 故事梗概、大纲或小说片段；
- 已有剧本或分镜；
- 人物、场景或风格设定；
- 一张参考图或已经生成的首帧；
- 单个镜头需求；
- 一条效果不好的生图或视频Prompt；
- 已经生成的视频片段及其问题描述。

Agent会区分：

- `PLANNED_REFERENCE`：已经设计好编号和Prompt，但图片还没有真实生成；
- `ACTUAL_REFERENCE`：用户已经上传、生成或选定的真实图片。

即使没有真实参考图，也可以先完成整套规划和Prompt，不会因此中断全流程。

## 安装

下载或克隆本仓库，将整个 `ai-native-video-architect-zh` 文件夹复制到Agent的Skills目录。

Windows：

```text
%USERPROFILE%\.agents\skills\ai-native-video-architect-zh
```

macOS / Linux：

```text
$HOME/.agents/skills/ai-native-video-architect-zh
```

不同Agent宿主的Skills目录可能不同，以对应产品的Skill安装规则为准。安装时必须复制整个文件夹，而不是只复制 `SKILL.md`。

## 怎么使用

安装完成后，在对话中直接点名Skill并说明任务即可。

### 1. 从一个想法完成整套制作包

```text
使用 $ai-native-video-architect-zh。
我想做一支3分钟、9:16竖屏的现实主义AI短片，主题是校园排斥，但不要直接表现暴力过程。
请执行 FULL_CREATION_PACKAGE，完成故事、剧本、视觉圣经、资产Prompt、完整镜头表、Control Frame、生图Prompt和逐镜头视频Prompt。
```

### 2. 把已有剧本改造成AI原生版本

```text
使用 $ai-native-video-architect-zh 的 TRANSFORM 模式。
分析下面剧本中不适合AI视频生成的部分，保留人物关系、核心选择和结尾，重写成更适合生成式影像的正式剧本，并继续完成制作提示词包。
```

### 3. 只处理一个镜头

```text
使用 $ai-native-video-architect-zh。
根据我提供的首帧，为这个6秒图生视频镜头编写完整Prompt。保护人物身份和首帧构图，只设置一个核心视觉事件，并写清人物动作、衣料、头发、背景变化、摄影机运动和结束状态。
```

### 4. 只生成图片Prompt

```text
使用 $ai-native-video-architect-zh。
为这个场景编写可直接复制的生图Prompt，明确主体、视觉张力、构图、机位、光线、色彩、材质、背景层次和空间连续性，不要只堆抽象审美词。
```

### 5. 诊断已有内容

```text
使用 $ai-native-video-architect-zh 的 DIAGNOSE 模式。
检查这份剧本和镜头表是否存在节奏断裂、视觉重复、人物动机不足、控制帧缺失、连续性问题或难以生成的镜头。先列出问题和影响，不要直接全部重写。
```

## 最终会得到什么

完整模式通常会交付：

1. 项目定位与创作假设；
2. 故事结构、人物关系和主题设计；
3. 正式剧本或完整视觉脚本；
4. 视觉圣经；
5. 角色、场景、道具和状态资产表及其生图Prompt；
6. 完整Shot镜头总表；
7. 每镜导演意图、摄影方向、灯光方向、表演方向和情绪曲线；
8. Shot与Control Frame绑定表；
9. 全部控制帧或分镜帧生图Prompt；
10. 全部逐镜头文生视频或图生视频Prompt；
11. 连续性、覆盖率、情绪强度和可生成性检查结果；
12. 可直接复制到外部工具使用的最终制作提示词包。

在没有真实生成媒体时，最终状态为：

```text
PROMPT_PACKAGE_READY
```

这表示设计与Prompt已经完成，不代表图片或视频已经通过真实生成验收。

## Control Frame是什么

本项目中的 `CF` 固定表示 **Control Frame（控制帧）**。

它不是角色参考图，也不是独立镜头，而是某个Shot内部用于锁定开始、结束或桥接状态的控制画面。

```text
SH-03
├── CF-SH03-S：开始控制帧
├── CF-SH03-E：结束控制帧
└── CF-SH03-B1：必要时的桥接控制帧
```

每个CF必须属于一个明确的Shot，不能脱离镜头单独存在。

## 人物表演设计

人物镜头不仅写“悲伤”“愤怒”或“害怕”，还会进一步拆解为：

- 人物目标和本镜头即时意图；
- 内部情绪、对外策略与内外矛盾；
- 视线、眼睑、眉、嘴、下颌和微表情；
- 呼吸、姿态、重心、肩背和手部动作；
- 0—5级的起始与结束情绪强度；
- 按时间排列的表演节拍；
- 摄影与灯光如何保证表演可读；
- 下一镜需要继承的结束状态。

空镜会使用环境节奏和观看关系，不会强行套用人物表演字段。

## 强执行契约

本包包含实验性的Contract Skill扩展。

在能够运行包内脚本的Agent环境中，Agent可以通过阶段状态、Schema校验、评分门禁、返修和完成凭证，减少跳步、漏项以及“加载了Skill却仍按模型默认习惯生成”的问题。

普通用户只需要正常调用Skill，不需要手动操作这些内部文件。

开发或调试时可以运行：

```bash
cd ai-native-video-architect-zh
python scripts/contract_runner.py start --request "创作任务"
```

完整协议见：[`contracts/execution-protocol.md`](ai-native-video-architect-zh/contracts/execution-protocol.md)。

无法执行脚本的只读Skill宿主仍可使用本包，但只能进入 `SOFT_CONTRACT` 模式，无法从技术层面强制模型遵守每一道门禁。

## 项目结构

```text
ai-native-video-architect-zh/
├── SKILL.md                 # Skill入口与完整执行规则
├── controllers/             # 导演、摄影、灯光、表演与全流程控制器
├── prompt-engineering/      # 资产、生图、视频和连续性Prompt编译规则
├── references/              # 情绪、叙事和专业参考资料
├── templates/               # 剧本、镜头表和完整制作包模板
├── evals/                   # 完整性、连续性与质量检查
├── contracts/               # 强执行协议与工作流
├── constitution/            # 不可变规则层
├── schemas/                 # 结构化校验Schema
├── scripts/                 # 校验与契约运行脚本
└── tests/                   # 测试文件
```

## 本地校验

```bash
cd ai-native-video-architect-zh
python scripts/validate_package.py
python scripts/verify_contract.py
python tests/test_meaning_gate.py
```

## 使用边界

- 本Skill负责创作、制作设计和Prompt编译，本身不直接生成图片或视频；
- 没有真实图片或视频时，只能完成规划层连续性检查，不能声称通过真实媒体验收；
- 不同生图和视频模型的能力不同，最终Prompt仍可能需要根据具体平台做少量适配；
- 复杂动作、多人交互、精确物理变化和长时间连续表演仍可能需要拆镜或分段生成；
- Skill会尽量减少无意义的逐步确认，但不会替代用户对题材、版权、安全和最终发布结果的判断。

## 许可证

本项目按照仓库中的 [`LICENSE`](LICENSE) 发布。
