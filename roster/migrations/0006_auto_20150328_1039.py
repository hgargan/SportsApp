# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0005_auto_20150328_1023'),
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
    ]
