# Visual Style, Color and Lighting Compiler V4.7

本模块逐镜灯光设计同时读取：

- `controllers/lighting-director.md`；
- `controllers/performance-director.md`；
- `prompt-engineering/render-medium-generation-route-contract.md`；
- 当前项目`RENDER_MEDIUM_LOCK`。

灯光必须说明可读性目标和情绪功能，并与关键表演区域一致。真实光源表示世界内部的位置、方向、衰减、遮挡和阴影关系成立，不等于必须真人摄影或照片写实。

## 一、先继承渲染媒介

色彩、灯光、曝光、材质和影像质感在编译前必须回答：

```yaml
medium_translation:
  render_medium_reference:
  character_surface_language:
  environment_surface_language:
  light_behavior:
  camera_and_optical_translation:
  texture_or_grain_language:
  forbidden_medium_drift: []
```

不同媒介使用不同表面与光学表达：

- 真人实拍：可以使用自然皮肤区域差异、现实服装工艺、真实镜头透视和实景摄影颗粒；
- 照片写实CG：使用可信PBR、次表面散射、毛发、布料与虚拟摄影机，但避免蜡像和游戏模板；
- 风格化3D动画：使用设计化面部、受控次表面散射、动画电影级着色器、发束与服装轮廓、绘画化但有动机的光影；不机械强调真人毛孔和真人写真；
- 二维或2.5D动画：使用线条、色块、平面明暗、分层深度、视差与绘画纹理；不机械加入PBR皮肤和照片噪点；
- 绘画、水墨、定格、游戏电影CG和混合媒介：按当前项目合同翻译。

禁止用“真实、电影感、高级感”绕过媒介判断。

## 二、色调不是单一滤镜

每个项目必须以六个核心维度建立色调：

```text
主色 + 辅助色 + 点缀色 + 色温 + 饱和度 + 明暗对比
```

并补充：白平衡或媒介等效基准、黑位、高光、角色表面关系、核心道具颜色和禁止颜色。

## 三、项目色调合同

```yaml
color_contract:
  render_medium_reference:
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
  white_balance_or_medium_equivalent:
  black_level:
  highlight_policy:
  character_surface_relation:
  costume_colors: []
  core_prop_colors: []
  forbidden_colors: []
  forbidden_filter_shortcuts: []
```

项目色调合同是全片基准，但不能替代逐镜灯光设计。

## 四、场景级灯光母合同

每个主要场景必须建立可跨机位继承的灯光事实：

```yaml
scene_lighting_master:
  render_medium_reference:
  time_and_weather:
  key_source:
  key_screen_direction:
  key_world_position:
  key_height:
  key_softness_or_edge_language:
  key_color_temperature_or_color_relation:
  fill_source:
  fill_color_temperature_or_relation:
  practical_lights: []
  background_light:
  default_lighting_ratio_or_value_relation:
  default_exposure_or_value_range:
  white_balance_or_medium_equivalent:
  shadow_direction:
  highlight_policy:
  black_level:
  atmospheric_elements:
  forbidden_unmotivated_lights: []
```

同一空间换机位时，窗户、门、太阳、月亮、灯具、火把、绘画化光源或其他世界光源的位置不能跟着摄影机移动。

二维、绘画或水墨媒介可以使用非物理但内部一致的光影设计，但必须明确它属于该项目的图形规则，并在相邻镜头稳定继承。

## 五、逐镜灯光合同

每张分镜图和每条视频Prompt必须根据当前机位重新说明主光在画面中的方向和对主体的影响：

```yaml
shot_lighting_contract:
  render_medium_reference:
  key_source:
  key_direction_relative_to_camera:
  key_direction_relative_to_subject:
  key_height:
  key_softness_or_edge_language:
  key_color_temperature_or_color_relation:
  key_intensity_or_value_priority:
  fill_source_and_intensity:
  practical_lights:
  rim_or_separation_light:
  background_light:
  lighting_ratio_or_value_relation:
  illuminated_areas:
  shadow_areas:
  shadow_direction:
  highlight_control:
  shadow_detail:
  atmosphere_and_volume:
  exposure_or_value_range:
  visibility_goal:
  emotional_function:
  performance_readability:
  allowed_change_during_shot:
  continuity_statement:
  forbidden_changes:
```

最低必须说明：

