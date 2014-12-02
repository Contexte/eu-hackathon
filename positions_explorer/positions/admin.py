from django.contrib import admin

from . import models


class AxisValuesAdmin(admin.TabularInline):
    model = models.AxisValues


class AxisAdmin(admin.ModelAdmin):
    inlines = (
        AxisValuesAdmin,
    )


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'original_id', 'status')


admin.site.register(models.AxisValues)
admin.site.register(models.Contributor, ContributorAdmin)
admin.site.register(models.Axis, AxisAdmin)
