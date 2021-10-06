from django.contrib import admin
from .models import Profile, StreetAddress, City, WorkArea


# Register your models here.
admin.site.register(Profile)
admin.site.register(StreetAddress)
admin.site.register(City)
admin.site.register(WorkArea)