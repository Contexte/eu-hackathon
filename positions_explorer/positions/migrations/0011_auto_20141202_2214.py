# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0010_auto_20141202_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='language_code',
            field=models.CharField(max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
    ]
