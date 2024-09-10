# Django - admin import:
from django.contrib import admin

# WanderSwiss - base admin models import:
from wanderswiss.base.admins.based_admin import BaseAdmin

# Capybara - hiking model import:
from hiking.models.multi_day_trial_model import MultiDayTrialModel
from hiking.models.event_model import UserEventModel
from hiking.models.route_model import RouteModel
from hiking.models.trial_model import TrialModel
from hiking.models.event_model import EventModel



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
        ('Base', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'created', 'updated',
                        'name', 'description',)
        }),
        ('Localization', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('start_point', 'middle_points', 'end_point',
                        'regions', 'countries',)
        }),
        ('Hike data', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('gps_data', 'distance', 'ascents', 'descents',
                        'min_elevation', 'max_elevation', 'route_type',)
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


class UserEventInline(admin.TabularInline):
    model = UserEventModel
    extra = 1
    autocomplete_fields = ['user']


@admin.register(EventModel)
class EventAdmin(BaseAdmin):

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
        ('Relations', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('route',)
        }),
    )
    readonly_fields = (
        'created', 'updated',
    )
    autocomplete_fields = ('route',)
    inlines = [UserEventInline]
    empty_value_display = '--None--'
