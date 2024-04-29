from main import app, app_contact, app_description, app_title  # type: ignore
from utils import api_doc  # type: ignore

if __name__ == "__main__":
    api_doc(
        app=app,
        app_title=app_title,
        app_description=app_description,
        app_contact=app_contact,
    )
