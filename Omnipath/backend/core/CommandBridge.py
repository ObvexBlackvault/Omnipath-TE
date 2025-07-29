from backend.core.ForkAlpha import ForkAlpha

class CommandBridge:
    def __init__(self):
        self.agents = {
            "alpha": None,
            "beta": None
        }

    def handle_command(self, command: str):
        if command == "boot_agent_alpha":
            self.agents["alpha"] = ForkAlpha()
            self.agents["alpha"].boot()
            return {"status": "ForkAlpha booted", "agent": "alpha"}
        elif command == "get_status":
            return self.get_status()
        else:
            return {"error": f"Unknown command '{command}'"}

    def get_status(self):
        status = {}
        for name, agent in self.agents.items():
            if agent:
                status[name] = agent.status()
            else:
                status[name] = "not running"
        return status
