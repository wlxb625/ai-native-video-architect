# Prompt工程资料提炼映射

## 目的

本文件记录用户提供的AI生图与视频Prompt工程资料如何被提炼进V4.0。它只做知识映射，不复制原资料的推广信息、链接、平台额度、临时模型排行或大量案例原文。

## 总体映射

| 原资料主题 | V4模块 |
|---|---|
| 剧本可制作性、人物场景先行、分镜一致性 | `controllers/post-script-production.md` |
| 主色调、场景色调、六维色调、夜景降噪 | `prompt-engineering/visual-style-color-light.md` |
| 光影关键词、伦勃朗光、窗光、火光、低调光 | `prompt-engineering/visual-style-color-light.md` |
| 角色板、三视图、面部特写、人物细节 | `prompt-engineering/asset-prompt-system.md` |
| 场景设定、道具设定、多人站位 | `prompt-engineering/asset-prompt-system.md` |
| 图片基础公式、超写实、图生图、局部修改、4K | `prompt-engineering/image-prompt-compiler.md`、`continuity-repair-system.md` |
| 分镜图、九宫格、多机位、一致性 | `prompt-engineering/storyboard-frame-system.md` |
| 视频基础公式、图生视频、首尾帧、动作、氛围 | `prompt-engineering/video-prompt-compiler.md` |
| 固定、推拉摇移、跟拍、环绕、FPV、焦点转移等 | `prompt-engineering/camera-movement-library.md` |
| 抽尾帧续拍、硬切、上下视频衔接、多角度穿帮 | `prompt-engineering/continuity-repair-system.md` |
| 人物台词错误、局部修复、夜景噪点 | `prompt-engineering/continuity-repair-system.md` |

## 提炼原则

1. 保留长期稳定的方法，不写死模型版本、平台价格、额度和临时榜单。
2. 将案例句式提炼为字段、公式、检查项和稳定替代，不机械复制整篇资料。
3. 图片和视频严格分工：静态瞬间由图片Prompt控制，时间过程由视频Prompt控制。
4. 每种资产和镜头根据功能调用不同模板，不使用一个万能Prompt替代全部任务。
5. 对多视图、多人站位、首尾帧和复杂动作，必须同时提供理想方案与稳定分步方案。
6. 用户提供的新资料优先于模型凭经验自由扩写；发生冲突时以项目剧本、视觉圣经和用户明确要求为最高约束。

## 资料主题索引

原资料中与V4生产层直接相关的主要章节包括：

- 视频主色调与场景设定；
- 图片光影关键词与色调一致性；
- 多人站位一致性；
- 超写实画质与分镜一致性；
- 角色板、人物三视图、面部特写、细节与道具；
- 场景设定、图生图修改、局部修改、4K增强；
- 图片生成基础公式；
- 视频生成基础公式与图生视频；
- 图片故事板、九宫格与多机位；
- 首尾帧视频、硬切镜头、人物动作和环境氛围；
- FPV、上下视频衔接、多角度穿帮和台词修复；
- 常用运镜与镜头语言。
