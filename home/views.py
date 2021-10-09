from datetime import datetime

from django.utils import timezone

from django.http import Http404
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User
from registration.models import Profile
from django.contrib.auth.decorators import permission_required
from .forms import AboutUsForm
from .models import AboutUs
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.


def index(request):
    return render(request, "index.html")
'''
def aboutUs (request):
    obj = AboutUs.objects.last()
    context = {
        'obj': obj
    }
    return render(request, 'about-us.html', context)
'''
def guide(request):
    return render(request, "user-guide.html")

def about_us(request):
    obj = AboutUs.objects.last()
    context = {
        'obj': obj
    }
    return render(request, "about-us.html", context)

def sendMail(request):
    messageSent = False
    if request.method == 'POST':

        form = EmailForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            subject = cd['name'] + ' - ' + cd['subject']
            message = cd['message']
            from_email = cd['email']

            # send the email to the recipent
            send_mail(subject, message,
                      from_email, ['gordanad2@msn.com'])

            # set the variable initially created to True
            messageSent = True

    else:
        form = EmailForm()

    return render(request, 'contact.html', {

        'form': form,
        'messageSent': messageSent,

    })
