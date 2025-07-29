from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_status_endpoint_returns_valid_agents():
    response = client.get("/api/status")
    assert response.status_code == 200
    data = response.json()
    assert "ForkAlpha" in data
    assert "ForkBeta" in data
    assert isinstance(data["ForkAlpha"], str)
    assert isinstance(data["ForkBeta"], str)
