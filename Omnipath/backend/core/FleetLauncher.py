from backend.core.ForkFleetController import ForkFleetController

class FleetLauncher:
    def __init__(self):
        self.controller = ForkFleetController()

    def launch(self):
        self.controller.boot_all()
        print("[FleetLauncher] All agents booted.")

    def deploy_mission(self, mission_data: dict):
        self.controller.assign_mission_to_all(mission_data)
        print(f"[FleetLauncher] Mission deployed to all agents: {mission_data}")
