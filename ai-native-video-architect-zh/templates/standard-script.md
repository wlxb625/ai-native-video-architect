# Standard Script Template

```yaml
project_title:
script_version:
primary_path:
platform:
duration:
aspect_ratio:
must_protect: []
confirmed_facts: []
open_facts: []
climax_owner:
ending_lock:

high_concept_lock:
  enabled:
  one_sentence_concept:
  core_mechanism:
  primary_task:
  irreversible_pressure:
  impossible_choice:
  signature_object:
  final_afterimage:
  forbidden_extra_mechanisms: []

hero_shot_plan:
  hook_shot:
  rule_shot:
  escalation_shot:
  climax_shot:
  afterimage_shot:
```

## 场景格式

```text
SCENE 01
内景/外景｜地点｜时间｜现实层级
预计时长：

可观看的动作、空间和道具状态。

人物名
（必要的动作或表演标注）
对白。

SFX / VO / RECORDING / ON-SCREEN TEXT：
声音或精确文字。
```

场景后记录：

```yaml
scene_function:
  current_task:
  task_progress:
  mechanism_state:
  new_information:
  new_cost:
  choice_pressure:
  retention_function:

scene_state:
  confirmed_facts_added: []
  knowledge_changes: []
  relationship_change:
  prop_changes: []
  mechanism_change:
  formal_change:

spectacle_check:
  is_hero_shot:
  hero_shot_role:
  source_rule:
  story_change:
  removable_without_story_change:
  setup_or_payoff:

stream_check:
  is_stream_segment:
  trigger:
  repeated_anchor:
  variation:
  why_this_scene_must_follow:

production_notes:
  must_lip_sync: []
  can_be_offscreen: []
  post_text_assets: []
  high_risk_actions: []
  stable_alternatives: []
```

## 高概念剧本检查

完成剧本后逐场确认：

1. 该场景是否推进同一个人物任务？
2. 该场景是否展示或升级同一个核心机制？
3. 该场景是否增加信息、风险、代价或选择压力？
4. 若是意识流段落，跳跃是否有共同锚点和因果？
5. 若是大片场面，删除后剧情是否改变？
6. 是否新增了概念简报中没有的核心规则？
7. 是否在为最后一幅画面准备物件、动作、声音或台词？

若一个场景以上七项全部为否，默认删除或与相邻场景合并。

## 结尾检查

```yaml
ending_regression:
  task_result:
  choice_result:
  irreversible_loss:
  mechanism_residue:
  signature_object_new_meaning:
  final_image:
  opening_callback:
  completed:
  still_open:
  overexplained:
```

最后一幅画面必须包含人物选择的后果，不得只展示更大的世界、下一只怪物或新组织标志。