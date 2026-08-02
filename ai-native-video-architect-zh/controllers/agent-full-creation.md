# Agent Full Creation Orchestrator V4.4

## 目标

当用户要求全套创作时，在Agent内部完成从开放故事创作到外部平台可执行Prompt的整条链路，同时严格区分**故事探索阶段**与**视觉制作阶段**。

```text
输入
→ 故事与剧本开放创作
→ 剧本门禁与NARRATIVE_LOCK
→ PROJECT_VISUAL_STRATEGY
→ 制作需求预分析
→ 规划资产与资产Prompt
→ 导演意图、摄影、灯光与表演设计
→ Shot拆解
→ CF设计
→ 图片Prompt
→ 视频Prompt
→ 内部验证与返修
→ FULL_CREATION_PACKAGE
```

项目视觉策略只能约束当前项目进入制作后的资产、镜头和Prompt，不能提前把所有故事锁成同一种审美。

## 一、任务路由

### SCRIPT_ONLY

用户只要求故事、剧本、视觉脚本或剧本改写时：

- 执行故事与剧本阶段；
- 完成必要的叙事检查；
- 输出剧本后停止；
- 不生成完整项目视觉策略、资产、Shot、CF或制作Prompt。

### DIAGNOSE_SCRIPT

只诊断人物、结构、主题、节奏、可视动作和生成难点，不强制进入视觉制作。

### ADAPT

用户已有成立内容并要求制作时：

- 先确认`NARRATIVE_LOCK`；
- 从当前剧本推导`PROJECT_VISUAL_STRATEGY`；
- 再进入资产、Shot、CF和Prompt。

### FULL_CREATION_PACKAGE

`CREATE`或`TRANSFORM`先完成剧本并通过剧本门禁，再自动进入`ADAPT`。视觉策略不得反向改变已锁定人物关系、核心机制、关键选择、高潮主体和结尾。

### SINGLE_IMAGE_PROMPT / IMAGE_TO_VIDEO

只建立当前图片或当前镜头的局部视觉合同，不伪称已经锁定整部作品。

## 二、设计态与实物态

Agent必须维护两套事实：

### 设计态

- 剧本、`NARRATIVE_LOCK`与项目视觉策略；
- 资产ID、Shot、CF和Prompt；
- 参考图用途和生成顺序；
- 预期连续性与备用方案。

### 实物态

- 用户真实生成或上传的图片；
- 实际选定尾帧；
- 实际生成片段；
- 真实验收结果。

全套Prompt包只要求设计态完整。实物态缺失不得阻止设计态交付。

## 三、NARRATIVE_LOCK

正式视觉制作前必须锁定：

- 主角或主体；
- 人物关系和核心处境；
- 世界规则或主要机制；
- 关键选择；
- 高潮行动者与不可逆变化；
- 结尾及开放程度；
- 主题意义；
- 用户允许修改的范围。

制作阶段可以改变实现方式和镜头方案，不能为了视觉风格擅自改写上述事实。

## 四、项目视觉策略

读取`controllers/project-visual-strategy.md`。

当用户未指定成熟视觉方向时，内部探索2—4个差异真实的视觉方向，再根据剧本支持度、观众体验、原创性和生产可行性选择主方向。

`PROJECT_VISUAL_STRATEGY`必须：

- 引用当前剧本证据；
- 标记`scope: PROJECT_ONLY`；
- 定义Style DNA、色彩、真实光源、材质、摄影、表演温度、声音、背景职责和视觉张力；
- 定义允许变化与禁止漂移；
- 给出资产、Shot、CF和生成实现的影响。

它保证当前项目内部统一，但不得让不同项目变成同一种作品。

## 五、资产覆盖规划

所有资产先注册ID，例如：

```text
CHAR-01-FACE   角色面部身份锚点
CHAR-01-TURN   角色正侧背结构参考
CHAR-01-COST   服装与发型结构参考
CHAR-01-HAND   手部与核心道具交互参考
LOC-01-MASTER  场景主布局空镜
LOC-01-REV     场景反向或必要机位参考
PROP-01        核心道具结构参考
STATE-01       污染、伤损、湿水、变装或阶段状态参考
STYLE-01       项目视觉策略参考
```

资产不是默认越少越好，也不是所有项目固定做全套。先预分析全部实际镜头需要的景别、正侧背角度、全身动作、近景、手部交互、服装结构、状态变化、场景反向机位和道具阶段，再决定资产集合。

