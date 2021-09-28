from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AboutUs (models.Model):
    content1 = models.TextField()
    content2 = models.TextField()
