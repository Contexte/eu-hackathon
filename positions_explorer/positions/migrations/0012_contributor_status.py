# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0011_auto_20141202_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'File'), (1, 'ID'), (2, 'Data'), (3, 'Qualified')]),
            preserve_default=True,
        ),
    ]
