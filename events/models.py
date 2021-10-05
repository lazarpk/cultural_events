from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

#SIFARNICI:


class CategoryEvents (models.Model):
    name = models.CharField(max_length=100)
    valid_from = models.DateField(null = True, blank = False)
    valid_to = models.DateField(null = True, blank = False)
    approved = models.BooleanField(default = False)
    status = models.BooleanField(default=True)

    @staticmethod
    def get_active():
        data = CategoryEvents.objects.filter(status = True, approved = True).all()
        return data

    def __str__(self):
        return self.name


class Age (models.Model):
    name = models.CharField(max_length=20)
    valid_from = models.DateField(null=True, blank=False)
    valid_to = models.DateField(null=True, blank=False)
    approved = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    @staticmethod
    def get_active():
        data = Age.objects.filter(status=True, approved=True).all()
        return data


class SpaceCharacteristics(models.Model):
    name = models.CharField(max_length = 150, default = '')
    valid_from = models.DateField(null=True, blank=False)
    valid_to = models.DateField(null=True, blank=False)
    approved = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    @staticmethod
    def get_active():
        data = SpaceCharacteristics.objects.filter(status=True, approved=True).all()
        return data


#TODO: dodati ovako i za ostale sifarnike vezane za dogadjaje



class Events (models.Model):
    event_name = models.CharField (max_length = 50, default = '');
    text = models.CharField (max_length = 200, default = '');
    category = models.ManyToManyField(CategoryEvents, verbose_name="kategorija");
    place = models.CharField (max_length = 30, default = '');
    time = models.DateTimeField(null = True, blank = True);
    age = models.ManyToManyField(Age, verbose_name="starosna doba posetilaca");
    space_characteristics = models.ManyToManyField(SpaceCharacteristics, verbose_name="karakteristike prostora");
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






