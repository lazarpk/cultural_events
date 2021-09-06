from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from registration.models import Profile

# Create your views here.
def index(request):
    #print(request.user.id)
    #user = Profile.objects.get(user_id=request.user.id)
    #print (user.city)
    return render(request, "index.html")