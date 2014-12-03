# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0012_contributor_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributor',
            name='contribution_axes',
        ),
        migrations.AddField(
            model_name='contributor',
            name='org_subtype',
            field=models.CharField(max_length=40, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contributor',
            name='org_type',
            field=models.CharField(max_length=40, null=True, blank=True),
            preserve_default=True,
        ),
    ]
