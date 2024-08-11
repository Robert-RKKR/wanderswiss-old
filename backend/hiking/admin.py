# Django - admin import:
from django.contrib import admin

# WanderSwiss - base admin models import:
from wanderswiss.base.admins.based_admin import BaseAdmin

# Capybara - hiking model import:
from hiking.models.multi_day_trial_model import MultiDayTrialModel
from hiking.models.route_model import RouteModel
from hiking.models.trial_model import TrialModel


# All admin classes:
@admin.register(MultiDayTrialModel)
class MultiDayTrialAdmin(BaseAdmin):

    list_display = (
        'name', 'is_active', 'created', 'updated',
    )
    list_display_links = (
        'name',
    )
    list_filter = (
        'is_active',
    )
    search_fields = (
        'name', 'description',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'created', 'updated', 'name', 'description',)
        }),
    )
    readonly_fields = (
        'created', 'updated',
    )
    empty_value_display = '--None--'


@admin.register(RouteModel)
class RouteAdmin(BaseAdmin):

    list_display = (
        'name', 'is_active', 'created', 'updated',
    )
    list_display_links = (
        'name',
    )
    list_filter = (
        'is_active',
    )
    search_fields = (
        'name', 'description',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'created', 'updated', 'name', 'description',)
        }),
    )
    readonly_fields = (
        'created', 'updated',
    )
    empty_value_display = '--None--'


@admin.register(TrialModel)
class TrialAdmin(BaseAdmin):

    list_display = (
        'name', 'is_active', 'created', 'updated',
    )
    list_display_links = (
        'name',
    )
    list_filter = (
        'is_active',
    )
    search_fields = (
        'name', 'description',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'created', 'updated', 'name', 'description',)
        }),
    )
    readonly_fields = (
        'created', 'updated',
    )
    empty_value_display = '--None--'
