"""Views for the "create_blog" application."""

# Django
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Local
from .models import MultiStepFormModel


def multistepformexample(request):
    """Download the data contained in the  "create_blog" application."""
    return render(request, 'multistepformexample.html')


def multistepformexample_save(request):
    """Save the data contained in the  "create_blog" application."""
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('multistepformexample'))
    else:
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
            return HttpResponseRedirect(reverse('multistepformexample'))
        else:
            multistepform = MultiStepFormModel(blog_name=blog_name, description=description,
                                               test=subject, twitter=twitter, facebook=facebook,
                                               instagram=instagram, pinterest=pinterest,
                                               image11=image1, image12=image2)
            try:
                MultiStepFormModel.objects.get(blog_name=blog_name)
                messages.error(request, 'Wpisałeś nazwę bloga który już istnieje.')
                return HttpResponseRedirect(reverse('multistepformexample'))
            except MultiStepFormModel.DoesNotExist:
                multistepform.save()
                messages.success(request, 'Stworzyłeś blog!')
                return HttpResponseRedirect(reverse('multistepformexample'))
