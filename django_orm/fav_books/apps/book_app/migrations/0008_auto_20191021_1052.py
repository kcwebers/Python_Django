# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-21 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0007_auto_20191018_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank='true', default='settings.MEDIA_ROOT/anonymous.jpg', null=True, upload_to=''),
        ),
    ]