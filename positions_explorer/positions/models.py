# -*- coding: utf-8 -*-

from django.db import models


class Axis(models.Model):

    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255)


class AxisValues(models.Model):

    axis = models.ForeignKey(Axis, related_name='values')
    value = models.CharField(max_length=140)


class Contributor(models.Model):

    AUTHORITY = 'authority'
    AUTHOR = 'author'
    CMOS = 'cmos'
    INSTITUTIONAL_USER = 'institutional-user'
    OTHER = 'other'
    PUBLISHER = 'publisher'
    SERVICE_PROVIDER = 'service-provider'
    USER = 'user'

    CONTRIBUTOR_KINDS = (
        (AUTHORITY, u'Authority'),
        (AUTHOR, u'Author'),
        (CMOS, u'CMOS'),
        (INSTITUTIONAL_USER, 'Institutional user'),
        (OTHER, u'Other'),
        (PUBLISHER, u'Éditeur'),
        (SERVICE_PROVIDER, u'Service provider'),
        (USER, u'User')
    )

    kind = models.CharField(max_length=19, choices=CONTRIBUTOR_KINDS, default=PUBLISHER)
    contribution_axes = models.ManyToManyField(Axis)
    contribution_values = models.ManyToManyField(AxisValues)
    contribution_file = models.FileField(null=True)
