# Generated by Django 3.2.7 on 2021-10-04 18:14

from django.db import migrations
from openpyxl import load_workbook


def load_cities (apps, schema_editor):
    City = apps.get_model ('registration', 'City')
    wb = load_workbook ('media/codebook_excel/Sifarnik_naselja_Srbije.xlsx')
    ws = wb.active
    for row in ws.values:
        city_name = row[0]
        if city_name is not None:
            city = City (name = city_name, valid_from='2021-10-01', valid_to='2022-10-01', approved=True, status=True)
            city.save()




def delete_cities(apps, schema_editor):
    City = apps.get_model('registration', 'City')
    City.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20210930_2304'),
    ]

    operations = [
        migrations.RunPython(load_cities, delete_cities)
    ]
