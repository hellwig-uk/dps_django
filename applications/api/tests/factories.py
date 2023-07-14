"""
Factories for common purposes, such as adding a user to the system.
"""
from django.contrib.auth import models
from factory import Sequence, post_generation
from factory.django import DjangoModelFactory

from applications.api.common.environment import MAKE

USERNAME_SU = "su-" + MAKE["SYSTEMUSER_MAIL"]
USERNAME_CU = "cu-" + MAKE["SYSTEMUSER_MAIL"]
PASSWORD = MAKE["SYSTEMUSER_PASS"]


def sequence_user(sequence, username):
    if sequence == 0:
        return username

    return f"{sequence}-" + username


class User(DjangoModelFactory):
    class Meta:
        model = models.User

    username = Sequence(lambda n: sequence_user(n, USERNAME_CU))
    email = Sequence(lambda n: sequence_user(n, USERNAME_CU))

    @post_generation
    def _set_password(self, create, args):
        assert args is None
        assert create
        self.set_password(PASSWORD)  # pylint:disable=E1101 #  false positive


class SuperUser(User):
    username = Sequence(lambda n: sequence_user(n, USERNAME_SU))
    email = Sequence(lambda n: sequence_user(n, USERNAME_SU))
    is_staff = True
    is_superuser = True
