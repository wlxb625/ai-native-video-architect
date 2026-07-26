# Post-Script Prompt Pipeline Stress Tests V4.1

## T01 SOURCE_MODULE_REQUIRED

用户要求“按照资料包生成生图Prompt”。

PASS：读取资料原文和对应Prompt工程模块，沿用原模板结构与负面约束。

FAIL：只凭通用经验写“电影感、高清、真实”，却声称来自资料包。

## T02 DIRECT_SCRIPT_ENTRY

用户提供已确认完整剧本。

PASS：保护故事与结尾，直接进入视觉、核心参考、分镜或用户指定的后续交付。

FAIL：要求重新选择创意方向或填写全部创作问卷。

## T03 UNIFIED_SKILL_CONTINUATION

Skill刚完成并确认剧本。

PASS：同一个Skill继续完成参考图Prompt、分镜帧Prompt和视频Prompt。

FAIL：声明剧本任务结束，要求切换到另一个Skill。

## T04 MINIMUM_REFERENCE_OUTPUT

60秒、双角色、单场景项目需要参考图Prompt。

PASS：只输出开始分镜真正需要的角色综合板、场景空镜、核心道具和必要特殊状态。

FAIL：默认拆分大量面部、发型、服装、手部、动作和多机位资产。

## T05 COMPLETE_REFERENCE_BLOCK

PASS：每项必要参考图的主体提示词、负面约束和输出要求位于同一复制块。

FAIL：让用户在多个章节自行拼接统一前缀。

## T06 SOURCE_VS_ADDITION

PASS：原资料模板和项目适配内容为主体，自行补充的稳定或修复方法明确标记。

FAIL：将自行设计的方法冒充原资料原文。

## T07 USER_SELF_AUDIT

用户表示候选图由自己审核。

PASS：不要求逐图上传；只有明确请求才辅助审核。

FAIL：每张图都要求返回并评分。

## T08 NEXT_MEANS_NEXT_DELIVERABLE

必要参考Prompt已完整交付，用户生成并回复“下一步”。

PASS：进入分镜设计。

FAIL：输出下一个并不存在的资产Prompt。

## T09 IMAGE_VIDEO_SEPARATION

PASS：静态图描述一个准确瞬间；视频描述动作过程、运镜和结束状态。

FAIL：一张图片Prompt要求先走、再拿、再转身、再离开。

## T10 COLOR_AND_LIGHT_SPECIFIC

PASS：主色、辅助色、点缀色、色温、饱和度、对比度以及真实光源方向明确。

FAIL：只写“电影感蓝色调”和“真实光照”。

## T11 REFERENCE_ROLE

PASS：说明角色图负责身份，空镜负责空间，道具图负责结构，上一张分镜负责连续性。

FAIL：只写“参考图一、图二和图三”。

## T12 FRAME_INHERITANCE

PASS：第一张分镜使用角色参考与场景空镜；后续分镜增加上一张满意分镜，只改变当前动作、景别和机位。

FAIL：每张分镜都重新从纯文字设计人物和场景。

## T13 STATIC_MOMENT

PASS：分镜图只表现刀尖尚未接触铜锈的准确瞬间。

FAIL：一张图同时表现完整刮除过程和结果。

## T14 END_FRAME_ON_DEMAND

PASS：复杂状态变化、准确动作终点或下一镜继承需要时增加尾帧。

FAIL：所有普通固定镜头都强制生成尾帧。

## T15 CAMERA_ENDPOINT

PASS：运镜有起点、方向、速度、幅度和终点。

FAIL：只写“镜头环绕推进升高”。

## T16 MOTION_LIMIT

PASS：五秒镜头只有一个主要动作和一种主要运镜。

FAIL：奔跑、转身、拔刀、爆炸、360度环绕和升空同时发生。

## T17 REPRESENTATIVE_TEST

PASS：普通项目先测试一个代表性镜头，确有高风险时再加一个测试。

FAIL：固定要求3至5个样片和完整跨角度矩阵。

## T18 TAIL_FRAME_CONTINUATION

PASS：上一段稳定尾帧作为唯一首帧，只继续剩余动作。

FAIL：续拍重新设计人物、服装和场景。

## T19 HARD_CUT_CONTINUITY

PASS：新机位继承站位、动作进度、左右手、道具和背景地标。

FAIL：硬切后人物换手、转向或背景跳变。

## T20 LOCAL_REPAIR

PASS：手部或镜面局部错误优先局部修复。

FAIL：局部错误导致整张稳定图、全部参考或整个剧本重做。

## T21 ESCALATE_AFTER_FAILURE

PASS：实际发生换脸后补面部参考，场景漂移后补必要新角度。

FAIL：尚未失败就提前制作全部控制资产。

## T22 UPSCALE_FIDELITY

PASS：4K增强保持身份、构图、光线和色调。

FAIL：增强过程重新布光和美化面孔。

## T23 DIALOGUE_SINGLE_SPEAKER

PASS：需要口型时单镜单说话人、短句、面部可见。

FAIL：多人同时说长台词且要求一次准确口型。

## T24 SCRIPT_FIDELITY

PASS：生产适配只改变实现方式。

FAIL：为降低难度擅自改变人物选择、高潮或结尾。
