# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 21:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifyme', '0004_auto_20170912_2115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ('-created',)},
        ),
    ]
