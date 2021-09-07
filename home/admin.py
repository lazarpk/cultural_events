from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Permission
from home.models import Category, Article, ArticleDeletionRequest

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(ArticleDeletionRequest)
admin.site.register(Permission)
