from fastapi.testclient import TestClient

from ifconfig.app import app


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "HOST": None,
        "REMOTE_ADDR": None,
    }


def test_root_with_single_params():
    response = client.get("/REMOTE_ADDR")
    assert response.status_code == 200
    assert response.json() == {
        "REMOTE_ADDR": None,
    }


def test_root_with_multiple_params():
    response = client.get("/HOST+REMOTE_ADDR")
    assert response.status_code == 200
    assert response.json() == {
        "HOST": None,
        "REMOTE_ADDR": None,
    }


def test_root_with_unknown_params():
    response = client.get("/UNKNOWN")
    assert response.status_code == 404
