# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-11 03:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0013_auto_20180411_1135'),
        ('perms', '0003_auto_20180225_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assetpermission',
            name='asset_groups',
        ),
        migrations.AddField(
            model_name='assetpermission',
            name='date_start',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date start'),
        ),
        migrations.AddField(
            model_name='assetpermission',
            name='nodes',
            field=models.ManyToManyField(blank=True, related_name='granted_by_permissions', to='assets.Node', verbose_name='Nodes'),
        ),
    ]
