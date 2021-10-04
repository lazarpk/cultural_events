from django.db import models
from django.contrib.auth.models import User
#from django.db.models.signals import post_save
#from django.dispatch import receiver


# Create your models here.

#SIFARNICI:

class StreetAddress (models.Model):
    name = models.CharField(max_length=45)
    valid_from = models.DateField(null=True, blank=False)
    valid_to = models.DateField(null=True, blank=False)
    approved = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    @staticmethod
    def get_active():
        data = StreetAddress.objects.filter(status=True, approved=True).all()
        return data


class City (models.Model):
    name = models.CharField(max_length=30)
    valid_from = models.DateField(null=True, blank=False)
    valid_to = models.DateField(null=True, blank=False)
    approved = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    @staticmethod
    def get_active():
        data = City.objects.filter(status=True, approved=True).all()
        return data


class WorkArea (models.Model):
    name = models.CharField(max_length=55)
    valid_from = models.DateField(null=True, blank=False)
    valid_to = models.DateField(null=True, blank=False)
    approved = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    @staticmethod
    def get_active():
        data = WorkArea.objects.filter(status=True, approved=True).all()
        return data


class Profile(models.Model):
    id = models.AutoField(primary_key= True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    address = models.ManyToManyField(StreetAddress, verbose_name="adresa")
    number = models.IntegerField()
    city = models.ManyToManyField(City, verbose_name="grad")
    contact_person = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    description = models.TextField(max_length=150)
    work_area = models.ManyToManyField(WorkArea, verbose_name="oblast delovanja")
    web_site = models.CharField(max_length=30)



#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)
#
#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()
