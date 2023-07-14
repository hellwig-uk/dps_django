"""
Test viewset, this is also just a smoke test.
"""

from django.contrib import admin
from django.contrib.auth import models
from django.contrib.auth.apps import AuthConfig
from django.test import TestCase

from ..common.admin import register_models_by_appconfig


class TestAdmin(TestCase):
    def test_register(self):
        for model in [models.Group, models.User, models.Permission]:
            try:
                admin.site.unregister(model)
            except admin.sites.NotRegistered:  # pragma: no cover
                pass

        register_models_by_appconfig(AuthConfig)
