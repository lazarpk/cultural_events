from django.contrib import admin

# Register your models here.
from .models import Adverts, AdvertDeleteRequest;


admin.site.register (Adverts);
admin.site.register (AdvertDeleteRequest)

