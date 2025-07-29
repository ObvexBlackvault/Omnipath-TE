from backend.core.ForkFleetController import ForkFleetController

class CoreStatus:
    def __init__(self):
        self.controller = ForkFleetController()

    def get_status_report(self):
        return self.controller.get_fleet_status()
