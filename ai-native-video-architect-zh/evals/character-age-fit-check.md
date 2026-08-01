# Character Age Fit Check V0.4

## 目的

判断主角年龄是否同时服务受众进入、角色可信度、人生阶段和剧情因果。此检查不执行“所有主角年轻化”，也不把中老年主角自动视为传播劣势。

## 核心原则

> 短视频和网文默认优先搜索年轻主角，但故事适配高于市场默认。

当职业资历、长期关系、亲子代际、退休处境、身体变化、时代记忆、权力位置或主题需要更长人生跨度时，中年或老年主角应被保留。反过来，若角色的处境、行动和目标天然属于青年阶段，不得为了“厚重”无必要地加龄。

## 评分（100分，最低80）

- audience_identification_and_market_fit：20
- role_and_life_stage_credibility：20
- story_dependency_of_age：20
- no_forced_rejuvenation_or_aging：20
- age_specific_dramatic_value：20

## 必查反证

1. 换成更年轻的人，职业经验、关系历史、权力位置或主题是否崩坏？
2. 换成更年长的人，行动能力、进入速度、欲望结构或受众代入是否变弱？
3. 当前年龄是否只来自作者习惯、演员想象或“年轻更好看/年长更深刻”的空泛判断？
4. 短视频或网文项目采用中老年主角时，是否提供了清晰、快速、可见的进入点？
5. 青年主角是否被赋予与年龄不相称的资历、权力或长期经历？

## 硬失败

- `FORCED_REJUVENATION`：更年长人生阶段是故事因果核心，却被强行改成青年。
- `UNNECESSARY_AGING`：年龄增加不服务故事，只用于伪造厚重感。
- `AGE_ROLE_CREDIBILITY_BREAK`：年龄与必要资历、关系历史或生活阶段明显矛盾。
- `AGE_SELECTED_WITHOUT_STORY_REASON`：无法说明为何是这个年龄。
- `YOUTH_DEFAULT_IGNORED_WITHOUT_REASON`：短视频/网文无年龄必要性，却习惯性选择中老年主角且无合理解释。

## 输出要求

评估器名固定为`character_age_fit_check`。必须引用当前阶段的`concept_id`、`beat_id`或`scene_id`作为证据。不得因主角年轻直接给高分，也不得因主角年长直接扣分。
