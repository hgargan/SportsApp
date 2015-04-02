# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0002_auto_20150330_1332'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ('season',), 'verbose_name_plural': 'Teams'},
        ),
        migrations.RemoveField(
            model_name='team',
            name='school',
        ),
        migrations.RemoveField(
            model_name='team',
            name='sport',
        ),
        migrations.AlterField(
            model_name='team',
            name='coach',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
