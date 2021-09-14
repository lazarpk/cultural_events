from django.db import models
from django.utils import timezone

# Create your models here.
class Events (models.Model):
    event_name = models.CharField (max_length = 50, default = '');
    text = models.CharField (max_length = 200, default = '');
    type = models.CharField (max_length = 30, default = '');
    place = models.CharField (max_length = 30, default = '');
    time = models.DateTimeField(default = timezone.now);
    age = models.IntegerField(default = False);
    space_characteristics = models.CharField(max_length = 150, default = '');
    date_published = models.DateTimeField (default = timezone.now);
    expiration_date = models.DateTimeField(default = timezone.now);
    author = models.CharField (max_length = 30, default = '');
    archive = models.CharField (max_length = 1, default = 'N');
    delete = models.CharField (max_length = 1, default = 'N');







