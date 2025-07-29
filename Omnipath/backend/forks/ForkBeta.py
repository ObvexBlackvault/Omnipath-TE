# Minimal ForkBeta structure with status
_agent_state = {
    "status": "idle",
    "mission": "None"
}

def get_status():
    return _agent_state

def boot():
    _agent_state["status"] = "active"
    _agent_state["mission"] = "Diagnostics"

def stop():
    _agent_state["status"] = "idle"
    _agent_state["mission"] = "None"
