# Generated by Django 3.2.7 on 2021-10-04 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_age_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='age',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
