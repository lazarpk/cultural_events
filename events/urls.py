from django.urls import path
from .views import index, event, create, archive_event, delete_event_request, delete_request_admin, delete_event

urlpatterns = [
    path ('', index, name = 'index'),
    path ('create/', create, name = 'create'),
    path ('<int:id>', event, name = 'event'),
    path ('<int:id>/archive', archive_event, name = 'archive_event'),
    path ('<int:id>/delete', delete_event_request, name = 'delete_event_request'),
    path ('administration/delete_request/', delete_request_admin, name = 'delete_request_admin'),
    path ('delete_request/<int:id>', delete_event, name = 'delete_event')
]