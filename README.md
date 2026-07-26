# AI Native Film Studio V4.0

一套中文AI电影全流程导演、剧本拆解、资产Prompt、分镜帧、视频Prompt与后期制作Skill。

显式调用：

```text
$ai-native-video-architect-zh
```

## 完整链路

```text
S00 创作需求
→ S01 创意方向
→ S02 故事方案
→ S03 剧本或视觉脚本
→ S04 剧本拆解
→ S05 视觉圣经
→ S06 资产计划
→ S07 整批资产Prompt与资产制作
→ S08 用户自审与资产确认
→ S09 分镜设计
→ S10 整批分镜帧Prompt
→ S11 核心样片
→ S12 整批视频生产与后期
→ S13 导演审查与交付
```

## V4.0：剧本之后的Prompt工程全流程

V4.0在V3.3的剧本优先、资产先行和进度导航基础上，加入完整的生图与视频Prompt生产系统：

- 色调六轴与真实光源合同；
- 面部身份板、三视图、发型、服装、手部与动作资产；
- 场景主布局、无人物空镜和多机位；
- 道具结构、尺寸、磨损和状态链；
- 图片Prompt编译、图生图修改、局部修复、降噪与4K增强；
- 分镜首帧、尾帧、九宫格、多人站位和硬切新机位；
- 图生视频、首尾帧视频、人物动作、环境氛围和声音；
- 固定、推拉摇移、跟拍、环绕、FPV、焦点转移等运镜；
- 抽尾帧续拍、多角度防穿帮、台词修复和失败恢复。

## 阶段交互规则

- S07一次性交付全部资产Prompt，不逐资产等待；
- S09一次性设计完整镜头表；
- S10一次性交付全部首尾帧Prompt；
- S11一次性交付核心样片测试包；
- S12一次性交付全片视频Prompt和后期方案；
- 用户默认在外部工具中自行筛选和审核；
- 用户回复“下一步”表示进入下一个阶段，不是同阶段下一张图；
- 只有用户明确请求时才由助手逐图或逐段辅助审核。

## Prompt工程模块

```text
ai-native-video-architect-zh/prompt-engineering/
├─ image-prompt-compiler.md
├─ visual-style-color-light.md
├─ asset-prompt-system.md
├─ storyboard-frame-system.md
├─ video-prompt-compiler.md
├─ camera-movement-library.md
└─ continuity-repair-system.md
```

剧本确认后的生产流程由：

```text
controllers/post-script-production.md
```

统一编排。

## 安装

```bash
git clone https://github.com/wlxb625/ai-native-video-architect.git
cd ai-native-video-architect/ai-native-video-architect-zh
```

复制到：

```text
Windows: %USERPROFILE%\.agents\skills\ai-native-video-architect-zh
macOS/Linux: $HOME/.agents/skills/ai-native-video-architect-zh
```

## 验证

```bash
python scripts/validate_package.py
```

详细说明见 `ai-native-video-architect-zh/README.md`。
