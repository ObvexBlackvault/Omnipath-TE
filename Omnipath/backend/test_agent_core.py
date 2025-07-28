from agents.agent.core import AgentCore

# Initialize test agent
agent = AgentCore(name="TestAgent", role="debugger")

# Simulate memory + action
agent.remember("Observed system boot")
result = agent.act("Scan environment")

# Show results
print("Status Report:")
print(agent.status_report())
print("\nLast Action:")
print(result)
