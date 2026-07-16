#!/usr/bin/env python3
"""Interactive helper for manually recording an AI-native score.

This does not replace qualitative review. It validates the hard gate and prints a level.
"""
from __future__ import annotations

FIELDS = [
    ('theme_coupling', 25),
    ('world_behavior', 20),
    ('narrative_participation', 20),
    ('evolution_closure', 15),
    ('medium_non_substitutability', 15),
    ('ai_aesthetic_awareness', 5),
]


def read_score(name: str, maximum: int) -> int:
    while True:
        raw = input(f'{name} (0-{maximum}): ').strip()
        try:
            value = int(raw)
        except ValueError:
            print('Enter an integer.')
            continue
        if 0 <= value <= maximum:
            return value
        print('Out of range.')


def level(total: int) -> str:
    if total < 30:
        return 'AI tool-use'
    if total < 50:
        return 'AI-enhanced'
    if total < 70:
        return 'AI-driven'
    if total < 85:
        return 'AI-native'
    return 'highly mature AI-native'


def main() -> None:
    scores = {name: read_score(name, maximum) for name, maximum in FIELDS}
    total = sum(scores.values())
    hard_gate = (
        total >= 70
        and scores['theme_coupling'] >= 16
        and scores['world_behavior'] >= 12
        and scores['narrative_participation'] >= 12
        and scores['medium_non_substitutability'] >= 9
    )
    print(f'\nTotal: {total}/100')
    print(f'Band: {level(total)}')
    print(f'AI-native hard gate: {"PASS" if hard_gate else "FAIL"}')


if __name__ == '__main__':
    main()
