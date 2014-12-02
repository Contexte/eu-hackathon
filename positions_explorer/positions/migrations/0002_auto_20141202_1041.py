# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributor',
            name='value',
        ),
        migrations.AddField(
            model_name='axisvalues',
            name='value',
            field=models.CharField(default='', max_length=140),
            preserve_default=False,
        ),
    ]
