# AI Native Film Studio V3.2

## AI原生电影导演、资产与制作工作室

显式调用：

```text
$ai-native-video-architect-zh
```

它把一个想法逐步转化为：

```text
创作访谈
→ 概念与剧本
→ 视觉叙事与镜头语言
→ Visual Bible
→ 角色、服装、场景与道具资产
→ Asset Readiness Gate
→ 首帧、尾帧与详细分镜
→ 视频动作Prompt、续拍和硬切
→ 制片、声音、调色、传播与导演审查
```

## V3.2最重要的变化

以前很多流程从剧本直接跳到逐镜头Prompt。即使每个镜头写得很长，模型仍会重新设计人物、建筑和道具。

V3.2改为**资产先行**：

- 角色先做生产三视图、面部身份、发型和姿态；
- 服装先做结构板和状态链；
- 场景先做主布局、无人物空镜和多机位；
- 道具先做尺寸、三视图、交互关系和状态版本；
- 镜头引用资产ID，不重复发明人物和空间；
- 图片Prompt负责静态画面，视频Prompt负责运动；
- 精确变化优先使用首尾帧；
- 同场继续使用尾帧续拍，换机位使用硬切连续性；
- 批量生成前先做Core Sample和资产审核。

## 创作前访谈

宽泛请求如“帮我写个剧本”会先通过选择或填空确认：

- 类型；
- 目标情绪；
- 剧情、视觉或意识流形式；
- 场景和主角；
- 关系或表达焦点；
- 对白与旁白；
- 结尾；
- 时长和画幅；
- 工具或制作阶段；
- 明确禁忌。

已给出的内容不会重复询问。确认后先提供2—3个差异明显的方向，选定后再写完整剧本。

## 双重路由

操作模式：

- `CREATE`
- `TRANSFORM`
- `DIAGNOSE`
- `ADAPT`

导演模式：

- `STORY_DIRECTOR`
- `VISUAL_DIRECTOR`
- `BLOCKBUSTER_DIRECTOR`
- `EXPERIMENTAL_DIRECTOR`
- `PRODUCTION_DIRECTOR`

## 输出层级

- `CONCEPT_DIRECTION`
- `DEVELOPMENT_PACKAGE`
- `ASSET_PACK`
- `DIRECTOR_PACKAGE`
- `DETAILED_STORYBOARD`
- `PRODUCTION_PACK`

## Asset Pack

### 角色

- 正面、严格侧面、背面三视图；
- 面部身份板；
- 发型正侧背；
- 服装状态；
- 手部与道具交互；
- 关键姿态和动作语言。

### 场景

- 主布局与出入口；
- 无人物空镜；
- 前中后景固定地标；
- 光线方向与时间天气；
- 多机位参考；
- 场景状态版本。

### 道具

- 尺寸和人体比例；
- 正侧背结构；
- 材质、工艺和历史；
- 持有和使用逻辑；
- 独特标记；
- 状态时间线。

核心文件：

- `controllers/asset-first-production.md`
- `evals/asset-readiness-score.md`
- `templates/asset-registry.md`
- `templates/character-asset-pack.md`
- `templates/environment-asset-pack.md`
- `templates/prop-asset-pack.md`
- `templates/frame-generation-pack.md`

## 详细分镜

用户未另行指定时，电影级横屏详细分镜可默认采用：

- 21:9；
- ARRI Alexa 35或Alexa LF成像参考；
- 克制anamorphic；
- 24fps、180度快门；
- 普通真实演员皮肤；
- 有来源的材质磨损；
- 柔和高光滚降和暗部纹理；
- 有动机的摄影机运动。

每个生产镜头包含资产引用、输入状态、首帧、唯一动作、摄影机计划、输出状态、必要尾帧、声音、风险和稳定替代。

## 图片Prompt与视频Prompt

图片Prompt负责：人物是谁、穿哪个版本、在哪里、道具是什么状态、构图和光线如何。

视频Prompt负责：使用哪张首帧、从什么状态开始、完成哪个动作、摄影机怎么动、最后停在哪里、哪些内容不能变化。

## 生产门槛

`Asset Readiness Score`：

- 85—100：可进入正式分镜或视频生成；
- 70—84：只做Core Sample；
- 低于70或存在硬失败：返回资产设计。

批量生产前至少验证：

- 一名角色跨两个角度一致；
- 一个场景跨两个机位一致；
- 一个核心道具稳定；
- 一次首尾帧或硬切衔接；
- 一个3—8秒Core Sample。

## 安装

```bash
git clone https://github.com/wlxb625/ai-native-video-architect.git
cd ai-native-video-architect/ai-native-video-architect-zh
```

Windows目录：

```text
%USERPROFILE%\.agents\skills\ai-native-video-architect-zh
```

macOS / Linux目录：

```text
$HOME/.agents/skills/ai-native-video-architect-zh
```

## 验证

```bash
python scripts/validate_package.py
```

## 当前边界

Skill保存稳定的创作和制作原则，不永久写死视频模型版本、价格、额度、平台算法和实时版权状态。需要时应查询最新信息。
