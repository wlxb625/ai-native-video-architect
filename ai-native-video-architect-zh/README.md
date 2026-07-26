# AI Native Film Studio V4.2

## 从创意、剧本到导演级生图、分镜和视频Prompt的完整中文Skill

显式调用：

```text
$ai-native-video-architect-zh
```

这个Skill同时负责：

```text
创意、故事与剧本创作
+
剧本确认后的参考图、分镜帧和导演级视频Prompt生产
```

用户不需要在剧本完成后切换到另一个Skill。

## 能力入口

- 从想法、人物、题材或情绪开始完成故事与剧本；
- 读取已有大纲、剧本或视觉脚本继续制作；
- 使用已有角色图、场景图、道具图或分镜图；
- 单独生成某个角色板、场景空镜、首尾帧或视频Prompt；
- 修复已经生成但不连贯、换脸、漂光或动作错误的视频。

## 剧本后生产

### 最小核心参考

普通短片默认只制作最必要的参考图：

- 每名主要角色一张综合角色板或三视图；
- 每个主要场景一张无人物空镜；
- 必须跨镜头稳定的核心道具结构或状态板；
- 剧情必须精确控制的特殊状态板。

独立面部、发型、服装、手部、多机位和技术测试只在实际失败后补充。

### 分镜设计

每镜明确镜头任务、主要动作、景别、焦段、机位、轴线、前中后景、构图、焦点、灯光、时长、结束状态和下一镜连接。

### 分镜帧Prompt

图片Prompt只描述准确静态瞬间。每镜都要设计首帧和结束帧合同；是否预生成尾帧，由视频生成模式决定。

第一张分镜通常使用：

```text
角色参考 + 场景空镜 + 核心道具参考 + 当前镜头要求
```

后续分镜优先使用：

```text
角色参考 + 场景空镜 + 上一张满意分镜 + 当前镜头要求
```

## V4.2 导演级视频Prompt

视频Prompt不再只是“人物缓慢移动、镜头推进”。每镜必须同时控制：

- 单首帧、首尾帧、抽尾帧续拍、遮挡硬切或分层合成；
- 前景、中景、背景和构图重心；
- 人物起始姿态、左右手、视线、重心和道具接触；
- 按秒划分的动作时间轴；
- 动作距离、方向、速度、重量和接触；
- 焦段、机位高度、距离、角度和屏幕方向；
- 运镜开始时间、结束时间、幅度和终点；
- 焦点、景深、曝光、白平衡、高光和暗部；
- 当前镜头具体的主光、辅光、色温、光比、亮区和阴影；
- 可截图验证的精确尾帧；
- 下一镜继承、声音、稳定项和负面约束。

### 单首帧边界

单首帧只用于呼吸、眨眼、雨、水波、布料微动等低幅度运动，并且下一镜不依赖准确姿势、手部、道具、焦点或构图。

单首帧仍须编写完整结束帧合同，并在生成后抽取稳定尾帧。

### 首尾帧默认条件

出现以下任一情况时默认使用首尾帧：

- 下一镜需要继承姿势、视线、手部或道具位置；
- 人物、服装、表情或状态变化；
- 道具被移动、翻转、打开、清理或破坏；
- 运镜改变最终构图、景别或焦点；
- 动作终点承担叙事信息；
- 单首帧容易随机结束。

### 复杂镜头

镜面人物、倒影、雾气、精确文字、遮挡前后状态切换和复杂手部，不强迫一个模型一次完成。优先使用两段视频、遮挡切换、抽尾帧续拍和分层合成。

## 逐镜灯光

每条最终视频Prompt必须写清：

- 真实光源；
- 世界空间方向和人物相对方向；
- 色温、软硬和强弱；
- 照亮的具体区域；
- 阴影区域与方向；
- 辅光、实景灯和背景光；
- 大致光比；
- 高光与暗部策略；
- 前后镜头连续性；
- 禁止闪烁、漂移、偏色和无来源轮廓光。

只写“真实光照、电影感、冷色调”属于硬失败。

## 用户资料优先

当用户提供Prompt工程资料、教程或模板时，必须先读取原文。原资料结构、主体Prompt、负面约束和输出方式优先；自行补充内容必须明确区分。

## 主要文件

- `SKILL.md`
- `AGENT.md`
- `controllers/post-script-production.md`
- `prompt-engineering/image-prompt-compiler.md`
- `prompt-engineering/visual-style-color-light.md`
- `prompt-engineering/asset-prompt-system.md`
- `prompt-engineering/storyboard-frame-system.md`
- `prompt-engineering/video-prompt-compiler.md`
- `prompt-engineering/continuity-repair-system.md`
- `templates/storyboard-frame-prompt-block.md`
- `templates/video-shot-prompt-block.md`

## 安装

```bash
git clone https://github.com/wlxb625/ai-native-video-architect.git
cd ai-native-video-architect/ai-native-video-architect-zh
python scripts/validate_package.py
```

Skill负责创作、导演设计和Prompt生产，不直接替代外部生图、视频生成、剪辑和声音软件。
