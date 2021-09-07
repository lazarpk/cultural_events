from django.urls import path
from .views import details
from .views import edit
urlpatterns = [
    path('', details, name = 'profile'),
    path('edit/', edit, name='edit'),
]