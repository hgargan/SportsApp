# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='athlete',
        ),
        migrations.AddField(
            model_name='athlete',
            name='team',
            field=models.ForeignKey(to='roster.Team', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='coach',
            field=models.CharField(default=b'', unique=True, max_length=50),
        ),
    ]
