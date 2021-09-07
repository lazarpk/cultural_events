from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('#', views.index, name="index"),
    path('novosti', views.news, name="Novosti"),
    path('articles/new', views.article_new, name="new_article"),
    path('articles/<int:id>', views.article, name="article"),
    path('articles/<int:id>/archive', views.article_archive, name="article"),
    path('articles/<int:id>/delete', views.article_create_delete_request, name="article"),

]