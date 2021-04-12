"""Forms for "create_blog" application."""

# Django
from django import forms

# Local
from .models import MultiStepsForm


class PostyForm(forms.ModelForm):
    """A class built from the MultiStepFormModel model."""

    class Meta:
        """Meta class for the MultiStepFormModel model."""

        model = MultiStepsForm
        fields = '__all__'