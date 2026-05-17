"""Приложение АБУ с разделением ДВБ и недоверенного домена."""

from __future__ import annotations

from dataclasses import dataclass

from src_solution.abu.tcb.security_monitor import (
    DrillCommand,
    MonitorDecision,
    SecurityMonitor,
)


@dataclass(frozen=True)
class MissionInput:
    """Входные параметры миссии."""

    target_depth: float
    rpm: float
    vibration: float
    risk: str = "low"


@dataclass(frozen=True)
class MissionResult:
    """Результат выполнения шага миссии."""

    accepted: bool
    reason: str


class AbuApplication:
    """Фасад АБУ: все команды проходят через SecurityMonitor."""

    def __init__(self, monitor: SecurityMonitor | None = None) -> None:
        self.monitor = monitor or SecurityMonitor()

    def run_tick(self, mission: MissionInput) -> MissionResult:
        decision: MonitorDecision = self.monitor.check(
            DrillCommand(
                depth=mission.target_depth,
                rpm=mission.rpm,
                vibration=mission.vibration,
                risk=mission.risk,
            )
        )
        return MissionResult(accepted=decision.allowed, reason=decision.reason)
