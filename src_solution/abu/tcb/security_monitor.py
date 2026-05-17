"""Монитор безопасности ДВБ."""

from __future__ import annotations

from dataclasses import dataclass

from .event_log import EventLog
from .safety import (
    enforce_depth_cap,
    enforce_rpm_cap,
    should_emergency_stop,
)


@dataclass(frozen=True)
class DrillCommand:
    """Команда бурения, поступающая на проверку."""

    depth: float
    rpm: float
    vibration: float
    risk: str = "low"


@dataclass(frozen=True)
class MonitorDecision:
    """Решение монитора безопасности."""

    allowed: bool
    reason: str


class SecurityMonitor:
    """Единая точка проверки команд перед выполнением."""

    def __init__(self, event_log: EventLog | None = None) -> None:
        self.event_log = event_log or EventLog()

    def check(self, command: DrillCommand) -> MonitorDecision:
        """Проверить команду по политикам безопасности."""
        if not enforce_depth_cap(command.depth):
            self.event_log.record("deny", "depth limit violation")
            return MonitorDecision(False, "depth limit violation")

        if not enforce_rpm_cap(command.rpm):
            self.event_log.record("deny", "rpm limit violation")
            return MonitorDecision(False, "rpm limit violation")

        if should_emergency_stop(command.vibration, command.risk):
            self.event_log.record("emergency_stop", "safety emergency stop")
            return MonitorDecision(False, "vibration or risk emergency stop")

        self.event_log.record("allow", "command allowed")
        return MonitorDecision(True, "ok")
