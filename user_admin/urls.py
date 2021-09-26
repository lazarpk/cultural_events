from django.urls import path
from . import views


urlpatterns = [
    path ('', views.index, name = 'index-admin' ),
    path('search-users/', views.search, name="search-users"),
    path('edit-users/', views.editUsers, name='edit-users'),
    path('categories-news', views.newsCategories, name='categories-news'),
    path('categories-news-edit/', views.newsCategoriesEdit, name='categories-news-edit'),
    path('categories-events', views.eventsCategories, name='categories-events'),
    path('categories-events-edit/', views.eventsCategoriesEdit, name='categories-events-edit'),
]