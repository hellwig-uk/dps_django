"""
Test views
"""
import os
import tempfile
from pathlib import Path
from shutil import rmtree
from unittest.mock import patch

from django.http import FileResponse, HttpResponse, HttpResponseNotFound
from django.test import TestCase
from django.urls import reverse

from .. import views


class TestDeveloperServer(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = tempfile.mkdtemp()
        cls.indexed_folder = os.path.join(cls.base, "with_index")
        os.makedirs(cls.indexed_folder)

        path_index = os.path.join(cls.indexed_folder, "index.html")
        with open(path_index, "w", encoding="utf8"):
            pass

        path_test = os.path.join(cls.base, "test.html")
        with open(path_test, "w", encoding="utf8"):
            pass

        return super(TestDeveloperServer, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        rmtree(cls.base)
        super(TestDeveloperServer, cls).tearDownClass()

    def test_get(self):
        request = type("request", (object,), {})
        with patch(
            "applications.api.views.settings.STATIC_ROOT",
            Path(self.indexed_folder),
        ):
            view = views.DeveloperServer()

            # expect a 404
            request.path = "/does-not-exist"
            returns = view.get(request)
            self.assertIsInstance(returns, HttpResponseNotFound)

            # expect a directory listing
            request.path = "/"
            returns = view.get(request)
            self.assertIsInstance(returns, HttpResponse)

            # expect a file response
            request.path = "/test.html"
            returns = view.get(request)
            self.assertIsInstance(returns, FileResponse)

            # expect a file response
            request.path = "/with_index"
            returns = view.get(request)
            self.assertIsInstance(returns, FileResponse)


class TestApiRootIndex(TestCase):
    url = reverse("api")

    def test_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("auth_urls", response.context)
        self.assertIn("app_urls", response.context)

    def test_get_context_data(self):
        patterns = [type("url", (object,), {"app_name": "a.b", "pattern": ""})]
        api_root_index = views.APIRootIndex(patterns=patterns)

        api_root_index.get_context_data()
