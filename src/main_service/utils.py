import json
import subprocess
from os import path
from pathlib import Path

from fastapi.openapi.utils import get_openapi


def latest_tag():
    """
    Fetches the latest Git tag of the current project.

    Returns:
        str or None: The latest Git tag if found, None otherwise.
    """
    try:
        tag = (
            subprocess.check_output(["git", "describe", "--tags", "--abbrev=0"])
            .decode()
            .strip()
        )
        print("latest_tag".format(tag))
        return tag

    except subprocess.CalledProcessError:
        print("got error")
        return "v0.0.0"


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
                version=latest_tag(),
                contact=app_contact,
                routes=app.routes,
            ),
            json_file,
            indent=2,
        )


if __name__ == "__main__":
    print(latest_tag())
