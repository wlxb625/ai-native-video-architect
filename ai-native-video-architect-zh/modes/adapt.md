# ADAPT Mode V4.0

把已成立作品转译为可执行的AI电影生产系统。ADAPT优先改变实现方式，不改变人物目标、关键选择、高潮主体、结尾和开放程度。

## 启动

读取：

- `config/progress-navigation.yaml`
- `controllers/post-script-production.md`
- 当前阶段所需的`prompt-engineering/`模块。

先判断用户材料属于S00—S13哪一阶段，不重复已完成步骤。

## 入口

```text
故事梗概 → S03
完整剧本 → S04
拆解与视觉圣经 → S06
需要资产Prompt → S07
已经生成并选定资产 → S08
资产确认完成 → S09
完整镜头表 → S10
完整分镜帧 → S11
核心样片通过 → S12
```

## Production Protection Contract

```yaml
production_protection:
  source_stage:
  return_stage:
  must_preserve: []
  allowed_implementation_changes: []
  forbidden_changes: []
  allowed_visual_drift: []
  forbidden_visual_drift: []
  target_delivery:
  budget_level:
```

## 剧本门槛

进入资产Prompt和视频生产前必须有已确认传统剧本或完整视觉脚本。只有概念、氛围图或零散镜头时返回S03。

## 剧本后必读

- `prompt-engineering/image-prompt-compiler.md`
- `prompt-engineering/visual-style-color-light.md`
- `prompt-engineering/asset-prompt-system.md`
- `prompt-engineering/storyboard-frame-system.md`
- `prompt-engineering/video-prompt-compiler.md`
- `prompt-engineering/camera-movement-library.md`
- `prompt-engineering/continuity-repair-system.md`

## V4.0 ADAPT工作流

1. S04拆解角色、服装、场景、道具、状态和风险；
2. S05建立色调六轴、真实光源和材质合同；
3. S06建立资产ID、参考职责、Prompt类型和生产顺序；
4. S07一次性交付全部资产完整Prompt；
5. S08默认用户自行生成和审核，回复“下一步”即通过资产阶段；
6. S09一次性设计完整镜头表；
7. S10一次性交付全部首帧、尾帧和修复Prompt；
8. S11一次性交付核心样片视频Prompt，用户确认后通过生产门；
9. S12一次性交付全片视频Prompt、运镜、续拍、硬切、修复、剪辑和声音；
10. S13审查和交付。

## 批量与确认

- `BATCH_STAGE_OUTPUT`：阶段为默认批次单位；
- `USER_SELF_AUDIT`：用户默认自行审核；
- `NEXT_MEANS_NEXT_STAGE`：用户说“下一步”进入下一S阶段；
- 只有明确要求“逐项来”时才拆分资产或镜头；
- 只有明确要求审核时才调用评分器。

## 图片与视频Prompt

图片Prompt负责一个静态瞬间、构图、机位、光线、色调、材质和准确状态。

视频Prompt负责指定首帧、唯一主要动作、起势/过程/收住、运镜起止、结束状态和禁止变化。

## 首尾帧、续拍与硬切

抽取上一段稳定尾帧作为下一段唯一首帧，只继续剩余动作。硬切允许换景别和机位，但必须保持人物、服装、道具、动作进度、站位、背景地标、光线和色调。

## S11 Core Sample Gate

核心样片至少验证角色跨角度、场景跨机位、核心道具、状态变化、一次续拍或硬切，以及主要运镜。用户回复“下一步”表示`CORE_SAMPLE_GATE = PASSED`。

## 稳定降级

1. 先修资产或分镜帧，不继续堆Prompt；
2. 连续复杂变化拆成首尾帧、硬切或分层；
3. 多人动作拆成站位板、反打和局部；
4. 大尺度奇观拆成前兆、发生、结果；
5. 保留人物动作、选择和不可逆结果；
6. 不用旁白替代本应由画面表达的信息。
