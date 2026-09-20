from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_receive_data():
    response = client.post(
        "/data",
        json={
            "name": "temperature",
            "value": 72.5
        }
    )

    assert response.status_code == 200
    assert response.json() =={
        "name": "temperature",
        "value": 72.5
    }

def test_read_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() =={
        "message": "Nimbus Analytics is running!"
    }

def test_receive_data_invalid_value():
    response = client.post(
        "/data",
        json={
            "name": "temperature",
            "value": "hello"
        }
    )

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", "value"]