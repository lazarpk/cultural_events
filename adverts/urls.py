from django.urls import path;

from .views import index;
from .views import create;
from .views import edit;

urlpatterns = [
    path ('', index, name = 'index'),
    path ('create/', create, name = 'create' ),
    path ('edit/', edit, name = 'edit')
]