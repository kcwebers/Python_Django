# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-19 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful_app', '0002_auto_20190619_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateTimeField(),
        ),
    ]
