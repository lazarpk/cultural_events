from django.urls import path
from .views import details
from .views import edit
from .views import searchOrg
urlpatterns = [
    path('', details, name = 'profile'),
    path('edit/', edit, name='edit'),
    path('search-organisations', searchOrg, name='search-org')
]