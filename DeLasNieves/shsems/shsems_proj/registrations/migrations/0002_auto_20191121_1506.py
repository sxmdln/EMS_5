# Generated by Django 2.0 on 2019-11-21 15:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20191121_1419'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registrations', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='registration',
            unique_together={('event', 'participant')},
        ),
    ]
