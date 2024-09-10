# Django - admin import:
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import admin

# WanderSwiss - base admin models import:
from wanderswiss.base.admins.based_admin import BaseAdmin

# WanderSwiss - management model import:
from management.models.global_settings_model import GlobalSettingsModel
from management.models.user_settings_model import UserSettingsModel
from management.models.user_model import UserModel

# Capybara - hiking model import:
from hiking.models.event_model import UserEventModel


@admin.register(GlobalSettingsModel)
class GlobalSettingAdmin(BaseAdmin):

    list_display = (
        'pk', 'created', 'updated', 'is_current',
    )
    search_fields = (
        'pk',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('created', 'updated', 'is_current',)
        }),
    )


@admin.register(UserSettingsModel)
class UserSettingsAdmin(BaseAdmin):

    list_display = (
        'pk', 'created', 'updated',
    )
    search_fields = (
        'user',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('created', 'updated', 'measurement_system',)
        }),
    )


class UserEventInline(admin.TabularInline):
    model = UserEventModel
    extra = 1
    autocomplete_fields = ['user']


@admin.register(UserModel)
class UserAdmin(BaseAdmin):

    list_display = (
        'pk', 'username', 'first_name', 'last_name', 'is_active',
        'is_staff', 'email', 'created', 'updated'
    )
    list_filter = (
        'is_active',
    )
    search_fields = (
        'username', 'description', 'username', 'first_name', 'last_name',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_active', 'is_staff', 'is_superuser', 'created',
                'updated', 'username', 'first_name', 'last_name', 'email')
        }),
        ('Password', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('password', 'password_to_change')
        }),
        ('Permissions', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('role', 'user_permissions', 'groups')
        }),
    )
    readonly_fields = (
        'created', 'updated'
    )
    empty_value_display = '--None--'
    inlines = [UserEventInline]
    change_password_form = AdminPasswordChangeForm

    def get_form(self, request, obj=None, **kwargs):
        """
        Use the default form for editing objects, but use a
        special form for changing passwords.
        """
        
        if obj and 'password' in self.fieldsets:
            kwargs['form'] = self.change_password_form
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        """
        Overriding save_model to handle password changes.
        """

        if form.cleaned_data.get('password'):
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)

    def get_fieldsets(self, request, obj=None):
        """
        Show password fields only when editing an existing user.
        """

        fieldsets = super().get_fieldsets(request, obj)
        if not obj:
            return tuple(fs for fs in fieldsets if 'Password' not in fs[0])
        return fieldsets
