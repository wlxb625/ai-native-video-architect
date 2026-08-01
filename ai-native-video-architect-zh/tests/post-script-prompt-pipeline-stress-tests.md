# Post-Script Prompt Pipeline Stress Tests V4.4

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

PASS：先判断每名角色一张独立身份主参考是否足够，只增加必要场景空镜、核心道具和特殊状态。

FAIL：默认密集六宫格，或固定拆分面部、全身、手部、服装和多机位资产。

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

## T31 EXECUTABLE_POSITIVE_PROMPT

资产内部已经列出85毫米焦段、左前5600K柔光、真实皮肤和旧棉麻材质。

PASS：这些信息全部再次自然写入用户直接复制的完整正向Prompt。

FAIL：正向Prompt只写人物外貌，摄影、灯光和材质只存在于外部字段。

## T32 NO_USER_SIDE_PROMPT_ASSEMBLY

用户需要一条可直接复制的资产Prompt。

PASS：一条完整正向Prompt已经融合主体、构图、摄影、光学、灯光、色彩和材质，另附负面Prompt与输出设置。

FAIL：让用户自行复制“统一摄影前缀”“灯光合同”和“人物描述”并拼接。

## T33 CHARACTER_REFERENCE_FORM

单角色60秒短片，主要镜头是中近景，服装结构简单。

PASS：默认先生成一张独立身份主参考；不必要时不增加全身、手部或三视图。

FAIL：无论镜头需要都固定生成六宫格或面部、全身、手部三张。

## T34 MULTIVIEW_ON_DEMAND

系列角色需要正侧背结构，所用模型已测试能稳定生成同一人物三视图。

PASS：可以采用标准人物三视图，并把同一身份、服装、比例、摄影和灯光要求写进完整正向Prompt。

FAIL：因为默认单图策略而禁止所有三视图，或没有稳定依据仍强制使用多视图。

## T35 STORYBOARD_INTEGRATED_PROMPT

分镜模板外部列出焦点、曝光和逐镜灯光。

PASS：最终分镜正向Prompt中再次包含这些信息，用户复制一次即可生成。

FAIL：分镜正向Prompt只写构图动作，关键摄影和灯光留在外部说明。

## T36 ABSTRACT_AESTHETIC_GROUNDING

用户要求画面“空灵、宿命、史诗、电影感”。

PASS：把这些词转译为主体状态、画面大形、空间尺度、主辅强调色、真实光源、明暗节奏、材质和背景结构。

FAIL：只在Prompt结尾堆“唯美、震撼、电影感、史诗感、8K”。

## T37 BACKGROUND_AS_SECOND_VISUAL_SUBJECT

剧情关键帧中人物处于巨浪、厂房、走廊或城市空间。

PASS：背景有明确功能、大形、近中远层次、方向、局部高潮及与人物的呼应或对抗。

FAIL：人物写得极细，背景只写“海边有雾”“昏暗房间”“城市夜景”。

## T38 TECHNICAL_ASSET_CLARITY_EXCEPTION

用户需要人物身份主参考、三视图或道具结构板。

PASS：优先身份、比例、结构、材质中性和可复用背景，不强制灾变背景或复杂戏剧光。

FAIL：把所有资产图都写成高冲击电影海报，导致身份和结构不可用。

## T39 IMAGE_TO_VIDEO_FIRST_FRAME_PROTECTION

用户上传一张人物、服装和构图已经确认的首帧。

PASS：Prompt首先锁定面部、年龄、骨相、发型发饰、服装结构、人体比例、主体位置、构图、场景、色调和光源，只允许规定运动。

FAIL：视频Prompt重新描述并重新设计人物、服装或背景。

## T40 SINGLE_CORE_VISUAL_EVENT

6秒图生视频镜头。

PASS：只有一个核心视觉事件，例如浪幕升起；人物微动作、纱、红带、运镜和光线都服务该事件。

FAIL：同时安排复杂舞蹈、巨浪砸下、红带爆发、镜头高速环绕、人物睁眼流泪和道具破碎。

## T41 MATERIAL_MOTION_CHOREOGRAPHY

首帧包含内外层薄纱、头发、红带、水雾和浪幕。

PASS：分别写动力、延迟、方向、速度、幅度、重量和前中远景速度差。

FAIL：全部写成“随风自然飘动”，同速同向无层次。

## T42 BACKGROUND_EVENT_TIMELINE

背景承担第二视觉主体。

PASS：写清背景初始状态、形成过程、中段扩大、视觉高潮和最终停点，并避免遮挡关键信息。

FAIL：只写“背景海浪翻涌、雾气流动”。

## T43 TEMPORAL_CLIMAX_AND_HOLD

6秒镜头需要视觉高潮。

PASS：前段稳定起势，中段形成主事件，最后1—2秒完成大形或动作停点并稳定保持。

FAIL：所有元素以同样速度漂满6秒，结尾没有明确变化或停住。

