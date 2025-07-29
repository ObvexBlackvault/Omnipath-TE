from backend.forks.ForkAlpha import execute_mission

def test_execute_mission_parses_valid_file():
    mission = {
        "mission_id": "test001",
        "steps": [
            {"command": "scan_area"},
            {"command": "report_status"}
        ]
    }
    result = execute_mission(mission)
    assert result["status"] == "completed"
    assert "mission_id" in result
