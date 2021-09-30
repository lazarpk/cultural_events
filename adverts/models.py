from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.admin import User

# Create your models here.
class Adverts ( models.Model):
    title = models.CharField( max_length=32);
    description = models.TextField();
    load_date = models.DateField();
    expire_date = models.DateField();
    author = models.ForeignKey(User, on_delete=models.CASCADE )
    date_archived = models.DateTimeField(null=True, blank=True);

    class Meta:
        permissions = [
            ('advert_can_create', 'Can create advert'),
            ('advert_edit', 'Can edit advert'),
            ('advert_can_archive', 'Can archive advert'),
            ('advert_can_delete', 'Can delete advert'),
        ]


class AdvertDeleteRequest(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Advert = models.ForeignKey(Adverts, on_delete=models.CASCADE)
    Date = models.DateTimeField(auto_now_add=True, blank=True)

    @staticmethod
    def get_if_exists(advert_id):
        try:
            request = AdvertDeleteRequest.objects.get(Advert=advert_id) is not None
            return request
        except ObjectDoesNotExist:
            return None
