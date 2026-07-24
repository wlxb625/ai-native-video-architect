# ADAPT Mode

把已成立作品转译为可执行的AI电影生产系统。ADAPT优先改变实现方式，不改变作品核心。

## 三级变化

- A：表现替换，如正反打、画外对白、文字后期、局部动画或声音补充。
- B：局部场景功能和镜头方案调整，需要语义与人物回归。
- C：改变人物目标、高潮、结尾、开放或形式核心，必须升级TRANSFORM。

## V3前置合同

```yaml
production_protection:
  must_preserve:
  allowed_implementation_changes:
  forbidden_changes:
  allowed_visual_drift:
  forbidden_visual_drift:
  allowed_sound_changes:
  target_delivery:
  budget_level:
```

## 通用流程

1. 建立Production Protection Contract。
2. 创建Visual Bible、Character Lock和Environment Lock。
3. 创建角色、场景、道具、文字、声音、风格和平台资产清单。
4. 将场景拆成有输入状态、单一动作和输出状态的镜头。
5. 为每镜填写景别、机位、运镜、揭示顺序、声画关系和剪辑连接。
6. 判断文生视频、图生视频、局部动画、分层合成、实拍或后期的最佳组合。
7. 按S/A/B/C评价镜头价值与风险。
8. 对S/A和CRITICAL/HIGH风险镜头提供Ideal/Stable/Minimum三档方案。
9. 识别Single Point of Failure并先做Core Sample。
10. 按视觉圣经、角色、标志镜头、高风险镜头、连接镜头的顺序生产。
11. 完成粗剪后运行事实、人物、对白、反转、视觉叙事、镜头、声音、传播和结尾回归。

## 逐镜头生产协议

```yaml
shot_production:
  id:
  priority: S | A | B | C
  narrative_function:
  input_state:
  output_state:
  subject_and_action:
  camera_plan:
  reveal_order:
  sound_relation:
  generation_method:
  reference_assets:
  continuity_anchors:
  forbidden_drift:
  ideal_execution:
  stable_execution:
  minimum_execution:
  single_point_of_failure:
  test_clip:
  edit_connection:
```

## 高概念大片适配

先锁定3—5个HERO_SHOT：

- HOOK_SHOT；
- RULE_SHOT；
- ESCALATION_SHOT；
- CLIMAX_SHOT；
- AFTERIMAGE_SHOT。

制作优先级：

1. 最后残像是否成立；
2. 高潮选择是否可看懂；
3. 第一次规则展示是否清楚；
4. 开场异常是否有停留理由；
5. 规模升级是否必要；
6. 补充环境与世界观镜头。

不得先做大量漂亮空镜，最后才发现人物选择无法拍清。

## 视觉叙事适配

视觉叙事项目必须保留：

- 人物重复动作；
- 关系物件；
- 母题的建立、变义和回收；
- 发现、接近、重解释和余留的顺序；
- 最后画面的停留时间和声音关系。

不得用旁白代替制作困难的视觉证据。可改用局部、反射、影子、空位、画外声和结果镜头。

## 稳定降级原则

1. 减少人群，保留尺度和关系；
2. 从全景改为局部、倒影、阴影、舷窗或监控；
3. 从复杂连续变形改为匹配剪辑和分层合成；
4. 用声音、光线和物件反应替代完整灾难模拟；
5. 保留人物动作与不可逆结果；
6. 最后才缩小世界规模。

不得降级为：

- 系统自动替人物完成选择；
- 旁白解释核心规则；
- 删除标志物导致结尾失去回环；
- 把高潮换成普通爆炸或随机形变；
- 改变谁行动、谁承担代价和结尾开放程度。

## 意识流制作

每次空间跳跃至少保留一个连续锚点：动作、物件、颜色、声音、构图、重力或时间规则；同时只改变一个主要叙事变量。

不得同时随机改变脸、服装、背景、光线、物理规则和现实层级。

## 声音制作

建立：

- 世界声资产；
- 人物微动作与呼吸；
- 声音母题的三次状态；
- 音乐进入和退出；
- 主动沉默；
- Voice Bible和口型替代方案。

声音可以解决空间和剪辑问题，但不能改变事实或替代关键人物行动。

## 生产管理输出

引用：

- `controllers/ai-production.md`
- `controllers/production-management.md`
- `controllers/camera-language.md`
- `controllers/sound-design.md`
- `templates/visual-bible.md`
- `templates/camera-shot-plan.md`
- `templates/production-pack.md`

至少输出：资产清单、生成顺序、S/A镜头、风险矩阵、稳定替代、后期需求和交付版本。

## 制作底线

三档方案可以降低规模，不能改变单一核心机制、人物主任务、艰难选择双方、私人不可逆代价、标志物新含义、最后图像，以及作品完成与开放的边界。
