# Django - forms and widgets import:
from django_jsonform.widgets import JSONFormWidget
from django import forms

# Capybara - connection template validator import:
from capybara.base.validators.json_validators import LIST_SCHEMA
from capybara.base.validators.json_validators import DICT_SCHEMA

# Capybara - management models import:
from management.models.global_settings_model import GlobalSettingsModel


# Global settings model form:
class GlobalSettingsAdminForm(forms.ModelForm):
    class Meta:
        model = GlobalSettingsModel
        fields = '__all__'
        widgets = {
            'http_default_headers': JSONFormWidget(
                schema=DICT_SCHEMA),
            'ssh_invalid_responses': JSONFormWidget(
                schema=LIST_SCHEMA),
            'report_colors': JSONFormWidget(
                schema=LIST_SCHEMA),
            'logger_application_exclusions': JSONFormWidget(
                schema=LIST_SCHEMA),
            'logger_application_inclusions': JSONFormWidget(
                schema=LIST_SCHEMA)
        }
