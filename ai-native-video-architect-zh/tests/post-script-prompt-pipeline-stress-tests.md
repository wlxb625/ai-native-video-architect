# Post-Script Prompt Pipeline Stress Tests V4.2

## T01 SOURCE_MODULE_REQUIRED

用户要求按照资料包生成Prompt。

PASS：先读取资料原文与相关Prompt模块，区分原模板和项目补充。

FAIL：只凭通用经验写“电影感、高清、真实”。

## T02 DIRECT_SCRIPT_ENTRY

用户提供已确认完整剧本。

PASS：保护故事与结尾，直接进入用户需要的后续交付。

FAIL：要求重新选择创意方向或填写全部问卷。

## T03 UNIFIED_SKILL_CONTINUATION

Skill刚完成并确认剧本。

PASS：同一个Skill继续完成参考图Prompt、分镜帧Prompt和视频Prompt。

FAIL：要求切换到另一个Skill。

## T04 MINIMUM_REFERENCE_OUTPUT

60秒、双角色、单场景项目需要参考图。

PASS：只输出必要角色综合板、场景空镜、核心道具和特殊状态。

FAIL：默认拆分大量面部、发型、服装、手部和多机位资产。

## T05 SOURCE_VS_ADDITION

PASS：原资料模板和项目适配内容为主体，自行补充内容明确标记。

FAIL：将自行设计的方法冒充原资料。

## T06 USER_SELF_AUDIT

PASS：不要求逐图上传；只有明确请求才辅助审核。

FAIL：每张图都要求返回评分。

## T07 NEXT_MEANS_NEXT_DELIVERABLE

PASS：完整交付后继续下一个相关交付物。

FAIL：只输出下一个资产或下一张图。

## T08 IMAGE_VIDEO_SEPARATION

PASS：静态图描述准确瞬间；视频描述时间过程。

FAIL：一张静态图要求先走、再拿、再转身、再离开。

## T09 END_FRAME_CONTRACT

每个镜头进入视频阶段前。

PASS：写清最后0.5秒人物、手部、道具、摄影机、焦点、灯光和下一镜继承。

FAIL：只有首帧和动作，没有结束帧合同。

## T10 SINGLE_START_FRAME_BOUNDARY

下一镜需要继承人物放下道具后的手部姿态。

PASS：生成尾帧，或生成后抽取稳定尾帧作为下一镜输入。

FAIL：只给单首帧，让模型自由决定手、道具和构图终点。

## T11 SINGLE_START_FRAME_ALLOWED

固定空镜只有雨滴和轻微灰尘运动，下一镜独立硬切。

PASS：可以单首帧，但仍写结束帧合同和稳定尾帧筛选标准。

FAIL：认为单首帧不需要控制结尾。

## T12 START_END_FRAME_CONTINUITY

人物抬手并最终停在镜面前，下一镜从该手势继续。

PASS：首尾帧身份、服装、道具、场景、主光、焦点和曝光一致，尾帧明确手掌距离镜面2厘米。

FAIL：尾帧换脸、光源反向或手部位置模糊。

## T13 TIMELINE_ACTION_BEATS

5秒镜头表现放置重物。

PASS：按0.0—0.8秒停顿、0.8—3.4秒下落、3.4—4.2秒承重接触、4.2—5.0秒松手停住描述。

FAIL：只写“人物缓慢把铜镜放下”。

## T14 ACTION_PHYSICS

人物搬动30厘米厚重铜镜。

PASS：双手分工、肩臂受力、下落距离、重心和接触震动明确。

FAIL：铜镜漂浮、单手轻拿或无重量。

## T15 CAMERA_CONTRACT

镜头使用极慢推进。

PASS：写明焦段、机位高度、开始时间、结束时间、推进方向、速度曲线、幅度5%和终点构图。

FAIL：只写“镜头缓慢推进”。

## T16 FIXED_CAMERA_CONTRACT

PASS：明确摄影机锁定，无平移、摇镜、旋转和数字变焦。

FAIL：省略摄影机字段，让模型自行添加运动。

## T17 OPTICAL_CONTRACT

镜中眼睛睁开后焦点转到现实人物眼部。

PASS：写明75毫米、景深、起始焦点、转移时间、最终焦点、镜头呼吸和曝光。

FAIL：只写“焦点转移到人物”。

## T18 PER_SHOT_LIGHTING

阴雨作坊内人物靠近左侧窗户。

PASS：写明5600K阴天窗光从世界空间左侧、人物左前上方35度进入，照亮左额、手背和铜镜左缘；右侧保持1:4阴影；2800K油灯只在刀柄形成局部高光；方向和色温全程固定。

FAIL：只写“冷色窗光、电影感”。

## T19 LIGHT_WORLD_POSITION

同一作坊从正面机位切到肩后机位。

PASS：窗户仍在世界空间左侧；换机位后重新计算画面相对方向，鼻影、镜面高光和地面阴影符合同一光源。

FAIL：主光永远写“画面左侧”，导致光源跟随摄影机移动。

## T20 LIGHTING_CONTINUITY

PASS：首尾帧主光来源、色温、光比、白平衡、曝光和高光位置一致。

FAIL：尾帧突然变亮、变暖、增加轮廓光或阴影反向。

## T21 EXPOSURE_AND_SHADOW_DETAIL

低调悬疑室内镜头。

PASS：略微欠曝、高光保护，暗部仍看清皮肤、旧木和工具轮廓。

FAIL：用全黑代替低调光。

## T22 FOREGROUND_MIDGROUND_BACKGROUND

肩后镜面构图。

PASS：写明前景肩膀、中景铜镜和手、背景木架，并规定各层运动。

FAIL：只描述人物动作，没有空间和构图。

## T23 END_HOLD

PASS：结尾稳定停留0.5秒或12至24帧，并明确下一镜继承内容。

FAIL：视频在动作中随机结束或尾态一闪而过。

## T24 TAIL_FRAME_CONTINUATION

PASS：抽取上一段最后稳定帧作为下一段唯一首帧，只继续剩余动作，并继承灯光和曝光。

FAIL：续拍重新设计人物、服装、背景或光线。

## T25 OCCLUSION_SWITCH

人物面部在手臂遮挡期间从状态D变为E。

PASS：分别生成遮挡前后两段，在完整遮挡处切换。

FAIL：强迫单次生成面部融化过程。

## T26 HARD_CUT_CONTINUITY

PASS：硬切继承人物位置、动作百分比、左右手、道具、背景地标、光源世界位置、色温和曝光。

FAIL：硬切后人物换方向、道具消失或光线反向。

## T27 LAYERED_COMPOSITE

镜中人物呼气产生薄雾。

PASS：人物底板、镜中层和雾气层按需分开，雾气范围与光线受控。

FAIL：让一个模型同时重构镜面、人物、雾气和现实背景。

## T28 SOUND_CAPABILITY

所用模型不支持原生声音。

PASS：声音字段进入后期计划。

FAIL：声称模型一定生成准确音效。

## T29 PROMPT_DETAIL_DENSITY

用户需要正式视频Prompt。

PASS：自然语言包含空间、时间轴、动作物理、摄影机、焦点景深、曝光、逐镜灯光、材质、精确尾帧、声音和负面约束。

FAIL：用三四句通用话概括整个镜头。

## T30 SCRIPT_FIDELITY

PASS：生产适配只改变实现方式。

FAIL：为降低难度擅自改变人物选择、高潮或结尾。
