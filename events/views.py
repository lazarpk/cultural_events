from django.shortcuts import render

# Create your views here.
from .models import Events
from .forms import EventsForm

def index (request):
    events = Events.objects.all ()
    context = {
        'events' : events
    }
    return render (request, 'events/index.html', context)

def create (request):
    form = EventsForm()
    context = {
        "form" : form
    }
    return render(request, 'events/create.html', context)
