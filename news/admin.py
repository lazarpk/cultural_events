from django.contrib import admin
from .models import Article, Category, ArticleDeletionRequest
from django.contrib.auth.models import Permission
# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(ArticleDeletionRequest)
admin.site.register(Permission)