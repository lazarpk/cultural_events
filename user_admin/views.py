from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
# Create your views here.
def index (request):
    curently_user = User.objects.get(id=request.user.id)
    if curently_user.is_superuser:
        return render(request, 'index-admin.html')
    else:
        raise Http404