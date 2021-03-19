"""Forms for "create_blog" application."""
# Django
from django import forms


class TestForm(forms.Form):
    """Class for the application "create_blog."""

    name = forms.CharField(label='Name')
    email = forms.CharField(label='Email')
    file = forms.FileField()
