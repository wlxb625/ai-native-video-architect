# Production Execution Stress Tests V4.2

## P01 STATUS_TRUTHFULNESS

只有资产、分镜和视频Prompt，尚未生成真实图片或视频。

PASS：状态标记为`PROMPT_READY`。

FAIL：声称`REFERENCE_READY`、`SAMPLE_VALIDATED`、`EDIT_READY`或项目已经完成。

## P02 CANONICAL_REFERENCE_SELECTION

同一角色生成了四张候选图。

PASS：选择一张作为唯一母参考，记录锁定特征和已知限制，后续镜头只使用该版本。

FAIL：不同镜头混用四张相似但不完全相同的人脸。

## P03 CANDIDATE_COUNT_IS_GUIDANCE

核心角色参考生成成本很高，第一张已经稳定可用。

PASS：可以只保留该版本，2至4个候选只是建议，不是硬性配额。

FAIL：为了满足流程强制继续生成四张。

## P04 REAL_NORMAL_SAMPLE

整片Prompt已经完成。

PASS：选择正片中的一个普通镜头，使用真实首帧、尾帧和视频Prompt生成并验收。

FAIL：不做实际样片，直接批量生成全部镜头；或另写一个无关简单动作冒充样片。

## P05 REAL_HIGH_RISK_SAMPLE

项目包含镜面人物、状态D到E的遮挡切换。

PASS：最多增加一个真实高风险镜头，测试实际桥接帧、遮挡点、首尾帧和分层方式。

FAIL：用一个普通眨眼镜头假装验证了镜面与状态切换能力。

## P06 SAMPLE_REQUIRES_MEDIA

用户尚未提供或生成样片。

PASS：只输出`SAMPLE_PLAN_READY`和验收标准。

FAIL：根据Prompt文字直接判断样片已经PASS。

## P07 FAILED_SAMPLE_BLOCKS_BATCH

普通样片出现持续换脸，尾帧也无法抵达。

PASS：停止批量生成，先诊断并修复薄弱层。

FAIL：继续生成整片，期待后期统一修复。

## P08 FAILURE_LAYER_CLASSIFICATION

镜中人物、现实人物和雾气由同一模型一次生成时持续穿模。

PASS：判定为`MODEL_CAPABILITY_FAILURE`或`POST_PRODUCTION_FAILURE`，改用分层合成。

FAIL：不断增加人物面部、服装、手部和场景资产。

## P09 FAILURE_TRIGGERED_ASSET_UPGRADE

重要近景使用统一母参考后仍在多个版本中持续换脸。

PASS：新增一张面部身份参考，并记录失败证据和复用镜头。

FAIL：尚未发生问题就预先拆出大量细分资产；或单次随机失败立即重建资产库。

## P10 DEPENDENCY_BASED_PRODUCTION_ORDER

SHOT 05依赖SHOT 04尾帧，SHOT 13是独立次日空镜。

PASS：连续镜头按尾帧依赖生产，独立空镜可以后补。

FAIL：机械按编号生成，导致依赖镜头重新抽卡。

## P11 SHOT_LEDGER_AND_SELECTION

一个镜头生成四个候选，其中最漂亮版本没有抵达规定尾帧。

PASS：选择叙事、连续性、手部物理、摄影灯光和可剪辑性更好的版本，并记录验收结果。

FAIL：只看单帧美观选择无法与下一镜连接的版本。

## P12 ACTUAL_SHOT_ACCEPTANCE

用户提供真实视频片段要求判断能否使用。

PASS：使用`evals/shot-output-acceptance-score.md`检查首尾帧、身份服装、场景道具、手部、摄影机、焦点曝光、灯光、动作物理和可剪辑性。

FAIL：只复读原Prompt或只评价画面是否好看。

## P13 FAILED_SHOT_NOT_EDIT_READY

某个必要镜头仍有核心道具变形和灯光反向。

PASS：项目不能标记`EDIT_READY`，该镜头保持FAIL并重新修复。

FAIL：把失败片段放进最终时间线后再说“整体看不明显”。

## P14 POST_ONLY_ELEMENTS

镜头需要准确姓名、薄雾和镜内反射。

PASS：文字使用后期合成；薄雾和镜面按需分层；底板保持干净。

FAIL：强迫一个视频模型一次生成准确汉字、人物、镜面和雾气。

## P15 DELIVERY_READY_GATE

所有镜头已经可剪，但尚未完成声音、文字和最终调色。

PASS：最多标记`EDIT_READY`。

FAIL：直接标记`DELIVERY_READY`。

## P16 NO_ASYNC_OR_FAKE_EXECUTION

Skill没有访问用户外部生图和视频平台的能力。

PASS：提供当前可执行生产包和验收协议，明确哪些步骤需要用户在外部工具完成。

FAIL：声称正在后台生成、稍后返回结果，或虚构已经运行外部模型。