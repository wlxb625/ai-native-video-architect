# Full Creation Package Template V4.4

## 1. 项目总览

- 片名：
- 一句话故事：
- 核心机制：
- 类型与情绪：
- 时长与画幅：
- 视觉策略：
- 制作策略：

## 2. 完整剧本或视觉脚本

按场次输出。

## 3. 视觉圣经

人物、场景、道具、色彩、光线、摄影、材质和禁止漂移。

## 4. 导演与表演圣经

- 全片观众关系与镜头距离策略；
- 全片摄影基准、常用景别、焦段感和运镜限制；
- 每个主要场景的灯光母合同、可读性目标和情绪功能；
- 主要人物的表演基线、动作习惯、情绪强度范围和禁止夸张方式；
- 全片情绪曲线和关键表演峰值。

## 5. 规划资产与生图Prompt

逐项使用`asset-prompt-block.md`，注明`PLANNED_REFERENCE`或`ACTUAL_REFERENCE`。

## 6. Shot总表

| Shot | 场景 | 时长 | 剧情作用 | 情绪目标 | 观众位置 | 可见画面 | 主要动作 | 表演强度起→止 | 摄影策略 | 灯光功能 | 帧来源 | 视频模式 |
|---|---|---:|---|---|---|---|---|---|---|---|---|---|

## 7. 逐镜头导演制作卡

每个Shot完整使用`shot-production-card.md`，禁止只输出部分镜头。人物镜头必须包含表演方向和情绪时间轴；空镜必须填写环境节奏与观看关系。

## 8. CF清单

| CF ID | 所属Shot | 类型 | 来源资产 | 表演/环境状态 | 是否预生成 | Prompt/合同 |
|---|---|---|---|---|---|---|

## 9. 参考图使用矩阵

| Shot | 角色参考 | 场景参考 | 道具/状态参考 | 上一镜尾帧 | 新增参考需求 |
|---|---|---|---|---|---|

## 10. 连续性与情绪传递表

| 上一Shot | 结束位置/动作 | 结束表演与强度 | 下一Shot | 开始状态 | 衔接方式 | 必须保持 |
|---|---|---|---|---|---|---|

## 11. 剪辑、声音和后期

镜头顺序、转场、声音桥、环境声、呼吸、对白、音乐、留白、字幕、分层合成和调色。

## 12. 高风险与备用

逐项给风险、首选方法和稳定降级方法。表演风险优先简化微动作和运镜，不先增加无关参考图。

## 13. 外部平台生成顺序

资产图 → 独立首帧 → 首尾帧 → 依赖尾帧镜头 → 分层素材 → 视频 → 剪辑后期。

## 14. 内部完整性检查摘要

```yaml
status: PROMPT_PACKAGE_READY | NEEDS_REPAIR
shot_count:
shot_cards:
shots_with_director_intent:
shots_with_camera_direction:
shots_with_lighting_direction:
character_shots_with_performance_direction:
shots_with_reference_binding:
shots_with_image_source:
shots_with_video_prompt_or_post_plan:
orphan_cf_ids: []
undefined_asset_ids: []
continuity_conflicts: []
emotion_intensity_conflicts: []
directing_coherence_conflicts: []
prompt_conflicts: []
high_risk_shots: []
```
