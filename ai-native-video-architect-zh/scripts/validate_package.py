from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
VERSION = "4.4.0"

REQUIRED = [
    "VERSION", "CONTRACT_VERSION", "EXECUTION.yaml", "SKILL.md", "AGENT.md", "README.md", "manifest.json", "agents/openai.yaml",
    "constitution/immutable.yaml", "constitution/integrity.json", "contracts/execution-protocol.md", "contracts/workflow.enforced.yaml",
    "adaptive/default-policy.yaml", "adaptive/policy.schema.json",
    "schemas/s00-brief.schema.json", "schemas/s01-concepts.schema.json", "schemas/s02-treatment.schema.json", "schemas/s03-script.schema.json",
    "schemas/generic-stage.schema.json", "schemas/evaluation.schema.json", "schemas/policy-patch.schema.json",
    "scripts/contract_runner.py", "scripts/apply_policy_patch.py", "scripts/verify_contract.py",
    "config/modes.yaml", "config/progress-navigation.yaml", "config/workflow.yaml", "config/scoring.yaml",
    "modes/create.md", "modes/transform.md", "modes/diagnose.md", "modes/adapt.md",
    "controllers/agent-full-creation.md", "controllers/post-script-production.md", "controllers/production-execution.md",
    "controllers/camera-director.md", "controllers/lighting-director.md", "controllers/performance-director.md",
    "prompt-engineering/asset-prompt-system.md", "prompt-engineering/shot-cf-binding-system.md",
    "prompt-engineering/image-prompt-compiler.md", "prompt-engineering/storyboard-frame-system.md",
    "prompt-engineering/video-prompt-compiler.md", "prompt-engineering/performance-prompt-compiler.md", "prompt-engineering/continuity-repair-system.md",
    "references/agent-full-creation-principles.md", "references/emotion-library.md",
    "templates/asset-prompt-block.md", "templates/shot-production-card.md",
    "templates/storyboard-frame-prompt-block.md", "templates/video-shot-prompt-block.md",
    "templates/full-creation-package.md", "templates/performance-direction-block.md",
    "evals/prompt-production-readiness-score.md", "evals/full-package-integrity-check.md",
    "evals/shot-output-acceptance-score.md", "evals/performance-direction-score.md", "evals/directing-coherence-check.md", "evals/climax-force-check.md", "evals/character-age-fit-check.md",
    "tests/agent-full-creation-stress-tests.md", "tests/post-script-prompt-pipeline-stress-tests.md", "tests/directing-performance-stress-tests.md",
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
    "强执行契约入口",
    "CONTRACT_COMPLETE",
    "SOFT_CONTRACT",
    "AI Native Film Studio V4.4",
    "FULL_CREATION_PACKAGE",
    "PLANNED_REFERENCE",
    "ACTUAL_REFERENCE",
    "固定表示 **Control Frame",
    "Shot与CF的唯一关系",
    "导演、摄影、灯光与表演控制",
    "FULL_PERFORMANCE_PROMPT",
    "Reference Binding合同",
    "Frame Source合同",
    "禁止空Prompt",
    "镜头覆盖率不变量",
    "内部检查与返修",
    "PROMPT_PACKAGE_READY",
    "参考图尚未生成就停止全套内容创作",
])

require_tokens("AGENT.md", [
    "AI Native Film Studio V4.4",
    "Contract Skill强执行义务",
    "CONTRACT_COMPLETE",
    "FULL_CREATION_PACKAGE",
    "PLANNED_REFERENCE",
    "Shot合同",
    "CF合同",
    "参考绑定合同",
    "Prompt覆盖合同",
    "人物表演方向",
    "情绪曲线",
    "PROMPT_PACKAGE_READY",
])

for rel in ["config/modes.yaml", "config/workflow.yaml", "config/scoring.yaml", "config/progress-navigation.yaml"]:
    require_tokens(rel, [f"version: {VERSION}"])

require_tokens("config/workflow.yaml", [
    "no_external_asset_gate_for_prompt_package: true",
    "S06_planned_reference_registry",
    "S08_complete_shot_list",
    "camera_lighting_performance_coherence",
    "performance_direction_score",
    "emotion_intensity_continuity",
    "S09_shot_cf_binding",
    "S10_frame_prompt_pack",
    "S11_video_prompt_pack",
    "S12_internal_validation_and_repair",
    "S13_full_creation_delivery",
    "PREVIOUS_TAIL_INHERITANCE",
    "PROMPT_PACKAGE_READY",
    "coverage_invariants",
])

require_tokens("controllers/agent-full-creation.md", [
    "设计态与实物态",
    "Shot编译",
    "CF编译",
    "参考解析",
    "FINAL_PACKAGE_INTEGRITY_CHECK",
])

require_tokens("prompt-engineering/shot-cf-binding-system.md", [
    "Shot–CF–Prompt Binding System",
    "CF不能脱离Shot独立存在",
    "PREVIOUS_TAIL_INHERITANCE",
    "空值处理",
    "coverage_report",
])

