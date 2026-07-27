from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
VERSION = "4.2.0"

REQUIRED = [
    "SKILL.md", "AGENT.md", "README.md", "manifest.json", "agents/openai.yaml",
    "config/modes.yaml", "config/progress-navigation.yaml", "config/workflow.yaml", "config/scoring.yaml",
    "modes/create.md", "modes/transform.md", "modes/diagnose.md", "modes/adapt.md",
    "controllers/post-script-production.md", "controllers/production-execution.md",
    "prompt-engineering/image-prompt-compiler.md",
    "prompt-engineering/visual-style-color-light.md",
    "prompt-engineering/asset-prompt-system.md",
    "prompt-engineering/storyboard-frame-system.md",
    "prompt-engineering/video-prompt-compiler.md",
    "prompt-engineering/camera-movement-library.md",
    "prompt-engineering/continuity-repair-system.md",
    "templates/asset-prompt-block.md",
    "templates/storyboard-frame-prompt-block.md",
    "templates/video-shot-prompt-block.md",
    "templates/production-runbook.md",
    "evals/prompt-production-readiness-score.md",
    "evals/shot-output-acceptance-score.md",
    "tests/post-script-prompt-pipeline-stress-tests.md",
    "tests/production-execution-stress-tests.md",
]

errors: list[str] = []

for rel in REQUIRED:
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing: {rel}")
    elif not path.read_text(encoding="utf-8").strip():
        errors.append(f"empty: {rel}")


def require_tokens(rel: str, tokens: list[str]) -> None:
    path = ROOT / rel
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    for token in tokens:
        if token not in text:
            errors.append(f"{rel} missing token: {token}")


skill = ROOT / "SKILL.md"
if skill.exists() and not skill.read_text(encoding="utf-8").startswith("---\n"):
    errors.append("SKILL.md missing YAML frontmatter")

require_tokens("SKILL.md", [
    "name: ai-native-video-architect-zh",
    "AI Native Film Studio V4.2",
    "剧本确认后，同一个Skill应继续完成下游工作",
    "独立身份主参考图",
    "资产Prompt双层合同",
    "单首帧图生视频",
    "首尾帧视频",
    "抽尾帧续拍",
    "逐镜灯光合同",
    "END_FRAME_CONTRACT",
    "母参考与生产状态合同",
    "SAMPLE_VALIDATED",
    "代表性样片与批量生成门槛",
    "生产队列、候选版本与镜头验收",
    "没有实际生成结果却声称样片已经通过",
    "下一步",
])

require_tokens("AGENT.md", [
    "AI Native Film Studio V4.2",
    "用户当前已经有什么成熟成果",
    "资产Prompt双层合同",
    "独立身份主参考图",
    "导演级视频Prompt合同",
    "逐镜灯光合同",
    "生产状态合同",
    "唯一母参考合同",
    "代表性样片门槛",
    "生产队列与版本台账",
    "没有实际生成结果时",
])

for rel in ["config/modes.yaml", "config/workflow.yaml", "config/scoring.yaml", "config/progress-navigation.yaml"]:
    require_tokens(rel, [f"version: {VERSION}"])

require_tokens("config/workflow.yaml", [
    "MINIMUM_VIABLE_REFERENCES",
    "SINGLE_IDENTITY_ANCHOR",
    "EXECUTABLE_INTEGRATED_POSITIVE_PROMPT",
    "DIRECTOR_GRADE_VIDEO_PROMPT",
    "production_execution_controller",
    "production_status_protocol",
    "S08_canonical_reference_selection",
    "S11_representative_test",
    "real_media_required_for_pass",
    "SAMPLE_PLAN_READY",
    "shot_generation_queue",
    "shot_ledger",
    "S13_actual_output_review_and_delivery",
    "MODEL_CAPABILITY_FAILURE",
    "DELIVERY_READY",
    "SINGLE_START_FRAME",
    "FIRST_LAST_FRAME",
    "OCCLUSION_SWITCH",
])

require_tokens("controllers/production-execution.md", [
    "Prompt完成不等于参考图完成",
    "生产状态协议",
    "唯一母参考选择",
    "SAMPLE_PLAN_READY",
    "失败分层诊断",
    "MODEL_CAPABILITY_FAILURE",
    "失败触发资产升级",
    "依赖顺序",
    "镜头生成队列",
    "shot_run",
    "候选版本和选择",
    "镜头验收",
    "剪辑与后期",
    "DELIVERY_READY",
])

require_tokens("templates/production-runbook.md", [
    "current_status",
    "canonical_references",
    "representative_tests",
    "sample_gate",
    "failure_diagnosis",
    "production_dependency_graph",
    "shot_queue",
    "shot_ledger",
    "asset_upgrade_log",
    "editing_plan",
    "final_quality_control",
])

require_tokens("evals/shot-output-acceptance-score.md", [
    "必须查看真实输出",
    "PLAN_ONLY",
    "首帧与尾帧忠实度",
    "人物身份与服装连续性",
    "场景、道具与手部交互",
    "摄影机执行",
    "焦点、景深与曝光",
    "灯光与色彩连续性",
    "动作时间轴与物理",
    "可剪辑性与连接",
    "没有真实生成结果却声称`PASS`",
])

