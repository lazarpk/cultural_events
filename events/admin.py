from django.contrib import admin
from .models import Events, EventDeleteRequest, CategoryEvents, Age, SpaceCharacteristics
from django.contrib.auth.models import Permission

# Register your models here.

admin.site.register (Events)
admin.site.register (EventDeleteRequest)
admin.site.register (CategoryEvents)
#admin.site.register (Permission)
admin.site.register (Age)
admin.site.register (SpaceCharacteristics)