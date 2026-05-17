"""Отдельный процесс-домен ДВБ: проверка команд бурения."""

from __future__ import annotations

import json
import sys

from src_solution.abu.tcb.security_monitor import DrillCommand, SecurityMonitor


def handle_request(payload: dict) -> dict:
    monitor = SecurityMonitor()
    command = DrillCommand(
        depth=float(payload["depth"]),
        rpm=float(payload["rpm"]),
        vibration=float(payload["vibration"]),
        risk=str(payload.get("risk", "low")),
    )
    decision = monitor.check(command)
    return {"allowed": decision.allowed, "reason": decision.reason}


def main() -> int:
    payload = json.loads(sys.stdin.read())
    print(json.dumps(handle_request(payload), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
