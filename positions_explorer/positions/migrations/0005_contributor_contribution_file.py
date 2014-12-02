# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0004_contributor_contribution_values'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='contribution_file',
            field=models.FileField(null=True, upload_to=b''),
            preserve_default=True,
        ),
    ]
