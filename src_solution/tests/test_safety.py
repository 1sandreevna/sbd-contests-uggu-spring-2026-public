from src_solution.abu.tcb.safety import (
    enforce_depth_cap,
    enforce_rpm_cap,
    should_emergency_stop,
)


def test_depth_cap_accepts_safe_depth() -> None:
    assert enforce_depth_cap(100.0) is True


def test_depth_cap_rejects_negative_and_too_deep() -> None:
    assert enforce_depth_cap(-1.0) is False
    assert enforce_depth_cap(250.0) is False


def test_rpm_cap_accepts_safe_rpm() -> None:
    assert enforce_rpm_cap(150.0) is True


def test_rpm_cap_rejects_invalid_rpm() -> None:
    assert enforce_rpm_cap(-1.0) is False
    assert enforce_rpm_cap(500.0) is False


def test_emergency_stop_on_vibration_or_high_risk() -> None:
    assert should_emergency_stop(1.2, "low") is True
    assert should_emergency_stop(0.1, "high") is True
    assert should_emergency_stop(0.1, "low") is False
