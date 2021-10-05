from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.utils import timezone

from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required

# Create your views here.
from .models import Events, EventDeleteRequest, CategoryEvents
from .forms import EventsForm


def index (request):
    events = Events.objects.filter (date_archived__isnull = True).order_by('time')[:10]
    dictValues = {}
    for event in events:
        eventItem = Events.objects.get(id=event.id)
        categories = eventItem.category.all()
        dictValues[event.id] = categories

    #return render (request, 'events/events.html', {'events' : events, 'values':dictValues })
    return render (request, 'events/index.html', {'events' : events})


@permission_required('events.event_can_create', '/login')
def create (request):
    if request.method == "GET":
        form = EventsForm()
        return render(request, 'events/create.html', {'form' : form})
    elif request.method == "POST":
        form = EventsForm(request.POST)

        if (form.is_valid()):
            event = form.save(commit = False)
            category = form.cleaned_data.get ('category')
            current_user = request.user
            event.author = current_user
            event.save()
            event.category.set(category)
            #return redirect ('events')

            return redirect ('index')
        else:

            return render (request, 'events/create.html', {'form' : form})

def event (request, *args, **kwargs):
    id = kwargs['id']
    event = Events.objects.get (pk = id)
    categories = event.category.all()

    if event is None:
        raise Http404
    else:
        return render (request, 'events/event.html', {'event': event, 'categories': categories})

def archive_event (request, *args, **kwargs):
    id = kwargs ['id']
    event = Events.objects.get (pk = id)

    if event is not None and event.date_archived is None and request.user.id == event.author.id:
        event.date_archived = timezone.now()
        event.save()
        message = 'Dogadjaj je arhiviran.'

        return render (request, 'events/request_success.html', {'success_message' : message})
    else:
        return HttpResponse(status = 400)

def delete_event_request (request, *args, **kwargs):
    id = kwargs ['id']
    event = Events.objects.get (pk = id)

    if event is not None and EventDeleteRequest.get_if_exists(event.id) is None and request.user.id == event.author.id:
        delete_event_request = EventDeleteRequest()
        delete_event_request.User = request.user
        delete_event_request.Event = event
        delete_event_request.save()
        message = 'Zahtev za brisanje dogadjaja je poslat administratoru.'

        return render (request, 'events/request_success.html', {'success_message' : message})
    else:
        return HttpResponse (status = 400)

def delete_request_admin(request):
    queryset = EventDeleteRequest.objects.all();
    if not queryset:
        message = 'Nema novih zahteva za brisanje.'
        return render (request, 'events/request_success.html', {'success_message' : message})
    else:
        context = {
            'object_list':queryset
        }

        return render(request, 'events/delete_request.html',context);


def delete_event(request, id):
    obj = EventDeleteRequest.objects.get(Event_id = id)
    obj2 = Events.objects.get(pk=id)
    obj.delete()
    obj2.delete()
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)
