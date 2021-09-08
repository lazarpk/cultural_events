from django.shortcuts import render

# Create your views here.
from .models import Events

def index (request):
    events = Events.objects.all ()
    context = {
        'events' : events
    }
    return render (request, 'events/index.html', context)

def create (request):
    return render(request, 'events/create.html')
