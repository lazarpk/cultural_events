# Generated by Django 3.2.7 on 2021-09-13 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20210913_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
