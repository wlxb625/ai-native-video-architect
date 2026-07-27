# Cross-File Consistency Audit V4.2

## 静态审计结论

- `SKILL.md`与`AGENT.md`均将Skill定义为“剧本创作 + Prompt生产 + 实际生产执行”的统一能力：PASS。
- 用户可从想法、大纲、完整剧本、参考图、镜头表、分镜图、视频Prompt、生成片段或剪辑版本直接进入：PASS。
- 已有剧本或实际媒体时不强制重走前置阶段：PASS。
- 普通短片默认采用最少必要参考，不建立完整影视资产库：PASS。
- 角色默认先判断一张独立身份主参考是否足够，不默认密集六宫格、三视图或固定多张：PASS。
- 全身、手部、三视图和综合角色板仍可按镜头需要、模型能力或实际失败启用：PASS。
- 资产Prompt采用“导演控制层 + 模型执行层”双层结构：PASS。
- 所有影响生成的摄影、灯光和材质必须融合进最终正向Prompt：PASS。
- 用户无需自行拼接统一前缀、摄影合同、灯光合同和主体描述：PASS。
- 每镜选择单首帧、首尾帧、抽尾帧续拍、两段硬切、遮挡切换或分层合成：PASS。
- 下一镜依赖准确尾态时必须预制或抽取稳定尾帧：PASS。
- 每镜要求`END_FRAME_CONTRACT`、`CAMERA_CONTRACT`、`OPTICAL_CONTRACT`和`LIGHTING_CONTRACT`：PASS。
- 视频Prompt使用分秒动作时间轴并量化方向、距离、速度和接触：PASS。
- 新增`controllers/production-execution.md`，负责母参考、样片门槛、失败分层、生产队列、版本台账、镜头验收、剪辑和交付：PASS。
- 新增`templates/production-runbook.md`，可记录真实母参考、样片证据、镜头队列、候选版本和最终质量检查：PASS。
- 新增`evals/shot-output-acceptance-score.md`，明确必须查看真实输出才能判定镜头PASS：PASS。
- 新增`tests/production-execution-stress-tests.md`，覆盖状态真实性、唯一母参考、真实样片、失败阻断、依赖生产、镜头台账和交付门槛：PASS。
- 工作流S08改为唯一母参考选择，S11改为真实代表性样片门槛，S12输出生产运行手册，S13审核实际镜头并组织剪辑交付：PASS。
- 项目状态明确区分`DESIGN_READY`、`PROMPT_READY`、`REFERENCE_READY`、`SAMPLE_VALIDATED`、`BATCH_GENERATION_READY`、`EDIT_READY`和`DELIVERY_READY`：PASS。
- 没有实际媒体时不得声称样片通过、可批量生成、可剪辑或已完成：PASS。
- 样片存在硬失败时阻断批量生产：PASS。
- 失败分层为`REFERENCE_FAILURE`、`CONTROL_FRAME_FAILURE`、`PROMPT_FAILURE`、`MODEL_CAPABILITY_FAILURE`和`POST_PRODUCTION_FAILURE`：PASS。
- 新增资产必须由真实、可复现的失败触发，不能用无限资产解决模型能力问题：PASS。
- 只有通过实际镜头验收的版本可以进入最终时间线：PASS。
- “下一步”表示下一个相关交付物；Prompt包后的下一步通常是母参考筛选或代表性样片，而不是继续无限写Prompt：PASS。

## 本次生产闭环修正覆盖

- `SKILL.md`
- `AGENT.md`
- `controllers/post-script-production.md`
- `controllers/production-execution.md`
- `modes/create.md`
- `modes/adapt.md`
- `config/workflow.yaml`
- `config/scoring.yaml`
- `evals/shot-output-acceptance-score.md`
- `templates/production-runbook.md`
- `tests/production-execution-stress-tests.md`
- `manifest.json`
- `agents/openai.yaml`
- `README.md`
- `scripts/validate_package.py`

## 兼容性说明

- S00至S13继续作为内部定位，不作为强制用户界面。
- 原资料中的三视图和综合角色板模板继续保留，没有被删除或判定为错误。
- 新增生产闭环不等于默认增加资产或要求用户逐项回报。
- 外部成本允许时建议每项核心参考或镜头生成2至4个候选，但该数字不是硬性配额。
- Skill可以提供生产运行手册和真实媒体验收，但不会虚构已经运行无法访问的外部生图、视频、剪辑或声音工具。
- `CREATE`、`TRANSFORM`、`DIAGNOSE`、`ADAPT`以及五种导演模式继续保留。

## 验证重点

安装后运行：

```bash
python scripts/validate_package.py
```

验证必须确认：

- 版本为4.2.0；
- 新生产控制器、运行手册、镜头验收评分器和压力测试均存在并登记在Manifest；
- 生产状态协议完整；
- 真实媒体是`SAMPLE_VALIDATED`、`EDIT_READY`和`DELIVERY_READY`的必要条件；
- 唯一母参考和禁止混用候选规则存在；
- 样片失败阻断批量生产；
- 失败分层和失败触发资产升级存在；
- 镜头队列、版本台账、实际输出验收与后期交付字段存在；
- 原有资产Prompt、逐镜灯光、生成模式和结束帧合同仍然完整。

## 当前验证限制

GitHub文件提交与逐文件静态核对已完成。当前执行环境没有仓库本地检出，因此无法真正运行`python scripts/validate_package.py`。正式安装环境中仍需执行该命令；在实际运行前，不声称验证脚本已经PASS。

平台能力、模型版本、价格、额度和规则仍需在真实任务中实时核实。