# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-20 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(default='2001-01-01'),
            preserve_default=False,
        ),
    ]