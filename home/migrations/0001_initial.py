# Generated by Django 3.2.6 on 2021-09-08 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=250, verbose_name='Naslov vesti')),
                ('Content', models.TextField(verbose_name='Tekst vesti')),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
                ('ArchivedDate', models.DateTimeField(blank=True, null=True)),
                ('UpdateDate', models.DateTimeField(blank=True, null=True)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [('article_can_create', 'Can create article'), ('article_edit', 'Can edit article'), ('article_can_archive', 'Can archive article'), ('article_can_delete', 'Can delete article')],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleDeletionRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reason', models.TextField()),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.article')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='Category',
            field=models.ManyToManyField(to='home.Category', verbose_name='Kategorija'),
        ),
    ]