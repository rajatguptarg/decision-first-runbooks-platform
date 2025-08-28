from fastapi.testclient import TestClient

from backend.app import app

client = TestClient(app)


def test_health_check():
    """Tests the /health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "ok": True,
        "data": {
            "status": "healthy",
            "service": "decision-first-runbooks-api",
            "version": "1.0.0",
        },
    }


def test_root():
    """Tests the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Decision First Runbooks API is running!"}
