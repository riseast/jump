# Generated by Django 2.1 on 2018-12-26 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0013_auto_20181123_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='protocol',
            field=models.CharField(choices=[('ssh', 'ssh'), ('rdp', 'rdp'), ('vnc', 'vnc')], default='ssh', max_length=8),
        ),
    ]
