# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-19 13:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrderUp', '0002_auto_20171019_1353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resturant',
            old_name='myaddress',
            new_name='address',
        ),
    ]
