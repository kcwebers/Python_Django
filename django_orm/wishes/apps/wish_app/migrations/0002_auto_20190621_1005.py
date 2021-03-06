# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-21 17:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wish_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='wishes_granted',
        ),
        migrations.RemoveField(
            model_name='user',
            name='wishes_made',
        ),
        migrations.AddField(
            model_name='wish',
            name='granted_by',
            field=models.ManyToManyField(related_name='wishes_granted', to='wish_app.User'),
        ),
        migrations.AddField(
            model_name='wish',
            name='liked_by',
            field=models.ManyToManyField(related_name='likes', to='wish_app.User'),
        ),
        migrations.AddField(
            model_name='wish',
            name='wished_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='wishes_made', to='wish_app.User'),
            preserve_default=False,
        ),
    ]
