from django.urls import path
from .views import index
from .views import create

urlpatterns = [
    path ('', index, name = 'events'),
    path ('create/', create, name = 'create')
]