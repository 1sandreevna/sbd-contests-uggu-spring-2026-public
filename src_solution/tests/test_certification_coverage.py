from abu.app import AbuApplication, MissionInput
from abu.other.numpy_workflow import average, vibration_score
from abu.other.pseudo_ai import anomaly_vibration, regime_suggest, risk_flag
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
from abu.tcb.security_monitor import DrillCommand, SecurityMonitor


def test_certification_exercises_tcb_and_other() -> None:
    log = EventLog()
    monitor = SecurityMonitor(log)

    assert monitor.check(DrillCommand(10.0, 100.0, 0.1)).allowed is True
    assert monitor.check(DrillCommand(250.0, 100.0, 0.1)).allowed is False
    assert monitor.check(DrillCommand(10.0, 400.0, 0.1)).allowed is False
    assert monitor.check(DrillCommand(10.0, 100.0, 1.2)).allowed is False
    assert monitor.check(DrillCommand(
        10.0, 100.0, 0.1, "high")).allowed is False

    assert len(log.last_events()) == 5

    assert depth_allowed(0.0) is True
    assert depth_allowed(201.0) is False
    assert rpm_allowed(300.0) is True
    assert rpm_allowed(301.0) is False
    assert vibration_allowed(0.9) is True
    assert vibration_allowed(1.0) is False
    assert risk_allowed("low") is True
    assert risk_allowed("high") is False

    assert enforce_depth_cap(200.0) is True
    assert enforce_depth_cap(201.0) is False
    assert enforce_rpm_cap(300.0) is True
    assert enforce_rpm_cap(301.0) is False
    assert should_emergency_stop(1.2, "low") is True
    assert should_emergency_stop(0.1, "high") is True
    assert should_emergency_stop(0.1, "low") is False

    assert anomaly_vibration([0.1, 1.0]) is True
    assert anomaly_vibration([]) is False
    assert regime_suggest(100.0)["rpm"] == 180.0
    assert regime_suggest(180.0)["rpm"] == 120.0
    assert risk_flag(190.0, 0.1) == "high"
    assert risk_flag(100.0, 0.8) == "medium"
    assert risk_flag(100.0, 0.1) == "low"

    assert average([]) == 0.0
    assert average([1.0, 2.0, 3.0]) == 2.0
    assert vibration_score([-1.0, 1.0]) == 1.0

    app = AbuApplication()
    assert app.run_tick(MissionInput(100.0, 100.0, 0.1)).accepted is True
    assert app.run_tick(MissionInput(300.0, 100.0, 0.1)).accepted is False
