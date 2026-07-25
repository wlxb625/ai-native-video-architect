from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
VERSION = "3.3.0"

REQUIRED = [
    "SKILL.md", "AGENT.md", "README.md", "manifest.json", "agents/openai.yaml",
    "config/modes.yaml", "config/progress-navigation.yaml", "config/workflow.yaml", "config/scoring.yaml",
    "modes/create.md", "modes/transform.md", "modes/diagnose.md", "modes/adapt.md",
    "core/story.md", "core/continuity.md", "core/dialogue.md", "core/transform.md", "core/production.md",
    "controllers/short-video.md", "controllers/comedy.md", "controllers/suspense.md",
    "controllers/horror.md", "controllers/emotion.md", "controllers/realism.md",
    "controllers/visual.md", "controllers/trend-culture.md", "controllers/high-concept-scifi.md",
    "controllers/visual-narrative.md", "controllers/camera-language.md",
    "controllers/asset-first-production.md", "controllers/detailed-storyboard.md",
    "controllers/ai-production.md", "controllers/style-reference.md", "controllers/virality.md",
    "controllers/production-management.md", "controllers/sound-design.md", "controllers/director-agent.md",
    "evals/semantic-hard-gate.md", "evals/drama-score.md", "evals/propagation-score.md",
    "evals/character-agency-check.md", "evals/twist-legality-check.md", "evals/dialogue-check.md",
    "evals/mechanism-overuse-check.md", "evals/production-score.md", "evals/transform-fidelity-score.md",
    "evals/high-concept-score.md", "evals/visual-narrative-score.md", "evals/camera-language-score.md",
    "evals/asset-readiness-score.md", "evals/director-package-score.md",
    "templates/concept-brief.md", "templates/beat-sheet.md", "templates/standard-script.md",
    "templates/diagnosis-report.md", "templates/transform-contract.md", "templates/production-pack.md",
    "templates/visual-bible.md", "templates/visual-narrative-board.md", "templates/camera-shot-plan.md",
    "templates/detailed-storyboard.md", "templates/director-package.md", "templates/asset-registry.md",
    "templates/character-asset-pack.md", "templates/environment-asset-pack.md",
    "templates/prop-asset-pack.md", "templates/frame-generation-pack.md", "templates/progress-status.md",
    "references/glossary.md", "references/platform-notes.md",
    "references/examples/high-concept-scifi-memory-fuel.md",
    "references/examples/visual-narrative-last-gardener.md",
    "tests/asset-first-stress-tests.md", "tests/progress-navigation-stress-tests.md",
    "tests/stress-test-suite.md", "audit/cross-file-consistency-audit.md",
]

errors = []
for rel in REQUIRED:
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing: {rel}")
    elif not path.read_text(encoding="utf-8").strip():
        errors.append(f"empty: {rel}")

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8") if (ROOT / "SKILL.md").exists() else ""
if not skill.startswith("---\n"):
    errors.append("SKILL.md missing YAML frontmatter")
if "name: ai-native-video-architect-zh" not in skill:
    errors.append("wrong skill name")

for token in [
    "CREATE", "TRANSFORM", "DIAGNOSE", "ADAPT",
    "STORY_DIRECTOR", "VISUAL_DIRECTOR", "BLOCKBUSTER_DIRECTOR",
    "EXPERIMENTAL_DIRECTOR", "PRODUCTION_DIRECTOR",
    "STORY_TREATMENT", "SCRIPT_PACKAGE", "SCRIPT_BREAKDOWN",
    "ASSET_PACK", "DETAILED_STORYBOARD", "PASS", "CONDITIONAL", "FAIL",
]:
    if token not in skill:
        errors.append(f"SKILL.md missing protocol token: {token}")

for token in [
    "项目进度导航", "S00：创作需求", "S03：剧本或视觉脚本", "S04：剧本拆解",
    "STORY_DIRECTION_CONFIRMATION", "SCRIPT_CONFIRMATION", "ASSET_CONFIRMATION",
    "STORYBOARD_CONFIRMATION", "CORE_SAMPLE", "current_stage", "completed_outputs",
    "next_stage", "config/progress-navigation.yaml", "templates/progress-status.md",
    "Asset Readiness Gate", "角色正面、严格侧面和背面生产三视图",
    "场景主布局、无人物空镜和多机位", "道具三视图、尺寸、结构和状态版本",
]:
    if token not in skill:
        errors.append(f"SKILL.md missing V3.3 token: {token}")

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
        expected_outputs = {
            "CREATIVE_BRIEF", "DIRECTION_OPTIONS", "STORY_TREATMENT", "SCRIPT_PACKAGE",
            "SCRIPT_BREAKDOWN", "ASSET_PLAN", "ASSET_PACK", "DETAILED_STORYBOARD", "PRODUCTION_PACK",
        }
        if not expected_outputs.issubset(set(manifest.get("output_levels", []))):
            errors.append("manifest missing V3.3 output levels")
        expected_stages = {f"S{i:02d}" for i in range(14)}
        if expected_stages != set(manifest.get("progress_stages", [])):
            errors.append("manifest progress stages must be S00 through S13")
        expected_gates = {
            "STORY_DIRECTION_CONFIRMATION", "SCRIPT_CONFIRMATION", "ASSET_CONFIRMATION",
            "STORYBOARD_CONFIRMATION", "CORE_SAMPLE_GATE",
        }
        if not expected_gates.issubset(set(manifest.get("confirmation_gates", []))):
            errors.append("manifest missing confirmation gates")
    except json.JSONDecodeError as exc:
        errors.append(f"invalid manifest.json: {exc}")

