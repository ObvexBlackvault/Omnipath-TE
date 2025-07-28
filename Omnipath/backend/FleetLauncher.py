from backend.forks.ForkAlpha import AgentAlpha
from backend.forks.ForkBeta import AgentBeta
from backend.forks.ForkGamma import AgentGamma

def launch_fleet():
    alpha = AgentAlpha()
    beta = AgentBeta()
    gamma = AgentGamma()

    alpha.run()
    beta.run()
    gamma.run()

if __name__ == "__main__":
    launch_fleet()
