try:
    from src_solution.abu.app import AbuApplication, MissionInput
    from src_solution.abu.other.numpy_workflow import average, vibration_score
    from src_solution.abu.other.pseudo_ai import estimate_risk, recommend_rpm
except ModuleNotFoundError:
    from abu.app import AbuApplication, MissionInput
    from abu.other.numpy_workflow import average, vibration_score
    from abu.other.pseudo_ai import estimate_risk, recommend_rpm


def test_app_blocks_high_risk() -> None:
    app = AbuApplication()

    result = app.run_tick(
        MissionInput(
            target_depth=100.0,
            rpm=100.0,
            vibration=0.1,
            risk="high",
        )
    )

    assert result.accepted is False
    assert "risk" in result.reason


def test_app_blocks_high_vibration() -> None:
    app = AbuApplication()

    result = app.run_tick(
        MissionInput(
            target_depth=100.0,
            rpm=100.0,
            vibration=1.5,
            risk="low",
        )
    )

    assert result.accepted is False
    assert "vibration" in result.reason


def test_pseudo_ai_estimates_risk() -> None:
    assert estimate_risk(190.0, 0.1) == "high"
    assert estimate_risk(100.0, 0.8) == "medium"
    assert estimate_risk(100.0, 0.1) == "low"


def test_pseudo_ai_recommends_rpm() -> None:
    assert recommend_rpm(160.0) == 120.0
    assert recommend_rpm(100.0) == 180.0


def test_numpy_workflow_average() -> None:
    assert average([]) == 0.0
    assert average([1.0, 2.0, 3.0]) == 2.0


def test_numpy_workflow_vibration_score() -> None:
    assert vibration_score([-1.0, 1.0, 2.0]) == 4.0 / 3.0
