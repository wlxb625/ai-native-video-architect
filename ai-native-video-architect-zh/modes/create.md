# CREATE Mode

从原始灵感建立创作需求、方向、故事、剧本或视觉脚本、资产、分镜与可制作方案。

## 启动协议

开始时先读取：

- `config/progress-navigation.yaml`
- `templates/progress-status.md`

然后确定：

1. 操作模式：CREATE；
2. 主导演模式：STORY_DIRECTOR / VISUAL_DIRECTOR / BLOCKBUSTER_DIRECTOR / EXPERIMENTAL_DIRECTOR / PRODUCTION_DIRECTOR；
3. 创作路径：COMMERCIAL / LITERARY / EXPERIMENTAL / HYBRID；
4. 当前阶段：S00—S13；
5. 本轮最小输出层级。

首次响应先显示当前进度。用户已有成熟材料时从对应阶段进入，不强制从S00开始。

## CREATE标准路径

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

## S00：创作需求

关键方向不足时，用选择题或填空确认：类型、情绪、形式、场景、主角、关系、规模、对白与旁白、结尾、时长、画幅、工具和禁忌。

已给出的信息不得重复询问。

## S01：创意方向

给出2—3个真正不同的方向。差异应来自：

- 人物任务；
- 核心事件或视觉规则；
- 情绪回报；
- 结尾；
- 制作方法和难度。

不得只更换美术风格。用户选择或明确合并后通过`STORY_DIRECTION_CONFIRMATION`。

## S02：故事方案

剧情片输出`Story Treatment`；无对白、广告、MV或实验项目可以输出`Visual Treatment`。

至少包含：

```yaml
story_treatment:
  one_sentence_story:
  protagonist_or_subject:
  primary_task_or_visual_action:
  central_event_or_rule:
  progression:
  emotional_arc:
  final_image:
```

高概念项目同时检查单一机制、不可逆压力、艰难选择和因果化核心画面。

## S03：剧本或视觉脚本

正式资产生产前必须完成可拆解文本。

### 剧情剧本

至少包含：场次、时间、地点、人物、动作、对白、道具和场景结束状态。

### 视觉脚本

至少包含：

```yaml
visual_scene:
  location_and_time:
  subject:
  initial_state:
  observable_action:
  environment_change:
  prop_change:
  emotional_change:
  final_state:
  next_scene_connection:
```

无对白不等于不需要剧本。传统格式不是唯一选择，但只有一句概念或一组意象时不能批量设计资产和分镜。

用户确认后通过`SCRIPT_CONFIRMATION`。

## S04：剧本拆解

提取：

- 角色、年龄、身份、身体与情绪状态；
- 发型、妆造、服装版本和变化点；
- 场景、布局、时间、天气和状态版本；
- 道具尺寸、材质、持有者、左右手、交互和状态链；
- 每个资产首次和最后出现；
- 制作难点与依赖镜头。

每一项资产必须能追溯到剧本或明确导演需求。

## S05—S08：视觉与资产

顺序必须是：

```text
Visual Bible
→ Asset Registry
→ 角色/服装/场景/道具资产
→ Asset Readiness Gate
```

资产评分：

- 85以上且无硬失败：进入正式分镜；
- 70—84：仅允许Core Sample；
- 低于70或有硬失败：返回S06/S07修复。

资产通过后由用户完成`ASSET_CONFIRMATION`。

## S09—S10：分镜与提示词

先设计镜头，再写提示词。

S09确定：镜头目的、资产依赖、输入状态、景别、机位、轴线、动作、运镜、揭示顺序、声音、输出状态、剪辑连接和风险替代。

通过`STORYBOARD_CONFIRMATION`后，S10才批量制作：

- 首帧图片Prompt；
- 必要时的尾帧图片Prompt；
- 视频动作Prompt；
- 禁止变化和连续性锚点。

图片Prompt负责静态身份和画面；视频Prompt负责运动，不重新发明资产。

## S11：Core Sample

正式批量生产前至少验证：

- 一名角色跨两个角度；
- 一个场景跨两个机位；
- 一个道具尺寸和状态；
- 一次首尾帧或硬切；
- 一个3—8秒样片。

`CORE_SAMPLE_GATE`未通过时返回具体薄弱阶段，不继续批量生成。

## S12—S13：制作、后期与交付

管理S/A/B/C、资产复用、生成批次、版本、续拍、硬切、剪辑、声音、音乐、字幕、调色和交付。最后运行导演审查，只修薄弱层。

## 高概念CREATE补充

高概念项目先通过概念压缩和故事方案，不直接铺写大量世界观或资产：

```yaml
one_sentence_concept:
core_mechanism:
primary_task:
irreversible_pressure:
impossible_choice:
signature_visuals:
final_image:
```

候选差异必须来自机制、人物选择或结尾，不得只是换美术风格。

## 视觉叙事CREATE补充

视觉叙事不是图片合集。必须建立：

- 人物—世界关系；
- 重复动作；
- 关系物件；
- 视觉母题的建立、变义与回收；
- 发现、接近、重解释、余留的顺序；
- 完整视觉脚本。

## CREATE禁止

- 不显示当前阶段就连续输出整套流程；
- 用户未选方向就宣称故事方向完成；
- 剧本未确认就进入正式资产生产；
- 只有概念或氛围图就批量写资产和分镜Prompt；
- 资产未审核就宣称角色、场景和道具一致；
- 分镜未确认就批量制作首尾帧；
- Core Sample失败仍继续批量生成；
- 强制所有作品反击、获胜、反转或封闭结尾；
- 把意识流理解为互不相关的超现实画面拼贴；
- 一次性机械输出全部模板，而不考虑当前决策阶段。
