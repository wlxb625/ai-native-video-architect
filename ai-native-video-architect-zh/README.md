# AI Native Film Studio V4.2

## 从创意、剧本到实际生产与交付的完整中文Skill

显式调用：

```text
$ai-native-video-architect-zh
```

这个Skill同时负责创意、故事与剧本创作，以及剧本确认后的核心参考图、分镜帧、导演级视频Prompt、母参考筛选、代表性样片、批量生成队列、镜头验收、剪辑和后期交付。用户不需要在剧本完成或Prompt完成后切换到另一套Skill。

## 能力入口

- 从想法、人物、题材或情绪开始完成故事与剧本；
- 读取已有大纲、剧本或视觉脚本继续制作；
- 使用已有角色图、场景图、道具图或分镜图；
- 单独生成角色参考、场景空镜、首尾帧或视频Prompt；
- 对已有生成片段进行真实验收、失败诊断和修复；
- 建立镜头版本台账、剪辑连接和后期交付方案。

## 最小核心参考

普通短片只制作真正必要的参考图。

角色先判断一张独立身份主参考是否足够，不默认三视图、综合角色板或密集六宫格。只有镜头或模型确实需要时才增加全身服装、面部近景、手部交互、标准三视图、综合角色板或特殊状态。

场景默认每个主要空间一张无人物空镜。核心道具和特殊状态只有跨镜头必须精确控制时才单独生成。

## 可直接复制的资产Prompt

Skill内部可以把摄影、光学、灯光、色彩和材质拆开检查，但用户最终复制的正向Prompt必须已经融合这些内容：

```text
主体身份与资产用途
+ 构图与主体位置
+ 摄影机、焦段、机位、焦点和景深
+ 曝光、白平衡、高光和暗部
+ 主光来源、方向、色温、软硬、亮区和阴影
+ 色彩与皮肤、布料、木材、金属等材质
+ 背景与一致性要求
```

不会要求用户自己拼接摄影合同、灯光合同和主体描述。负面Prompt及画幅、分辨率等设置可以独立提供。

## 分镜与导演级视频Prompt

每镜先设计镜头任务、主要动作、景别、焦段、机位、前中后景、构图、焦点、逐镜灯光、精确尾态和下一镜连接。

图片Prompt只描述准确静态瞬间，并将摄影、焦点、曝光、逐镜灯光和材质写进完整正向Prompt。

视频Prompt按镜头选择单首帧、首尾帧、抽尾帧续拍、两段硬切、遮挡切换或分层合成，并控制分秒动作、动作物理、摄影机、焦点曝光、逐镜灯光、精确结束帧、声音和负面约束。

镜面人物、倒影、薄雾、准确文字、复杂状态切换和高风险手部不强迫一个模型一次完成。

## Prompt完成后的实际生产

Skill不会在交付Prompt包后假装项目已经完成。生产状态严格区分：

```text
DESIGN_READY
PROMPT_READY
REFERENCE_READY
SAMPLE_VALIDATED
BATCH_GENERATION_READY
EDIT_READY
DELIVERY_READY
```

- 只有Prompt时最多是`PROMPT_READY`；
- 真实母参考已经选定才能是`REFERENCE_READY`；
- 真实样片通过才能是`SAMPLE_VALIDATED`；
- 所有必要镜头已有通过版本才能是`EDIT_READY`；
- 剪辑、声音、文字、调色和最终检查完成才能是`DELIVERY_READY`。

## 唯一母参考

每个长期继承的角色、场景、道具和特殊状态只选择一个当前主版本。外部成本允许时可生成2至4个候选，但该数量只是建议。

候选选择优先身份或结构正确、可覆盖主要镜头、没有明显错误、灯光材质符合项目规则和方便后续参考。不得在不同镜头中混用多张相似角色脸。

## 代表性样片门槛

默认先测试一个来自正片的普通镜头。项目存在镜面、状态变化、多人同步、复杂手部、遮挡切换或高难运镜时，再测试最多一个真实高风险镜头。

样片必须使用实际首帧、尾帧、桥接帧和真实生成模式。没有实际媒体时只能输出样片计划，不能宣称样片已经通过。

普通样片和必要高风险样片存在硬失败时，不直接批量生成整片。

## 失败分层

生成失败后先判断属于：

- `REFERENCE_FAILURE`
- `CONTROL_FRAME_FAILURE`
- `PROMPT_FAILURE`
- `MODEL_CAPABILITY_FAILURE`
- `POST_PRODUCTION_FAILURE`

优先简化Prompt或动作、修复首尾帧、固定机位、缩短片段、补尾帧或续拍、遮挡切换或分层合成，最后才新增参考资产。

新增面部、全身、手部、第二场景角度或状态图，必须由真实、可复现的失败触发。

## 生产队列与镜头验收

生产顺序默认是：

```text
唯一母参考
→ 代表性镜头首尾帧
→ 普通样片与必要高风险样片
→ 修复薄弱层
→ 剩余控制帧
→ 连续剧情镜头
→ 独立空镜和片尾镜头
→ 分层合成、文字、声音、调色和剪辑
```

每镜建立台账，记录生成模式、母参考、首尾帧、Prompt版本、候选媒体、验收分数、失败维度、修复动作和剪辑连接。

选择版本时，叙事与尾态、身份连续、手部物理、摄影焦点灯光和可剪辑性均优先于单帧美观。

实际生成片段使用`evals/shot-output-acceptance-score.md`验收。只有通过版本进入最终时间线。

## 主要生产文件

- `SKILL.md`
- `AGENT.md`
- `controllers/post-script-production.md`
- `controllers/production-execution.md`
- `prompt-engineering/asset-prompt-system.md`
- `prompt-engineering/storyboard-frame-system.md`
- `prompt-engineering/video-prompt-compiler.md`
- `evals/prompt-production-readiness-score.md`
- `evals/shot-output-acceptance-score.md`
- `templates/production-runbook.md`
- `templates/asset-prompt-block.md`
- `templates/storyboard-frame-prompt-block.md`
- `templates/video-shot-prompt-block.md`

## 安装

```bash
git clone https://github.com/wlxb625/ai-native-video-architect.git
cd ai-native-video-architect/ai-native-video-architect-zh
python scripts/validate_package.py
```

Skill负责创作、导演设计、Prompt生产、生产组织和验收。它不会虚构已经运行无法访问的外部生图、视频、剪辑或声音软件。