from django.urls import path
from .views import events, event, create, archive_event, delete_event_request

urlpatterns = [
    path ('events/', events, name = 'events'),
    path ('create/', create, name = 'create'),
    path ('event/<int:it>', event, name = 'event'),
    path ('events/<int:it>/archive', archive_event, name = 'event'),
    path ('events/<int:it>/delete', delete_event_request, name = 'event'),
]