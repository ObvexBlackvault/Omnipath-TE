from forks.agent_alpha import AgentAlpha
from forks.agent_beta import AgentBeta
from forks.agent_gamma import AgentGamma

# Instantiate the agents
alpha = AgentAlpha()
beta = AgentBeta()
gamma = AgentGamma()

# Run them (init + 1st heartbeat)
alpha.run()
beta.run()
gamma.run()

print("[Fleet Launch] Alpha, Beta, Gamma deployed into Omnipath.")
