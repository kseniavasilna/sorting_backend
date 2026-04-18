import pytest
from main import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_sort_endpoint(client):
    payload = {
        "values": [{"value":"green", "meta":"a"},
                   {"value":"red", "meta":"b"},
                   {"value":"blue", "meta":"c"}],
        "order_rule": {"red": "0", "blue": "1", "green": "2"}
    }

    response = client.post("/sort", json=payload)

    assert response.status_code == 200
    data = response.get_json()

    assert data["sorted"] == [{"value":"red", "meta":"b"}, {"value":"blue", "meta":"c"}, {"value":"green", "meta":"a"}]

def test_sort_empty_request(client):
    response = client.post("/sort", json={})

    assert response.status_code == 200
    assert response.get_json()["sorted"] == []


def test_sort_missing_values(client):
    payload = {"order_rule": {"red": "0"}}

    response = client.post("/sort", json=payload)

    assert response.status_code == 200
    assert response.get_json()["sorted"] == []