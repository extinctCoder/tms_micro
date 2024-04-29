import uvicorn
from fastapi import FastAPI, Response
from utils import latest_tag  # type: ignore

app_title = "User Service"
app_description = (
    "User related entrypoints of simple task management system Micro Service backend."
)

app_contact = {
    "name": "Sabbir Ahmed Shourov",
    "url": "https://www.github.com/extinctCoder",
    "email": "write2shourov@gmail.com",
}

app = FastAPI(
    title=app_title,
    description=app_description,
    version=latest_tag(),
    contact=app_contact,
)


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
        dict: A dictionary with a message key indicating the user service.
    """
    return {"msg": "user_service"}


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
