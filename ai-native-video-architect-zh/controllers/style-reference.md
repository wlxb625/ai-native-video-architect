# Style & Reference Controller

## 目标

把用户提供的电影、类型、年代、媒介或审美参考拆成可执行的视觉DNA，再组合为原创方案。参考用于分析语言，不用于复制具体作品、角色、镜头或在世创作者的独特风格。

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

## 参考拆解

不要输出“某导演风格”。改写为可观察参数，例如：

- 巨大建筑与极小人物形成文明压迫；
- 慢速稳定镜头与长停留制造宿命感；
- 潮湿旧工业材质制造被使用过的未来；
- 水、植物、镜面和废墟承担记忆与精神变化；
- 日常动作与不可能环境形成温柔奇异感；
- 正常空间中的微小逻辑错误制造心理不安。

## 组合规则

- 一个方案最多选择一个主视觉逻辑、一个辅助时间逻辑和一个声音逻辑；
- 不把多个参考的显眼特征平均混合；
- 必须增加项目自己的视觉母题、材质规则或声画规则；
- 去掉参考名称后，方案仍应完整、可描述、可生成。

## 原创性检查

1. 是否存在项目专属的物件、动作或空间规则？
2. 是否能用一句不依赖作品名称的话描述气质？
3. 是否复制了可识别角色、场景、构图或台词？
4. 是否把参考转化为叙事功能，而非表面滤镜？
5. 是否适合当前AI生产条件？

## 输出格式

```yaml
reference_analysis:
  desired_effect:
  extracted_parameters:
  rejected_surface_traits:
  original_recombination:
  project_signature:
  production_implications:
```

## 禁止

- 直接要求模型复制某部电影的具体镜头；
- 仅靠导演或艺术家姓名充当提示词；
- 把风格当作色彩滤镜；
- 让参考覆盖人物、机制和项目自身主题。
