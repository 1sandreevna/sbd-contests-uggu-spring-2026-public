import pytest

from src_solution.abu.domains.ipc_client import call_domain


@pytest.mark.security
def test_tcb_monitor_runs_as_separate_process() -> None:
    result = call_domain(
        "src_solution.abu.domains.tcb_monitor_process",
        {
            "depth": 100.0,
            "rpm": 100.0,
            "vibration": 0.1,
            "risk": "low",
        },
    )

    assert result == {"allowed": True, "reason": "ok"}


@pytest.mark.security
def test_tcb_monitor_process_blocks_unsafe_command() -> None:
    result = call_domain(
        "src_solution.abu.domains.tcb_monitor_process",
        {
            "depth": 250.0,
            "rpm": 100.0,
            "vibration": 0.1,
            "risk": "low",
        },
    )

    assert result["allowed"] is False
    assert "depth" in result["reason"]


@pytest.mark.security
def test_other_ai_runs_as_separate_process() -> None:
    result = call_domain(
        "src_solution.abu.domains.other_ai_process",
        {
            "target_depth": 190.0,
            "vibration": 0.1,
        },
    )

    assert result == {"risk": "high"}
