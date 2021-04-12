"""The MultiStepFormModel application models are registered here."""

# Django
from django.contrib import admin

# Project
from blog.models import MultiStepsForm

admin.site.register(MultiStepsForm)
