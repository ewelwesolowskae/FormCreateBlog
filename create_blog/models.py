"""Models for the "create_blog" application."""

# Django
from django.db import models


class MultiStepFormModel(models.Model):
    """A class for MultiStepForm in "create_blog" application."""

    blog_name = models.CharField(max_length=255, null=True, unique=True)
    description = models.CharField(max_length=255)
    test = models.CharField(max_length=255, null=True)
    twitter = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    pinterest = models.CharField(max_length=255)
    image11 = models.ImageField(null=True, upload_to='media')
    image12 = models.ImageField(null=True)
