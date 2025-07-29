class ForkBaseAgent:
    def __init__(self, name: str):
        self.name = name
        self.status = "idle"
        self.mission = None

    def boot(self):
        self.status = "active"
        print(f"[{self.name}] Booted and ready.")

    def stop(self):
        self.status = "offline"
        print(f"[{self.name}] Shutdown complete.")

    def get_status(self):
        return {
            "name": self.name,
            "status": self.status,
            "current_mission": self.mission.get("mission_id") if self.mission else None
        }

    def assign_mission(self, mission_data: dict):
        self.mission = mission_data
        self.status = "engaged"
        print(f"[{self.name}] Assigned mission {mission_data.get('mission_id')}")
