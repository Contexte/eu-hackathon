# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0009_auto_20141202_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='contribution_axes',
            field=models.ManyToManyField(to='positions.Axis', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contributor',
            name='contribution_file',
            field=models.FileField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contributor',
            name='contribution_values',
            field=models.ManyToManyField(to='positions.AxisValues', null=True, blank=True),
            preserve_default=True,
        ),
    ]
