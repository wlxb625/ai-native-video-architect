# Concept Brief Template

```yaml
project_title:
mode:
work_depth:
primary_path:
secondary_paths: []
genre_controllers: []
format:
platform:
duration:
aspect_ratio:
audience:

path_responsibilities:
  commercial:
  literary:
  experimental:
  propagation:
  trend_culture:
  priority_when_conflict:

logline:
retell_without_terms:
core_experience:
core_promise:
audience_question:
theme_question:
unique_value:

high_concept:
  enabled:
  familiar_anchor:
  one_sentence_concept:
  core_mechanism:
  mechanism_input:
  mechanism_output:
  mechanism_limit:
  mechanism_cost:
  primary_task:
  task_failure:
  countdown_or_point_of_no_return:
  impossible_choice:
  choice_side_a_value:
  choice_side_b_value:
  irreversible_loss:
  signature_object:
  hook_image:
  rule_image:
  escalation_image:
  climax_image:
  final_afterimage:
  final_image_reframes:
  required_terms: []
  worldbuilding_budget:
  removed_or_merged_ideas: []


character_age_strategy:
  market_context:
  target_audience:
  default_strategy: YOUTH_PRIORITY_WITH_STORY_FIT_OVERRIDE
  protagonist_name:
  approximate_age:
  age_band: CHILD | TEEN | YOUNG_ADULT | MIDDLE_AGED | OLDER_ADULT | AGELESS_OR_NONHUMAN
  role_or_life_stage:
  youth_priority_applies:
  decision: YOUNG_SELECTED | OLDER_SELECTED_FOR_STORY_FIT | AGE_SPECIFIC_SELECTED | AGE_NEUTRAL | AGELESS_OR_NONHUMAN
  why_this_age:
  what_breaks_if_younger:
  what_breaks_if_older:
  required_experience_years:
  plausible_experience_start_age:

primary_subject:
characters: []
primary_agency_type:
first_action:
limited_choice:
intentional_passivity:
relationship_core:
private_emotional_cost:

world_rules: []
opposition:
causality_type:
structure_type:
opening:
first_15_seconds:
first_30_seconds:
middle_change:
midpoint_reframe:
climax_type:
climax_owner:
climax_action:
ending_type:
ending_completed:
ending_open:
common_confirmed_fact:

mechanism:
  role:
  trigger:
  input:
  output:
  cannot_do: []
  cost:
  failure:
  verification:

hero_shots:
  - id:
    role: HOOK_SHOT | RULE_SHOT | ESCALATION_SHOT | CLIMAX_SHOT | AFTERIMAGE_SHOT
    image:
    source_rule:
    immediate_story_change:
    cost_or_reveal:
    stable_version:

stream_of_consciousness:
  enabled:
  mother_rule:
  repeated_anchor:
  allowed_variations: []
  forbidden_randomness: []

dialogue_strategy:
visual_strategy:
sound_strategy:

trend:
  enabled:
  level:
  element:
  lifecycle:
  character_fit:
  story_function:
  expiration_risk:
  timeless_version:

propagation:
  first_contact:
  first_five_seconds:
  first_thirty_seconds:
  middle_retention:
  payoff:
  final_beat:
  retell_sentence:
  cover_frame:
  comment_question:
  comment_share_rewatch:

production:
  method:
  must_protect: []
  forbidden_changes: []
  critical_risks: []
  core_sample:
  hero_shot_priority: []
  ideal_plan: []
  stable_plan: []
  minimum_cost_plan: []

next_mode:
next_template:
```

## 使用规则

- 非高概念项目可将`high_concept.enabled`设为false，并省略不适用字段。
- 高概念项目在`one_sentence_concept`、`core_mechanism`、`primary_task`、`impossible_choice`与`final_afterimage`未成立前，不进入完整剧本。
- `hero_shots`默认3—5项，不能把所有场景都标为核心镜头。
- `removed_or_merged_ideas`必须记录主动舍弃的好点子，防止后续又无意塞回剧本。
- 短视频和网文默认先考虑年轻主角，但必须比较年龄反事实；中老年更适合职业资历、关系历史、人生阶段或主题时，禁止强行年轻化。
