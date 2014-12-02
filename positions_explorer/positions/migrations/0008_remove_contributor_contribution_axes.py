# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0007_contributor_language_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributor',
            name='contribution_axes',
        ),
    ]
