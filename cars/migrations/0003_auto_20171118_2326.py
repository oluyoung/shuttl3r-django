# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_carorder_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carorder',
            name='pickup_time',
        ),
        migrations.AlterField(
            model_name='carorder',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Ongoing', 'Ongoing'), ('Not Started', 'Not Started')], default='Not Started', max_length=30),
        ),
    ]
