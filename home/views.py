from datetime import datetime

from django.utils import timezone

from django.http import Http404
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User
from registration.models import Profile
from django.contrib.auth.decorators import permission_required
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.


def index(request):
    #print(request.user.id)
    #user = Profile.objects.get(user_id=request.user.id)
    #print (user.city)
    return render(request, "index.html")

def guide(request):
    return render(request, "user-guide.html")

def about_us(request):
    return render(request, "about-us.html")

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
