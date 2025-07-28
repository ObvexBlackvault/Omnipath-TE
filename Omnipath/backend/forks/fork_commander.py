from forks.agent_beta import AgentBeta
from forks.agent_alpha import AgentAlpha

class ForkCommander:
    def __init__(self):
        self.forks = []
        self.spawn_initial_forks()

    def spawn_initial_forks(self):
        agent = AgentAlpha()
        self.forks.append(agent)

    def broadcast_command(self, command):
        for fork in self.forks:
            if hasattr(fork, "receive_command"):
                fork.receive_command(command)
            else:
                print(f"[{fork.name}] No command receiver implemented.")

    def list_forks(self):
        return [fork.name for fork in self.forks]

    def spawn_initial_forks(self):
        alpha = AgentAlpha()
        beta = AgentBeta()
        self.forks.append(alpha)
        self.forks.append(beta)
