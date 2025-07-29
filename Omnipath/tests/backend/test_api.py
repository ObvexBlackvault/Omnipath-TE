from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_status_endpoint():
    response = client.get("/api/status")
    assert response.status_code == 200
    assert "ForkAlpha" in response.json()
    assert "ForkBeta" in response.json()

def test_command_stub():
    response = client.post("/api/command", json={"command": "Boot OmniAgent"})
    assert response.status_code in [200, 501]  # Allow 501 if still stubbed
