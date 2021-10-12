from django.db import models
from django.contrib.auth.admin import User

class Poll(models.Model):
    question = models.TextField('Pitanje')
    author = models.ForeignKey(User, on_delete=models.CASCADE )
    option_one = models.CharField('Prva opcija',max_length=30)
    option_two = models.CharField('Druga opcija', max_length=30)
    option_three = models.CharField('Treca opcija', max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    public= models.BooleanField('Rezultati ankete su javni', default=True)
    voter = models.ManyToManyField(User, related_name='voter')

    class Meta:
        permissions = [
            ('poll_can_create', 'Can create poll')
        ]
    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count
