# Generated by Django 3.0.4 on 2020-05-03 11:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('playlist_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]