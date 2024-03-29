"""Models for the "create_blog" application."""

# Django
from django.db import models


class MultiStepsForm(models.Model):
    """A class for MultiStepForm in "blog" application."""

    blog_name = models.CharField(max_length=255, null=True, unique=True)
    description = models.CharField(max_length=255)
    topic = models.CharField(max_length=255, null=True)
    twitter = models.CharField(max_length=255, null=True)
    facebook = models.CharField(max_length=255, null=True)
    instagram = models.CharField(max_length=255, null=True)
    pinterest = models.CharField(max_length=255, null=True)
    image1 = models.ImageField(null=True, upload_to='media')
    image2 = models.ImageField(null=True, upload_to='media')