存在以下需求时，相应资产必须列为REQUIRED，而不是等待失败后再补：

- 重要近景：独立面部身份依据；
- 正、侧、背或转身、背影：三视图或等效结构依据；
- 全身、俯身、跪姿、走动：全身比例与服装结构依据；
- 精确手部叙事：手部与道具交互依据；
- 灰烬、伤损、湿水、变装等累积：状态进程依据；
- 反向机位或空间局部：对应场景布局依据；
- 道具开合、页面、破损或阶段变化：道具状态依据。

每个资产必须说明用途、使用Shot、项目视觉策略继承、Prompt、负面约束和输出规则。

## 六、Shot编译

每个Shot必须先形成结构化镜头事实，再写Prompt：

```yaml
shot_id:
scene_id:
narrative_purpose:
visual_description:
input_state:
primary_action:
director_intent:
camera_direction:
lighting_direction:
performance_direction:
emotion_curve:
exact_end_state:
project_visual_strategy_reference:
reference_bindings:
frame_source_mode:
control_frames:
generation_mode:
continuity_handoff:
risk_and_fallback:
```

不得直接从一句剧情摘要跳到自由Prompt。

## 七、CF编译

CF只承担当前Shot的可见控制状态：

```yaml
control_frame:
  cf_id:
  shot_id:
  type: START | END | BRIDGE | TEXT_CONTRACT_ONLY
  visible_state:
  project_visual_strategy_reference:
  source_assets: []
  inherited_state:
  positive_prompt:
  negative_prompt:
  output_rules:
```

若不需要预生成尾帧，必须建立`TEXT_CONTRACT_ONLY`并明确抽取稳定尾帧的选择标准。

## 八、参考解析

每个Shot必须解析为：

```text
项目视觉策略
+ 身份与结构参考
+ 场景和必要机位参考
+ 必要道具或状态参考
+ 上一镜尾帧或当前新构图参考
```

没有新图时写明继承，不得留空。

## 九、逐镜头Prompt编译

### 图片Prompt

描述首帧、尾帧或桥接帧的单一静态瞬间。剧情帧同时编译当前项目视觉策略、视觉张力来源、背景职责与大形、前中后景和冻结运动痕迹；技术型资产板优先生产清晰度。

### 视频Prompt

描述该静态瞬间之后按时间发生的变化。图生视频先锁定首帧身份、美术、构图和光线，再围绕唯一核心视觉事件控制身体部位动作顺序、内外层材质运动、背景事件、摄影机、灯光、最后1—2秒视觉峰值、结束状态和下一镜传递。

### POST_ONLY

精确文字、复杂镜面、图层效果或纯剪辑镜头可以标记为POST_ONLY，但必须给素材来源、后期操作和剪辑位置。

## 十、内部验证

按顺序执行：

1. `NARRATIVE_LOCK_PRESERVATION_CHECK`；
2. `PROJECT_VISUAL_STRATEGY_SCOPE_CHECK`；
3. `PROJECT_VISUAL_STRATEGY_CONFORMANCE_CHECK`；
4. `ASSET_ANGLE_INTERACTION_STATE_COVERAGE_CHECK`；
5. `SHOT_COMPLETENESS_CHECK`；
6. `CF_BINDING_CHECK`；
7. `PROMPT_COVERAGE_CHECK`；
8. `DIRECTING_COHERENCE_CHECK`；
9. `PERFORMANCE_DIRECTION_SCORE`；
10. `PAIRWISE_CONTINUITY_CHECK`；
11. `PROMPT_CONFLICT_CHECK`；
12. `GENERATION_FEASIBILITY_CHECK`；
13. `FINAL_PACKAGE_INTEGRITY_CHECK`。

发现问题后局部修复，不重新随机改写整部作品。

## 十一、外部生成顺序

最终包末尾给出：

1. 先生成哪些身份、结构、状态和场景资产；
2. 哪些资产存在依赖关系；
3. 哪些首帧可以并行；
4. 哪些Shot必须依赖上一镜真实尾帧；
5. 哪些使用首尾帧；
6. 哪些需要分层或后期；
7. 哪个普通镜头和哪个高风险镜头适合先实测。

这只是执行建议，不是阻塞完整Prompt包的确认门。
