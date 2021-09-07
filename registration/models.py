from django.db import models
from django.contrib.auth.models import User
#from django.db.models.signals import post_save
#from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    id = models.AutoField(primary_key= True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    address = models.CharField(max_length=45)
    number = models.IntegerField()
    city = models.CharField(max_length=30)
    contact_person = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    description = models.TextField(max_length=150)
    work_area = models.CharField(max_length=55)
    web_site = models.CharField(max_length=30)

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)
#
#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()
