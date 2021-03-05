"""Accounts models."""
# Django
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Extended CustomUser."""

    def __str__(self):  # noqa: D105
        return self.username
