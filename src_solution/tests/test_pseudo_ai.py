from src_solution.abu.other.pseudo_ai import (
    anomaly_vibration,
    regime_suggest,
    risk_flag,
)


def test_anomaly_vibration_detects_large_sample() -> None:
    assert anomaly_vibration([0.1, 0.2, 1.1]) is True


def test_anomaly_vibration_accepts_empty_and_safe_samples() -> None:
    assert anomaly_vibration([]) is False
    assert anomaly_vibration([0.1, -0.3, 0.4]) is False


def test_regime_suggest_changes_with_depth() -> None:
    shallow = regime_suggest(100.0)
    deep = regime_suggest(180.0)

    assert shallow["rpm"] == 180.0
    assert deep["rpm"] == 120.0


def test_risk_flag_values() -> None:
    assert risk_flag(190.0, 0.1) == "high"
    assert risk_flag(100.0, 0.8) == "medium"
    assert risk_flag(100.0, 0.1) == "low"
