# Django - admin import:
from django.contrib import admin

# WanderSwiss - base admin models import:
from wanderswiss.base.admins.based_admin import BaseAdmin

# WanderSwiss - management model import:
from management.models.global_settings_model import GlobalSettingsModel
from management.models.user_model import UserModel


@admin.register(GlobalSettingsModel)
class GlobalSettingAdmin(BaseAdmin):

    list_display = (
        'pk', 'is_current', 'updated',
    )
    search_fields = (
        'name',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_current',)
        }),
    )


@admin.register(UserModel)
class UserAdmin(BaseAdmin):

    list_display = (
        'pk', 'name', 'is_active', 'is_staff', 'email', 'created', 'updated'
    )
    list_filter = (
        'is_active',
    )
    search_fields = (
        'name', 'description'
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'is_staff', 'created',
                'updated', 'name', 'email')
        }),
        ('Password', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('password', 'password_to_change')
        }),
        ('Permissions', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('user_permissions', 'groups')
        }),
    )
    readonly_fields = (
        'created', 'updated'
    )
    empty_value_display = '--None--'
