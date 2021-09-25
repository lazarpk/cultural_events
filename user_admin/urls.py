from django.urls import path
from . import views


urlpatterns = [
    path ('', views.index, name = 'index-admin' ),
    path('search-users/', views.search, name="search-users"),
    path('edit-users/', views.editUsers, name='edit-users'),
]