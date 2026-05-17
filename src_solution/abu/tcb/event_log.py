"""Журнал событий ДВБ."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class EventLog:
    """Простой журнал событий безопасности."""

    events: list[dict[str, str]] = field(default_factory=list)

    def record(self, event_type: str, message: str) -> None:
        self.events.append(
            {
                "time": datetime.now(timezone.utc).isoformat(),
                "type": event_type,
                "message": message,
            }
        )

    def last_events(self) -> list[dict[str, str]]:
        return list(self.events)
