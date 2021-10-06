# Generated by Django 3.2.7 on 2021-10-05 21:30

from django.db import migrations


def load_workarea (apps, schema_editor):
    WorkArea = apps.get_model ('registration', 'WorkArea')
    workarea_association = WorkArea (name = 'Udruzenje', valid_from='2021-10-01', valid_to='2022-10-01', approved=True, status=True)
    workarea_association.save()
    workarea_foundation = WorkArea (name = 'Fondacija', valid_from='2021-10-01', valid_to='2022-10-01', approved=True, status=True)
    workarea_foundation.save()
    workarea_union = WorkArea (name = 'Savez', valid_from='2021-10-01', valid_to='2022-10-01', approved=True, status=True)
    workarea_union.save()
    workarea_nonprofit = WorkArea (name = 'Neprofitna organizacija', valid_from='2021-10-01', valid_to='2022-10-01', approved=True, status=True)
    workarea_nonprofit.save()


def delete_workarea(apps, schema_editor):
    Age = apps.get_model("registration", "WorkArea")
    Age.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_address_migration'),
    ]

    operations = [
        migrations.RunPython(load_workarea, delete_workarea),
    ]
