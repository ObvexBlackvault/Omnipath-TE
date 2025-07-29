from backend.forks import ForkAlpha, ForkBeta

COMMAND_REGISTRY = {
    "boot_forkalpha": ForkAlpha.boot,
    "stop_forkalpha": ForkAlpha.stop,
    "boot_forkbeta": ForkBeta.boot,
    "stop_forkbeta": ForkBeta.stop,
    "status_forkalpha": ForkAlpha.get_status,
    "status_forkbeta": ForkBeta.get_status
}

def execute_command(command: str) -> str:
    command = command.strip().lower()
    if command in COMMAND_REGISTRY:
        result = COMMAND_REGISTRY[command]()
        return f"Executed '{command}' successfully." if result is None else str(result)
    else:
        raise ValueError(f"Unknown command: {command}")
