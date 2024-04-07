import uvicorn
from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/healthcheck")
def healthcheck():
    return Response(status_code=200)


@app.get("/")
def root_api():
    return {"msg": "auth_service"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
