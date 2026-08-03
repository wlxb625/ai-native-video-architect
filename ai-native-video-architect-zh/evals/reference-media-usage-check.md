# Reference Media Usage Check V4.4

## 用途

检查S10控制帧与S11视频Prompt中的参考图、首尾帧和用户媒体是否真正成为可执行输入，而不是只停留在内部资产编号或外部备注。

## 一、逐控制帧检查

每个START、END和BRIDGE CF必须具备：

- 用户实际上传槽位，例如参考图1、参考图2、当前底图；
- 可定位文件名；
- 内部资产ID；
- PLANNED_REFERENCE、ACTUAL_REFERENCE、INHERITED_CF或USER_MEDIA状态；
- IDENTITY、COSTUME、LOCATION_LAYOUT、PROP_STRUCTURE、VISIBLE_STATE、POSE_INTERACTION或STYLE_LIGHT类型；
- 每张图的具体职责；
- HARD_LOCK、HIGH、MEDIUM或LOW优先级；
- 允许影响和禁止影响；
- 推荐平台绑定；
- 平台不支持多参考时的降级方案。

控制帧正向Prompt开头必须用自然语言直接调用这些上传图，例如“使用参考图1锁定人物身份”。只写`C1、L2、P5`或“参考上传图片”判定失败。

## 二、逐视频Shot检查

每个生成型视频Shot必须具备：

- 首帧及其文件名、职责和平台槽位；
- 尾帧、Bridge帧或完整文字尾帧合同；
- 人物身份参考；
- 当前服装和可见状态参考；
- 场景布局与主光世界位置参考；
- 关键道具结构和状态参考；
- 给视频模型的自然语言参考使用指令；
- 参考冲突优先级；
- 必须锁定的静态元素；
- 允许运动的元素；
- 首尾帧静态一致性检查；
- 平台绑定与降级方案。

视频正向Prompt必须直接说明如何使用首帧、尾帧和其他参考图，不能只在Prompt外附表。

## 三、冲突检查

逐镜检查参考之间是否冲突：

- 人物面孔、年龄和骨相；
- 发型、服装和配饰结构；
- 人物左右方向、屏幕方向和轴线；
- 场景入口、窗户、桌案和固定地标；
- 道具尺寸、数量、朝向和独特标记；
- 主光世界位置、白平衡和曝光；
- 首帧起点和尾帧终点动作完成百分比。

首尾帧存在上述冲突时，必须先修复静帧。将冲突帧直接交给视频模型判定REPAIR。

## 四、优先级检查

默认优先顺序应当明确：

```text
当前Shot首帧或真实底图
> 当前Shot尾帧或Bridge帧
> 上一镜真实尾帧
> 已批准人物身份图
> 当前服装与状态图
> 当前道具结构与状态图
> 场景布局与光源参考
> 姿态交互参考
> 风格色调参考
```

姿态图不得覆盖身份，风格图不得改变年龄、服装结构、道具数量和空间布局。

## 五、真实性检查

- PLANNED_REFERENCE必须明确尚未真实生成；
- ACTUAL_REFERENCE必须有真实生成、上传或用户批准依据；
- 不能声称仅靠Prompt已经实现角色一致性；
- 在母版资产未生成时，下游内容只能标记为制作计划或待验证Prompt包；
- 用户应能根据清单准确找到并上传对应文件。

## 六、平台可执行性检查

每个任务必须说明通用平台槽位或降级方式：

- 身份参考槽；
- 普通图片参考槽；
- 风格参考槽；
- 视频首帧槽；
- 视频尾帧槽；
- 遮罩图生图；
- 合成参考板；
- 不支持时的分步生成或后期合成。

平台未知时使用通用名称，不得虚构具体平台按钮。

## 七、直接失败条件

出现以下任一情况，状态为REPAIR：

- 任一人物控制帧没有人物身份参考且没有合理豁免；
- 任一连续镜头没有首帧、上一镜尾帧或场景身份依据；
- 只列内部ID，没有文件名和上传槽位；
- 参考职责只写“保持一致”；
- 生图Prompt没有直接调用参考图；
- 视频Prompt没有直接调用首帧、尾帧或角色参考；
- 没有参考优先级；
- 没有允许影响和禁止影响；
- 首尾帧冲突却继续生成视频；
- 平台限制没有降级方案；
- 将PLANNED_REFERENCE描述为已验证真实参考；
- 用户无法判断需要上传哪些图片以及如何绑定。

## 八、结果格式

```yaml
status: PASS | REPAIR
image_reference_manifest_coverage:
image_reference_use_instruction_coverage:
video_reference_manifest_coverage:
video_reference_use_instruction_coverage:
reference_priority_coverage:
start_end_static_consistency_coverage:
platform_binding_coverage:
platform_fallback_coverage:
planned_actual_status_accuracy:
id_only_reference_violations: []
missing_upload_file_names: []
missing_reference_roles: []
reference_conflicts: []
missing_platform_fallbacks: []
repair_actions: []
```

所有coverage必须为100%，所有异常数组必须为空，才能PASS。
