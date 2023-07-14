"""
Test the mangement command
"""
from django.core import management
from django.test import TestCase


class AddTestCase(TestCase):
    def test_01_add(self):
        management.call_command("add_test_data")
