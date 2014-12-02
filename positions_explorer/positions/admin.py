from django.contrib import admin

from . import models


class ContributorAdmin(admin.ModelAdmin):
    pass


class AxisAdmin(admin.ModelAdmin):
    pass


class AxisValuesAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Contributor, ContributorAdmin)
admin.site.register(models.Axis, AxisAdmin)
admin.site.register(models.AxisValues, AxisValuesAdmin)
