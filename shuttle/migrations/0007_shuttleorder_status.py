# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-06 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuttle', '0006_auto_20171206_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='shuttleorder',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Ongoing', 'Ongoing'), ('Not Started', 'Not Started'), ('Cancelled', 'Cancelled')], default='Not Started', max_length=30),
            preserve_default=False,
        ),
    ]