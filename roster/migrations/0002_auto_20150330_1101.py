# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='athlete',
            options={'ordering': ('lastname', 'firstname', 'year', 'hometown', 'highschool'), 'verbose_name_plural': 'Athletes'},
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='name',
        ),
        migrations.RemoveField(
            model_name='team',
            name='athlete',
        ),
        migrations.AddField(
            model_name='athlete',
            name='firstname',
            field=models.CharField(default=b'', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='athlete',
            name='lastname',
            field=models.CharField(default=b'', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='athletes',
            field=models.ForeignKey(related_name=b'teams', default=b'', to='roster.Team', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='athlete',
            name='description',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='event',
            name='athletes',
            field=models.ManyToManyField(related_name=b'events', null=True, to=b'roster.Athlete'),
        ),
        migrations.AlterField(
            model_name='team',
            name='coach',
            field=models.CharField(default=b'', unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='team',
            name='season',
            field=models.CharField(max_length=50),
        ),
    ]
