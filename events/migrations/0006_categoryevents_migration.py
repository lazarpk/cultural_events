# Generated by Django 3.2.7 on 2021-10-04 20:44

from django.db import migrations


def load_categoryevents (apps, schema_editor):
    CategoryEvents = apps.get_model ('events', 'CategoryEvents')
    categoryevents_music = CategoryEvents (name = 'Muzika', valid_from='2021-10-01', valid_to='2022-10-01', approved=True, status=True)
    categoryevents_music.save()
    categoryevents_festival = CategoryEvents (name = 'Festival', valid_from='2021-10-01', valid_to='2022-10-01', approved=True, status=True)
    categoryevents_festival.save()
    categoryevents_exhibit = CategoryEvents (name = 'Izlozba', valid_from='2021-10-01', valid_to='2022-10-01', approved=True, status=True)
    categoryevents_exhibit.save()
    categoryevents_theatre = CategoryEvents (name = 'Pozoriste', valid_from='2021-10-01', valid_to='2022-10-01', approved=True, status=True)
    categoryevents_theatre.save()


def delete_categoryevents (apps, schema_editor):
    CategoryEvents = apps.get_model("events", "CategoryEvents")
    CategoryEvents.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20210930_2242'),
    ]

    operations = [
        migrations.RunPython(load_categoryevents, delete_categoryevents),
    ]