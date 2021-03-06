from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AboutUs (models.Model):
    content1 = models.TextField()
    content2 = models.TextField()
from django.db import models

'''
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email

''''''

class Category(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return 'Category: ' + self.Name


class Article(models.Model):
    Title = models.CharField(max_length=250, verbose_name="Naslov vesti")
    Content = models.TextField(verbose_name="Tekst vesti")
    Category = models.ManyToManyField(Category, verbose_name="Kategorija")
    CreationDate = models.DateTimeField(auto_now_add=True, blank=True)
    ArchivedDate = models.DateTimeField(null=True, blank=True)
    UpdateDate = models.DateTimeField(null=True, blank=True)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("article_can_create", "Can create article"),
            ("article_edit", "Can edit article"),
            ("article_can_archive", "Can archive article"),
            ("article_can_delete", "Can delete article"),
        ]


class ArticleDeletionRequest(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Article = models.ForeignKey(Article, on_delete=models.CASCADE)
    Reason = models.TextField()
    Date = models.DateTimeField(auto_now_add=True, blank=True)

    @staticmethod
    def get_if_exists(article_id):
        try:
            request = ArticleDeletionRequest.objects.get(Article=article_id) is not None
            return request
        except ObjectDoesNotExist:
            return None
'''
