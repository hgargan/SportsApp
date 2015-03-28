# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0004_auto_20150328_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='description',
            field=models.TextField(default=b''),
        ),
    ]
