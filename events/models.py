from django.db import models

# Create your models here.
class Events (models.Model):
    event_name = models.CharField(max_length=50)
