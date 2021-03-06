# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-06 23:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuttle', '0009_auto_20171206_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shuttleorder',
            name='evening_pickup_time',
            field=models.TimeField(blank=True, choices=[(datetime.time(5, 0), '5:00'), (datetime.time(5, 30), '5:30'), (datetime.time(6, 0), '6:00'), (datetime.time(6, 30), '6:30'), (datetime.time(7, 0), '7:00'), (datetime.time(7, 30), '7:30'), (datetime.time(8, 0), '8:00'), (datetime.time(8, 30), '8:30')], null=True, verbose_name="User's Evening Pickup Time"),
        ),
        migrations.AlterField(
            model_name='shuttleorder',
            name='morning_pickup_time',
            field=models.TimeField(blank=True, choices=[(datetime.time(5, 0), '5:00'), (datetime.time(5, 30), '5:30'), (datetime.time(6, 0), '6:00'), (datetime.time(6, 30), '6:30'), (datetime.time(7, 0), '7:00'), (datetime.time(7, 30), '7:30'), (datetime.time(8, 0), '8:00'), (datetime.time(8, 30), '8:30')], null=True, verbose_name="User's Morning Pickup Time"),
        ),
    ]
