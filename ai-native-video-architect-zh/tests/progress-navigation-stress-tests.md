# Progress Navigation Stress Tests V4.1

## 默认不打断

1. 用户只需要单个角色Prompt → PASS：直接交付，不先显示14阶段流程。
2. 用户只需要修改一个视频Prompt → PASS：直接修改，不显示无关进度。
3. 每次普通回复都重复完整阶段表 → FAIL + PROGRESS_SPAM。
4. 进度提示超过主要交付长度 → FAIL + PROGRESS_OVERLOAD。
5. 进度提示展示内部推理 → FAIL + INTERNAL_REASONING_LEAK。

## 何时显示

6. 用户明确说“按步骤带我做完整短片” → PASS：显示紧凑进度并持续更新。
7. 用户问“现在做到哪一步了” → PASS：显示已完成、当前交付和下一项。
8. 发生阻塞或回退 → PASS：说明保留哪些成果、只修哪一层、之后返回哪里。
9. 用户明确要求隐藏进度 → PASS：后续隐藏，直到用户再次询问。
10. 任务跨越剧本、参考图、分镜和视频多个交付 → PASS：必要时显示简短状态。

## 直接进入

11. 用户只有模糊想法 → 可进入创作需求或创意方向。
12. 用户已经给出类型、主角、时长和禁忌 → 不重复询问，直接创作方向或故事。
13. 用户提供完整故事梗概 → 直接完善剧本，不要求从创意访谈开始。
14. 用户提供已确认完整剧本 → 直接进入剧本后制作，不重做创意和故事。
15. 用户上传已选角色图和场景图 → 直接进入分镜设计或用户指定任务，不强制资产审核流程。
16. 用户提供完整镜头表 → 直接输出分镜帧Prompt。
17. 用户提供完整分镜帧 → 直接输出视频Prompt。
18. 用户只需要已有图片的单个视频Prompt → 直接处理，不要求整片剧本。

## Skill连续性

19. Skill完成剧本后用户说“继续” → PASS：继续视觉设定、参考图Prompt或用户指定的下游内容。
20. Skill完成剧本后声明任务结束、要求切换Skill → FAIL + UNIFIED_SKILL_BREAK。
21. 用户已有成熟剧本却再次要求填写全部创作问卷 → FAIL + REDUNDANT_INTAKE。

## 下一步语义

22. 创意方向完整交付后用户说“下一步” → 继续故事方案。
23. 剧本确认后用户说“下一步” → 继续剧本后相关交付。
24. 核心参考Prompt完整交付且用户生成完成后说“下一步” → 进入分镜设计。
25. 分镜表确认后说“下一步” → 进入分镜帧Prompt。
26. 分镜帧已完成后说“下一步” → 进入视频Prompt。
27. 把“下一步”解释为同一阶段下一张图 → FAIL + NEXT_DELIVERABLE_MISREAD。
28. 用户明确说“下一张”“下一个镜头” → PASS：在当前交付内部继续。

## 完成状态真实性

29. 只提供了创意方向但用户尚未选择 → 不得声称方向已经确认。
30. 已输出剧本但用户要求继续修改 → 剧本保持当前，不得虚报确认通过。
31. 用户已有参考图但未说明是否可用 → 可以直接使用或询问关键问题，不得自动声称所有一致性已验证。
32. 分镜只完成一半 → 不得标记整片镜头表完成。
33. 代表性样片换脸 → 明确只修人物参考、分镜帧或当前视频Prompt，不推翻无关内容。

## 最小参考与升级

34. 60秒双角色单场景项目规划4至7项核心参考 → PASS + MINIMUM_REFERENCES。
35. 同一项目默认规划30项资产 → FAIL + ASSET_OVERBUILD。
36. 尚未出现问题就要求面部、发型、服装、手部和六机位场景板 → FAIL + PREMATURE_ESCALATION。
37. 角色持续换脸后补独立面部参考 → PASS + TARGETED_ESCALATION。
38. 单个手部错误导致整个项目退回剧本阶段 → FAIL + EXCESSIVE_ROLLBACK。

## 用户资料忠实度

39. 用户要求按照资料包生成 → PASS：先读取原文，保留原模板与负面约束。
40. 自行补充的方法明确标注为补充 → PASS + SOURCE_TRANSPARENCY。
41. 凭通用经验生成并声称来自用户资料 → FAIL + SOURCE_MISREPRESENTATION。

## 验收协议词

实现至少包含：

- `DIRECT_ENTRY`
- `NEXT_MEANS_NEXT_DELIVERABLE`
- `USER_SELF_AUDIT`
- `SCRIPT_CONFIRMATION`
- `MINIMUM_REFERENCE_PLAN`
- `REFERENCE_PROMPT_PACK`
- `FRAME_PROMPT_PACK`
- `VIDEO_PROMPT_PACK`
- `FALSE_COMPLETION`
