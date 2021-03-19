"""Dockstring in ViewClassForm."""
# Django
from django.shortcuts import render
from django.views import View

# Project
from create_blog.forms import TestForm


class ViewClassForm(View):
    """Dockstring  for ViewClassForm."""

    def get(self, request, *args, **kwargs):
        """Dockstring  for get."""
        form = TestForm()
        return render(request, 'testform.html', {'form': form})

    def post(self, request, *args, **kwargs):
        """Dockstring  for post."""
        pass
