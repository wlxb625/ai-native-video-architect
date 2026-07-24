# TRANSFORM Mode

修改已有作品，必须先确定改写等级、保护合同和变化预算。

## 五级改写

- LEVEL_0：校对。
- LEVEL_1：轻优化，默认保护人物、关系、事实、高潮、结尾和形式规则。
- LEVEL_2：结构、场景、视觉表达或镜头功能优化，需全面回归。
- LEVEL_3：商业、文学、实验、类型、热梗、高概念或视觉导演方向增强，必须说明收益与代价。
- LEVEL_4：深度改编，可重建人物、世界、类型和结尾，但必须明确授权并标记新版本。

## 保护合同

```yaml
transform_contract:
  level:
  must_preserve:
  allowed_changes:
  explicitly_authorized:
  forbidden_changes:
  change_budget:
  desired_gain:
  acceptable_loss:
  director_mode_target:
```

## 通用流程

1. 提取原作核心、独特价值、有意选择和真实问题。
2. 区分BUG、RISK、CHOICE、OPPORTUNITY和PREFERENCE。
3. 建立保护合同与变化预算。
4. 先修事实，再修人物、结构、视觉叙事、镜头、高潮、结尾、对白、声音、传播和制作。
5. 每次修改说明获得什么、失去什么、哪些内容被保护。
6. 热梗权限单独记录；需要时输出CURRENT与TIMELESS版本。
7. 使用Transform Fidelity Score及相关V3评估器回归。

## 高概念压缩改写

当原作存在“长片信息量塞进短片”“奇观很多但主线模糊”“身份反转可预测”“意识流像概念图拼贴”时，默认使用LEVEL_2或LEVEL_3，不直接LEVEL_4。

### 提取唯一核心

```yaml
compression_contract:
  strongest_unique_idea:
  must_preserve_emotion:
  must_preserve_character_relationship:
  must_preserve_signature_object:
  must_preserve_final_feeling:
  current_primary_task:
  target_primary_task:
  current_core_mechanisms: []
  selected_core_mechanism:
  ideas_to_merge: []
  ideas_to_remove: []
  ideas_to_save_for_other_projects: []
```

删除设定不等于否定创意。移除的好点子进入 `ideas_to_save_for_other_projects`。

### 把世界问题改成人物问题

将抽象问题转为私人代价和可观察行动。例如：

- 集体记忆污染 → 主角必须删除关于某个人的最后记忆；
- 方舟能源不足 → 主角决定燃烧哪段人生；
- 时间线不稳定 → 每次修复都会失去一段共同经历；
- 系统失控 → 必须由人物主动确认谁承担损失。

### 统一奇观

```yaml
spectacle_transform:
  current_image:
  current_function:
  selected_core_rule:
  new_causal_function:
  keep_merge_or_delete:
```

不能说明 `new_causal_function` 的奇观默认删除或合并。

### 升级选择而非增加反转

优先让中段真相改变代价与选择，不默认添加“主角其实是AI、死人、复制体或异常源”。

保留身份反转时，必须说明任务、选择、代价和前文图像如何改变。

## 解释型文本转视觉叙事

当问题是旁白、对白、字幕承担了本应被看见的内容时，使用LEVEL_2视觉化改写。

### 第一步：提取解释信息

```yaml
exposition_item:
  current_text:
  required_fact_or_emotion:
  who_needs_to_understand:
  when_it_must_be_understood:
  visual_evidence_options: []
  sound_evidence_options: []
  text_still_required:
```

### 第二步：转为人物行动

优先使用：

- 重复动作改变；
- 物件的持有、位置、损坏或缺席；
- 空间被使用的痕迹；
- 人物对同一环境的不同反应；
- 声音提前、延后、反差或缺席；
- 结果镜头代替复杂过程。

不要把所有对白删除。保留对白若它承担言语行为、关系压力、误解、拒绝、试探或身份差异。

### 第三步：建立视觉母题递进

每个主要母题检查：

1. 第一次提出问题；
2. 第二次改变理解；
3. 第三次完成情绪回收。

仅更换颜色或重复特写，不算变义。

### 第四步：锁定重解释与余留

先确定哪个后段图像改变前文，再回填开场和中段证据。结尾不得靠新增旁白解释改写后的主题。

## 镜头语言改写

当剧本成立但分镜像画面清单时，使用LEVEL_2：

```yaml
shot_transform:
  current_shot:
  current_primary_function:
  problem:
  target_primary_function:
  input_state:
  output_state:
  reveal_order:
  movement_motivation:
  sound_relation:
  edit_connection:
  stable_alternative:
```

优先修复：

- 没有主功能的镜头；
- 无动机运镜；
- 同镜头事件过载；
- 视觉重心不清；
- 揭示顺序缺失；
- 前后状态无法连接；
- 高难度但价值低的镜头。

不得把所有镜头都改成慢推进、环绕或大全景来制造“电影感”。

## 声音改写

把“全程铺音乐”改为世界声、人物声、声音母题、音乐曲线和沉默。声音改写不得引入新事实或改变开放程度。

## 制作导向改写

若稳定实现需要改变场景表现但不改变场景功能，可以LEVEL_2调整：

- 多人同框 → 画外声、反打、视线和物件反应；
- 连续复杂动作 → 前因、局部和结果；
- 大规模灾难 → 环境反应、声音、倒影和局部证据；
- 精确手部 → 遮挡、插入镜头或结果状态；
- 长口型 → 背影、设备播放、旁听者反应或后期。

改变谁行动、谁选择、谁承担代价时，必须升级LEVEL_3或LEVEL_4并获得授权。

## 输出顺序

高概念或视觉化改写默认先展示：

1. 原版一句话复述；
2. 原版最强概念与必须保护；
3. 真实问题及其分类；
4. 保留、合并、删除和视觉化表；
5. 改写后一句话概念；
6. 人物任务、核心机制、视觉母题和最后图像；
7. 关键场景或镜头变化；
8. 完整改写稿或导演包；
9. 收益、损失和回归结果。

## 越界

以下变化需要授权或升级等级：

- 新增背叛、身份反转、全面胜利或改结局；
- 删除明确指定的核心人物；
- 改变人物关系性质；
- 把开放结尾改为明确生死；
- 把文学或实验中心改成纯商业爽点；
- 用完全不同的机制替换原作独特机制；
- 改变高潮由谁选择、谁行动和谁承担代价；
- 为了降低制作难度，用解释替代原作核心视觉证据。
