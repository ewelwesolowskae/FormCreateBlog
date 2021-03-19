"""Views for the "create_blog" application."""
# Django
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def multistepformexample(request):
    """Download the data contained in the  "create_blog" application."""
    return render(request, 'multistepformexample.html')


def multistepformexample_save(request):
    """Save the data contained in the  "create_blog" application."""
    if request.method == 'POST':
        # bname = request.POST.get('bname')
        # description = request.POST.get('description')
        # twitter = request.POST.get('twitter')
        # facebook = request.POST.get('facebook')
        # instagram = request.POST.get('instagram')
        # pinterest = request.POST.get('pinterest')
        messages.error(request, 'Error in Saving Data')
        return HttpResponseRedirect(reverse('multistepformexample'))
        #     multistepform.save()
        #     messages.success(request, "Data Save Successfully")
        #     return HttpResponseRedirect(reverse('multistepformexample'))
        # except ImportWarning:
        #     messages.error(request, "Error in Saving Data")
        #     return HttpResponseRedirect(reverse('multistepformexample'))
    else:
        return HttpResponseRedirect(reverse('multistepformexample'))
