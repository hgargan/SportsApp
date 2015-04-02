# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0003_auto_20150330_1359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ('sport', 'season'), 'verbose_name_plural': 'Teams'},
        ),
        migrations.AddField(
            model_name='team',
            name='sport',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
