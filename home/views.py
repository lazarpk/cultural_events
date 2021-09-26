from datetime import datetime

from django.utils import timezone

from django.http import Http404
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from registration.models import Profile
from django.contrib.auth.decorators import permission_required

# Create your views here.


def index(request):
    return render(request, "index.html")

def aboutUs (request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact.html')

def guide(request):
    return render(request, 'guide.html')
