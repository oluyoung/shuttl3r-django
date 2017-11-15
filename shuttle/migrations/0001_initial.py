# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 07:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RouteStop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_no', models.IntegerField()),
                ('stop_location', models.CharField(max_length=255)),
                ('morning_start_time', models.TimeField(blank=True, null=True)),
                ('evening_start_time', models.TimeField(blank=True, null=True)),
                ('latitude', models.CharField(blank=True, max_length=25, null=True)),
                ('longitude', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'verbose_name_plural': 'RouteStops',
                'verbose_name': 'RouteStop',
            },
        ),
        migrations.CreateModel(
            name='ShuttleBus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_type', models.CharField(choices=[('Mini Bus', 'Mini Bus'), ('Coaster Bus', 'Coaster Bus')], max_length=15, verbose_name='Bus Type')),
                ('license', models.CharField(max_length=10, verbose_name='License Plate')),
            ],
            options={
                'verbose_name_plural': 'ShuttleBuses',
                'verbose_name': 'ShuttleBus',
            },
        ),
        migrations.CreateModel(
            name='ShuttleOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('subscription', models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], max_length=10)),
                ('morning_pickup_time', models.TimeField(choices=[('5:00', '5:00'), ('5:30', '5:30'), ('6:00', '6:00'), ('6:30', '6:30'), ('7:00', '7:00'), ('7:30', '7:30'), ('8:00', '8:00'), ('8:30', '8:30')], verbose_name="User's Morning Pickup Time")),
                ('evening_pickup_time', models.TimeField(choices=[('5:00', '5:00'), ('5:30', '5:30'), ('6:00', '6:00'), ('6:30', '6:30'), ('7:00', '7:00'), ('7:30', '7:30'), ('8:00', '8:00'), ('8:30', '8:30')], verbose_name="User's Evening Pickup Time")),
                ('isRenewing', models.BooleanField(verbose_name="Is User's Subscription Renewed?")),
                ('evening_pickup_stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evening_pickup_stop', to='shuttle.RouteStop')),
                ('morning_pickup_stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='morning_pickup_stop', to='shuttle.RouteStop')),
            ],
            options={
                'verbose_name_plural': 'ShuttleOrders',
                'verbose_name': 'ShuttleOrder',
            },
        ),
        migrations.CreateModel(
            name='ShuttleRoute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats_num', models.IntegerField(verbose_name='No. of Seats')),
                ('seats_available', models.IntegerField(default=models.IntegerField(verbose_name='No. of Seats'), verbose_name='No. of Seats Available')),
                ('route_name', models.CharField(max_length=255, verbose_name='Route Title')),
                ('startpoint', models.CharField(max_length=255, verbose_name='Route Start Location')),
                ('morning_start_time', models.TimeField(verbose_name='Route Morning Start Time')),
                ('start_latitude', models.CharField(blank=True, max_length=25, null=True, verbose_name='Route Start Location Latitude')),
                ('start_longitude', models.CharField(blank=True, max_length=25, null=True, verbose_name='Route Start Location Longitude')),
                ('endpoint', models.CharField(max_length=255, verbose_name='Route End Location')),
                ('evening_start_time', models.TimeField(verbose_name='Route Evening Start Time')),
                ('end_latitude', models.CharField(blank=True, max_length=25, null=True, verbose_name='Route End Location Latitude')),
                ('end_longitude', models.CharField(blank=True, max_length=25, null=True, verbose_name='Route End Location Longitude')),
                ('daily_price', models.FloatField(verbose_name='Route Daily Price')),
                ('weekly_price', models.FloatField(verbose_name='Route Weekly Price')),
                ('monthly_price', models.FloatField(verbose_name='Route Monthly Price')),
                ('is_available', models.BooleanField(default=True, verbose_name='Is Route Still Available for Subscribers?')),
            ],
            options={
                'verbose_name_plural': 'ShuttleRoutes',
                'verbose_name': 'ShuttleRoute',
            },
        ),
        migrations.AddField(
            model_name='shuttleorder',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route', to='shuttle.ShuttleRoute'),
        ),
    ]
