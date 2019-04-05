# Generated by Django 2.1.4 on 2018-12-07 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0023_auto_20181016_1650'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ops', '0002_celerytask'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommandExecution',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('command', models.TextField(verbose_name='Command')),
                ('_result', models.TextField(blank=True, null=True, verbose_name='Result')),
                ('is_finished', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_start', models.DateTimeField(null=True)),
                ('date_finished', models.DateTimeField(null=True)),
                ('hosts', models.ManyToManyField(to='assets.Asset')),
                ('run_as', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.SystemUser')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='adhoc',
            name='run_as',
        ),
        migrations.AddField(
            model_name='adhoc',
            name='hosts',
            field=models.ManyToManyField(to='assets.Asset', verbose_name='Host'),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_by',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Name'),
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together={('name', 'created_by')},
        ),
    ]
