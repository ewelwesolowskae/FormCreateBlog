"""URL for blog application."""
# Django
from django.urls import path

# Project
from blog.views import IndexView
from blog.views import multistepformexample_save

urlpatterns = [
    path('multistepformexample/', IndexView.as_view(), name='multistepformexample'),
    path('multistepformexample/', multistepformexample_save, name='multistepformexample'),
    path('multistepformexample_save/', multistepformexample_save,
         name='multistepformexample_save'),

 ]
