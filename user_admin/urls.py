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
    path('statistics/', views.statistics, name='statistics'),
    path('statistics-user/', views.statisticsUser, name='statistics-user'),
    path('about-us-edit/', views.aboutUsEdit, name='about-us-edit'),
    path('reports', views.reports, name='reports'),
    path('codebooks-edit/', views.codebooksEdit, name='codebooks-edit'),
    path('workareas/', views.workArea, name='workareas'),
    path('workareas-edit', views.workAreaEdit, name='workareas-edit'),
    path('spacecharacteristics', views.spaceCharacteristic, name='spacecharacteristics'),
    path('spacecharacteristics-edit', views.spaceCharacteristicsEdit, name='spacecharacteristics-edit'),
    path('categories-events-delete/', views.eventsCategoriesDelete, name='categories-events-delete'),
    path('categories-news-delete/', views.newsCategoriesDelete, name='categories-news-delete'),
    path('workareas-delete', views.workAreaDelete, name='workareas-delete'),
    path('spacecharacteristics-delete', views.spaceCharacteristicsDelete, name='spacecharacteristics-delete'),
    path('codebooks-requests/', views.codebooksRequests, name='codebooks-requests'),
    path('codebooks-requests/events', views.codebooksRequestsEvents, name='codebooks-requests-events'),
    path('codebooks-requests/events/approve/', views.codebooksRequestsEventsApprove ,name='codebooks-requests-events-approve')
]