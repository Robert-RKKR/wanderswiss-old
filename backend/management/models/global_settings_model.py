# Python -import:
import copy

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - connection template validator import:
from wanderswiss.base.validators.json_validators import json_list_validator

# WanderSwiss - constance import:
from wanderswiss.base.constants.notification import ExclusionInclusionChoices
from wanderswiss.base.constants.notification import SeverityChoices

# WanderSwiss - html template import:
from management.templates.html_templates import base_html_template

# WanderSwiss - base model import:
from wanderswiss.base.models.base_model import BaseModel

# Global settings dictionary:
global_settings = {}


# Global setting model class:
class GlobalSettingsModel(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Global settings')
        verbose_name_plural = _('Global settings')

        # Overwrite default permissions:
        default_permissions = ()
        permissions = (
            ('read_write', 'Read and write access.'),
            ('read_only', 'Read only access')
        )

    # Current global settings:
    is_current = models.BooleanField(
        verbose_name=_('Current global settings'),
        help_text=_('Indicates if these settings are the active ones used by '
                    'the Capybara application. Only one set of settings can '
                    'be active at a time.'),
        default=True,
        unique=True,
    )

    # Model data time information:
    created = models.DateTimeField(
        verbose_name=_('Created'),
        help_text=_('The date and time when the global settings was created. This '\
                    'timestamp is automatically set when the object is created.'),
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name=_('Updated'),
        help_text=_('The date and time when these global settings were last '
                    'updated. This helps in tracking changes to settings over '
                    'time.'),
        auto_now=True,
    )

    # Notification logger settings:
    notification_level = models.IntegerField(
        verbose_name=_('Notification severity level'),
        help_text=_('The level of severity for actions that trigger '
                    'notifications. For example, a high severity level might '
                    'trigger notifications for critical issues, while a '
                    'lower level might include warnings and informational '
                    'messages.'),
        choices=SeverityChoices.choices,
        default=SeverityChoices.INFO,
    )
    logger_level = models.IntegerField(
        verbose_name=_('Logger severity level'),
        help_text=_('The level of severity for actions that are logged. '
                    'This setting determines which events are recorded in '
                    'the log files. A higher level might include only errors '
                    'and critical issues, while a lower level might also '
                    'include warnings and informational messages.'),
        choices=SeverityChoices.choices,
        default=SeverityChoices.CRITICAL,
    )
    logger_db = models.BooleanField(
        verbose_name=_('Logger DB'),
        help_text=_('Indicates whether log messages should be stored in '
                    'the database. This can be useful for keeping a '
                    'persistent log history.'),
        default=False,
    )
    logger_cli = models.BooleanField(
        verbose_name=_('Logger CLI'),
        help_text=_('Indicates whether log messages should be displayed in '
                    'the command-line interface (CLI) console. This can be '
                    'useful for real-time monitoring and debugging.'),
        default=False,
    )
    logger_application_option = models.IntegerField(
        verbose_name=_('Application Logging Option'),
        help_text=_('Determines whether applications should be excluded '
            'or included in logging.'),
        choices=ExclusionInclusionChoices.choices,
        default=ExclusionInclusionChoices.NONE,
    )
    logger_application_exclusions = models.JSONField(
        verbose_name=_('Applications to Exclude from Logging'),
        help_text=_('List of applications to be excluded from logging. '
            'Logger will work for all applications except those provided here.'),
        validators=[json_list_validator],
        null=True,
        blank=True,
    )
    logger_application_inclusions = models.JSONField(
        verbose_name=_('Applications to Include in Logging'),
        help_text=_('List of applications to be included in logging. '
            'Logger will work only for these applications.'),
        validators=[json_list_validator],
        null=True,
        blank=True,
    )

    # Report settings:
    report_colors = models.JSONField(
        verbose_name=_('Reports colors'),
        help_text=_('Xxx.'),
        default=[
            '#36a2eb', '#00bef1', '#00d6dc', '#2ae8b5', '#a0f48b', '#7978d2',
            '#9260ba', '#a3459b', '#ab2576', '#f37659', '#fa6e76', '#f867ab',
            '#a74573', '#e17aa7', '#9fadbd', '#3b4856', '#265e58', '#eee8a9',
            '#35837b', '#79fac5', '#39c08f', '#008a5d'
        ],
        validators=[json_list_validator],
    )
    report_html_template = models.TextField(
        verbose_name=_('Report HTML base template'),
        help_text=_('Xxx.'),
        default=base_html_template
    )

    # Collecting data timers:
    collecting_system_data_interval = models.PositiveIntegerField(
        verbose_name=_('Metrics Collection Interval'),
        help_text=_('The interval in minutes at which system metrics '\
            'should be collected.'),
        default=1
    )

    # object representation:
    def __repr__(self) -> str:
        return str(self.pk)

    def __str__(self) -> str:
        return str(self.pk)

    @property
    def __dict__(self):
        return {
            'is_current': self.is_current,
            'created': self.created,
            'updated': self.updated,
            'notification_level': self.notification_level,
            'logger_level': self.logger_level,
            'logger_db': self.logger_db,
            'logger_cli': self.logger_cli,
            'report_colors': self.report_colors,
            'logger_application_option': self.logger_application_option,
            'logger_application_exclusions': self.logger_application_exclusions,
            'logger_application_inclusions': self.logger_application_inclusions,
            'report_html_template': self.report_html_template,
        }

    # Natural key representation:
    def natural_key(self):
        return str(self.pk)

    # Overwrite default save method:
    def save(self, *args, **kwargs):
        # Call the original save method to perform the actual save:
        super().save(*args, **kwargs)
        # Check if saved settings are current:
        if self.is_current:
            # Collect and save global settings object content:
            self.update_global_settings_dictionary()
        # Update time XXXXXXXX:
        # self._update_celery_schedule()

    def update_global_settings_dictionary(self):
        # Collect global settings object content:
        data = self.__dict__
        # Update global settings dictionary:
        global_settings.update(data)

    # def _update_celery_schedule(self):
    #     from django_celery_beat.models import PeriodicTask, IntervalSchedule

    #     interval, created = IntervalSchedule.objects.get_or_create(
    #         every=self.collecting_system_data_interval,
    #         period=IntervalSchedule.MINUTES,
    #     )

    #     PeriodicTask.objects.update_or_create(
    #         name='collect_system_metrics',
    #         defaults={
    #             'interval': interval,
    #             'task': 'collect_system_metrics',
    #         }
    #     )

# Collect global settings helper function:
def collect_global_settings(
        key: str):
    """ Collect global settings. """
    
    if global_settings:
        # Collect data from global settings dictionary:
        value = global_settings.get(key, False)
    else: # Try to collect global settings if they exist:
        collect_settings = GlobalSettingsModel.objects.get_or_create(
            is_current=True)
        # Update global settings dictionary:
        collect_settings[0].update_global_settings_dictionary()
        # Collect data from global settings dictionary:
        value = global_settings.get(key, False)
    
    # Return a copy of the value if it's a dictionary,
    # otherwise return the value itself:
    return copy.deepcopy(value) if isinstance(value, dict) else value
