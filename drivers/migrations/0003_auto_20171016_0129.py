# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 00:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0002_auto_20171016_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverinfo',
            name='category',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=7),
        ),
    ]