1. 主光或主明暗来源是什么；
2. 光从画面哪一侧、人物哪一侧和什么高度进入；
3. 光是柔光、硬光、绘画化边缘光还是明确图形切面；
4. 冷暖、色温或颜色关系；
5. 照亮人物脸部、手部、服装或道具的哪些区域；
6. 哪些区域保持阴影，阴影朝哪里落；
7. 辅光和实景灯的强度或明度关系；
8. 大致光比或明暗层级；
9. 高光是否保护，暗部保留哪些结构与材质；
10. 光源或图形明暗逻辑在整段视频中不得无因移动、闪烁和改变。

## 六、光影公式

```text
当前渲染媒介
+ 世界内部成立的光源或明暗来源
+ 世界空间位置
+ 相对摄影机方向
+ 相对主体方向
+ 光线颜色、色温或色彩关系
+ 光线软硬、边缘语言和强度
+ 照亮区域
+ 阴影区域和方向
+ 辅光与实景灯
+ 光比或明度层级
+ 高光与暗部
+ 可读性目标与情绪功能
+ 表演关键区域
+ 镜头内允许的有动机变化
+ 连续性
```

禁止只写“真实光照、电影感、冷色窗光、动漫打光、3D灯光”。

## 七、曝光、焦点与景深

灯光设计必须与光学或媒介层级设计配合：

```yaml
exposure_and_focus:
  render_medium_reference:
  exposure_or_value_state:
  white_balance_or_medium_equivalent:
  highlight_protection:
  shadow_detail:
  depth_of_field_or_layer_separation:
  focus_target:
  focus_transition:
  lens_breathing_or_medium_equivalent:
```

- 真人、写实CG和三维动画可说明曝光、白平衡、镜头景深与虚拟摄影机焦点；
- 二维、2.5D、绘画和水墨项目可以用线条清晰度、明度层级、色彩边缘、分层虚化与视差表达焦点；
- 高光不能吞掉人物表面、镜面、刀刃、纸张或核心道具信息；
- 低调光不等于死黑；
- 焦点必须落在具体对象；
- 景深或虚化必须服务叙事，不能用来掩盖结构错误。

## 八、常用打光选择

### 自然顺光

适合身份展示和生活场景。必须说明光源位置、亮区与阴影，不得只写“柔和自然光”。

### 侧光

适合人物情绪、古风、历史、纪录、动画和悬疑。写清哪侧脸亮、哪侧脸暗、鼻影或风格化面部阴影方向。

### 侧逆光

适合轮廓分离和人物登场。不能无来源增加强轮廓光，也不能让正面信息消失。

### 逆光剪影

适合背影、告别和结尾。需要看清人物时必须补充低强度正面环境反射光或媒介等效明度分离。

### 窗口光或门缝光

适合室内悬念、手部和道具特写。写明窗口在世界空间中的位置、光束进入角度、照亮区域和阴影方向。

### 火光或烛光

暖色实景光应有合理衰减和轻微动态，但不能导致人物脸部光线乱跳。环境仍需建立对比层次，禁止全画面橙黄覆盖。

### 低调高对比光

适合秘密和压迫。关键人物、手部和道具必须可读，背景暗部仍保留空间地标。

### 柔光

适合亲密和身份参考。柔光不是无方向平光，仍需写明来源方向与阴影过渡。

### 顶光

适合审问、孤独和仪式。避免眼窝死黑、角色表面失读和无来源底光。

### 动画电影塑形光

适合风格化3D角色。明确面部主明暗、受控次表面散射、眼睛高光、发束明暗、服装大形与背景分离，禁止变成商业真人美妆灯或游戏默认轮廓光。

### 图形化二维光影

适合二维、2.5D、绘画与实验动画。明确色块、边缘、明度层、投影形状和帧间稳定性，禁止同时要求照片级体积光与平面图形互相冲突。

## 九、视频中的灯光连续性

视频Prompt必须明确：

- 主光或主明暗逻辑固定在世界空间或项目图形规则中；
- 人物移动时，亮暗变化符合距离、朝向或当前媒介规则；
- 面部阴影、道具高光和地面阴影连续；
- 实景灯或动画光效只允许剧本规定的自然波动；
- 禁止曝光跳变、光线闪烁、阴影漂移和色温呼吸；
- 首帧与尾帧的主光方向、色彩关系和明暗基准必须匹配；
- 抽尾帧续拍必须继承上一段的光线事实；
- 风格化动画不得在运动中突然真人化、塑料化或游戏截图化。

## 十、场景连续性

每个分镜Prompt必须继承：

