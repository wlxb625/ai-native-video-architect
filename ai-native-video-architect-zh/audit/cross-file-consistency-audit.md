# Cross-File Consistency Audit V4.2

## 静态审计结论

- `SKILL.md`与`AGENT.md`均将Skill定义为“剧本创作 + 剧本后Prompt生产”的统一能力：PASS。
- 用户可从想法、大纲、完整剧本、参考图、镜头表、分镜图或单个Prompt直接进入：PASS。
- 已有剧本时不强制重走创作阶段：PASS。
- 普通短片默认采用最少必要参考，不建立完整影视资产库：PASS。
- 角色默认先判断一张独立身份主参考是否足够，不默认密集六宫格、三视图或固定多张：PASS。
- 全身、手部、三视图和综合角色板仍可按镜头需要、模型能力或用户资料模板启用：PASS。
- 用户提供Prompt资料时，原模板、主体提示和负面约束优先，自行补充必须区分：PASS。
- 资产Prompt采用“导演控制层 + 模型执行层”双层结构：PASS。
- 导演控制层可拆分摄影、光学、灯光、色彩和材质用于自检：PASS。
- 所有影响生成的摄影、灯光和材质必须再次融合进最终正向Prompt：PASS。
- 用户无需自行拼接统一前缀、摄影合同、灯光合同和主体描述：PASS。
- 负面Prompt和比例、分辨率等输出设置允许独立提供：PASS。
- 分镜首尾帧的摄影、焦点、曝光、逐镜灯光和材质同样必须进入最终正向Prompt：PASS。
- 每镜在视频Prompt前选择单首帧、首尾帧、抽尾帧续拍、两段硬切、遮挡切换或分层合成：PASS。
- 单首帧仅用于低幅度运动且下一镜不依赖准确尾态：PASS。
- 下一镜依赖姿势、视线、手部、道具、焦点或构图时，必须预制或抽取稳定尾帧：PASS。
- 每镜均要求`END_FRAME_CONTRACT`：PASS。
- 每镜视频Prompt均要求`CAMERA_CONTRACT`、`OPTICAL_CONTRACT`和`LIGHTING_CONTRACT`：PASS。
- 逐镜灯光包含真实光源、方向、高度、色温、软硬、光比、亮区、阴影和连续性：PASS。
- 视频Prompt使用分秒动作时间轴，并量化方向、距离、速度和接触：PASS。
- 模板、控制器、CREATE、ADAPT、工作流、评分器、压力测试、说明和验证脚本均已同步：PASS。
- “下一步”表示下一个相关交付物，而不是下一张图或下一个资产：PASS。

## 本次修正覆盖

- `SKILL.md`
- `AGENT.md`
- `controllers/post-script-production.md`
- `prompt-engineering/asset-prompt-system.md`
- `templates/asset-prompt-block.md`
- `modes/create.md`
- `modes/adapt.md`
- `config/modes.yaml`
- `config/workflow.yaml`
- `config/scoring.yaml`
- `evals/prompt-production-readiness-score.md`
- `tests/post-script-prompt-pipeline-stress-tests.md`
- `agents/openai.yaml`
- `README.md`
- `scripts/validate_package.py`

## 兼容性说明

- S00至S13继续作为内部定位，不作为强制用户界面。
- 原资料中的三视图和综合角色板模板继续保留，没有被删除或判定为错误。
- 新默认是“先单张身份锚点，再按镜头需要升级”，不是“所有角色必须拆成多张”。
- V4.2增加的是Prompt执行完整度和镜头控制，不等于增加资产数量。
- `CREATE`、`TRANSFORM`、`DIAGNOSE`、`ADAPT`以及五种导演模式继续保留。

## 验证重点

安装后运行：

```bash
python scripts/validate_package.py
```

验证必须确认：

- 版本为4.2.0；
- 资产最终正向Prompt包含摄影、灯光和材质；
- 不要求用户自行拼接；
- 角色参考形式按镜头需要选择；
- 每镜结束帧合同存在；
- 单首帧边界明确；
- 摄影机、光学、逐镜灯光字段存在；
- 视频Prompt不只是动作摘要；
- Manifest包含六种视频生成模式和四项视频合同。

## 当前验证限制

GitHub文件提交与逐文件静态核对已完成。当前执行环境无法解析`github.com`，因此无法克隆默认分支并真正运行`python scripts/validate_package.py`。正式安装环境中仍需执行该命令；在实际运行前，不声称本地验证脚本已经PASS。

平台能力、模型版本、价格、额度和规则仍需在真实任务中实时核实。