require_tokens("templates/shot-production-card.md", [
    "【可见画面描述】",
    "【导演意图】",
    "【逐镜灯光方向】",
    "【人物表演方向】",
    "【情绪与表演时间轴】",
    "【参考绑定】",
    "【帧来源模式】",
    "【Control Frames】",
    "【图片Prompt交付】",
    "【完整视频正向Prompt｜直接复制】",
])

require_tokens("templates/full-creation-package.md", [
    "规划资产与生图Prompt",
    "Shot总表",
    "逐镜头导演制作卡",
    "CF清单",
    "参考图使用矩阵",
    "内部完整性检查摘要",
    "导演与表演圣经",
    "连续性与情绪传递表",
])
require_tokens("templates/performance-direction-block.md", ["【内外情绪】", "【情绪节拍】", "【结束表演状态】"])

require_tokens("evals/full-package-integrity-check.md", [
    "硬性计数",
    "ID完整性",
    "内容完整性",
    "Prompt一致性",
    "导演一致性",
    "情绪强度",
    "PROMPT_PACKAGE_READY",
])

require_tokens("tests/agent-full-creation-stress-tests.md", [
    "FULL_PACKAGE_NO_ASSET_GATE",
    "SHOT_WITHOUT_PROMPT",
    "CF_ORPHAN",
    "INHERITED_FRAME_NOT_BLANK",
    "POST_ONLY_COVERAGE",
    "PAIRWISE_CONTINUITY",
    "FULL_PACKAGE_STATUS",
])


require_tokens("controllers/camera-director.md", ["director_intent", "观众位置", "运镜的情绪语法", "硬失败"])
require_tokens("controllers/lighting-director.md", ["lighting_direction", "可读性", "情绪功能", "灯光与表演协同"])
require_tokens("controllers/performance-director.md", ["performance_direction", "内外矛盾", "情绪节拍", "强度标尺", "哭戏控制"])
require_tokens("references/emotion-library.md", ["压住恐惧", "隐忍悲伤", "单颗泪水", "隐忍愤怒", "释然"])
require_tokens("prompt-engineering/performance-prompt-compiler.md", ["Performance Prompt Compiler V4.4", "FULL_PERFORMANCE_PROMPT", "长提示词模式", "哭戏编译"])
require_tokens("evals/performance-direction-score.md", ["Performance Direction Score V4.4", "情绪只有标签", "摄影可读性", "灯光可读性"])
require_tokens("evals/directing-coherence-check.md", ["Camera–Lighting–Performance Coherence Check V4.4", "导演意图", "表演终点与End CF不同"])
require_tokens("tests/directing-performance-stress-tests.md", ["DIR-01", "DIR-06", "DIR-10"])


require_tokens("EXECUTION.yaml", ["kind: contract-skill", "execution_mode: enforced_when_scripts_available", "fail_closed_soft_contract", "final_artifact_release_only_after_receipt"])
require_tokens("constitution/immutable.yaml", ["IMMUTABLE_CONSTITUTION", "HIGHER_LAYER_WINS", "missing_evidence: FAIL", "生成者不得用自我声明替代独立评估产物", "STORY_FIT_OVERRIDES_MARKET_DEFAULT"])
require_tokens("contracts/workflow.enforced.yaml", ["G01_CONCEPT", "G02_TREATMENT", "G03_SCRIPT", "G12_FULL_PACKAGE", "history_fingerprint", "climax_force_check", "character_age_fit_check"])
require_tokens("contracts/execution-protocol.md", ["ACTIVATION_RECEIPT", "prepare → submit → evaluate → finalize", "CONTRACT_COMPLETE"])

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
        for key, expected in {
            "reference_statuses": {"PLANNED_REFERENCE", "ACTUAL_REFERENCE"},
            "design_status_protocol": {"PROMPT_PACKAGE_READY"},
            "frame_source_modes": {"NEW_START_FRAME", "PREVIOUS_TAIL_INHERITANCE", "FIRST_LAST_FRAME", "EXISTING_USER_FRAME", "TEXT_TO_VIDEO", "POST_ONLY"},
            "control_frame_types": {"START", "END", "BRIDGE", "TEXT_CONTRACT_ONLY"},
            "performance_modes": {"CHARACTER_PERFORMANCE", "NON_CHARACTER_PERFORMANCE", "FULL_PERFORMANCE_PROMPT"},
        }.items():
            if not expected.issubset(set(manifest.get(key, []))):
                errors.append(f"manifest missing {key}")
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

require_tokens("evals/climax-force-check.md", ["STRONG_DRAMATIC_PEAK", "CLIMAX_IS_ONLY_CLOSING_RITUAL", "counterfactual_challenges"])

require_tokens("evals/character-age-fit-check.md", ["YOUTH_PRIORITY_WITH_STORY_FIT_OVERRIDE", "FORCED_REJUVENATION", "AGE_ROLE_CREDIBILITY_BREAK"])
