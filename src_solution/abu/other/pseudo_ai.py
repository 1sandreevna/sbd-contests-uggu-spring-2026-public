"""Недоверенный псевдо-ИИ АБУ."""

from __future__ import annotations


def anomaly_vibration(samples: list[float], threshold: float = 0.9) -> bool:
    """Определить аномальную вибрацию."""
    if not samples:
        return False
    return max(abs(item) for item in samples) > threshold


def regime_suggest(depth_m: float) -> dict[str, float]:
    """Предложить режим бурения."""
    if depth_m > 150.0:
        return {"rpm": 120.0, "feed": 0.4}
    return {"rpm": 180.0, "feed": 0.7}


def risk_flag(depth_m: float, vibration: float) -> str:
    """Вернуть уровень риска."""
    if depth_m > 180.0:
        return "high"
    if vibration > 0.7:
        return "medium"
    return "low"


def estimate_risk(depth: float, vibration: float) -> str:
    """Совместимый alias для текущих тестов решения."""
    return risk_flag(depth, vibration)


def recommend_rpm(depth: float) -> float:
    """Совместимый alias для текущих тестов решения."""
    return regime_suggest(depth)["rpm"]
