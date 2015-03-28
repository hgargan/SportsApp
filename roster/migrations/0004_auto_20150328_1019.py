# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0003_auto_20150325_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='athletes',
            field=models.ManyToManyField(related_name=b'events', null=True, to=b'roster.Athlete'),
        ),
    ]
