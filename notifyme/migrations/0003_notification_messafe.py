# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifyme', '0002_notification_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='messafe',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
