# Style & Reference Controller

## 目标

在剧本已经成立并进入制作阶段后，把用户提供的电影、类型、年代、媒介或审美参考拆成可执行的视觉DNA，再组合为当前项目的原创视觉方案。

参考用于分析语言，不用于复制具体作品、角色、镜头或在世创作者的独特风格。

本控制器不得在故事探索阶段用固定风格限制题材、人物、结构或结尾。完整使用边界见`controllers/project-visual-strategy.md`。

## 项目作用域

所有输出必须标记为当前项目专属：

```yaml
scope: PROJECT_ONLY
narrative_lock_reference:
script_evidence: []
```

新项目必须重新推导，不得自动继承上一项目的色彩、摄影、材质、表演温度和背景规则。

## Style DNA

每个风格方案至少定义：

```yaml
style_dna:
  spatial_logic:
  human_scale:
  time_feeling:
  color_system:
  material_system:
  lighting_logic:
  camera_temperament:
  performance_temperature:
  sound_world:
  graphic_and_text_rules:
  original_signature:
```

每个字段必须说明它如何支持当前剧本中的人物、冲突、高潮或结尾，不能只描述表面效果。

## 参考拆解

不要输出“某导演风格”。改写为可观察参数，例如：

- 巨大建筑与极小人物形成文明压迫；
- 慢速稳定镜头与长停留制造宿命感；
- 潮湿旧工业材质制造被使用过的未来；
- 水、植物、镜面和废墟承担记忆与精神变化；
- 日常动作与不可能环境形成温柔奇异感；
- 正常空间中的微小逻辑错误制造心理不安。

这些只是拆解方法，不是所有项目的默认审美。

## 多方向探索

用户未指定成熟方向时，内部探索2—4个真正不同的方案。差异必须涉及空间、写实程度、光线、色彩、材质、摄影、表演、声音或生产方法，不得只是同一方案换滤镜。

选择时比较：

- 对当前剧本的支持；
- 观众体验；
- 原创性；
- 生成稳定性；
- 时长、画幅与平台适配；
- 资产和连续性成本。

## 组合规则

- 一个方案最多选择一个主视觉逻辑、一个辅助时间逻辑和一个声音逻辑；
- 不把多个参考的显眼特征平均混合；
- 必须增加项目自己的视觉母题、材质规则或声画规则；
- 去掉参考名称后，方案仍应完整、可描述、可生成；
- 不得为追求参考感改写`NARRATIVE_LOCK`。

## 原创性检查

1. 是否存在项目专属的物件、动作或空间规则？
2. 是否能用一句不依赖作品名称的话描述气质？
3. 是否复制了可识别角色、场景、构图或台词？
4. 是否把参考转化为叙事功能，而非表面滤镜？
5. 是否适合当前AI生产条件？
6. 是否与上一项目产生无依据的审美重复？

## 输出格式

```yaml
reference_analysis:
  scope: PROJECT_ONLY
  narrative_lock_reference:
  desired_effect:
  script_evidence: []
  extracted_parameters:
  rejected_surface_traits:
  alternative_directions_considered: []
  original_recombination:
  project_signature:
  production_implications:
```

## 禁止

- 在剧本成立前强制锁定完整项目视觉体系；
- 直接要求模型复制某部电影的具体镜头；
- 仅靠导演或艺术家姓名充当提示词；
- 把风格当作色彩滤镜；
- 让参考覆盖人物、机制和项目自身主题；
- 把某一项目的风格值写成Skill默认；
- 让所有项目自动采用相同的冷暖、节奏、构图或表演温度。
