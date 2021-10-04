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
    #print(request.user.id)
    #user = Profile.objects.get(user_id=request.user.id)
    #print (user.city)
    return render(request, "index.html")


    #return render(request, "index.html")
