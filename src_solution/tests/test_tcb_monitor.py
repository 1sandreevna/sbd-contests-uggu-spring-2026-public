try:
    from src_solution.abu.tcb.event_log import EventLog
    from src_solution.abu.tcb.security_monitor import (
        DrillCommand,
        SecurityMonitor,
    )
except ModuleNotFoundError:
    from abu.tcb.event_log import EventLog
    from src_solution.abu.tcb.security_monitor import (
        DrillCommand,
        SecurityMonitor,
    )


def test_monitor_allows_safe_command() -> None:
    log = EventLog()
    monitor = SecurityMonitor(log)

    decision = monitor.check(DrillCommand(
        depth=50.0, rpm=120.0, vibration=0.2))

    assert decision.allowed is True
    assert decision.reason == "ok"
    assert log.last_events()[-1]["type"] == "allow"


def test_monitor_denies_high_risk() -> None:
    monitor = SecurityMonitor()

    decision = monitor.check(
        DrillCommand(depth=50.0, rpm=120.0, vibration=0.2, risk="high")
    )

    assert decision.allowed is False
    assert "risk" in decision.reason


def test_monitor_emergency_stop_on_vibration() -> None:
    log = EventLog()
    monitor = SecurityMonitor(log)

    decision = monitor.check(DrillCommand(
        depth=50.0, rpm=120.0, vibration=1.2))

    assert decision.allowed is False
    assert log.last_events()[-1]["type"] == "emergency_stop"
