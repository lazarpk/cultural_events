from django.contrib import admin
from .models import Events, EventDeleteRequest
from django.contrib.auth.models import Permission

# Register your models here.

admin.site.register (Events)
admin.site.register (EventDeleteRequest)
#admin.site.register (Permission)