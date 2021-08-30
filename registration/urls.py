from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration, name = 'registration'),
    path('reg_guest/', views.register, name = 'reg_guest'),
    path('reg_org/', views.register_org, name = 'reg_org'),
]