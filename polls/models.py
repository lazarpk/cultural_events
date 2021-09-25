from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    question = models.TextField('Pitanje')
    option_one = models.CharField('Prva opcija',max_length=30)
    option_two = models.CharField('Druga opcija', max_length=30)
    option_three = models.CharField('Treca opcija', max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count