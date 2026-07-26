from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
VERSION = "4.0.0"

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
    "controllers/ai-production.md", "controllers/post-script-production.md",
    "controllers/style-reference.md", "controllers/virality.md",
    "controllers/production-management.md", "controllers/sound-design.md", "controllers/director-agent.md",
    "prompt-engineering/image-prompt-compiler.md", "prompt-engineering/visual-style-color-light.md",
    "prompt-engineering/asset-prompt-system.md", "prompt-engineering/storyboard-frame-system.md",
    "prompt-engineering/video-prompt-compiler.md", "prompt-engineering/camera-movement-library.md",
    "prompt-engineering/continuity-repair-system.md",
    "evals/semantic-hard-gate.md", "evals/drama-score.md", "evals/propagation-score.md",
    "evals/character-agency-check.md", "evals/twist-legality-check.md", "evals/dialogue-check.md",
    "evals/mechanism-overuse-check.md", "evals/production-score.md", "evals/transform-fidelity-score.md",
    "evals/high-concept-score.md", "evals/visual-narrative-score.md", "evals/camera-language-score.md",
    "evals/asset-readiness-score.md", "evals/prompt-production-readiness-score.md",
    "evals/director-package-score.md",
    "templates/concept-brief.md", "templates/beat-sheet.md", "templates/standard-script.md",
    "templates/diagnosis-report.md", "templates/transform-contract.md", "templates/production-pack.md",
    "templates/visual-bible.md", "templates/visual-narrative-board.md", "templates/camera-shot-plan.md",
    "templates/detailed-storyboard.md", "templates/director-package.md", "templates/asset-registry.md",
    "templates/character-asset-pack.md", "templates/environment-asset-pack.md",
    "templates/prop-asset-pack.md", "templates/frame-generation-pack.md", "templates/progress-status.md",
    "templates/asset-prompt-block.md", "templates/storyboard-frame-prompt-block.md",
    "templates/video-shot-prompt-block.md",
    "references/glossary.md", "references/platform-notes.md", "references/prompt-engineering-source-map.md",
    "references/examples/high-concept-scifi-memory-fuel.md",
    "references/examples/visual-narrative-last-gardener.md",
    "tests/asset-first-stress-tests.md", "tests/progress-navigation-stress-tests.md",
    "tests/post-script-prompt-pipeline-stress-tests.md", "tests/stress-test-suite.md",
    "audit/cross-file-consistency-audit.md",
]

errors = []
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


skill_path = ROOT / "SKILL.md"
skill = skill_path.read_text(encoding="utf-8") if skill_path.exists() else ""
if not skill.startswith("---\n"):
    errors.append("SKILL.md missing YAML frontmatter")
require_tokens("SKILL.md", [
    "name: ai-native-video-architect-zh", "AI Native Film Studio V4.0",
    "CREATE", "TRANSFORM", "DIAGNOSE", "ADAPT",
    "STORY_DIRECTOR", "VISUAL_DIRECTOR", "BLOCKBUSTER_DIRECTOR",
    "EXPERIMENTAL_DIRECTOR", "PRODUCTION_DIRECTOR",
    "S07 整批资产Prompt", "S10 整批分镜帧Prompt", "S12 整批视频生产",
    "ASSET_PROMPT_PACK", "FRAME_PROMPT_PACK", "CORE_SAMPLE_PACK", "VIDEO_PROMPT_PACK",
    "USER_SELF_AUDIT", "下一步", "prompt-engineering/image-prompt-compiler.md",
    "prompt-engineering/video-prompt-compiler.md", "PASS", "CONDITIONAL", "FAIL",
])

for rel in ["config/modes.yaml", "config/workflow.yaml", "config/scoring.yaml", "config/progress-navigation.yaml"]:
    require_tokens(rel, [f"version: {VERSION}"])

