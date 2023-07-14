import dj_database_url
import importlib
import os

ENVIRONMENT = os.environ.get("ENV", "MAIN")
SETTINGS = importlib.import_module(f"_django.settings.{ENVIRONMENT}")
globals().update(SETTINGS.__dict__)

if not os.environ.get("DATABASE_URL", False):
    os.environ["DATABASE_URL"] = "sqlite:///db.sqlite3"

DATABASES = {
    "default": dj_database_url.config(conn_max_age=600),
}