require_tokens("prompt-engineering/asset-prompt-system.md", [
    "先做最少参考",
    "导演控制层",
    "模型执行层",
    "完整正向Prompt",
    "一张独立身份主参考图",
    "标准人物三视图",
    "综合角色板",
    "场景空镜",
    "道具三视图",
    "LEAN（默认）",
    "CONTROLLED（失败后升级）",
    "要求用户自行把多个字段拼成可用Prompt",
])

require_tokens("templates/asset-prompt-block.md", [
    "默认使用轻量资产块",
    "【内部导演检查】",
    "【完整正向Prompt｜直接复制】",
    "不能只写人物或场景描述",
    "默认先生成一张独立的角色身份主参考",
])

require_tokens("prompt-engineering/video-prompt-compiler.md", [
    "导演级Prompt",
    "先决定生成模式",
    "结束帧合同",
    "时间轴动作编译",
    "摄影机合同",
    "焦点、景深和曝光合同",
    "逐镜灯光合同",
    "不得为了“方便复制”压缩成几句通用话",
])

require_tokens("templates/video-shot-prompt-block.md", [
    "【生成模式与选择理由】",
    "【画面空间与构图】",
    "【时长与时间轴】",
    "【摄影机合同】",
    "【焦点、景深与曝光】",
    "【逐镜灯光合同】",
    "【结束帧合同】",
    "【下一镜继承】",
])

require_tokens("templates/storyboard-frame-prompt-block.md", [
    "【前景、中景、背景】",
    "【焦点、景深与曝光】",
    "【逐镜灯光设计】",
    "【结束帧合同】",
    "【尾帧是否预生成】",
])

require_tokens("evals/prompt-production-readiness-score.md", [
    "参考形式与职责",
    "图片Prompt执行完整度",
    "最终正向Prompt",
    "生成模式与尾帧控制",
    "摄影机与光学合同",
    "逐镜灯光合同",
    "结束帧合同",
])

require_tokens("tests/post-script-prompt-pipeline-stress-tests.md", [
    "SINGLE_START_FRAME_BOUNDARY",
    "END_FRAME_CONTRACT",
    "PER_SHOT_LIGHTING",
    "PROMPT_DETAIL_DENSITY",
    "EXECUTABLE_POSITIVE_PROMPT",
    "CHARACTER_REFERENCE_FORM",
    "STORYBOARD_INTEGRATED_PROMPT",
])

require_tokens("tests/production-execution-stress-tests.md", [
    "STATUS_TRUTHFULNESS",
    "CANONICAL_REFERENCE_SELECTION",
    "REAL_NORMAL_SAMPLE",
    "REAL_HIGH_RISK_SAMPLE",
    "SAMPLE_REQUIRES_MEDIA",
    "FAILED_SAMPLE_BLOCKS_BATCH",
    "FAILURE_LAYER_CLASSIFICATION",
    "FAILURE_TRIGGERED_ASSET_UPGRADE",
    "DEPENDENCY_BASED_PRODUCTION_ORDER",
    "SHOT_LEDGER_AND_SELECTION",
    "ACTUAL_SHOT_ACCEPTANCE",
    "DELIVERY_READY_GATE",
])

manifest_path = ROOT / "manifest.json"
if manifest_path.exists():
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("version") != VERSION:
            errors.append(f"manifest version must be {VERSION}")

        listed = set(manifest.get("files", []))
        for rel in REQUIRED:
            if rel not in listed and rel != "manifest.json":
                errors.append(f"manifest missing file: {rel}")

        expected_modes = {
            "SINGLE_START_FRAME", "FIRST_LAST_FRAME", "TAIL_FRAME_CONTINUATION",
            "TWO_SEGMENT_HARD_CUT", "OCCLUSION_SWITCH", "LAYERED_COMPOSITE",
        }
        if not expected_modes.issubset(set(manifest.get("video_generation_modes", []))):
            errors.append("manifest missing video generation modes")

        expected_contracts = {"CAMERA_CONTRACT", "OPTICAL_CONTRACT", "LIGHTING_CONTRACT", "END_FRAME_CONTRACT"}
        if not expected_contracts.issubset(set(manifest.get("video_contracts", []))):
            errors.append("manifest missing video contracts")

        expected_statuses = {"DESIGN_READY", "PROMPT_READY", "REFERENCE_READY", "SAMPLE_VALIDATED", "BATCH_GENERATION_READY", "EDIT_READY", "DELIVERY_READY"}
        if not expected_statuses.issubset(set(manifest.get("production_status_protocol", []))):
            errors.append("manifest missing production status protocol")

        expected_failures = {"REFERENCE_FAILURE", "CONTROL_FRAME_FAILURE", "PROMPT_FAILURE", "MODEL_CAPABILITY_FAILURE", "POST_PRODUCTION_FAILURE"}
        if not expected_failures.issubset(set(manifest.get("failure_layers", []))):
            errors.append("manifest missing production failure layers")

        expected_stages = {f"S{i:02d}" for i in range(14)}
        if expected_stages != set(manifest.get("progress_stages", [])):
            errors.append("manifest progress stages must remain S00 through S13")
    except json.JSONDecodeError as exc:
        errors.append(f"invalid manifest.json: {exc}")

for path in ROOT.rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    if "\ufffd" in text:
        errors.append(f"encoding replacement character: {path.relative_to(ROOT)}")

result = {
    "skill": "ai-native-video-architect-zh",
    "version": VERSION,
    "required_files": len(REQUIRED),
    "status": "FAIL" if errors else "PASS",
    "errors": errors,
}

print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(1 if errors else 0)