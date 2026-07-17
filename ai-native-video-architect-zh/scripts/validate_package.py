from pathlib import Path
import re, sys, json

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'SKILL.md','AGENT.md','README.md',
    'modes/create.md','modes/transform.md','modes/diagnose.md','modes/adapt.md',
    'core/story.md','core/continuity.md','core/dialogue.md','core/transform.md','core/production.md',
    'controllers/short-video.md','controllers/comedy.md','controllers/suspense.md','controllers/horror.md',
    'controllers/emotion.md','controllers/realism.md','controllers/visual.md','controllers/trend-culture.md',
    'evals/semantic-hard-gate.md','evals/drama-score.md','evals/propagation-score.md',
    'evals/character-agency-check.md','evals/twist-legality-check.md','evals/dialogue-check.md',
    'evals/mechanism-overuse-check.md','evals/production-score.md','evals/transform-fidelity-score.md',
    'templates/concept-brief.md','templates/beat-sheet.md','templates/standard-script.md',
    'templates/diagnosis-report.md','templates/transform-contract.md','templates/production-pack.md',
    'references/glossary.md','references/platform-notes.md','tests/stress-test-suite.md',
    'audit/cross-file-consistency-audit.md'
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

for p in ROOT.rglob('*.md'):
    text=p.read_text(encoding='utf-8')
    if '\ufffd' in text: errors.append(f'encoding replacement character: {p.relative_to(ROOT)}')

manifest={
    'skill':'ai-native-video-architect-zh',
    'markdown_files':len(list(ROOT.rglob('*.md'))),
    'required_files':len(REQUIRED),
    'status':'FAIL' if errors else 'PASS',
    'errors':errors,
}
print(json.dumps(manifest, ensure_ascii=False, indent=2))
sys.exit(1 if errors else 0)
