# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-06 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuttle', '0005_auto_20171206_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shuttleorder',
            name='daily_pickup_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='shuttleroute',
            name='daily_price',
            field=models.IntegerField(verbose_name='Route Daily Price'),
        ),
        migrations.AlterField(
            model_name='shuttleroute',
            name='monthly_price',
            field=models.IntegerField(verbose_name='Route Monthly Price'),
        ),
        migrations.AlterField(
            model_name='shuttleroute',
            name='weekly_price',
            field=models.IntegerField(verbose_name='Route Weekly Price'),
        ),
    ]
