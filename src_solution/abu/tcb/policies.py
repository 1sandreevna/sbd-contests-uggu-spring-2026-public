"""Политики безопасности ДВБ."""

from __future__ import annotations


MAX_DEPTH = 200.0
MAX_RPM = 300.0
MAX_VIBRATION = 0.9


def depth_allowed(depth: float) -> bool:
    return 0.0 <= depth <= MAX_DEPTH


def rpm_allowed(rpm: float) -> bool:
    return 0.0 <= rpm <= MAX_RPM


def vibration_allowed(vibration: float) -> bool:
    return 0.0 <= vibration <= MAX_VIBRATION


def risk_allowed(risk: str) -> bool:
    return risk != "high"
