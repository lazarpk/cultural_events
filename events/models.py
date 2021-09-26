from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
class CategoryEvents (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Events (models.Model):
    event_name = models.CharField (max_length = 50, default = '');
    text = models.CharField (max_length = 200, default = '');
    category = models.ManyToManyField(CategoryEvents, verbose_name="kategorija");
    place = models.CharField (max_length = 30, default = '');
    time = models.DateTimeField(null = True, blank = True);
    age = models.IntegerField(default = False);
    space_characteristics = models.CharField(max_length = 150, default = '');
    date_published = models.DateTimeField (auto_now_add = True, blank = True);
    expiration_date = models.DateTimeField(null = True, blank = True);
    author = models.ForeignKey (User, on_delete = models.CASCADE);
    date_archived = models.DateTimeField (null = True, blank = True);


    class Meta:
        permissions = [
            ('event_can_create', 'Can create event'),
            ('event_edit', 'Can edit event'),
            ('event_can_archive', 'Can archive event'),
            ('event_can_delete', 'Can delete event'),
        ]

class EventDeleteRequest (models.Model):
    User = models.ForeignKey(User, on_delete = models.CASCADE)
    Event = models.ForeignKey(Events, on_delete = models.CASCADE)
    Date = models.DateTimeField(auto_now_add = True, blank = True)

    @staticmethod
    def get_if_exists (event_id):
        try:
            request = EventDeleteRequest.objects.get(Event = event_id) is not None
            return request
        except ObjectDoesNotExist:
            return None






