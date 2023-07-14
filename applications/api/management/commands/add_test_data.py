"""
This goes through the applications and if they have a module tests.data and that
module has the function add, it will call it.
"""
import importlib
import os

from django.apps import apps
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        assert isinstance(args, tuple)
        assert isinstance(kwargs, dict)

        for config in apps.get_app_configs():  # pragma: no cover
            if not config.module.__name__.startswith("applications."):
                continue

            path = os.path.join(
                os.path.dirname(config.module.__file__),
                "tests",
                "data.py",
            )
            if not os.path.exists(path):
                continue

            dot_path = config.module.__name__ + ".tests.data"
            data = importlib.import_module(dot_path)
            if hasattr(data, "add"):
                data.add()
