from django.urls import path;

from .views import index;
from .views import results;
from .views import vote;

from .views import create




urlpatterns = [
    path ('', index, name = 'index'),
    path('create/', create, name = 'create'),
    path('<int:id>/results/', results, name='results'),
    path('<int:id>/vote/', vote, name='vote'),
]