from backend.core.ForkBaseAgent import ForkBaseAgent
from backend.core.mission_validator import validate_mission

class ForkBeta(ForkBaseAgent):
    def __init__(self):
        super().__init__("ForkBeta")

    def execute_mission(self, mission_path: str):
        mission_data = validate_mission(mission_path)
        self.assign_mission(mission_data)
        print(f"[ForkBeta] Executing mission steps:")
        for step in mission_data["commands"]:
            print(f"→ Executing: {step}")
        self.status = "idle"
        print("[ForkBeta] Mission complete.")
