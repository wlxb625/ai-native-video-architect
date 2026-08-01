# CREATE Mode V4.4

从原始灵感建立AI原生故事、剧本和完整制作提示词包。

## 启动

判断用户已有想法、大纲、剧本、参考图、镜头表、分镜帧、视频Prompt或生成片段，只补齐缺失内容。

用户要求“全套”“完整”“用于外部平台实测”时，直接执行：

```text
CREATE → ADAPT → FULL_CREATION_PACKAGE
```

不得在剧本、参考图Prompt或母参考选择处停止。

## 创意与剧本

故事至少包含人物任务、关系或规则、可观察递进、关键选择、高潮和最后图像。整片Prompt生产前必须有可制作剧情剧本或视觉脚本。

## Agent内完整制作

剧本成立后自动读取：

- `controllers/agent-full-creation.md`；
- `controllers/post-script-production.md`；
- `controllers/camera-director.md`；
- `controllers/lighting-director.md`；
- `controllers/performance-director.md`；
- `references/emotion-library.md`；
- `prompt-engineering/performance-prompt-compiler.md`；
- `prompt-engineering/asset-prompt-system.md`；
- `prompt-engineering/shot-cf-binding-system.md`；
- `prompt-engineering/storyboard-frame-system.md`；
- `prompt-engineering/image-prompt-compiler.md`；
- `prompt-engineering/video-prompt-compiler.md`；
- `prompt-engineering/continuity-repair-system.md`；
- `evals/full-package-integrity-check.md`；
- `templates/full-creation-package.md`。

## 规划参考

Agent先生成资产ID与Prompt，再使用这些规划资产完成所有Shot和CF。真实图片尚未生成不阻塞后续。

必须区分：

- `PLANNED_REFERENCE`；
- `ACTUAL_REFERENCE`。

## Shot与CF

每个Shot必须有可见描述、导演意图、观众位置、摄影方向、逐镜灯光、开始状态、主要动作、结束状态、参考绑定、帧来源、CF、图片来源、视频Prompt和连续性传递。人物镜头还必须有内外情绪、可见微表情、呼吸与身体语言、0—5强度和情绪时间轴。

CF固定表示Control Frame，属于Shot，不得孤立存在。

## 完整交付

默认使用`templates/full-creation-package.md`，一次性交付全部资产Prompt、全部Shot制作卡、全部CF Prompt和全部视频Prompt。

内容过长时可以分镜头区间呈现，但同一任务内必须覆盖所有Shot。

## 内部返修

执行剧本闭环、资产覆盖、Shot完整性、CF绑定、Prompt覆盖、摄影—灯光—表演一致性、表演可读性、情绪强度连续性、相邻镜头连续性、Prompt冲突和生成可行性检查。最多两轮修复。

## 状态

没有真实媒体时，完整包状态为：

```text
PROMPT_PACKAGE_READY
```

## CREATE禁止

- 剧本完成后停止；
- 资产Prompt完成后要求用户先生成再继续；
- 部分Shot没有描述、导演字段、表演控制、参考或Prompt；
- CF没有绑定Shot；
- 继承上一镜却只写“同上”；
- 全套请求只输出前几个镜头；
- 没有真实媒体却声称样片已通过。
