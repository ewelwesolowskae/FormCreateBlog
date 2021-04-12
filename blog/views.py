"""Views for the "create_blog" application."""

# Django
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView

# Local
from .models import MultiStepsForm


class Form(forms.Form):
    """Form class in "blog" application."""

    class Meta:
        """Meta class for "blog application."""

        model = MultiStepsForm


class BlogCreator(ListView):
    """BlogCreator class in "blog" application."""

    template_name = 'multistepformexample.html'

    model = MultiStepsForm


class IndexView(generic.ListView):
    """IndexView class in "blog" application."""

    template_name = 'multistepformexample.html'

    def get_queryset(self):
        """Return all objects from the MultiStepForm model."""
        return MultiStepsForm.objects.all()


class DetailView(generic.DetailView):
    """DetailViews class in "blog" application."""

    model = MultiStepsForm
    template_name = 'multistepformexample.html'


class MultiStepFormExample(generic.ListView):
    """Class for MultiStepForm in "blog" application."""

    def multistepformexample(request):  # noqa: D105
        """Download the data contained in the  "blog" application."""
        return render(request, 'multistepformexample.html')


def multistepformexample_save(request):
    """Save the data contained in the  "blog" application."""
    if request.method == 'POST':
        blog_name = request.POST.get('blog_name')
        description = request.POST.get('description')
        subject = request.POST.get('subject')
        twitter = request.POST.get('twitter')
        facebook = request.POST.get('facebook')
        instagram = request.POST.get('instagram')
        pinterest = request.POST.get('pinterest')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        if blog_name == '':
            messages.error(request, 'Nie podałeś nazwy Twojego bloga.')
        else:
            multistepform = MultiStepsForm(blog_name=blog_name, description=description,
                                           test=subject, twitter=twitter, facebook=facebook,
                                           instagram=instagram, pinterest=pinterest,
                                           image11=image1, image12=image2)
            try:
                MultiStepsForm.objects.get(blog_name=blog_name)
                messages.error(request, 'Wpisałeś nazwę bloga który już istnieje.')

            except MultiStepsForm.DoesNotExist:
                multistepform.save()
                messages.success(request, 'Stworzyłeś blog!')
    return HttpResponseRedirect(reverse('multistepformexample'))
