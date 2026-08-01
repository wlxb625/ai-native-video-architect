# Meaning & Thematic Necessity Check V0.5

## 目的

判断作品为什么值得被讲述，以及意义是否真正写进人物、冲突、高潮与结尾，而不是成稿后补上的主题口号。

本门禁有两种合法路径：

1. `THEMATIC_MEANING_REQUIRED`：除抽象、无厘头和纯形式实验外的默认路径。
2. `FORMAL_ABSURDIST_EXCEPTION`：仅适用于明确的抽象、无厘头或纯形式实验。

## A. 主题意义路径

作品必须回答：

- 正在讨论哪个真实的人类困境？
- 两种互相冲突、但都能被理解的价值是什么？
- 主角起初相信什么，这一信念如何被事件持续逼迫？
- 高潮行动怎样以行为而不是台词回应核心问题？
- 结尾留下了怎样的余波、代价或未被轻易解决的问题？
- 去掉古风、科幻、悬疑或职业包装后，故事还剩下什么？
- 为什么当下观众值得花时间观看？

不得只给出“勇敢做自己、珍惜眼前人、正义战胜邪恶、亲情可贵”等可套用在任何作品上的结论。

## B. 形式/无厘头例外路径

不强求传统人物信念变化或明确主题，但必须证明：

- 形式目的明确；
- 观众体验明确；
- 重复、断裂、无因果或荒诞具有内部模式；
- 形式在结尾前发生升级、变形、耗尽或反转；
- 随机性并非作者无法组织内容的借口；
- 改成普通叙事后会失去该作品的核心体验。

## 评分（100分，最低80）

统一分项：

- `necessity_or_formal_intent`：20
- `conflict_or_pattern_logic`：20
- `belief_or_audience_experience`：20
- `climax_or_formal_culmination`：20
- `ending_residue_or_aftereffect`：20

## 硬失败

- `THEME_ADDED_AFTER_PLOT`
- `GOOD_PERSON_VS_BAD_PERSON_ONLY`
- `NO_COMPETING_VALUES`
- `PROTAGONIST_BELIEF_UNCHANGED`
- `CLIMAX_DOES_NOT_ANSWER_THEME`
- `GENRE_DEVICE_WITHOUT_HUMAN_MEANING`
- `ENDING_ONLY_PROVES_HERO_WAS_RIGHT`
- `EXPERIMENT_LABEL_USED_AS_ESCAPE`
- `RANDOMNESS_WITHOUT_FORMAL_LOGIC`
- `NO_CREATIVE_NECESSITY`

## 反证要求

主题路径必须检查：

- 去掉类型包装，核心困境仍存在；
- 两个价值都可理解；
- 主角信念确实受到压力；
- 高潮通过行动回答主题；
- 结尾不是口号总结；
- 主题不是成稿后补加。

例外路径必须检查：

- 例外类型已明确声明；
- 形式逻辑贯穿作品；
- 观众体验是有意设计的；
- 不是为了随机而随机；
- 形式在结尾前发生累积或变化。

## 输出要求

评估器名固定为`meaning_and_thematic_necessity_check`。S01引用`concept_id`，S02引用`beat_id`，S03引用`scene_id`。任何只引用主题说明、不引用作品实际事件的评分不得通过。
