# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-20 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0007_driverorder_reservation_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverorder',
            name='reservation_number',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
