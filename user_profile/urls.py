from django.urls import path
from .views import details
from .views import edit
from .views import searchOrg
from . views import profileUser
from .views import codebooksEdit
from .views import eventsCategoriesOrg
from .views import newsCategoriesOrg
from .views import workAreaOrg
from .views import spaceCharacteristicOrg
urlpatterns = [
    path('', details, name = 'profile'),
    path('edit/', edit, name='edit'),
    path('search-organisations', searchOrg, name='search-org'),
    path('user/', profileUser, name='profileUser'),
    path('codebooks-edit-org', codebooksEdit, name='codebooks-edit-org'),
    path('categories-events', eventsCategoriesOrg, name='categories-events-org'),
    path('categories-news', newsCategoriesOrg, name='categories-news-org'),
    path('workareas', workAreaOrg, name='workareas-org'),
    path('spacecharacteristics', spaceCharacteristicOrg,name='spacecharacteristics-org')
]