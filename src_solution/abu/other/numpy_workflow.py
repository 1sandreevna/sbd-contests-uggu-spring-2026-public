"""Недоверенный расчётный модуль.

В реальном решении здесь может использоваться numpy, но зависимость
не входит в ДВБ и не помещается в requirements ДВБ.
"""

from __future__ import annotations


def average(values: list[float]) -> float:
    """Среднее значение."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def vibration_score(samples: list[float]) -> float:
    """Оценка вибрации."""
    return average([abs(item) for item in samples])
