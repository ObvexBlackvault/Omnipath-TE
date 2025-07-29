import json
import os

REQUIRED_FIELDS = ["mission_id", "commands"]

def validate_mission(mission_path: str) -> dict:
    if not os.path.exists(mission_path):
        raise FileNotFoundError(f"Mission file not found: {mission_path}")

    with open(mission_path, "r") as f:
        try:
            mission_data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {e}")

    for field in REQUIRED_FIELDS:
        if field not in mission_data:
            raise ValueError(f"Missing required mission field: {field}")

    if not isinstance(mission_data["commands"], list):
        raise ValueError("The 'commands' field must be a list.")

    return mission_data

