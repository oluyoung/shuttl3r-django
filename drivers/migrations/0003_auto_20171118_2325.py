# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0002_auto_20171115_0828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driverorder',
            name='pickup_time',
        ),
        migrations.AlterField(
            model_name='driverorder',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Ongoing', 'Ongoing'), ('Not Started', 'Not Started')], default='Not Started', max_length=30),
        ),
    ]
