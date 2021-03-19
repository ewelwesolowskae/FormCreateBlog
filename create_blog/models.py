"""Models for the "create_blog" application."""

# Django
from django.db import models


class MultiStepFormModel(models.Model):
    """A class for MultiStepForm in "create_blog" application."""

    # id = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255, blank=True)
    pinterest = models.CharField(max_length=255, blank=True)
    objects = models.Manager()
