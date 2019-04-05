# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180419_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otp_level',
            field=models.SmallIntegerField(choices=[(0, 'Disable'), (1, 'Enable'), (2, 'Force enable')], default=0, verbose_name='MFA'),
        ),
    ]
