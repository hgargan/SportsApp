# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0002_auto_20150325_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='season',
            field=models.CharField(max_length=50),
        ),
    ]
