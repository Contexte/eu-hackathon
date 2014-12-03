# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0013_auto_20141203_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='axis',
            name='description',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
