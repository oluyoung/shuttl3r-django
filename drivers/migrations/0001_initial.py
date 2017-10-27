# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 23:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver_CV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('how_many_years_driving_professionally', models.IntegerField()),
                ('last_employer_name', models.CharField(max_length=255)),
                ('last_employer_address', models.CharField(max_length=255)),
                ('last_employer_number', models.CharField(max_length=255)),
                ('reason_for_leaving', models.CharField(max_length=255)),
                ('license_id', models.CharField(max_length=15)),
                ('license_exp_date', models.DateField()),
                ('medical_conditions', models.TextField()),
                ('referee1', models.CharField(max_length=255)),
                ('home_office_num1', models.CharField(max_length=255)),
                ('home_office_addr1', models.CharField(max_length=255)),
                ('referee2', models.CharField(max_length=255, null=True)),
                ('home_office_num2', models.CharField(max_length=255, null=True)),
                ('home_office_addr2', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Driver_CV',
                'verbose_name_plural': 'Driver_CVs',
            },
        ),
        migrations.CreateModel(
            name='DriverInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('mid_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('image_url', models.URLField()),
                ('home_address', models.CharField(max_length=255)),
                ('phone_num1', models.CharField(max_length=11)),
                ('phone_num2', models.CharField(max_length=11, null=True)),
                ('category', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=7)),
                ('isAvailable', models.BooleanField()),
                ('nextAvailability', models.DateField()),
            ],
            options={
                'verbose_name': 'DriverInfo',
                'verbose_name_plural': 'DriverInfos',
            },
        ),
        migrations.CreateModel(
            name='DriverOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('is_within_lagos', models.BooleanField()),
                ('pickup_address', models.CharField(max_length=255)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver', to='drivers.DriverInfo')),
            ],
            options={
                'verbose_name': 'DriverOrder',
                'verbose_name_plural': 'DriverOrders',
            },
        ),
        migrations.AddField(
            model_name='driver_cv',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.DriverInfo'),
        ),
    ]
