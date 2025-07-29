from backend.core.ForkAlpha import ForkAlpha

class CommandBridge:
    @staticmethod
    def execute_command(command: str):
        if command == "boot_agent_alpha":
            agent = ForkAlpha()
            agent.boot()
            return "ForkAlpha booted"
        elif command == "get_status":
            return "System nominal"
        else:
            raise ValueError(f"Unknown command: {command}")
