# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-18 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0003_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank='true', upload_to='media/images'),
        ),
    ]
