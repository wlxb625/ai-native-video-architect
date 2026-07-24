from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
VERSION = "3.1.0"

REQUIRED = [
    "SKILL.md", "AGENT.md", "README.md", "manifest.json", "agents/openai.yaml",
    "config/modes.yaml", "config/workflow.yaml", "config/scoring.yaml",
    "modes/create.md", "modes/transform.md", "modes/diagnose.md", "modes/adapt.md",
    "core/story.md", "core/continuity.md", "core/dialogue.md", "core/transform.md", "core/production.md",
    "controllers/short-video.md", "controllers/comedy.md", "controllers/suspense.md",
    "controllers/horror.md", "controllers/emotion.md", "controllers/realism.md",
    "controllers/visual.md", "controllers/trend-culture.md", "controllers/high-concept-scifi.md",
    "controllers/visual-narrative.md", "controllers/camera-language.md",
    "controllers/detailed-storyboard.md", "controllers/ai-production.md",
    "controllers/style-reference.md", "controllers/virality.md",
    "controllers/production-management.md", "controllers/sound-design.md",
    "controllers/director-agent.md",
    "evals/semantic-hard-gate.md", "evals/drama-score.md", "evals/propagation-score.md",
    "evals/character-agency-check.md", "evals/twist-legality-check.md", "evals/dialogue-check.md",
    "evals/mechanism-overuse-check.md", "evals/production-score.md",
    "evals/transform-fidelity-score.md", "evals/high-concept-score.md",
    "evals/visual-narrative-score.md", "evals/camera-language-score.md",
    "evals/director-package-score.md",
    "templates/concept-brief.md", "templates/beat-sheet.md", "templates/standard-script.md",
    "templates/diagnosis-report.md", "templates/transform-contract.md", "templates/production-pack.md",
    "templates/visual-bible.md", "templates/visual-narrative-board.md",
    "templates/camera-shot-plan.md", "templates/detailed-storyboard.md",
    "templates/director-package.md",
    "references/glossary.md", "references/platform-notes.md",
    "references/examples/high-concept-scifi-memory-fuel.md",
    "references/examples/visual-narrative-last-gardener.md",
    "tests/stress-test-suite.md", "audit/cross-file-consistency-audit.md",
]

errors = []

for rel in REQUIRED:
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing: {rel}")
    elif not path.read_text(encoding="utf-8").strip():
        errors.append(f"empty: {rel}")

skill_path = ROOT / "SKILL.md"
skill = skill_path.read_text(encoding="utf-8") if skill_path.exists() else ""
if not skill.startswith("---\n"):
    errors.append("SKILL.md missing YAML frontmatter")
if "name: ai-native-video-architect-zh" not in skill:
    errors.append("wrong skill name")

for token in [
    "CREATE", "TRANSFORM", "DIAGNOSE", "ADAPT",
    "STORY_DIRECTOR", "VISUAL_DIRECTOR", "BLOCKBUSTER_DIRECTOR",
    "EXPERIMENTAL_DIRECTOR", "PRODUCTION_DIRECTOR",
    "PASS", "CONDITIONAL", "FAIL",
]:
    if token not in skill:
        errors.append(f"SKILL.md missing protocol token: {token}")

for token in [
    "一句话概念", "单一核心机制", "单一人物任务", "艰难选择", "最后图像",
    "controllers/high-concept-scifi.md", "evals/high-concept-score.md",
    "controllers/visual-narrative.md", "controllers/camera-language.md",
    "controllers/ai-production.md", "controllers/sound-design.md",
    "controllers/director-agent.md", "evals/director-package-score.md",
]:
    if token not in skill:
        errors.append(f"SKILL.md missing V3 token: {token}")

manifest_path = ROOT / "manifest.json"
if manifest_path.exists():
    try:
        manifest_data = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest_data.get("version") != VERSION:
            errors.append(f"manifest version must be {VERSION}")
        listed = set(manifest_data.get("files", []))
        for rel in REQUIRED:
            if rel not in listed and rel != "manifest.json":
                errors.append(f"manifest missing file: {rel}")
        expected_director_modes = {
            "STORY_DIRECTOR", "VISUAL_DIRECTOR", "BLOCKBUSTER_DIRECTOR",
            "EXPERIMENTAL_DIRECTOR", "PRODUCTION_DIRECTOR",
        }
        if not expected_director_modes.issubset(set(manifest_data.get("director_modes", []))):
            errors.append("manifest missing director modes")
        if "DETAILED_STORYBOARD" not in set(manifest_data.get("output_levels", [])):
            errors.append("manifest missing detailed storyboard output level")
        if "DETAILED_STORYBOARD" not in set(manifest_data.get("specialized_controllers", [])):
            errors.append("manifest missing detailed storyboard controller")
    except json.JSONDecodeError as exc:
        errors.append(f"invalid manifest.json: {exc}")

controller_tokens = {
    "controllers/high-concept-scifi.md": ["one_sentence_concept", "core_rule", "impossible_choice", "final_image"],
    "controllers/visual-narrative.md": ["VISUAL_WALLPAPER", "人物—世界关系", "视觉母题"],
    "controllers/camera-language.md": ["reveal_order", "movement_motivation", "stable_alternative", "详细分镜模式"],
    "controllers/detailed-storyboard.md": ["21:9", "ARRI Alexa 35", "24fps", "180度", "真实演员质感", "单镜头最低描述密度"],
    "controllers/ai-production.md": ["Visual Bible", "Character Lock", "Environment Lock", "Cinematic Master Spec"],
    "controllers/director-agent.md": ["STORY_DIRECTOR", "VISUAL_DIRECTOR", "Director Critique"],
}

for rel, tokens in controller_tokens.items():
    path = ROOT / rel
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    for token in tokens:
        if token not in text:
            errors.append(f"{rel} missing token: {token}")

score_tokens = {
    "evals/high-concept-score.md": ["Concept Compression", "Mechanism Unity", "Spectacle Causality", "Final Afterimage"],
    "evals/visual-narrative-score.md": ["人物—世界关系", "重解释能力", "情绪余留"],
    "evals/camera-language-score.md": ["镜头目的", "揭示顺序", "可剪辑与可生成"],
    "evals/director-package-score.md": ["概念统一性", "AI生产可行性", "weakest_layer"],
}

for rel, tokens in score_tokens.items():
    path = ROOT / rel
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    for token in tokens:
        if token not in text:
            errors.append(f"{rel} missing dimension: {token}")

storyboard_template_path = ROOT / "templates/detailed-storyboard.md"
storyboard_template = storyboard_template_path.read_text(encoding="utf-8") if storyboard_template_path.exists() else ""
for token in [
    "统一画幅：21:9", "摄影机参考", "默认快门角度：180°",
    "21:9构图", "人物与表演", "光线与曝光", "中文生成提示词", "Negative / Avoid",
]:
    if token not in storyboard_template:
        errors.append(f"detailed storyboard template missing token: {token}")

agent_meta_path = ROOT / "agents/openai.yaml"
agent_meta = agent_meta_path.read_text(encoding="utf-8") if agent_meta_path.exists() else ""
for token in ["V3.0", "视觉叙事", "镜头语言", "导演包"]:
    if token not in agent_meta:
        errors.append(f"agent metadata missing token: {token}")

for path in ROOT.rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    if "\ufffd" in text:
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
