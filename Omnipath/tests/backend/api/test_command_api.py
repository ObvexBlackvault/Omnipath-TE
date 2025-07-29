import pytest
from fastapi.testclient import TestClient
from backend.api.command_api import app

client = TestClient(app)

def test_command_bridge_route():
    response = client.post("/api/command", json={"command": "Boot OmniAgent"})
    assert response.status_code == 200
    assert "received" in response.json().get("message", "").lower()
