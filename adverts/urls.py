from django.urls import path;

from .views import index;
from .views import create;
from .views import edit;
from .views import archive_advert;
from .views import delete_advert_request;
from .views import delete_request_admin;
from .views import delete_advert;



urlpatterns = [
    path ('', index, name = 'index'),
    path ('create/', create, name = 'create' ),
    path ('edit/', edit, name = 'edit'),
    path ('<int:id>/archive', archive_advert, name = 'advert'),
    path ('<int:id>/delete', delete_advert_request, name = 'advert'),
    path ('delete_request/', delete_request_admin, name = 'delete_request_admin'),
    path('delete_request/<int:id>/', delete_advert, name = 'delete_advert'),
    ]