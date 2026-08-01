# Visual Style, Color and Lighting Compiler

V4.4逐镜灯光设计同时读取`controllers/lighting-director.md`。灯光必须说明可读性目标和情绪功能，并与`controllers/performance-director.md`的关键表演区域一致。


## 色调不是单一滤镜

每个项目必须以六个核心维度建立色调：

```text
主色 + 辅助色 + 点缀色 + 色温 + 饱和度 + 明暗对比
```

并补充：白平衡、黑位、高光、肤色关系、核心道具颜色和禁止颜色。

## 项目色调合同

```yaml
color_contract:
  project_type:
  era_and_location:
  emotional_goal:
  primary_colors: []
  secondary_colors: []
  accent_colors: []
  accent_usage:
  saturation:
  color_temperature:
  contrast:
  white_balance:
  black_level:
  highlight_policy:
  skin_tone_relation:
  costume_colors: []
  core_prop_colors: []
  forbidden_colors: []
```

项目色调合同是全片基准，但不能替代逐镜灯光设计。

## 场景级灯光母合同

每个主要场景必须建立可跨机位继承的灯光事实：

```yaml
scene_lighting_master:
  time_and_weather:
  key_source:
  key_screen_direction:
  key_world_position:
  key_height:
  key_softness:
  key_color_temperature:
  fill_source:
  fill_color_temperature:
  practical_lights: []
  background_light:
  default_lighting_ratio:
  default_exposure:
  white_balance:
  shadow_direction:
  highlight_policy:
  black_level:
  atmospheric_elements:
  forbidden_unmotivated_lights: []
```

同一空间换机位时，摄影机可以移动，但窗户、门、太阳、月亮、灯具和火把在世界空间中的位置不能跟着摄影机移动。

## 逐镜灯光合同

每张分镜图和每条视频Prompt必须根据当前机位重新说明主光在画面中的方向和对主体的影响：

```yaml
shot_lighting_contract:
  key_source:
  key_direction_relative_to_camera:
  key_direction_relative_to_subject:
  key_height:
  key_softness:
  key_color_temperature:
  key_intensity:
  fill_source_and_intensity:
  practical_lights:
  rim_or_separation_light:
  background_light:
  lighting_ratio:
  illuminated_areas:
  shadow_areas:
  shadow_direction:
  highlight_control:
  shadow_detail:
  atmosphere_and_volume:
  exposure:
  visibility_goal:
  emotional_function:
  performance_readability:
  allowed_change_during_shot:
  continuity_statement:
  forbidden_changes:
```

最低必须说明：

1. 主光是真实的什么光源；
2. 光从画面哪一侧、人物哪一侧和什么高度进入；
3. 光是柔光、硬光还是有明确边缘的定向光；
4. 光线冷暖或具体色温；
5. 照亮人物脸部、手部、服装或道具的哪些区域；
6. 哪些区域保持阴影，阴影朝哪里落；
7. 辅光和实景灯的强度；
8. 大致光比，例如1:2、1:4或1:6；
9. 高光是否保护，暗部保留哪些材质；
10. 光源在整段视频中不得移动、闪烁、改变色温和阴影方向。

## 光影公式

```text
真实光源
+ 世界空间位置
+ 相对摄影机方向
+ 相对主体方向
+ 光线颜色或色温
+ 光线软硬和强度
+ 照亮区域
+ 阴影区域和方向
+ 辅光与实景灯
+ 光比
+ 高光与暗部
+ 可读性目标与情绪功能
+ 表演关键区域
+ 镜头内允许的有动机变化
+ 连续性
```

禁止只写“真实光照、电影感、冷色窗光”。

## 曝光、焦点与景深

灯光设计必须与光学设计配合：

```yaml
exposure_and_focus:
  exposure_state:
  white_balance:
  highlight_protection:
  shadow_detail:
  depth_of_field:
  focus_target:
  focus_transition:
  lens_breathing:
```

- 曝光写明正常、略微欠曝或局部高光保护；
- 白平衡不能在相邻镜头随机变化；
- 高光不能吞掉人物皮肤、镜面、刀刃或纸张信息；
- 低调光不等于死黑；
- 焦点必须落在具体对象；
- 景深选择必须服务叙事，而不是用虚化掩盖错误。

## 常用打光选择

### 自然顺光

