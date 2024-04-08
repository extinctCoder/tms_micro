from .main import app as main_app
from fastapi.testclient import TestClient


tmp_client = TestClient(main_app)


def test_healthcheck():
    assert tmp_client.get("/healthcheck").status_code == 200


def test_app():
    assert tmp_client.get("/").json() == {"msg": "main_service"}


if __name__ == "__main__":
    test_healthcheck()
    test_app()
