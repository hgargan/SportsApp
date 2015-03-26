# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('hometown', models.CharField(max_length=50)),
                ('highschool', models.CharField(max_length=75)),
                ('description', models.TextField(default=b'', max_length=1000)),
            ],
            options={
                'ordering': ('name', 'year', 'hometown', 'highschool'),
                'verbose_name_plural': 'Athletes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('athletes', models.ManyToManyField(related_name=b'events', to='roster.Athlete')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Events',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sport', models.CharField(unique=True, max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('season', models.CharField(unique=True, max_length=50)),
                ('coach', models.CharField(unique=True, max_length=50)),
                ('athlete', models.OneToOneField(to='roster.Athlete')),
            ],
            options={
                'ordering': ('school', 'sport', 'season'),
                'verbose_name_plural': 'Teams',
            },
            bases=(models.Model,),
        ),
    ]
