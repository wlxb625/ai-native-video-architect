# Sound Design Controller

## 目标

让声音参与世界、人物、规则、节奏和结尾，而不是在画面完成后随意铺一层音乐。

## 三层声音

### World Sound

定义世界在没有对白和音乐时如何被听见：空间大小、材料、机器、天气、远近层次和异常规则。

### Character Sound

通过呼吸、脚步、衣物、触碰、停顿、吞咽和动作节奏表现人物状态。人物声音不是必须放大，而是必须有选择。

### Theme Sound

选择一个可重复、可变奏的声音母题，并至少经历：

1. 建立；
2. 变义；
3. 回收或缺席。

## 声音母题协议

```yaml
sound_motif:
  source:
  first_meaning:
  second_meaning:
  final_meaning_or_absence:
  relation_to_character:
  relation_to_core_mechanism:
```

母题可以是折纸、门锁、广播、呼吸、金属收缩、水滴、轮轨或电流，但必须与人物或规则建立关系。

## 声画关系

- 同步：声音确认动作；
- 提前：声音先于画面提出问题；
- 延后：声音跨剪辑保留上一场意义；
- 反差：画面与声音制造复杂情绪；
- 欺骗：声音先被误认，后揭示真实来源；
- 缺席：本应出现的声音消失，形成变化；
- 沉默：主动削减声音，让选择或失去显现。

禁止画面、对白、字幕、音乐四次重复同一情绪和事实。

## 空间层级

```yaml
sound_space:
  near:
  middle:
  far:
  offscreen:
  moving_source:
```

闭眼时应能通过声音判断空间尺度、材料和危险方向。

## 音乐曲线

不要只写“史诗、悲伤、温暖”。定义：

- 音乐何时进入；
- 何时退出；
- 每段承担的情绪变化；
- 乐器或音色；
- 节奏密度；
- 高潮前是否压低；
- 结尾是否保留环境声或母题。

音乐不能替代人物变化。

## Voice Bible

需要对白或配音时记录：

```yaml
voice_bible:
  age_feeling:
  vocal_texture:
  pace:
  breath:
  sentence_length:
  emotional_control:
  forbidden_delivery:
```

对白表演必须服从人物当下行为，不使用统一“电影腔”。

## 镜头联动

- 慢推进：逐渐增加局部声音或压低背景；
- 拉远：扩大环境层级，人物声变小；
- 特写：减少无关层，突出触碰、呼吸或物件；
- 揭示：可用声音提前、同步或故意延后；
- 失去：优先考虑突然削减，而非持续加大音乐。

## 输出要求

```yaml
sound_plan:
  world_sound:
  character_sound:
  motif:
  silence_moments:
  music_curve:
  voice_bible:
  shot_sync_notes:
  trailer_sound_hook:
  production_assets:
```
