# DIAGNOSE Mode

只分析作品为什么成立或失效，默认不直接重写。

## 五类发现

- BUG：非预期错误。
- RISK：当前成立但可能失效。
- CHOICE：有意设计，应保护。
- OPPORTUNITY：可选增强。
- PREFERENCE：审美、市场或受众偏好。

## 优先级

P0基础失控；P1核心体验；P2表达效率；P3可选优化。

高概念和导演包的P1顺序：

1. 一句话概念与核心情绪；
2. 单一核心机制或形式规则；
3. 人物任务、可观察行动或有意不行动；
4. 艰难选择与代价；
5. 人物—世界关系；
6. 视觉母题与重解释；
7. 镜头观看目的和揭示顺序；
8. 奇观因果；
9. 最后残像；
10. AI可生成、可剪辑和可恢复性；
11. 其他世界观、风格和包装细节。

不得先纠结术语、滤镜、镜头型号或风格名称，而忽略作品无法被理解和复述。

## 每项发现必须包含

位置、证据、已建立规则、分类、优先级、影响、最小修复、较强方向、must_protect和下一模式。

## 高概念诊断

```yaml
high_concept_diagnosis:
  current_retell_sentence:
  strongest_unique_idea:
  competing_core_ideas: []
  primary_task:
  task_confusion:
  core_mechanism:
  extra_mechanisms: []
  impossible_choice:
  choice_bypass:
  causal_hero_shots: []
  decorative_spectacles: []
  predictable_twist:
  final_afterimage:
  worldbuilding_to_remove_or_merge: []
```

## 视觉叙事诊断

读取 `controllers/visual-narrative.md` 与 `evals/visual-narrative-score.md`。

```yaml
visual_narrative_diagnosis:
  character_world_relationship:
  observable_character_action:
  exposition_dependency:
  recurring_action:
  relationship_object:
  motifs:
    - motif:
      first_state:
      changed_state:
      final_state:
  visual_wallpaper_shots: []
  hidden_history_evidence: []
  reinterpretation_image:
  residue_image:
  missing_visual_evidence: []
```

重点回答：

- 删除人物后作品是否仍完全相同？
- 删除旁白和字幕后，主要关系是否仍可理解？
- 人物是否只观看世界，没有行动或状态变化？
- 母题是否真正变义，还是重复作为装饰？
- 最后图像是否完成或改变前文？

## 镜头语言诊断

读取 `controllers/camera-language.md` 与 `evals/camera-language-score.md`。

```yaml
camera_diagnosis:
  shots_without_primary_goal: []
  unmotivated_camera_moves: []
  overloaded_shots: []
  unclear_visual_priority: []
  missing_reveal_order: []
  continuity_breaks: []
  editability_risks: []
  generation_risks: []
  stable_alternatives: []
```

不要因为镜头静止、缓慢或长停留而直接判错。检查的是停留是否产生理解、压迫、观察或余韵。

## 声音诊断

检查：

- 是否只有背景音乐，没有世界声；
- 人物状态是否有呼吸、动作、停顿或声音选择；
- 是否存在声音母题及其变义；
- 是否画面、对白、字幕和音乐重复解释；
- 沉默是否被主动设计；
- 声音是否改变事实、反转或开放程度。

## 制作诊断

```yaml
production_diagnosis:
  missing_visual_bible:
  character_drift_risks: []
  environment_drift_risks: []
  shot_input_output_gaps: []
  s_and_a_shots_without_fallback: []
  high_cost_low_value_shots: []
  single_points_of_failure: []
  recommended_core_sample:
```

镜头很漂亮但无法和前后镜头连接时，属于制作与镜头问题，不自动归因于模型能力。

## 导演包诊断

使用 `evals/director-package-score.md` 定位最薄弱层。不得因为某一层低分就无理由重写已通过的概念、人物和结尾。

## 路由

- 改人物、结构、高潮、结尾、机制、形式规则或传播结构：TRANSFORM。
- 把解释转为人物行动、视觉证据和母题递进：TRANSFORM LEVEL_2或LEVEL_3。
- 只需重新设计镜头目的、揭示顺序和声画关系：TRANSFORM LEVEL_2或ADAPT，取决于是否改变场景功能。
- 只需拆资产、锁角色、改生成方法、补声音、后期和替代：ADAPT。
- 仅是偏好、合法设计或可接受风险：NONE。

## 诊断禁止

- 因概念复杂就默认改成简单俗套；
- 因没有反转就强制添加身份反转；
- 把所有超现实画面、静止镜头和开放结尾判为问题；
- 只说“节奏慢、信息多、电影感不足”，不指出具体证据；
- 把制作困难误判为创作失败；
- 用户要求只诊断时直接输出完整替代剧本。
