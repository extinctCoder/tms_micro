from fastapi.testclient import TestClient

from .main import app as user_app

tmp_client = TestClient(user_app)


def test_healthcheck():
    """
    Test Health Check

    This function tests the health check endpoint to ensure the server is running properly.
    """
    assert tmp_client.get("/healthcheck").status_code == 200


def test_app():
    """
    Test Application Root

    This function tests the root endpoint of the application to ensure it returns the expected JSON response.
    """
    assert tmp_client.get("/").json() == {"msg": "user_service"}


if __name__ == "__main__":
    test_healthcheck()
    test_app()
