# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addToList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_text', models.CharField(max_length=40)),
                ('pubdate', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