适合身份展示和生活场景。必须说明光源位置、亮区与阴影，不得只写“柔和自然光”。

### 侧光

适合人物情绪、古风、历史、纪录和悬疑。写清哪侧脸亮、哪侧脸暗、鼻影和颧骨阴影方向。

### 侧逆光

适合轮廓分离和人物登场。不能无来源增加强轮廓光，也不能让正面死黑。

### 逆光剪影

适合背影、告别和结尾。需要看清人物时必须补充低强度正面环境反射光。

### 窗口光或门缝光

适合室内悬念、手部和道具特写。写明窗户在世界空间中的位置、光束进入角度、照亮区域和阴影方向。

### 火光或烛光

暖色实景光应有合理衰减和轻微动态，但不能导致人物脸部光线乱跳。环境仍需冷色或暗色层次，禁止全画面橙黄。

### 低调高对比光

适合秘密和压迫。关键人物、手部和道具必须有可验证光源，背景暗部仍保留空间地标。

### 柔光

适合亲密和身份参考。柔光不是无方向平光，仍需写明光源方向与阴影过渡。

### 顶光

适合审问、孤独和仪式。避免眼窝死黑和无来源底光。

## 视频中的灯光连续性

视频Prompt必须明确：

- 主光固定在世界空间中的位置；
- 人物移动时，亮暗变化符合真实距离和朝向；
- 鼻影、脸颊阴影、道具高光和地面阴影连续；
- 实景灯亮度只允许剧本规定的自然波动；
- 禁止曝光跳变、光线闪烁、阴影漂移和色温呼吸；
- 首帧与尾帧的主光方向、白平衡和曝光必须匹配；
- 抽尾帧续拍必须继承上一段的光线事实。

## 场景连续性

每个分镜Prompt必须继承：

- 相同主色体系；
- 相同白平衡基准；
- 相同色温关系；
- 相同肤色与背景关系；
- 相同黑位和高光策略；
- 相同场景主光世界位置；
- 点缀色只能出现在预定人物、道具、光源或情节重点。

不同时间允许自然明暗变化，但必须在剧本和视觉设定中有依据，并说明变化幅度。

## 夜景与暗场规则

- 暗部保留材质和空间地标；
- 角色面部、手部和核心道具至少有一种可验证光源；
- 避免脏灰、压缩噪点、彩色斑块和死黑；
- 不使用无来源病态绿光作为恐怖捷径；
- 夜景降噪只修复噪点、边缘和色彩，不重构灯光。

## 真实材质与影像质感

根据镜头实际写明皮肤、布料、木材、金属、纸张、水面、玻璃、烟雾和尘埃如何受光。推荐：

- 真实摄影透视；
- 自然景深；
- 宽动态范围；
- 高光不过曝；
- 暗部保留细节；
- 轻微细腻颗粒；
- 克制锐化；
- 真实皮肤、衣料和道具反光。

不要把所有项目机械写成高对比、强轮廓光或超浅景深。

## 编译到最终Prompt

每条图片或视频Prompt必须包含当前镜头相关的：

```text
主色与辅助色
+ 当前真实光源
+ 光源方向、高度、软硬和色温
+ 主体具体受光区域
+ 阴影区域与方向
+ 辅光、实景灯和光比
+ 曝光、焦点和景深
+ 高光和暗部要求
+ 点缀色用途
+ 首尾帧和相邻镜头连续性
```

不得只在Prompt包开头写一次全局灯光，然后在每镜中省略。

## 色调与灯光硬失败

- 将主色理解为整张图单色覆盖；
- 人物肤色被背景色严重污染；
- 同一场景不同镜头白平衡随机变化；
- 主光在世界空间中跟随摄影机移动；
- 只写“真实光照、电影感、冷色调”；
- 未说明主体亮区、阴影和暗部；
- 首尾帧主光方向、色温或曝光不一致；
- 表演依赖眼神、嘴、手或身体变化，但灯光让关键区域不可读；
- 灯光为了情绪无原因变色、闪烁或自动跟随人物；
- 视频中出现曝光闪烁、阴影漂移和色温跳变；
- 点缀色大面积泛滥；
- 夜景主体完全不可读；
- 高光过曝掩盖核心信息；
- “高级感”只依靠青橙滤镜、蓝色滤镜或低曝光。
