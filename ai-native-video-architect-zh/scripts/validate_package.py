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
    print(f'错误：{message}', file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    for path in sorted(EXPECTED):
        if not (ROOT / path).is_file():
            fail(f'缺少必要文件：{path}')

    skill_files = [p for p in ROOT.rglob('*') if p.is_file() and p.name.lower() == 'skill.md']
    if len(skill_files) != 1:
        fail(f'必须且只能有一个 SKILL.md，当前发现 {len(skill_files)} 个')

    skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
    fm = re.match(r'^---\n(.*?)\n---\n', skill, flags=re.S)
    if not fm:
        fail('SKILL.md 缺少 YAML 前置元数据')
    front = fm.group(1)
    if not re.search(r'^name:\s*ai-native-video-architect-zh\s*$', front, re.M):
        fail('前置元数据中的 name 缺失或不正确')
    if not re.search(r'^description:\s*\S', front, re.M):
        fail('前置元数据中的 description 缺失')

    links = re.findall(r'`((?:references|modes|controllers|templates|evals|examples|scripts)/[^`]+)`', skill)
    for rel in links:
        if not (ROOT / rel).exists():
            fail(f'SKILL.md 引用了不存在的路径：{rel}')

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
        fail('manifest 未登记文件：' + ', '.join(missing))
    if extra:
        fail('manifest 登记了不存在的文件：' + ', '.join(extra))

    csv_path = ROOT / 'evals/trigger-tests.csv'
    if csv_path.stat().st_size < 100:
        fail('触发测试 CSV 似乎为空')

    print(f'通过：已校验 {len(actual) + 1} 个文件，目录 {ROOT.name}')


if __name__ == '__main__':
    main()
