# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0003_auto_20141202_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='contribution_values',
            field=models.ManyToManyField(to='positions.AxisValues'),
            preserve_default=True,
        ),
    ]
