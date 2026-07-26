# Post-Script Prompt Pipeline Stress Tests

## T01 SOURCE_MODULE_REQUIRED

用户要求“按照资料包生成生图Prompt”。

PASS：读取Prompt工程模块并使用明确公式。
FAIL：只凭通用经验写“电影感、高清、真实”。

## T02 BATCH_ASSET_OUTPUT

用户要求所有资产Prompt。

PASS：S07一次性输出完整Asset Registry，单资产一个完整复制块。
FAIL：只给第一个角色，要求生成后回来再继续。

## T03 FULL_COPY_BLOCK

PASS：正向Prompt、负面Prompt、输出规则、依赖和修复都在同一资产块。
FAIL：让用户在多个章节自行拼接统一前缀。

## T04 NEXT_MEANS_NEXT_STAGE

S07完整交付后用户说“下一步”。

PASS：视为用户已自行执行/确认，进入S09。
FAIL：输出下一个资产Prompt。

## T05 USER_SELF_AUDIT

用户表示候选图由自己审核。

PASS：不再要求逐图上传；只有明确请求才辅助审核。
FAIL：每张图都要求返回并评分。

## T06 IMAGE_VIDEO_SEPARATION

PASS：静态图描述准确瞬间；视频描述动作过程和运镜。
FAIL：一张图片Prompt要求先走、再拿、再转身、再离开。

## T07 COLOR_SIX_AXIS

PASS：主色、辅助色、点缀色、色温、饱和度和对比度明确。
FAIL：只写“电影感蓝色调”。

## T08 LIGHT_SOURCE_SPECIFIC

PASS：写清光源、方向、颜色、照亮对象和暗部。
FAIL：只写“真实光照”。

## T09 REFERENCE_ROLE

PASS：说明角色图负责身份、空镜负责场景、道具图负责结构。
FAIL：只写“参考图一和图二”。

## T10 STATIC_MOMENT

PASS：首帧是刀尖尚未接触，道具和动作空间清楚。
FAIL：首帧同时表现完整刮除过程。

## T11 FIRST_LAST_FRAME

PASS：高风险状态变化有首尾帧和中间动作说明。
FAIL：只用一张首帧要求精确变到复杂终态。

## T12 CAMERA_ENDPOINT

PASS：运镜有起点、方向、速度、距离和终点。
FAIL：只写“镜头环绕推进升高”。

## T13 MOTION_LIMIT

PASS：五秒镜头只有一个主要动作和一种主要运镜。
FAIL：奔跑、转身、拔刀、爆炸、360环绕、升空同时发生。

## T14 TAIL_FRAME_CONTINUATION

PASS：上一段稳定尾帧作为唯一首帧，只继续剩余动作。
FAIL：续拍重新设计人物、服装和场景。

## T15 HARD_CUT_CONTINUITY

PASS：新机位继承站位、动作进度、左右手、道具和背景地标。
FAIL：硬切后人物换手、转向或背景跳变。

## T16 MULTI_ANGLE_BLOCKING

PASS：同一场景人物不动，只移动摄影机。
FAIL：九宫格九张图人物和道具位置随机变化。

## T17 LOCAL_REPAIR

PASS：手部错误优先局部修复。
FAIL：手部错误导致整张已稳定图重生成并换脸。

## T18 UPSCALE_FIDELITY

PASS：4K增强保持身份、构图、光线和色调。
FAIL：增强过程重新布光和美化面孔。

## T19 DIALOGUE_SINGLE_SPEAKER

PASS：单镜单说话人、单句台词、面部可见。
FAIL：多人同时说长台词且要求一次准确口型。

## T20 SCRIPT_FIDELITY

PASS：生产适配只改变实现方式。
FAIL：为降低难度擅自改变人物选择、高潮或结尾。
