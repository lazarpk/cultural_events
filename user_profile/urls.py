from django.urls import path
from .views import details
urlpatterns = [
    path('', details, name = 'profile')
]