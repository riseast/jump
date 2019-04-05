# Generated by Django 2.1.1 on 2018-11-09 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20181105_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='source',
            field=models.CharField(choices=[('local', 'Local'), ('ldap', 'LDAP/AD'), ('openid', 'OpenID')], default='local', max_length=30, verbose_name='Source'),
        ),
    ]
