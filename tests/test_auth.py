from tms import auth_app
from fastapi.testclient import TestClient


tmp_client = TestClient(auth_app)


def test_healthcheck():
    assert tmp_client.get("/healthcheck").status_code == 200


def test_app():
    assert tmp_client.get("/").json() == {"msg": "auth_service"}


if __name__ == "__main__":
    test_healthcheck()
    test_app()
