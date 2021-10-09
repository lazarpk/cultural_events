from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.admin import User
from django.utils import timezone

# Create your models here.
class Adverts ( models.Model):
    title = models.CharField( max_length=32, verbose_name='Naslov');
    description = models.TextField(verbose_name="Opis oglasa");
    load_date = models.DateField(verbose_name="Datum postavljanja oglasa");
    expire_date = models.DateField(verbose_name='Datum isticanja oglasa');
    author = models.ForeignKey(User, on_delete=models.CASCADE, )
    date_archived = models.DateTimeField(null=True, blank=True);

    class Meta:
        permissions = [
            ('advert_can_create', 'Can create advert'),
            ('advert_edit', 'Can edit advert'),
            ('advert_can_archive', 'Can archive advert'),
            ('advert_can_delete', 'Can delete advert'),
        ]
    def __str__(self):
        return self.title

class AdvertDeleteRequest(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE,)
    Advert = models.ForeignKey(Adverts, on_delete=models.CASCADE,)
    Date = models.DateTimeField(auto_now_add=True, blank=True)

    @staticmethod
    def get_if_exists(advert_id):
        try:
            request = AdvertDeleteRequest.objects.get(Advert=advert_id) is not None
            return request
        except ObjectDoesNotExist:
            return None

    def __str__(self):
        return self.Advert.title