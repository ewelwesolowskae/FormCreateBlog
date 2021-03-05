"""Accounts models."""
# Django
from django.contrib.auth.models import AbstractUser
# from django.db import models


class CustomUser(AbstractUser):
    """Extended CustomUser."""

    def __str__(self):  # noqa: D105
        return self.username

    def username_test(self, id):
        """
        
        """