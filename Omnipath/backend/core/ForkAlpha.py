from backend.core.ForkBaseAgent import ForkBaseAgent
from backend.core.mission_validator import validate_mission

class ForkAlpha(ForkBaseAgent):
    def __init__(self):
        super().__init__("ForkAlpha")

    def execute_mission(self, mission_path: str):
        mission_data = validate_mission(mission_path)
        self.assign_mission(mission_data)
        print(f"[ForkAlpha] Executing mission steps:")
        for step in mission_data["commands"]:
            print(f"→ Executing: {step}")
        self.status = "idle"
        print("[ForkAlpha] Mission complete.")
