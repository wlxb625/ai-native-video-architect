#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    'SKILL.md',
    'agents/openai.yaml',
    'references/core-workflow.md',
    'modes/create.md',
    'modes/transform.md',
    'modes/diagnose.md',
    'modes/adapt.md',
    'controllers/realism.md',
    'controllers/horror.md',
    'controllers/comedy.md',
    'evals/trigger-tests.csv',
    'manifest.txt',
}


def fail(message: str) -> None:
    print(f'ERROR: {message}', file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    for path in sorted(EXPECTED):
        if not (ROOT / path).is_file():
            fail(f'missing required file: {path}')

    skill_files = [p for p in ROOT.rglob('*') if p.is_file() and p.name.lower() == 'skill.md']
    if len(skill_files) != 1:
        fail(f'exactly one SKILL.md is required, found {len(skill_files)}')

    skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
    fm = re.match(r'^---\n(.*?)\n---\n', skill, flags=re.S)
    if not fm:
        fail('SKILL.md lacks YAML front matter')
    front = fm.group(1)
    if not re.search(r'^name:\s*ai-native-video-architect\s*$', front, re.M):
        fail('front matter name is missing or incorrect')
    if not re.search(r'^description:\s*\S', front, re.M):
        fail('front matter description is missing')

    links = re.findall(r'`((?:references|modes|controllers|templates|evals|examples|scripts)/[^`]+)`', skill)
    for rel in links:
        if not (ROOT / rel).exists():
            fail(f'SKILL.md references missing path: {rel}')

    manifest_path = ROOT / 'manifest.txt'
    manifest = [line.strip() for line in manifest_path.read_text(encoding='utf-8').splitlines() if line.strip()]
    actual = sorted(
        str(p.relative_to(ROOT))
        for p in ROOT.rglob('*')
        if p.is_file()
        and p.name != 'manifest.txt'
        and '__pycache__' not in p.parts
        and p.suffix != '.pyc'
    )
    missing = sorted(set(actual) - set(manifest))
    extra = sorted(set(manifest) - set(actual))
    if missing:
        fail('manifest missing files: ' + ', '.join(missing))
    if extra:
        fail('manifest lists nonexistent files: ' + ', '.join(extra))

    csv_path = ROOT / 'evals/trigger-tests.csv'
    if csv_path.stat().st_size < 100:
        fail('trigger test CSV appears empty')

    print(f'OK: validated {len(actual) + 1} files in {ROOT.name}')


if __name__ == '__main__':
    main()
