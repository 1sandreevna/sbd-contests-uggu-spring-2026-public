"""Отдельный недоверенный домен: псевдо-AI рекомендации."""

from __future__ import annotations

import json
import sys

from src_solution.abu.other.pseudo_ai import risk_flag


def handle_request(payload: dict) -> dict:
    risk = risk_flag(
        float(payload["target_depth"]),
        float(payload["vibration"]),
    )
    return {"risk": risk}


def main() -> int:
    payload = json.loads(sys.stdin.read())
    print(json.dumps(handle_request(payload), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
