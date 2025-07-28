from backend.forks.agent_alpha import AgentAlpha
from backend.forks.agent_beta import AgentBeta
from backend.forks.agent_gamma import AgentGamma

def launch_fleet():
    print("[FleetLauncher] Initializing agent fleet...")

    alpha = AgentAlpha()
    beta = AgentBeta()
    gamma = AgentGamma()

    alpha.run()
    beta.run()
    gamma.run()

if __name__ == "__main__":
    launch_fleet()
