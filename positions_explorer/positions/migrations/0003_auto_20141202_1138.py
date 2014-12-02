# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0002_auto_20141202_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributor',
            name='contribution_axis',
        ),
        migrations.AddField(
            model_name='contributor',
            name='contribution_axes',
            field=models.ManyToManyField(to='positions.Axis'),
            preserve_default=True,
        ),
    ]
