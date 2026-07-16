#!/usr/bin/env python3
"""交互式记录 AI 原生性评分。

该脚本只负责检查硬门槛，不能替代定性创作判断。
"""
from __future__ import annotations

FIELDS = [
    ('主题耦合', 25),
    ('世界行为', 20),
    ('叙事参与', 20),
    ('演化与收束', 15),
    ('媒介不可替代性', 15),
    ('AI美学自觉', 5),
]


def read_score(name: str, maximum: int) -> int:
    while True:
        raw = input(f'{name}（0-{maximum}）：').strip()
        try:
            value = int(raw)
        except ValueError:
            print('请输入整数。')
            continue
        if 0 <= value <= maximum:
            return value
        print('分数超出范围。')


def level(total: int) -> str:
    if total < 30:
        return 'AI工具化'
    if total < 50:
        return 'AI增强'
    if total < 70:
        return 'AI驱动'
    if total < 85:
        return 'AI原生'
    return '高成熟度AI原生'


def main() -> None:
    scores = {name: read_score(name, maximum) for name, maximum in FIELDS}
    total = sum(scores.values())
    hard_gate = (
        total >= 70
        and scores['主题耦合'] >= 16
        and scores['世界行为'] >= 12
        and scores['叙事参与'] >= 12
        and scores['媒介不可替代性'] >= 9
    )
    print(f'\n总分：{total}/100')
    print(f'等级：{level(total)}')
    print(f'AI原生硬门槛：{"通过" if hard_gate else "未通过"}')


if __name__ == '__main__':
    main()
