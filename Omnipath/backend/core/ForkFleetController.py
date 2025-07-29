from backend.core.ForkAlpha import ForkAlpha
from backend.core.ForkBeta import ForkBeta

class ForkFleetController:
    def __init__(self):
        self.fleet = {
            "ForkAlpha": ForkAlpha(),
            "ForkBeta": ForkBeta()
        }

    def get_status(self):
        return {name: agent.get_status() for name, agent in self.fleet.items()}

    def execute_mission(self, agent_name: str, mission_path: str):
        if agent_name not in self.fleet:
            return {"error": f"Agent {agent_name} not found"}
        try:
            self.fleet[agent_name].execute_mission(mission_path)
            return {"status": "success", "message": f"{agent_name} completed mission"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def assign_all(self, mission_path: str):
        results = {}
        for name, agent in self.fleet.items():
            try:
                agent.execute_mission(mission_path)
                results[name] = "completed"
            except Exception as e:
                results[name] = f"error: {str(e)}"
        return results
