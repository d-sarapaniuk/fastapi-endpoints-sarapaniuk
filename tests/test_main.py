from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_sum():
    response = client.post("/sum", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5}
    
def test_repeat():
    response = client.post("/repeat", json={"text": "hi", "times": 3})
    assert response.status_code == 200
    assert response.json() == {"result": "hihihi"}
    
def test_repeat_invalid_times():
    response = client.post("/repeat", json={"text": "hi", "times": 0})
    assert response.status_code == 422  # validation error