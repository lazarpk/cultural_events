from django.urls import path;

from .views import index;
from .views import create;
from .views import edit;
from .views import archive_advert;
from .views import delete_advert_request;

urlpatterns = [
    path ('', index, name = 'index'),
    path ('create/', create, name = 'create' ),
    path ('edit/', edit, name = 'edit'),
    path ('<int:id>/archive', archive_advert, name = 'advert'),
    path ('<int:id>/delete', delete_advert_request, name = 'advert'),
]