import uvicorn
from fastapi import FastAPI, Response
from utils import latest_tag  # type: ignore

app_title = "Main Service"
app_description = (
    "Main entrypoint of simple task management system Micro Service backend."
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


@app.get("/healthcheck", status_code=200, tags=["healthcheck"])
def healthcheck():
    """Health Check Endpoint.

    Returns:
        Response: A FastAPI Response indicating the health status.
    """
    pass
    # return Response(status_code=200)


@app.get("/", tags=["service"])
def root():
    """
    Root API endpoint.

    Returns:
        dict: A dictionary with a message key indicating the main service.
    """
    return {"msg": "main_service"}


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

    # uvicorn.run(app, host="0.0.0.0", port=8001)
    import json

    from fastapi.openapi.utils import get_openapi

    with open("openapi.json", "w") as json_file:
        json.dump(
            get_openapi(
                title=app_title,
                description=app_description,
                version=latest_tag(),
                contact=app_contact,
                routes=app.routes,
            ),
            json_file,
            indent=2,
        )
