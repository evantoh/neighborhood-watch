# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-17 09:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighborupdate', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Profile',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='neighborhood_location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='neighborhood_name',
            new_name='name',
        ),
    ]
