# AI Native Film Studio V3.3

一套中文AI电影导演、剧本拆解、资产设计与制作Skill。

显式调用：

```text
$ai-native-video-architect-zh
```

调用后会先显示当前项目进度：已经完成什么、正在做什么、本轮交付什么、需要用户确认什么、下一步是什么。

## 完整链路

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

## V3.3：可见进度与剧本优先

V3.3解决两个流程问题：

1. 用户不知道当前做到哪一步；
2. “资产先行”容易被误解成没有剧本就先做角色和场景。

正确顺序是：

> 故事和剧本先确定；资产相对于正式分镜帧和视频生成先行。

正式生产前先完成剧本或视觉脚本，并从中拆解角色、服装、场景、道具和状态变化。之后建立Visual Bible、资产台账、生产资产与审核门，再进入分镜设计、首尾帧和视频Prompt。

## 项目进度提示

默认格式：

```text
【项目进度｜S04/13 剧本拆解】
已完成：✓ 创作需求 ✓ 创意方向 ✓ 故事方案 ✓ 剧本
正在进行：提取角色、服装、场景、道具和状态变化
本轮交付：剧本拆解表
需要你确认：是否遗漏关键资产或状态
下一步：S05 视觉圣经
```

用户已有完整剧本、资产或分镜时，Skill会从对应阶段进入，不强制重走全部流程；但未经审核的资产不会直接标记为通过。

## 确认门

- `STORY_DIRECTION_CONFIRMATION`
- `SCRIPT_CONFIRMATION`
- `ASSET_CONFIRMATION`
- `STORYBOARD_CONFIRMATION`
- `CORE_SAMPLE_GATE`

未确认的方向、剧本、资产和分镜不会被虚假标记为完成。Core Sample未通过时不得批量生成。

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

## 核心文件

- `config/progress-navigation.yaml`
- `templates/progress-status.md`
- `config/workflow.yaml`
- `controllers/director-agent.md`
- `controllers/asset-first-production.md`
- `evals/asset-readiness-score.md`
- `tests/progress-navigation-stress-tests.md`

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
