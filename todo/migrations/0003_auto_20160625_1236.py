# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-25 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_addtolist_pubdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtolist',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='addtolist',
            name='is_selected',
            field=models.BooleanField(default=False),
        ),
    ]