"""IPC-клиент для запуска доменов АБУ в отдельных процессах."""

from __future__ import annotations

import json
import subprocess
import sys


def call_domain(module: str, payload: dict) -> dict:
    completed = subprocess.run(
        [sys.executable, "-m", module],
        input=json.dumps(payload),
        text=True,
        capture_output=True,
        check=True,
    )
    return json.loads(completed.stdout)
