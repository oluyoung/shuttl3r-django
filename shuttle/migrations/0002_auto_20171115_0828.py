# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 07:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shuttle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shuttleorder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='routestop',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shuttle.ShuttleRoute'),
        ),
    ]
