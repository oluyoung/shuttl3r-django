# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20171118_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carorder',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Ongoing', 'Ongoing'), ('Not Started', 'Not Started'), ('Cancelled', 'Cancelled')], default='Not Started', max_length=30),
        ),
    ]
