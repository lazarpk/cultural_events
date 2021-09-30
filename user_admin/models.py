from django.db import models

# Create your models here.
class Reports (models.Model):
    title = models.CharField(max_length=200)
    date_from = models.DateField()
    date_to = models.DateField()
    num_users = models.IntegerField()
    num_events = models.IntegerField()
    num_adverts = models.IntegerField()
    num_articles = models.IntegerField()