# Python -import:
import copy

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - connection template validator import:
from wanderswiss.base.validators.json_validators import json_list_dict_validator
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
    updated = models.DateTimeField(
        verbose_name=_('Updated'),
        help_text=_('The date and time when these global settings were last '
                    'updated. This helps in tracking changes to settings over '
                    'time.'),
        auto_now=True,
    )

    # Global settings:
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

    # HTTP settings:
    http_timeout = models.IntegerField(
        verbose_name=_('HTTP session timeout'),
        help_text=_('The maximum amount of time (in seconds) that the Capybara '
                    'application will wait for a response to an HTTP '
                    'request before closing the connection. This setting '
                    'helps to avoid indefinitely hanging requests.'),
        default=10,
    )
    http_default_headers = models.JSONField(
        verbose_name=_('HTTP default headers'),
        help_text=_('Default headers to include in HTTP requests. This can '
                    'include headers like "Content-Type", "Authorization", '
                    'and other custom headers required by the API endpoints '
                    'the application interacts with.'),
        default=[{'Key':'Content-Type', 'Value': 'application/json'}],
        validators=[json_list_dict_validator],
    )
    http_max_workers = models.IntegerField(
        verbose_name=_('HTTP Max workers'),
        help_text=_('Xxx.'),
        default=10,
    )

    # SSH settings:
    ssh_timeout = models.IntegerField(
        verbose_name=_('SSH session timeout'),
        help_text=_('The maximum amount of time (in seconds) that the Capybara '
                    'application will wait for a response to an SSH request '
                    'before closing the connection. This helps to prevent '
                    'indefinitely hanging SSH sessions.'),
        default=10,
    )
    ssh_repeat = models.IntegerField(
        verbose_name=_('SSH repeat connection'),
        help_text=_('The number of times the application will retry an SSH '
                    'connection if the initial attempt fails. This setting '
                    'can help improve reliability in unstable network '
                    'environments.'),
        default=2,
    )
    ssh_invalid_responses = models.JSONField(
        verbose_name=_('SSH invalid responses'),
        help_text=_('A list of strings that represent invalid responses from '
                    'the host. These are used to identify and handle errors '
                    'during SSH sessions. For example, certain network devices '
                    'might return specific error messages like "invalid input '
                    'detected" or "command not found" when a command fails.'),
        default=[
            '% Invalid input detected',
            'syntax error, expecting',
            'Error: Unrecognized command',
            '%Error',
            'command not found',
            'Syntax Error: unexpected argument',
            '% Unrecognized command found at',
            'invalid input detected',
            'cdp is not enabled',
            'incomplete command',
            'no spanning tree instance exists',
            'lldp is not enabled',
            'snmp agent not enabled',
        ],
    )
    ssh_max_workers = models.IntegerField(
        verbose_name=_('SSH Max workers'),
        help_text=_('Xxx.'),
        default=10,
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
            'updated': self.updated,
            'notification_level': self.notification_level,
            'logger_level': self.logger_level,
            'logger_db': self.logger_db,
            'logger_cli': self.logger_cli,
            'http_timeout': self.http_timeout,
            'http_default_headers': self.http_default_headers,
            'http_max_workers': self.http_max_workers,
            'ssh_timeout': self.ssh_timeout,
            'ssh_repeat': self.ssh_repeat,
            'ssh_invalid_responses': self.ssh_invalid_responses,
            'ssh_max_workers': self.http_max_workers,
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
        self._update_celery_schedule()

    def update_global_settings_dictionary(self):
        # Collect global settings object content:
        data = self.__dict__
        # Update global settings dictionary:
        global_settings.update(data)

    def _update_celery_schedule(self):
        from django_celery_beat.models import PeriodicTask, IntervalSchedule

        interval, created = IntervalSchedule.objects.get_or_create(
            every=self.collecting_system_data_interval,
            period=IntervalSchedule.MINUTES,
        )

        PeriodicTask.objects.update_or_create(
            name='collect_system_metrics',
            defaults={
                'interval': interval,
                'task': 'collect_system_metrics',
            }
        )

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
