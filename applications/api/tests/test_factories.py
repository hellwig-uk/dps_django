"""
The test for factory, it mainly is there for a smoke test.
"""

from django.test import TestCase

from . import factories


class TestFactory(TestCase):
    def test_01_user(self):
        user_1 = factories.User()
        user_2 = factories.User()
        self.assertEqual(user_1.username, factories.USERNAME_CU)
        self.assertNotEqual(user_2.username, factories.USERNAME_CU)
        self.assertIn(
            factories.USERNAME_CU,
            user_2.username,
        )

    def test_02_superuser(self):
        superuser = factories.SuperUser()
        self.assertIn(factories.USERNAME_SU, superuser.username)
