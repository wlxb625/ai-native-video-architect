# Agent Full Creation Orchestrator V4.4

## 目标

当用户要求全套创作时，在Agent内部完成从创作输入到外部平台可执行Prompt的整条链路，不等待真实参考图或样片返回。

```text
输入
→ 剧本
→ 视觉规则
→ 规划资产与资产Prompt
→ 导演意图、摄影、灯光与表演设计
→ Shot拆解
→ CF设计
→ 图片Prompt
→ 视频Prompt
→ 内部验证与返修
→ FULL_CREATION_PACKAGE
```

## 一、设计态与实物态

Agent必须维护两套事实：

### 设计态

- 剧本、视觉规则、资产ID；
- Shot、CF和Prompt；
- 参考图用途和生成顺序；
- 预期连续性与备用方案。

### 实物态

- 用户真实生成或上传的图片；
- 实际选定尾帧；
- 实际生成片段；
- 真实验收结果。

全套Prompt包只要求设计态完整。实物态缺失不得阻止设计态交付。

## 二、设计态资产注册

所有资产先注册ID：

```text
CHAR-01      角色身份锚点
CHAR-01-FULL 角色全身服装参考
LOC-01       场景无人物空镜
PROP-01      核心道具结构参考
STATE-01     特殊状态参考
STYLE-01     项目风格参考
```

每个资产必须说明：用途、使用镜头、Prompt、负面约束和输出规则。

## 三、Shot编译

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
reference_bindings:
frame_source_mode:
control_frames:
generation_mode:
continuity_handoff:
risk_and_fallback:
```

不得直接从一句剧情摘要跳到自由Prompt。

## 四、CF编译

CF只承担当前Shot的可见控制状态：

```yaml
control_frame:
  cf_id:
  shot_id:
  type: START | END | BRIDGE | TEXT_CONTRACT_ONLY
  visible_state:
  source_assets: []
  inherited_state:
  positive_prompt:
  negative_prompt:
  output_rules:
```

若不需要预生成尾帧，必须建立`TEXT_CONTRACT_ONLY`并明确抽取稳定尾帧的选择标准。

## 五、参考解析

每个Shot必须解析为：

```text
身份参考
+ 场景参考
+ 必要道具或状态参考
+ 上一镜尾帧或当前新构图参考
```

没有新图时写明继承，不得留空。

## 六、逐镜头Prompt编译

### 图片Prompt

描述首帧、尾帧或桥接帧的单一静态瞬间；剧情帧同时编译视觉张力来源、背景功能与大形、前中后景和冻结运动痕迹，资产板则优先生产清晰度。

### 视频Prompt

描述该静态瞬间之后按时间发生的变化。图生视频先锁定首帧身份、美术、构图和光线，再围绕唯一核心视觉事件控制身体部位动作顺序、内外层材质运动、背景事件、摄影机、灯光、最后1—2秒视觉峰值、结束状态和下一镜传递。

### POST_ONLY

精确文字、复杂镜面、图层效果或纯剪辑镜头可以标记为POST_ONLY，但必须给素材来源、后期操作和剪辑位置。

## 七、内部验证

按顺序执行：

1. `ASSET_COVERAGE_CHECK`；
2. `SHOT_COMPLETENESS_CHECK`；
3. `CF_BINDING_CHECK`；
4. `PROMPT_COVERAGE_CHECK`；
5. `DIRECTING_COHERENCE_CHECK`；
6. `PERFORMANCE_DIRECTION_SCORE`；
7. `PAIRWISE_CONTINUITY_CHECK`；
8. `PROMPT_CONFLICT_CHECK`；
9. `GENERATION_FEASIBILITY_CHECK`；
10. `FINAL_PACKAGE_INTEGRITY_CHECK`。

发现问题后局部修复，不重新随机改写整部作品。

## 八、外部生成顺序

最终包末尾给出：

1. 先生成哪些资产图；
2. 哪些首帧可以并行；
3. 哪些Shot必须依赖上一镜真实尾帧；
4. 哪些使用首尾帧；
5. 哪些需要分层或后期；
6. 哪个普通镜头和哪个高风险镜头适合先实测。

这只是执行建议，不是阻塞完整Prompt包的确认门。
