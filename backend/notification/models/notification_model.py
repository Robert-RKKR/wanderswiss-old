# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# WanderSwiss - constance import:
from wanderswiss.base.constants.notification import SeverityChoices

# WanderSwiss - base model import:
from wanderswiss.base.models.base_model import BaseModel


# Notification model class:
class NotificationModel(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')

        # Default ordering:
        ordering = ['-timestamp']

        # Overwrite default permissions:
        default_permissions = ()
        permissions = (
            ('read_write', 'Read and write access.'),
            ('read_only', 'Read only access')
        )
    
    # Base notification data:
    timestamp = models.DateTimeField(
        verbose_name=_('Timestamp'),
        help_text=_('The date and time when the notification was created. '
                    'This field is automatically populated when the '
                    'notification is created.'),
        auto_now_add=True,
    )
    severity = models.IntegerField(
        verbose_name=_('Severity level'),
        help_text=_('The severity level of the notification. Indicates the '
                    'importance or urgency of the notification.'),
        choices=SeverityChoices.choices,
        default=0,
    )
    task_id = models.CharField(
        verbose_name=_('Task ID'),
        help_text=_('The unique identifier of the task associated with this '
                    'notification. Helps in tracking and correlating '
                    'notifications to specific tasks.'),
        max_length=64,
        null=True,
        blank=True,
    )
    message = models.CharField(
        verbose_name=_('Message'),
        help_text=_('The notification message detailing the event or action. '
                    'This message provides information about the notification. '
                    'The message must be between 1 and 1024 characters long.'),
        max_length=1024,
        error_messages={
            'invalid': _('Enter a valid notification message. It must contain '
                        '1 to 1024 digits.'),
        },
    )
    url = models.CharField(
        verbose_name=_('URL'),
        help_text=_('The URL to the object related to this notification. '
                    'This can be used to provide a direct link to the relevant '
                    'object or page within the application.'),
        max_length=256,
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
