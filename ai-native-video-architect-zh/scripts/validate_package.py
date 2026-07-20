from pathlib import Path
import re, sys, json

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'SKILL.md','AGENT.md','README.md','manifest.json',
    'modes/create.md','modes/transform.md','modes/diagnose.md','modes/adapt.md',
    'core/story.md','core/continuity.md','core/dialogue.md','core/transform.md','core/production.md',
    'controllers/short-video.md','controllers/comedy.md','controllers/suspense.md','controllers/horror.md',
    'controllers/emotion.md','controllers/realism.md','controllers/visual.md','controllers/trend-culture.md',
    'controllers/high-concept-scifi.md',
    'evals/semantic-hard-gate.md','evals/drama-score.md','evals/propagation-score.md',
    'evals/character-agency-check.md','evals/twist-legality-check.md','evals/dialogue-check.md',
    'evals/mechanism-overuse-check.md','evals/production-score.md','evals/transform-fidelity-score.md',
    'evals/high-concept-score.md',
    'templates/concept-brief.md','templates/beat-sheet.md','templates/standard-script.md',
    'templates/diagnosis-report.md','templates/transform-contract.md','templates/production-pack.md',
    'references/glossary.md','references/platform-notes.md',
    'references/examples/high-concept-scifi-memory-fuel.md',
    'tests/stress-test-suite.md','audit/cross-file-consistency-audit.md'
]
errors=[]
for rel in REQUIRED:
    p=ROOT/rel
    if not p.exists(): errors.append(f'missing: {rel}')
    elif not p.read_text(encoding='utf-8').strip(): errors.append(f'empty: {rel}')

skill=(ROOT/'SKILL.md').read_text(encoding='utf-8') if (ROOT/'SKILL.md').exists() else ''
if not skill.startswith('---\n'): errors.append('SKILL.md missing YAML frontmatter')
if 'name: ai-native-video-architect-zh' not in skill: errors.append('wrong skill name')
for token in ['CREATE','TRANSFORM','DIAGNOSE','ADAPT','PASS','CONDITIONAL','FAIL']:
    if token not in skill: errors.append(f'SKILL.md missing protocol token: {token}')

for token in [
    '一句话概念','单一核心机制','单一人物任务','艰难选择','最后图像',
    'controllers/high-concept-scifi.md','evals/high-concept-score.md'
]:
    if token not in skill: errors.append(f'SKILL.md missing high-concept token: {token}')

manifest_path=ROOT/'manifest.json'
if manifest_path.exists():
    try:
        manifest_data=json.loads(manifest_path.read_text(encoding='utf-8'))
        if manifest_data.get('version') != '2.1.0':
            errors.append('manifest version must be 2.1.0')
        listed=set(manifest_data.get('files', []))
        for rel in REQUIRED:
            if rel not in listed and rel not in {'manifest.json'}:
                errors.append(f'manifest missing file: {rel}')
    except json.JSONDecodeError as exc:
        errors.append(f'invalid manifest.json: {exc}')

high_concept=(ROOT/'controllers/high-concept-scifi.md').read_text(encoding='utf-8') if (ROOT/'controllers/high-concept-scifi.md').exists() else ''
for token in ['one_sentence_concept','core_rule','impossible_choice','final_image']:
    if token not in high_concept:
        errors.append(f'high-concept controller missing token: {token}')

high_score=(ROOT/'evals/high-concept-score.md').read_text(encoding='utf-8') if (ROOT/'evals/high-concept-score.md').exists() else ''
for token in ['Concept Compression','Mechanism Unity','Spectacle Causality','Final Afterimage']:
    if token not in high_score:
        errors.append(f'high-concept score missing dimension: {token}')

for p in ROOT.rglob('*.md'):
    text=p.read_text(encoding='utf-8')
    if '\ufffd' in text: errors.append(f'encoding replacement character: {p.relative_to(ROOT)}')

manifest={
    'skill':'ai-native-video-architect-zh',
    'version':'2.1.0',
    'markdown_files':len(list(ROOT.rglob('*.md'))),
    'required_files':len(REQUIRED),
    'status':'FAIL' if errors else 'PASS',
    'errors':errors,
}
print(json.dumps(manifest, ensure_ascii=False, indent=2))
sys.exit(1 if errors else 0)