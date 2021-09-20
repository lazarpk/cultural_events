from django.db import models

# Create your models here.
class Adverts ( models.Model):
    title = models.CharField( max_length=32);
    description = models.TextField();
    load_date = models.DateField();
    expire_date = models.DateField();
    archived = models.Choices ('archived', 'YES NO');

class Archived(models.IntegerChoices):
    NO = 0, ('No')
    YES = 1, ('Yes')

    __empty__ = ('(Unknown)')
