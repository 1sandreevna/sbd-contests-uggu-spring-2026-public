try:
    from src_solution.abu.app import AbuApplication, MissionInput
except ModuleNotFoundError:
    from abu.app import AbuApplication, MissionInput


def test_app_allows_safe_mission_tick() -> None:
    app = AbuApplication()

    result = app.run_tick(MissionInput(
        target_depth=100.0, rpm=150.0, vibration=0.1))

    assert result.accepted is True
    assert result.reason == "ok"


def test_app_blocks_unsafe_mission_tick() -> None:
    app = AbuApplication()

    result = app.run_tick(MissionInput(
        target_depth=300.0, rpm=150.0, vibration=0.1))

    assert result.accepted is False
    assert "depth" in result.reason
