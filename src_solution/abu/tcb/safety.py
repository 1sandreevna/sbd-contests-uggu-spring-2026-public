"""Safety-проверки доверенной вычислительной базы АБУ."""

from __future__ import annotations


def enforce_depth_cap(depth_m: float, max_depth_m: float = 200.0) -> bool:
    """Проверить, что глубина в допустимом диапазоне."""
    return 0.0 <= depth_m <= max_depth_m


def enforce_rpm_cap(rpm: float, max_rpm: float = 300.0) -> bool:
    """Проверить, что обороты в допустимом диапазоне."""
    return 0.0 <= rpm <= max_rpm


def should_emergency_stop(vibration: float, risk: str) -> bool:
    return vibration >= 1.0 or risk == "high"
