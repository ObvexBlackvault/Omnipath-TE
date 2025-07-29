import pytest
from fastapi.testclient import TestClient
from backend.api.status_api import app

client = TestClient(app)

def test_status_endpoint():
    response = client.get("/api/status")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
