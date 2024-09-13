# Django - admin import:
from django.contrib import admin

# WanderSwiss - base admin models import:
from wanderswiss.base.admins.based_admin import BaseAdmin

# Capybara - hiking model import:
from hiking.models.multi_day_trial_model import MultiDayTrialTrialModel
from hiking.models.multi_day_trial_model import MultiDayTrialModel
from hiking.models.trial_model import TrialRouteModel
from hiking.models.event_model import UserEventModel
from hiking.models.route_model import RouteModel
from hiking.models.trial_model import TrialModel
from hiking.models.event_model import EventModel



# All admin inline classes:
class MultiDayTrialTrialInline(admin.TabularInline):
    model = MultiDayTrialTrialModel
    extra = 1
    autocomplete_fields = ['multi_day_trial']


class TrialMultiDayTrialTrialInline(admin.TabularInline):
    model = MultiDayTrialTrialModel
    extra = 1
    autocomplete_fields = ['trial']


class TrialRouteInline(admin.TabularInline):
    model = TrialRouteModel
    extra = 1
    autocomplete_fields = ['trial']


class RouteTrialInline(admin.TabularInline):
    model = TrialRouteModel
    extra = 1
    autocomplete_fields = ['route']


class UserEventInline(admin.TabularInline):
    model = UserEventModel
    extra = 1
    autocomplete_fields = ['user']


# All admin classes:
@admin.register(MultiDayTrialModel)
class MultiDayTrialAdmin(BaseAdmin):

    list_display = (
        'name', 'is_active', 'creator', 'created', 'updated',
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
            'fields': ('is_active', 'creator', 'created', 'updated',
                       'name', 'description',)
        }),
        ('MDT information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('days',)
        }),
    )
    readonly_fields = (
        'creator', 'created', 'updated',
    )
    inlines = [MultiDayTrialTrialInline]
    empty_value_display = '--None--'


@admin.register(RouteModel)
class RouteAdmin(BaseAdmin):

    list_display = (
        'name', 'is_active', 'creator', 'created', 'updated',
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
            'fields': ('is_active', 'creator', 'created', 'updated',
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
        'creator', 'created', 'updated',
    )
    inlines = [RouteTrialInline]
    empty_value_display = '--None--'


@admin.register(TrialModel)
class TrialAdmin(BaseAdmin):

    list_display = (
        'name', 'is_active', 'creator', 'created', 'updated',
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
            'fields': ('is_active', 'creator', 'created', 'updated',
                       'name', 'description',)
        }),
    )
    readonly_fields = (
        'creator', 'created', 'updated',
    )
    inlines = [TrialMultiDayTrialTrialInline, TrialRouteInline]
    empty_value_display = '--None--'


@admin.register(EventModel)
class EventAdmin(BaseAdmin):

    list_display = (
        'name', 'is_active', 'creator', 'created', 'updated',
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
            'fields': ('is_active', 'creator', 'created', 'updated',
                       'name', 'description',)
        }),
        ('Relations', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('route',)
        }),
    )
    readonly_fields = (
        'creator', 'created', 'updated',
    )
    autocomplete_fields = ('route',)
    inlines = [UserEventInline]
    empty_value_display = '--None--'
