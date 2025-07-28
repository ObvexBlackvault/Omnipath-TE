from forks.agent_alpha import AgentAlpha
from agents.system.archivist import Archivist
from agents.system.commander import Commander
from agents.system.guardian import Guardian
from forks.fork_commander import ForkCommander
from core.trace_log import write_trace
from utils.helpers import now

# Initialize internal bots
archivist = Archivist()
commander = Commander()
guardian = Guardian()

# Boot log
write_trace({
    "type": "system_boot",
    "timestamp": now(),
    "modules": ["archivist", "commander", "guardian"]
})

# Run health check
env_status = guardian.check_env_health()
write_trace({
    "type": "env_status",
    "status": env_status
})

# Example loop check (disabled for now)
archived_logs = archivist.read_logs()
# loops_found = guardian.loop_check(archived_logs)
loops_found = []  # Temporarily bypassed

if loops_found:
    write_trace({
        "type": "loop_detected",
        "agents": loops_found,
        "timestamp": now()
    })

# Commander test ping
commander.queue_check()

# === Launch Agent Alpha ===
agent = AgentAlpha()
agent.run()

# === Launch Fork Commander ===
fleet = ForkCommander()
fleet.broadcast_command("Standby and monitor.")
print(f"Fleet Active: {fleet.list_forks()}")
