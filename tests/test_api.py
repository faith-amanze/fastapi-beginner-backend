from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_returns_status_version_and_timestamp():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["version"] == "1.0.0"
    assert "timestamp" in data

def test_chat_valid_request():
    response = client.post("/chat", json={"message": "Hello"})
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["answer"] == "You said: Hello"

def test_chat_rejects_empty_message():
    response = client.post("/chat", json={"message": ""})
    assert response.status_code == 422
