# Generated by Django 3.2.6 on 2021-09-01 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_remove_profile_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default=None, max_length=45),
            preserve_default=False,
        ),
    ]
