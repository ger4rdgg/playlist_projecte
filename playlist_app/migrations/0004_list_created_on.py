# Generated by Django 3.0.6 on 2020-05-09 14:04

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('playlist_app', '0003_auto_20200509_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='created_on',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.now),
        ),
    ]