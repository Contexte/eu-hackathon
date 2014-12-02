from django.contrib import admin

from . import models


class AxisValuesAdmin(admin.TabularInline):
    model = models.AxisValues


class AxisAdmin(admin.ModelAdmin):
    inlines = (
        AxisValuesAdmin,
    )


class ContributorAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.AxisValues)
admin.site.register(models.Contributor, ContributorAdmin)
admin.site.register(models.Axis, AxisAdmin)
