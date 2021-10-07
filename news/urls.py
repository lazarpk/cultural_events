from django.urls import path
from . import views

urlpatterns = [
    path('#', views.index, name="index"),
    path('articles/', views.articles, name="articles"),
    path('create_article/', views.article_new, name="article_new"),
    path('<int:id>', views.article, name="article"),
    path('<int:id>/archive', views.article_archive, name="article_archive"),
    path('articles/<int:id>/delete', views.article_create_delete_request, name="article_delete_request"),
    path ('administration/delete_request/', views.delete_request_admin, name = 'delete_request_admin'),
    path ('delete_request/<int:id>', views.delete_news, name = 'delete_news'),

]