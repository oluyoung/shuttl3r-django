# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=35, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=35, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('phone_num', models.CharField(max_length=11, verbose_name='Phone Number')),
                ('default_pickup_addr', models.CharField(blank=True, max_length=255, null=True, verbose_name='Default Pickup Address')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Users',
                'verbose_name': 'User',
            },
        ),
    ]
