import pytest

try:
    from src_solution.abu.app import AbuApplication, MissionInput
    from src_solution.abu.other.numpy_workflow import average, vibration_score
    from src_solution.abu.other.pseudo_ai import (
        anomaly_vibration,
        regime_suggest,
        risk_flag,
    )
    from src_solution.abu.tcb.event_log import EventLog
    from src_solution.abu.tcb.policies import (
        depth_allowed,
        risk_allowed,
        rpm_allowed,
        vibration_allowed,
    )
    from src_solution.abu.tcb.safety import (
        enforce_depth_cap,
        enforce_rpm_cap,
        should_emergency_stop,
    )
    from src_solution.abu.tcb.security_monitor import (
        DrillCommand,
        SecurityMonitor,
    )
except ModuleNotFoundError:
    from abu.app import AbuApplication, MissionInput
    from abu.other.numpy_workflow import average, vibration_score
    from abu.other.pseudo_ai import (
        anomaly_vibration,
        regime_suggest,
        risk_flag,
    )
    from abu.tcb.event_log import EventLog
    from abu.tcb.policies import (
        depth_allowed,
        risk_allowed,
        rpm_allowed,
        vibration_allowed,
    )
    from abu.tcb.safety import (
        enforce_depth_cap,
        enforce_rpm_cap,
        should_emergency_stop,
    )
    from abu.tcb.security_monitor import (
        DrillCommand,
        SecurityMonitor,
    )


@pytest.mark.security
def test_security_monitor_blocks_depth_over_limit() -> None:
    monitor = SecurityMonitor()

    decision = monitor.check(DrillCommand(
        depth=250.0, rpm=100.0, vibration=0.1))

    assert decision.allowed is False
    assert "depth" in decision.reason


@pytest.mark.security
def test_security_monitor_covers_all_denies_and_allow() -> None:
    log = EventLog()
    monitor = SecurityMonitor(log)

    assert monitor.check(
        DrillCommand(10.0, 100.0, 0.1)
    ).allowed is True
    assert monitor.check(
        DrillCommand(10.0, 400.0, 0.1)
    ).allowed is False
    assert monitor.check(
        DrillCommand(10.0, 100.0, 1.2)
    ).allowed is False
    decision = monitor.check(
        DrillCommand(10.0, 100.0, 0.1, "high")
    )
    assert decision.allowed is False

    events = log.last_events()
    assert len(events) == 4
    assert events[0]["type"] == "allow"
    assert events[-1]["type"] == "emergency_stop"


@pytest.mark.security
def test_security_policies_are_enforced() -> None:
    assert depth_allowed(0.0) is True
    assert depth_allowed(200.0) is True
    assert depth_allowed(-1.0) is False
    assert depth_allowed(201.0) is False

    assert rpm_allowed(0.0) is True
    assert rpm_allowed(300.0) is True
    assert rpm_allowed(-1.0) is False
    assert rpm_allowed(301.0) is False

    assert vibration_allowed(0.0) is True
    assert vibration_allowed(0.9) is True
    assert vibration_allowed(-0.1) is False
    assert vibration_allowed(1.0) is False

    assert risk_allowed("low") is True
    assert risk_allowed("medium") is True
    assert risk_allowed("high") is False


@pytest.mark.security
def test_security_safety_helpers() -> None:
    assert enforce_depth_cap(100.0) is True
    assert enforce_depth_cap(-1.0) is False
    assert enforce_depth_cap(250.0) is False

    assert enforce_rpm_cap(100.0) is True
    assert enforce_rpm_cap(-1.0) is False
    assert enforce_rpm_cap(400.0) is False

    assert should_emergency_stop(1.2, "low") is True
    assert should_emergency_stop(0.1, "high") is True
    assert should_emergency_stop(0.1, "low") is False


@pytest.mark.security
def test_security_other_domain_inputs_are_checked() -> None:
    assert anomaly_vibration([0.1, 0.2, 1.1]) is True
    assert anomaly_vibration([]) is False
    assert anomaly_vibration([0.1, 0.2]) is False

    assert regime_suggest(100.0)["rpm"] == 180.0
    assert regime_suggest(180.0)["rpm"] == 120.0

    assert risk_flag(190.0, 0.1) == "high"
    assert risk_flag(100.0, 0.8) == "medium"
    assert risk_flag(100.0, 0.1) == "low"

    assert average([]) == 0.0
    assert average([1.0, 2.0, 3.0]) == 2.0
    assert vibration_score([-1.0, 1.0, 2.0]) == 4.0 / 3.0


@pytest.mark.security
def test_security_app_flow() -> None:
    app = AbuApplication()

    assert app.run_tick(MissionInput(100.0, 100.0, 0.1)).accepted is True
    assert app.run_tick(MissionInput(300.0, 100.0, 0.1)).accepted is False
    assert app.run_tick(MissionInput(100.0, 400.0, 0.1)).accepted is False
    assert app.run_tick(MissionInput(100.0, 100.0, 1.2)).accepted is False
    assert app.run_tick(MissionInput(
        100.0, 100.0, 0.1, "high")).accepted is False
