# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# WanderSwiss - object representation model import:
from notification.models.object_representation_model import ObjectRepresentationModel

# WanderSwiss - constance import:
from wanderswiss.base.constants.notification import ApplicationChoices
from wanderswiss.base.constants.notification import SeverityChoices


# Log model class:
class LogModel(ObjectRepresentationModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Log')
        verbose_name_plural = _('Logs')

        # Default ordering:
        ordering = ['-timestamp']

        # Overwrite default permissions:
        default_permissions = ()
        permissions = (
            ('read_write', 'Read and write access.'),
            ('read_only', 'Read only access')
        )
    
    # Base log data:
    timestamp = models.DateTimeField(
        verbose_name=_('Timestamp'),
        help_text=_('The date and time when the log entry was created. This '
                    'field is automatically populated when the log is created, '
                    'providing an accurate record of the log event.'),
        auto_now_add=True,
    )
    severity = models.IntegerField(
        verbose_name=_('Severity level'),
        help_text=_('The level of severity associated with the log entry. '
                    'This indicates the importance or urgency of the logged '
                    'event, such as information, warning, or error.'),
        choices=SeverityChoices.choices,
        default=SeverityChoices.DEBUG
    )
    task_id = models.CharField(
        verbose_name=_('Task ID'),
        help_text=_('The unique identifier of the task associated with this '
                    'log entry. This helps in tracking and correlating logs '
                    'to specific tasks or operations within the application.'),
        max_length=64,
        null=True,
        blank=True,
    )
    application = models.IntegerField(
        verbose_name=_('Application'),
        help_text=_('The name of the application that generated this log entry. '
                    'This helps in identifying which part of the system is '
                    'responsible for the logged event.'),
        choices=ApplicationChoices.choices,
        default=ApplicationChoices.NONE
    )
    message = models.CharField(
        verbose_name=_('Message'),
        help_text=_('The log message describing the event. This message '
                    'provides detailed information about the event, which is '
                    'useful for debugging and tracking purposes. The message '
                    'must be between 1 and 1024 characters long.'),
        max_length=1024,
        error_messages={
            'invalid': _('Enter a valid notification message. It must contain '
                        '1 to 1024 digits.'),
        },
    )

    # Execution time:
    execution_time = models.FloatField(
        verbose_name=_('Execution time'),
        help_text=_('The time taken to execute the logged event. This value '
                    'is useful for performance monitoring and optimization.'),
        null=True,
        blank=True,
    )

    # Additional data:
    additional_data = models.JSONField(
        verbose_name=_('Additional data'),
        help_text=_('Any additional data related to the log entry. This can '
                    'include context-specific information that provides more '
                    'insight into the logged event.'),
        null=True,
        blank=True,
    )

    # Object representation:
    def __repr__(self) -> str:
        return f'{self.pk}: {self.message}'

    def __str__(self) -> str:
        return  f'{self.pk}: {self.message}'

    # Natural key representation:
    def natural_key(self):
        return str(self.message)
