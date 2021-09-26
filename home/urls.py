from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.aboutUs, name='about-us'),
    path("contact/", views.contact, name='contact'),
    path("guide/", views.guide, name='guide'),
]