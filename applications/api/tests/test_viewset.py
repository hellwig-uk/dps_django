"""
Test viewset, this is also just a smoke test.
"""
from django.test import TestCase

from ..common.viewsets import ModelViewSet


class TestViewSet(TestCase):
    def test_model_view_set(self):
        view_set = ModelViewSet()
        with self.assertRaises(AttributeError):
            view_set.get_queryset()
