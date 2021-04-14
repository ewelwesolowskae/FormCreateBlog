"""Views for the "create_blog" application."""

# Django
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

# Local
from .models import MultiStepsForm


class BlogCreator(generic.ListView):
    """BlogCreator class in "blog" application."""

    template_name = 'multistepformexample.html'
    model = MultiStepsForm


class IndexView(generic.ListView):
    """IndexView class in "blog" application."""

    template_name = 'multistepformexample.html'
    model = MultiStepsForm


class DetailView(generic.DetailView):
    """DetailViews class in "blog" application."""

    model = MultiStepsForm
    template_name = 'multistepformexample.html'


def multistepformexample_save(request):
    """Save the data contained in the  "blog" application."""
    if request.method == 'POST':
        blog_name = request.POST.get('blog_name')
        description = request.POST.get('description')
        topic = request.POST.get('topic')
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
                                           topic=topic, twitter=twitter, facebook=facebook,
                                           instagram=instagram, pinterest=pinterest,
                                           image1=image1, image2=image2)
            try:
                MultiStepsForm.objects.get(blog_name=blog_name)
                messages.error(request, 'Wpisałeś nazwę bloga który już istnieje.')

            except MultiStepsForm.DoesNotExist:
                multistepform.save()
                messages.success(request, 'Stworzyłeś blog!')
    return HttpResponseRedirect(reverse('multistepformexample'))
