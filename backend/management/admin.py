# Django - admin import:
from django.contrib import admin

# Capybara - base admin models import:
from capybara.base.admins.based_admin import BaseAdmin

# Capybara - management model import:
from management.models.global_settings_model import GlobalSettingsModel
from management.models.user_model import AdministratorModel

# Capybara - management form import:
from management.forms.global_settings_form import GlobalSettingsAdminForm


@admin.register(GlobalSettingsModel)
class GlobalSettingAdmin(BaseAdmin):

    form = GlobalSettingsAdminForm

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
        ('Notification settings', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('logger_db', 'logger_cli',
                'notification_level', 'logger_level', 'logger_application_option',
                'logger_application_exclusions', 'logger_application_inclusions',),
        }),
        ('HTTP settings', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('http_timeout', 'http_default_headers',
                'http_max_workers'),
        }),
        ('SSH settings', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('ssh_timeout', 'ssh_repeat',
                'ssh_invalid_responses', 'ssh_max_workers'),
        }),
        ('Intervals settings', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('collecting_system_data_interval',),
        }),
        ('Report settings', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('report_colors', 'report_html_template',),
        }),
    )


@admin.register(AdministratorModel)
class AdministratorAdmin(BaseAdmin):

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
