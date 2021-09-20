from django.db import models

# Create your models here.
class Adverts ( models.Model):
    title = models.CharField( max_length=32);
    description = models.TextField();
    date_time_load = models.DateTimeField();
    date_time_expire = models.DateTimeField();
    archived = models.Choices ('archived', 'YES NO');
