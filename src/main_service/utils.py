import json
from os import environ, path
from pathlib import Path

from fastapi.openapi.utils import get_openapi


def api_doc(app, app_title, app_description, app_contact):
    service_dir = Path(__file__).resolve().parent
    service_name = path.basename(service_dir)
    docs_dir = service_dir.parent.parent.joinpath("docs")
    with open(
        "{}/openapi.{}.json".format(str(docs_dir), service_name), "w"
    ) as json_file:
        json.dump(
            get_openapi(
                title=app_title,
                description=app_description,
                version=environ.get("LATEST_TAG", "v0.0.0"),
                contact=app_contact,
                routes=app.routes,
            ),
            json_file,
            indent=2,
        )


if __name__ == "__main__":
    print("Latest TAG is : {}".format(environ.get("LATEST_TAG", "v0.0.0")))
