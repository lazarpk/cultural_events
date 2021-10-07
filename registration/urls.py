from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration, name = 'registration'),
    path('reg_guest/', views.register, name = 'reg_guest'),
    path('reg_org/', views.register_org, name = 'reg_org'),
    path('categories-events-new', views.AddEventsCategory, name='categories-events-new'),
    path('categories-news-new', views.AddNewsCategory, name='categories-news-new'),
    path('workareas-new', views.AddWorkArea, name='workareas-new'),
    path('spacecharacteristics-new', views.AddSpaceCharacteristic, name='spacecharacteristics-new')
]