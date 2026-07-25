# AI Native Film Studio V3.3

## AI原生电影导演、剧本拆解、资产与制作工作室

显式调用：

```text
$ai-native-video-architect-zh
```

调用后，Skill会先告诉你目前做到哪一步：

```text
【项目进度｜S04/13 剧本拆解】
已完成：✓ 创作需求 ✓ 创意方向 ✓ 故事方案 ✓ 剧本
正在进行：提取角色、服装、场景、道具和状态变化
本轮交付：剧本拆解表
需要你确认：是否遗漏关键资产或状态
下一步：S05 视觉圣经
```

它不会默认所有项目都从零开始。你有完整剧本时可直接进入剧本拆解；有资产图时会先进入资产审核；有完整资产和分镜帧时会先做Core Sample。

## 完整短视频流程

```text
S00 创作需求
→ S01 创意方向
→ S02 故事方案
→ S03 剧本或视觉脚本
→ S04 剧本拆解
→ S05 视觉圣经
→ S06 资产计划
→ S07 资产制作
→ S08 资产审核
→ S09 分镜设计
→ S10 分镜帧与提示词
→ S11 核心样片
→ S12 批量制作与后期
→ S13 导演审查与交付
```

## 为什么必须先有剧本

“资产先行”并不是没有故事就先做角色和场景。

正确含义是：

> 相对于正式分镜帧和视频生成，资产必须先行；相对于故事和剧本，资产不能盲目先行。

角色、服装、场景和道具提示词都需要从剧本中提取：

- 角色是谁、处于什么身体和情绪状态；
- 穿什么服装，在哪一场发生变化；
- 场景是什么空间，人物从哪里进入和离开；
- 道具由谁持有、使用哪只手、状态如何变化；
- 每项资产在哪些镜头中出现。

没有可拆解剧本或视觉脚本时，只能做概念探索，不能宣称已经得到可稳定生产的资产和分镜。

传统对白剧本不是唯一格式。无对白、意识流、广告或MV可以使用完整视觉脚本，但至少要包含：主体、场景、初始状态、动作、环境变化、道具变化、情绪变化、结束状态和下一场连接。

## 项目进度导航

进度提示会在以下时机出现：

- 第一次调用Skill；
- 用户选定方向、确认剧本、确认资产或确认分镜后；
- 当前阶段完成并进入下一阶段；
- 资产审核或Core Sample未通过；
- 用户带着现有剧本、资产或分镜中途进入；
- 用户询问“现在做到哪一步”。

进度不会虚报：

- 未选择的方向不能显示完成；
- 未确认的剧本不能显示完成；
- 用户自带资产也必须先审核；
- 只完成部分分镜不能把整个阶段标记完成；
- Core Sample失败不能进入批量生产。

用户明确说“不显示进度”后，可以隐藏进度提示。

## 四个确认门和一个生产门

### STORY_DIRECTION_CONFIRMATION

确认选定的方向、主角、核心事件、情绪和结尾方向。

### SCRIPT_CONFIRMATION

确认剧本或视觉脚本内容已锁定，可以进行制作拆解。

### ASSET_CONFIRMATION

资产评分达到85且无硬失败后，确认角色、服装、场景、道具和状态版本。

### STORYBOARD_CONFIRMATION

确认镜头数量、目的、动作、构图、机位、运镜、时长和制作难度。

### CORE_SAMPLE_GATE

至少验证一名角色、一个主场景、一个核心道具、一次首尾帧或硬切和一个3—8秒样片。未通过不得批量生成。

## 创作前访谈

宽泛请求如“帮我做一个短视频”会先通过选择或填空确认：

- 类型和题材；
- 目标情绪；
- 剧情、视觉或意识流形式；
- 场景和主角；
- 关系或表达焦点；
- 对白与旁白；
- 结尾；
- 时长和画幅；
- 工具或制作阶段；
- 明确禁忌。

已给出的内容不会重复询问。确认后先提供2—3个差异明显的方向，选定后进入故事方案和剧本。

## 剧本拆解

剧本确认后，Skill不会直接跳到长篇Prompt，而会先提取：

### 角色

- 年龄、身份、性格和身体状态；
- 首次与最后出现；
- 情绪和动作语言；
- 需要保持一致的角度和景别。

### 发型、妆造和服装

- 发型结构；
- 服装内外层；
- 每套服装使用场次；
- 淋湿、染血、破损、沾灰等状态变化点。

### 场景

- 空间布局、出入口和固定地标；
- 时间、天气和主光方向；
- 同一空间的不同剧情状态；
- 需要生成的空镜与多机位。

### 道具

- 尺寸、材质和独特标记；
- 持有者、左右手和使用方式；
- 出现场次；
- 状态时间线和产生镜头。

## Visual Bible与Asset Pack

剧本拆解后建立Visual Bible，再制作资产。

### 角色资产

- 正面、严格侧面、背面生产三视图；
- 面部身份板；
- 发型正侧背；
- 服装结构与状态；
- 手部与道具交互；
- 关键姿态和动作语言。

### 场景资产

- 主布局和出入口；
- 无人物空镜；
- 前中后景固定地标；
- 光线方向、时间与天气；
- 多机位参考；
- 场景状态版本。

### 道具资产

- 尺寸和人体比例；
- 正侧背结构；
- 材质、工艺和历史；
- 持有与使用逻辑；
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

## 分镜设计与分镜提示词

分镜分两步：

### S09 分镜设计

先决定：

- 镜头为什么存在；
- 景别、机位和轴线；
- 人物唯一主要动作；
- 摄影机运动和动机；
- 观众先看到什么；
- 镜头如何结束；
- 下一镜继承什么；
- 生成风险和替代方案。

### S10 分镜帧与提示词

分镜确认后，才引用已批准资产制作首帧、尾帧和Prompt。

图片Prompt负责：人物是谁、穿哪个版本、在哪里、道具是什么状态、构图和光线如何。

视频Prompt负责：使用哪张首帧、从什么状态开始、完成哪个动作、摄影机怎么动、最后停在哪里、哪些内容不能变化。

## 详细分镜默认摄影规格

用户未另行指定时，电影级横屏详细分镜可默认采用：

- 21:9；
- ARRI Alexa 35或Alexa LF成像参考；
- 克制anamorphic；
- 24fps、180度快门；
- 普通真实演员皮肤；
- 有来源的材质磨损；
- 柔和高光滚降和暗部纹理；
- 有动机的摄影机运动。

这些是默认值，不覆盖用户明确指定的画幅和风格。

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

- `CREATIVE_BRIEF`
- `DIRECTION_OPTIONS`
- `STORY_TREATMENT`
- `SCRIPT_PACKAGE`
- `SCRIPT_BREAKDOWN`
- `DEVELOPMENT_PACKAGE`
- `ASSET_PLAN`
- `ASSET_PACK`
- `DIRECTOR_PACKAGE`
- `DETAILED_STORYBOARD`
- `PRODUCTION_PACK`

## 关键文件

- `config/progress-navigation.yaml`
- `templates/progress-status.md`
- `config/workflow.yaml`
- `controllers/director-agent.md`
- `controllers/asset-first-production.md`
- `controllers/detailed-storyboard.md`
- `tests/progress-navigation-stress-tests.md`

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
