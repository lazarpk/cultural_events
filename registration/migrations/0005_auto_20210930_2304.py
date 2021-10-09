# Generated by Django 3.2.7 on 2021-09-30 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_profile_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('valid_from', models.DateField(null=True)),
                ('valid_to', models.DateField(null=True)),
                ('approved', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='StreetAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('valid_from', models.DateField(null=True)),
                ('valid_to', models.DateField(null=True)),
                ('approved', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('valid_from', models.DateField(null=True)),
                ('valid_to', models.DateField(null=True)),
                ('approved', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='work_area',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.ManyToManyField(to='registration.StreetAddress', verbose_name='adresa'),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.ManyToManyField(to='registration.City', verbose_name='grad'),
        ),
        migrations.AddField(
            model_name='profile',
            name='work_area',
            field=models.ManyToManyField(to='registration.WorkArea', verbose_name='oblast delovanja'),
        ),
    ]