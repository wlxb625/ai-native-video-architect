# AI Native Film Studio V4.4

一套在Agent内部完成 **故事、剧本、视觉资产、导演意图、摄影指导、逐镜灯光、人物表演、情绪曲线、Control Frame、生图Prompt、生视频Prompt和内部连续性检查** 的中文AI原生影视创作Skill。

```text
$ai-native-video-architect-zh
```

## V4.4新增什么

### 提示词视觉密度修订

本修订不增加用户需要选择的新模块，也不改变调用方式。生图、文生视频、图生视频和分镜Prompt仍由原流程自动输出，但默认增加：

- 抽象审美词必须落地为构图、光线、色彩、空间和材质；
- 剧情图片必须明确视觉张力来源，背景作为第二视觉主体参与表达；
- 图生视频先保护首帧，再围绕一个核心视觉事件编排人物、材质、背景和摄影机；
- 头发、内外层衣料、丝带、水、雾等分别描述运动速度和轨迹；
- 背景必须有形成过程、视觉高潮和结束状态；
- 短镜头最后1—2秒必须形成清晰峰值并收住；
- 技术型身份板、三视图和结构板仍以清晰、中性和可复用为先。

用户仍然只需提出“生成生图Prompt”“根据此图生成视频Prompt”或“完成全套制作包”，无需理解内部规则。

V4.3解决了Shot、CF、参考图和Prompt断层；V4.4继续解决“画面完整但没有戏”：

- 每个Shot先写导演意图、观众位置、信息优先级和揭示顺序；
- 摄影不再只填景别和焦段，而是说明为什么这样拍；
- 灯光增加可读性目标、情绪功能、表演关键区域和有动机变化；
- 人物表演拆成目标、内部情绪、对外策略、内外矛盾、微表情、呼吸、姿态、重心、手部和情绪强度；
- 4—6秒镜头默认只有一个主要情绪转折；
- 支持克制哭戏、单颗泪水、压住恐惧、隐忍愤怒、羞耻、怀疑、释然等可执行表演；
- 支持`FULL_PERFORMANCE_PROMPT`长提示词模式，但禁止重复堆词；
- 增加摄影—灯光—表演一致性和情绪强度连续性检查。

## 核心闭环

```text
想法或已有剧本
→ 完整剧本/视觉脚本
→ 视觉圣经与规划资产Prompt
→ 全片导演、摄影、灯光与表演基准
→ 完整Shot总表
→ 每镜导演意图、摄影、灯光、表演与情绪曲线
→ Shot–CF绑定
→ 全部控制帧生图Prompt
→ 全部逐镜头生视频Prompt
→ 内部连续性、情绪强度、冲突、覆盖率与可生成性返修
→ 完整制作提示词包
```

## CF定义

CF固定表示 **Control Frame（控制帧）**，只能属于一个Shot。

## 每个人物Shot都必须交付

- 人物目标与本镜头即时意图；
- 内部情绪、对外策略和内外矛盾；
- 起始与结束情绪强度0—5；
- 视线、眼睑、眉、嘴、下颌；
- 呼吸、肩背、姿态、重心、左右手；
- 分秒情绪节拍；
- 摄影和灯光如何让表演可读；
- 禁止夸张表演；
- 下一镜继承的表演结束状态。

空镜使用`NON_CHARACTER_PERFORMANCE`并填写环境节奏与观看关系，不得留空。

## 安装

复制整个`ai-native-video-architect-zh`文件夹到：

Windows：`%USERPROFILE%\.agents\skills\ai-native-video-architect-zh`

macOS / Linux：`$HOME/.agents/skills/ai-native-video-architect-zh`

校验：

```bash
python scripts/validate_package.py
```

## 照骨实测调用

```text
使用 $ai-native-video-architect-zh V4.4。以《照骨》完成FULL_CREATION_PACKAGE。所有检查在Agent内部完成，不等待真实参考图。除剧本、视觉圣经、资产Prompt、完整Shot、CF、生图和视频Prompt外，每个Shot必须提供导演意图、观众位置、摄影方向、逐镜灯光方向；所有人物镜头必须提供人物目标、内部情绪、对外策略、内外矛盾、微表情、呼吸、身体语言、0—5情绪强度和分秒情绪曲线。输出核心表演Prompt和可直接复制的FULL_PERFORMANCE_PROMPT。检查摄影、灯光和表演是否互相支持，并确保上一镜结束表演状态能够衔接下一镜开始状态。
```

## 输出状态

没有真实媒体时，完整设计包状态为`PROMPT_PACKAGE_READY`。


## Contract Skill强执行扩展

本版本新增实验性的`Contract Skill Extension 0.1`。它不改变原有导演、剧本、分镜和Prompt方法，而是新增不可变规则层、自适应策略层、阶段隔离、Schema校验、评分门禁、返修状态和完成凭证。

在支持脚本的Agent环境中：

```bash
python scripts/contract_runner.py start --request "创作任务"
python scripts/contract_runner.py prepare --task-id <TASK_ID>
```

Agent必须按生成的Stage Packet工作。完整协议见`contracts/execution-protocol.md`。

普通只读Skill宿主仍可加载本包，但只能提供`SOFT_CONTRACT`兼容模式，无法从技术上阻止模型跳步。

## Contract 0.4人物年龄适配

短视频与网文默认优先探索青年主角，但年龄最终由故事、职业资历、关系历史和人生阶段决定。通过`evals/character-age-fit-check.md`及S01—S03年龄审计防止强行年轻化或无必要老化。

## Contract 0.5主题意义与形式例外

除明确的抽象、无厘头和纯形式实验外，叙事作品必须在S01—S03证明主题意义与创作必要性：真实的人类困境、两个可理解价值、人物信念受压、高潮行动回应主题以及结尾余波。抽象与无厘头作品不强制传统主题，但必须证明形式目的、观众体验、内部模式和非随机性，普通故事不得借实验标签绕过。
