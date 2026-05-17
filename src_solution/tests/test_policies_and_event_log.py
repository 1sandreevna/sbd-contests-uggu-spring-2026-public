try:
    from src_solution.abu.tcb.event_log import EventLog
    from src_solution.abu.tcb.policies import (
        depth_allowed,
        risk_allowed,
        rpm_allowed,
        vibration_allowed,
    )
except ModuleNotFoundError:
    from abu.tcb.event_log import EventLog
    from abu.tcb.policies import (
        depth_allowed,
        risk_allowed,
        rpm_allowed,
        vibration_allowed,
    )


def test_depth_policy_boundaries() -> None:
    assert depth_allowed(0.0) is True
    assert depth_allowed(200.0) is True
    assert depth_allowed(-1.0) is False
    assert depth_allowed(201.0) is False


def test_rpm_policy_boundaries() -> None:
    assert rpm_allowed(0.0) is True
    assert rpm_allowed(300.0) is True
    assert rpm_allowed(-1.0) is False
    assert rpm_allowed(301.0) is False


def test_vibration_policy_boundaries() -> None:
    assert vibration_allowed(0.0) is True
    assert vibration_allowed(0.9) is True
    assert vibration_allowed(-0.1) is False
    assert vibration_allowed(1.0) is False


def test_risk_policy() -> None:
    assert risk_allowed("low") is True
    assert risk_allowed("medium") is True
    assert risk_allowed("high") is False


def test_event_log_records_multiple_events() -> None:
    log = EventLog()

    log.record("allow", "first")
    log.record("deny", "second")

    events = log.last_events()
    assert len(events) == 2
    assert events[0]["type"] == "allow"
    assert events[1]["type"] == "deny"
    assert events[1]["message"] == "second"
