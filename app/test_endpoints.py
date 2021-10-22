from app.main import app
from fastapi.testclient import TestClient

Client = TestClient(app)


def test_get_home():
    response = Client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_post_home():
    response = Client.post("/")
    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]
