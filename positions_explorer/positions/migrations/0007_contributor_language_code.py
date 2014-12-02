# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0006_auto_20141202_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='language_code',
            field=models.CharField(default='en', max_length=2),
            preserve_default=False,
        ),
    ]
