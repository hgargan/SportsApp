# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sport', models.CharField(unique=True, max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('season', models.CharField(default=b'', max_length=50)),
                ('coach', models.CharField(default=b'', unique=True, max_length=50)),
                ('athletes', models.ManyToManyField(default=b'', related_name=b'teams', null=True, to='roster.Athlete')),
            ],
            options={
                'ordering': ('school', 'sport', 'season'),
                'verbose_name_plural': 'Teams',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='athlete',
            options={'ordering': ('lastname', 'firstname', 'year', 'hometown', 'highschool'), 'verbose_name_plural': 'Athletes'},
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='name',
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
    ]