require_tokens("config/progress-navigation.yaml", [
    "NEXT_MEANS_NEXT_STAGE", "USER_SELF_AUDIT", "BATCH_STAGE_OUTPUT",
    "S00", "S07", "S08", "S10", "S11", "S12", "S13",
])
require_tokens("config/workflow.yaml", [
    "S00_creative_brief", "S03_script_or_visual_script", "S04_script_breakdown",
    "S07_asset_prompt_pack_and_production", "S08_user_asset_confirmation",
    "S10_storyboard_frame_prompt_pack", "S11_core_sample", "S12_batch_video_production_and_post",
    "USER_SELF_AUDIT", "NEXT_MEANS_NEXT_STAGE",
])
require_tokens("controllers/post-script-production.md", [
    "S04 剧本拆解", "S07 资产制作Prompt", "完整整批资产Prompt包",
    "USER_SELF_AUDIT", "下一步", "S10 分镜帧Prompt", "S12 批量视频制作",
])
require_tokens("prompt-engineering/image-prompt-compiler.md", [
    "图片Prompt基础公式", "一个静态瞬间", "正向Prompt", "负面Prompt", "输出规则",
])
require_tokens("prompt-engineering/visual-style-color-light.md", [
    "primary_colors", "secondary_colors", "accent_colors", "color_temperature",
    "saturation", "contrast", "真实光源",
])
require_tokens("prompt-engineering/asset-prompt-system.md", [
    "面部身份板", "生产三视图", "场景主布局", "道具结构", "局部修复",
])
require_tokens("prompt-engineering/storyboard-frame-system.md", [
    "首帧", "尾帧", "多人站位", "九宫格", "多机位",
])
require_tokens("prompt-engineering/video-prompt-compiler.md", [
    "视频Prompt基础公式", "唯一主要动作", "起势", "过程", "收住", "结束状态",
])
require_tokens("prompt-engineering/camera-movement-library.md", [
    "固定镜头", "推镜", "拉镜", "跟拍", "环绕", "FPV", "焦点转移", "硬切",
])
require_tokens("prompt-engineering/continuity-repair-system.md", [
    "抽尾帧续拍", "硬切", "多角度", "局部修复", "夜景", "4K", "台词",
])
require_tokens("templates/asset-prompt-block.md", [
    "【正向Prompt】", "【负面Prompt】", "【输出规则】", "【稳定生成方案】",
])
require_tokens("templates/storyboard-frame-prompt-block.md", [
    "【首帧正向Prompt】", "【首帧负面Prompt】", "【尾帧正向Prompt】",
])
require_tokens("templates/video-shot-prompt-block.md", [
    "【视频正向Prompt】", "【视频负面Prompt】", "【结束状态】", "【失败修复】",
])
require_tokens("tests/post-script-prompt-pipeline-stress-tests.md", [
    "SOURCE_MODULE_REQUIRED", "BATCH_ASSET_OUTPUT", "FULL_COPY_BLOCK",
    "NEXT_MEANS_NEXT_STAGE", "USER_SELF_AUDIT", "IMAGE_VIDEO_SEPARATION",
    "COLOR_SIX_AXIS", "CAMERA_ENDPOINT", "TAIL_FRAME_CONTINUATION",
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
        expected_outputs = {
            "CREATIVE_BRIEF", "DIRECTION_OPTIONS", "STORY_TREATMENT", "SCRIPT_PACKAGE",
            "SCRIPT_BREAKDOWN", "ASSET_PLAN", "ASSET_PROMPT_PACK", "ASSET_PACK",
            "SHOT_LIST_AND_CAMERA_PLAN", "FRAME_PROMPT_PACK", "CORE_SAMPLE_PACK",
            "VIDEO_PROMPT_PACK", "PRODUCTION_PACK", "DIRECTOR_REVIEW_AND_DELIVERY",
        }
        if not expected_outputs.issubset(set(manifest.get("output_levels", []))):
            errors.append("manifest missing V4 output levels")
        expected_stages = {f"S{i:02d}" for i in range(14)}
        if expected_stages != set(manifest.get("progress_stages", [])):
            errors.append("manifest progress stages must be S00 through S13")
        expected_contracts = {"BATCH_STAGE_OUTPUT", "USER_SELF_AUDIT", "NEXT_MEANS_NEXT_STAGE"}
        if not expected_contracts.issubset(set(manifest.get("interaction_contracts", []))):
            errors.append("manifest missing V4 interaction contracts")
    except json.JSONDecodeError as exc:
        errors.append(f"invalid manifest.json: {exc}")

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
