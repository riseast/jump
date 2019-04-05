# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-27 16:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('terminal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='terminal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='terminal.Terminal'),
        ),
        migrations.AddField(
            model_name='status',
            name='terminal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='terminal.Terminal'),
        ),
        migrations.AddField(
            model_name='task',
            name='terminal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='terminal.Terminal'),
        ),
        migrations.AddField(
            model_name='terminal',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='terminal', to=settings.AUTH_USER_MODEL, verbose_name='Application User'),
        ),
        migrations.AlterField(
            model_name='terminal',
            name='name',
            field=models.CharField(max_length=32, verbose_name='Name'),
        ),
    ]
