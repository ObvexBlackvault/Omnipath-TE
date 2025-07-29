from backend.agents import ForkAlpha, ForkBeta

def test_forkalpha_executes_mission():
    mission = [{"command": "scan"}, {"command": "report"}]
    agent = ForkAlpha()
    agent.load_mission(mission)
    assert agent.current_mission == mission

def test_forkbeta_executes_mission():
    mission = [{"command": "explore"}, {"command": "map"}]
    agent = ForkBeta()
    agent.load_mission(mission)
    assert agent.current_mission == mission
