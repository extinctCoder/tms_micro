import uvicorn
from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/healthcheck")
def healthcheck():
    """
    Endpoint for health check.

    Returns:
        Response: A Response object with status code 200 indicating successful health check.
    """
    return Response(status_code=200)


@app.get("/")
def root_api():
    """
    Root API endpoint.

    Returns:
        dict: A dictionary with a message key indicating the auth service.
    """
    return {"msg": "auth_service"}


if __name__ == "__main__":
    """
    Entry point for running the FastAPI server.
    Starts the FastAPI server using Uvicorn with the specified host and port.

    Usage:
        Run this module directly to start the FastAPI server:
        ```
        python main.py
        ```

    Note:
        The FastAPI server will be accessible at the specified host and port.

    """
    uvicorn.run(app, host="0.0.0.0", port=8000)
