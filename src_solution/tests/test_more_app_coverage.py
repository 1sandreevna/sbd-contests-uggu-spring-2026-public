try:
    from src_solution.abu.app import AbuApplication, MissionInput
except ModuleNotFoundError:
    from abu.app import AbuApplication, MissionInput


def test_app_blocks_bad_rpm() -> None:
    app = AbuApplication()

    result = app.run_tick(
        MissionInput(
            target_depth=100.0,
            rpm=400.0,
            vibration=0.1,
            risk="low",
        )
    )

    assert result.accepted is False
    assert "rpm" in result.reason


def test_app_boundary_values_are_allowed() -> None:
    app = AbuApplication()

    result = app.run_tick(
        MissionInput(
            target_depth=200.0,
            rpm=300.0,
            vibration=0.9,
            risk="medium",
        )
    )

    assert result.accepted is True
    assert result.reason == "ok"
