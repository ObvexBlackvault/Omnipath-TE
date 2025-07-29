from backend.core.ForkAlpha import ForkAlpha
from backend.core.ForkBeta import ForkBeta

def get_agent_statuses():
    alpha = ForkAlpha(agent_name="ForkAlpha")
    beta = ForkBeta(agent_name="ForkBeta")

    agents = [alpha, beta]
    return [
        {
            "name": agent.agent_name,
            "status": agent.get_status(),
            "mission": agent.current_mission()
        }
        for agent in agents
    ]