- 相同主色体系；
- 相同白平衡或媒介色彩基准；
- 相同冷暖关系；
- 相同角色表面与背景关系；
- 相同黑位和高光策略；
- 相同场景主光世界位置或图形明暗规则；
- 相同材质和着色语言；
- 点缀色只能出现在预定人物、道具、光源或情节重点。

不同时间允许自然明暗变化，但必须在剧本和视觉设定中有依据，并说明变化幅度。

## 十一、夜景与暗场规则

- 暗部保留材质、轮廓和空间地标；
- 角色面部、手部和核心道具至少有一种可验证的可读性来源；
- 避免脏灰、压缩噪点、彩色斑块和死黑；
- 不使用无来源病态绿光作为恐怖捷径；
- 夜景降噪只修复噪点、边缘和色彩，不重构灯光；
- 二维或绘画暗场用明度、边缘和色块保证可读性，不机械模拟相机噪点。

## 十二、材质与影像质感

材质必须根据当前媒介写成可观察属性。

### 真人实拍与照片写实CG

按需使用：

- 自然皮肤区域差异、细小纹理和可信反光；
- 布料纤维、缝线、折痕和工艺；
- 木材、金属、纸张、玻璃、水、烟雾和尘埃的现实属性；
- 真实摄影透视、自然景深、宽动态范围和克制颗粒。

这些内容不是其他媒介的默认前缀。

### 风格化3D动画

按需使用：

- 设计化角色表面与动画电影级着色器；
- 受控次表面散射，不追求真人毛孔堆积；
- 发束、发片或曲线毛发的明暗分组与轮廓；
- 服装材质通过大形、褶皱、粗糙度和受力表现；
- 环境PBR可以被绘画化取舍，但材质类别必须清楚；
- 高光、边缘、阴影和纹理服务角色设计与画面层级；
- 禁止蜡像、塑料皮肤、真人照片贴图感和普通游戏资产感。

### 二维、2.5D、绘画与水墨

按需使用：

- 线条粗细、边缘硬软、色块、笔触、纸面、墨色、干湿和叠色；
- 分层景深、视差、局部纹理与图形化阴影；
- 禁止用照片纹理和复杂PBR替代绘画设计。

### 定格

按需使用实体布料、纸、黏土、木材、金属、纤维、模型接缝和逐帧人工痕迹，保持材料尺度可信。

### 游戏电影CG与混合媒介

明确引擎感、角色着色、环境材质、实时或离线渲染特征及分层合成职责，不使用“游戏CG”作为笼统质量判断。

## 十三、编译到最终Prompt

每条图片或视频Prompt必须包含当前镜头相关的：

```text
当前渲染媒介与表面语言
+ 主色与辅助色
+ 当前世界内部成立的光源或明暗来源
+ 方向、高度、软硬、边缘和冷暖关系
+ 主体具体受光区域
+ 阴影区域与方向
+ 辅光、实景灯和光比或明度层级
+ 曝光、焦点、景深或媒介等效层级
+ 高光和暗部要求
+ 角色、服装、道具和环境着色
+ 点缀色用途
+ 首尾帧和相邻镜头连续性
+ 禁止媒介漂移
```

不得只在Prompt包开头写一次全局灯光，然后在每镜中省略；也不得每镜重复一段与当前动作无关的真人摄影前缀。

## 十四、色调、灯光与媒介硬失败

- 没有读取`RENDER_MEDIUM_LOCK`；
- 把主色理解为整张图单色覆盖；
- 人物表面被背景色严重污染；
- 同一场景不同镜头色彩基准随机变化；
- 主光在世界空间中跟随摄影机移动；
- 只写“真实光照、电影感、动漫打光、冷色调”；
- 未说明主体亮区、阴影和暗部；
- 首尾帧主光方向、色彩关系或曝光不一致；
- 表演依赖眼神、嘴、手或身体变化，但灯光让关键区域不可读；
- 灯光为了情绪无原因变色、闪烁或自动跟随人物；
- 视频中出现曝光闪烁、阴影漂移和色温跳变；
- 点缀色大面积泛滥；
- 夜景主体完全不可读；
- 高光过曝掩盖核心信息；
- 高级感只依靠青橙滤镜、蓝色滤镜或低曝光；
- 风格化3D动画机械加入真人毛孔、真人写真、蜡像皮肤或游戏默认边光；
- 二维或绘画项目机械加入照片级PBR皮肤与相机噪点；
- 真人项目被动漫、二维或游戏CG示例污染；
- 角色、服装和背景使用互不相容的媒介与着色语言。