controller_tokens = {
    "controllers/asset-first-production.md": ["Asset Readiness Gate", "Production Turnaround", "Empty Plate", "尾帧续拍", "硬切连续性"],
    "controllers/ai-production.md": ["Asset Registry", "图片Prompt与视频Prompt分离", "Core Sample"],
    "controllers/detailed-storyboard.md": ["21:9", "ARRI Alexa 35", "24fps", "资产依赖", "首帧与尾帧"],
    "controllers/director-agent.md": ["Progress Navigation Contract", "SCRIPT_CONFIRMATION", "剧本优先与资产先行", "CORE_SAMPLE_GATE"],
    "core/continuity.md": ["production_continuity", "prop_continuity", "硬切连续性"],
}
for rel, tokens in controller_tokens.items():
    text = (ROOT / rel).read_text(encoding="utf-8") if (ROOT / rel).exists() else ""
    for token in tokens:
        if token not in text:
            errors.append(f"{rel} missing token: {token}")

progress_config = (ROOT / "config/progress-navigation.yaml").read_text(encoding="utf-8") if (ROOT / "config/progress-navigation.yaml").exists() else ""
for token in [
    "enabled_by_default", "current_stage", "completed_outputs", "user_decision_if_needed",
    "S00", "S03", "S04", "S08", "S11", "S13", "entry_inference", "DIAGNOSE", "TRANSFORM",
]:
    if token not in progress_config:
        errors.append(f"progress navigation config missing token: {token}")

workflow = (ROOT / "config/workflow.yaml").read_text(encoding="utf-8") if (ROOT / "config/workflow.yaml").exists() else ""
for token in [
    "S00_creative_brief", "S01_direction_options", "S02_story_treatment",
    "S03_script_or_visual_script", "S04_script_breakdown", "S05_visual_bible",
    "S06_asset_plan", "S07_asset_production", "S08_asset_readiness_gate",
    "S09_shot_design", "S10_storyboard_frames_and_prompts", "S11_core_sample",
    "S12_batch_production_and_post", "S13_director_review_and_delivery",
]:
    if token not in workflow:
        errors.append(f"workflow missing stage: {token}")

for rel, tokens in {
    "templates/progress-status.md": ["紧凑版", "修复回退版", "中途进入版", "DIAGNOSE版", "TRANSFORM版", "S13 导演审查与交付"],
    "templates/asset-registry.md": ["ready_for_storyboard_frames", "镜头帧资产", "资产依赖"],
    "templates/character-asset-pack.md": ["生产三视图", "面部身份板", "服装状态"],
    "templates/environment-asset-pack.md": ["无人物空镜", "多机位环境板", "空间主布局"],
    "templates/prop-asset-pack.md": ["道具三视图Prompt", "状态时间线", "道具与人物交互板"],
    "templates/frame-generation-pack.md": ["首帧 FRAME_SH_IN", "尾帧 FRAME_SH_OUT", "尾帧续拍", "硬切镜头"],
}.items():
    text = (ROOT / rel).read_text(encoding="utf-8") if (ROOT / rel).exists() else ""
    for token in tokens:
        if token not in text:
            errors.append(f"{rel} missing token: {token}")

asset_tests = (ROOT / "tests/asset-first-stress-tests.md").read_text(encoding="utf-8") if (ROOT / "tests/asset-first-stress-tests.md").exists() else ""
for token in ["STRUCTURED_INTAKE", "PRODUCTION_TURNAROUND", "FRAME_PAIR_READY", "VERSION_SAFE"]:
    if token not in asset_tests:
        errors.append(f"asset-first stress tests missing token: {token}")

progress_tests = (ROOT / "tests/progress-navigation-stress-tests.md").read_text(encoding="utf-8") if (ROOT / "tests/progress-navigation-stress-tests.md").exists() else ""
for token in [
    "FALSE_COMPLETION", "SCRIPT_GATE_BYPASS", "SCRIPT_FIRST_ASSET_READY",
    "STORY_DIRECTION_CONFIRMATION", "SCRIPT_CONFIRMATION", "ASSET_CONFIRMATION",
    "STORYBOARD_CONFIRMATION", "CORE_SAMPLE_GATE",
]:
    if token not in progress_tests:
        errors.append(f"progress navigation stress tests missing token: {token}")

agent_meta = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8") if (ROOT / "agents/openai.yaml").exists() else ""
for token in ["V3.3", "进度", "剧本", "资产", "首尾帧"]:
    if token not in agent_meta:
        errors.append(f"agent metadata missing token: {token}")

for path in ROOT.rglob("*.md"):
    if "\ufffd" in path.read_text(encoding="utf-8"):
        errors.append(f"encoding replacement character: {path.relative_to(ROOT)}")

result = {
    "skill": "ai-native-video-architect-zh",
    "version": VERSION,
    "markdown_files": len(list(ROOT.rglob("*.md"))),
    "required_files": len(REQUIRED),
    "status": "FAIL" if errors else "PASS",
    "errors": errors,
}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(1 if errors else 0)
