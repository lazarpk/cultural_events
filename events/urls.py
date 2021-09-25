from django.urls import path
from .views import events, event, create, archive_event, delete_event_request

urlpatterns = [
    path ('events/', events, name = 'events'),
    path ('events/create/', create, name = 'create'),
    path ('events/<int:id>', event, name = 'event'),
    path ('events/<int:id>/archive', archive_event, name = 'event'),
    path ('events/<int:id>/delete', delete_event_request, name = 'event'),
]