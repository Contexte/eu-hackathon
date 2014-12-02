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
        (PUBLISHER, u'Editor'),
        (SERVICE_PROVIDER, u'Service provider'),
        (USER, u'User')
    )

    kind = models.CharField(max_length=19, choices=CONTRIBUTOR_KINDS, default=OTHER)
    contribution_axes = models.ManyToManyField(Axis)
    contribution_values = models.ManyToManyField(AxisValues)
    contribution_file = models.FileField(null=True)

    # parser result fields
    activities = models.TextField(null=True, blank=True)
    area_of_interest = models.TextField(null=True, blank=True)
    countries = models.TextField(null=True, blank=True)
    extra_financial_info = models.TextField(null=True, blank=True)
    fax_number = models.TextField(null=True, blank=True)
    financial_year = models.TextField(null=True, blank=True)
    goals = models.TextField(null=True, blank=True)
    head_office_address = models.TextField(null=True, blank=True)
    original_id = models.TextField(null=True, blank=True)
    lobbying_expenditure = models.TextField(null=True, blank=True)
    lobbying_section = models.TextField(null=True, blank=True)
    lobbying_subsection = models.TextField(null=True, blank=True)
    lobbyists_contact_position = models.TextField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    networking = models.TextField(null=True, blank=True)
    num_natural_members = models.TextField(null=True, blank=True)
    num_org_members = models.TextField(null=True, blank=True)
    org_members = models.TextField(null=True, blank=True)
    register_url = models.TextField(null=True, blank=True)
    registration_date = models.TextField(null=True, blank=True)
    retrieved_at = models.TextField(null=True, blank=True)
    telephone = models.TextField(null=True, blank=True)
    update_date = models.TextField(null=True, blank=True)
