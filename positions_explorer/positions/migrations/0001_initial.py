# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Axis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AxisValues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('axis', models.ForeignKey(related_name='values', to='positions.Axis')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.CharField(default=b'publisher', max_length=19, choices=[(b'authority', 'Authority'), (b'author', 'Author'), (b'cmos', 'CMOS'), (b'institutional-user', b'Institutional user'), (b'other', 'Other'), (b'publisher', '\xc9diteur'), (b'service-provider', 'Service provider'), (b'user', 'User')])),
                ('value', models.CharField(max_length=140)),
                ('contribution_axis', models.ForeignKey(to='positions.Axis')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
