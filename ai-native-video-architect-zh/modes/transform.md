# TRANSFORM Mode

修改已有作品，必须先确定改写等级和保护合同。

## 五级改写

- LEVEL_0：校对。
- LEVEL_1：轻优化，默认保护人物、关系、事实、高潮、结尾。
- LEVEL_2：结构优化，可调整场景与顺序，需全面回归。
- LEVEL_3：商业/文学/实验/类型/热梗/高概念方向增强，必须说明收益与代价。
- LEVEL_4：深度改编，可重建人物、世界、类型和结尾，但必须明确授权并标记新版本。

## 通用流程

1. 提取原作核心、独特价值、有意选择和真实问题。
2. 建立must_preserve / allowed_changes / authorized / forbidden。
3. 建立变化预算。
4. 先修事实，再修人物、结构、高潮、结尾、对白、传播和制作。
5. 热梗权限单独记录；需要时输出CURRENT与TIMELESS版本。
6. 用Transform Fidelity Score回归。

## 高概念压缩改写

当原作存在“长片信息量塞进短片”“奇观很多但主线模糊”“身份反转可预测”“意识流像概念图拼贴”时，默认使用LEVEL_2或LEVEL_3，不直接LEVEL_4。

### 第一步：提取唯一核心

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

删除设定不等于否定创意。被移除的好点子应记录到`ideas_to_save_for_other_projects`，防止因为舍不得而重新塞回当前短片。

### 第二步：把世界问题改成人物问题

将抽象问题转为私人代价：

- “集体记忆污染” → 主角必须删除关于某个人的最后记忆；
- “方舟能源不足” → 方舟要求燃烧主角最重要的人生片段；
- “时间线不稳定” → 每次修复都会让主角失去一段共同经历；
- “系统失控” → 系统只能通过一个人物主动确认牺牲对象恢复。

### 第三步：统一奇观

逐场填写：

```yaml
spectacle_transform:
  current_image:
  current_function:
  selected_core_rule:
  new_causal_function:
  keep_merge_or_delete:
```

不能说明`new_causal_function`的奇观默认删除或合并。

### 第四步：升级选择而非增加反转

优先把中段真相用于改变代价与选择，不默认添加“主角其实是AI/死人/复制体/异常源”。

如果保留身份反转，必须说明：

- 任务如何改变；
- 选择双方如何改变；
- 谁承担代价；
- 哪些前文画面获得新含义。

### 第五步：锁定结尾残像

先确定最后一幅画面，再检查开场、中段是否建立对应的物件、动作、颜色、声音或台词。

结尾不得靠额外旁白解释压缩后的主题。

## 高概念改写输出

用户要求优化高概念作品时，默认先展示：

1. 原版一句话复述；
2. 原版最强概念；
3. 互相竞争的设定；
4. 压缩后一句话概念；
5. 保留、合并、删除表；
6. 新核心机制、人物任务和艰难选择；
7. 新HERO_SHOT与最后残像；
8. 完整改写稿。

## 越界

轻优化中新增背叛、身份反转、全面胜利或改结局，均属于未经授权深度改编。

高概念压缩中，以下变化也必须获得授权或升级等级：

- 删除用户明确指定的核心人物；
- 改变人物关系性质；
- 把开放结尾改为明确生死；
- 把文学/实验中心改成纯商业爽点；
- 用完全不同的核心机制替换原作独特机制；
- 改变高潮由谁选择、谁行动和谁承担代价。