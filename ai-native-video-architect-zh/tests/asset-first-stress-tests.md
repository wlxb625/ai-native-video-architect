# Asset-First Production Stress Tests

1. 用户只说“写个古装剧本”，Agent直接决定题材、主角、关系和结尾 → FAIL + INTAKE_SKIPPED。
2. Agent用选择与填空收集类型、情绪、形式、人物、结尾、时长画幅和禁忌，再给三个不同方向 → PASS + STRUCTURED_INTAKE。
3. 用户已经给出无对白、60秒、古装东方美学，Agent再次询问相同问题 → FAIL + DUPLICATE_QUESTION。
4. 只有艺术角色海报，人物角度被裁切，却宣称三视图已锁定 → FAIL + ART_BOARD_NOT_TURNAROUND。
5. 同一角色正面、严格侧面和背面保持脸、发型、服装和比例一致 → PASS + PRODUCTION_TURNAROUND。
6. 三视图侧面实际为四分之三角度，背面人物回头 → FAIL + TURNAROUND_INVALID。
7. 面部身份板保留毛孔、不对称、发际线和不同角度骨相 → PASS + FACE_IDENTITY_READY。
8. 服装只写“逐渐变红”，没有COST_A/B/C和产生变化的镜头 → FAIL + COSTUME_STATE_MISSING。
9. 服装状态链只改变袖口染色和灰烬位置，结构、材质和鞋履保持一致 → PASS + COSTUME_STATE_CHAIN。
10. 场景每个镜头重新生成，没有无人物空镜和主布局 → FAIL + ENVIRONMENT_UNLOCKED。
11. 同一场景有宽景空镜、平面布局和六个机位，门窗柱体与主光方向一致 → PASS + ENVIRONMENT_ASSET_READY。
12. 多机位图中同一扇门在左侧、右侧和背景随机移动 → FAIL + ENVIRONMENT_LAYOUT_DRIFT。
13. 核心道具只写“古旧铜镜”，没有尺寸、结构、铜绿分布和状态 → FAIL + PROP_UNDERSPECIFIED。
14. 道具三视图、人体比例、握持方式、独特裂纹和状态链完整 → PASS + PROP_ASSET_READY。
15. 道具从右手无动作跳到左手 → FAIL + PROP_HAND_CONTINUITY。
16. 每个镜头重复整套人物外貌和场景设定，却没有引用资产ID → FAIL + ASSET_REINVENTION。
17. 镜头引用CHAR_C01、COST_C01_B、SCENE_S02、PROP_P01_C并只描述当前状态 → PASS + ASSET_REFERENCED。
18. 图片Prompt负责构图和静态状态，视频Prompt负责一个动作和摄影机运动 → PASS + PROMPT_LAYER_SEPARATION。
19. 视频Prompt被大量外貌与风格词淹没，没有明确动作终点 → FAIL + VIDEO_PROMPT_NO_MOTION_CONTRACT。
20. 服装变色、道具燃烧和花苞开放使用首尾帧，并锁定不变资产 → PASS + FRAME_PAIR_READY。
21. 首尾帧之间人物脸、场景结构和光线方向一起变化 → FAIL + FRAME_PAIR_IDENTITY_BREAK。
22. 复杂奇观拆为稳定人物底板、场景底板、效果层和灰烬层 → PASS + LAYERED_COMPOSITE。
23. 一个镜头同时要求人物奔跑、换装、建筑坍塌和360度环绕 → FAIL + SHOT_OVERLOAD。
24. 上一段尾帧被登记为下一段唯一首帧，只继续剩余动作 → PASS + TAIL_FRAME_CONTINUATION。
25. 尾帧续拍重新设计人物服装和背景 → FAIL + CONTINUATION_RESET。
26. 硬切改变景别，但保留动作完成百分比、左右手、地标和主光方向 → PASS + HARD_CUT_CONTINUITY。
27. 硬切后人物突然换方向、道具消失、背景变成另一处 → FAIL + HARD_CUT_BREAK。
28. 未做Core Sample就批量生成40个镜头 → FAIL + PREMATURE_BATCH。
29. 一名角色、一个场景、一个道具、两个机位和一个首尾帧测试通过后扩展 → PASS + BATCH_GATE_PASSED。
30. Asset Readiness为72分，系统允许做Core Sample但禁止批量生产 → PASS + CONDITIONAL_ASSET_GATE。
31. Asset Readiness低于70仍声称可直接生产 → FAIL + ASSET_GATE_BYPASSED。
32. 已批准资产被直接覆盖且无法回滚 → FAIL + VERSION_OVERWRITE。
33. 新尝试递增版本号并保留选中版本 → PASS + VERSION_SAFE。
34. 为降低难度删除关键人物选择 → FAIL并升级TRANSFORM。
35. 稳定替代仅改变景别、合成方式或动作拆分，人物选择和结尾不变 → PASS + ADAPTATION_FIDELITY。
