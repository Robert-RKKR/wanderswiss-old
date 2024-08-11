# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# WanderSwiss - object representation model import:
from notification.models.object_representation_model import ObjectRepresentationModel

# WanderSwiss - constance import:
from wanderswiss.base.constants.action_type import ActionTypeChoices

# WanderSwiss - management model import:
from management.models.user_model import UserModel


# Change model class:
class ChangeLogModel(ObjectRepresentationModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Change')
        verbose_name_plural = _('Changes')

        # Default ordering:
        ordering = ['-timestamp']

        # Overwrite default permissions:
        default_permissions = ()
        permissions = (
            ('read_write', 'Read and write access.'),
            ('read_only', 'Read only access')
        )
    
    # Model data time information:
    timestamp = models.DateTimeField(
        verbose_name=_('Timestamp'),
        help_text=_('The date and time when the change was created. This field '
                    'automatically records the exact moment when the change '
                    'entry is added to the log.'),
        auto_now_add=True,
    )

    # User information:
    user = models.ForeignKey(
        UserModel,
        verbose_name=_('User'),
        help_text=_('The user responsible for the change. This field '
                    'links to the user who performed the action, '
                    'providing accountability and traceability.'),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    # Change details:
    action_type = models.IntegerField(
        verbose_name=_('Type of action'),
        help_text=_('The type of action that was performed on the object. This '
                    'could include actions such as creation, modification, or '
                    'deletion of records. The choices are defined in the '
                    'ActionTypeChoices constant.'),
        choices=ActionTypeChoices.choices,
        default=0,
    )
    after = models.JSONField(
        verbose_name=_('JSON object representation after change'),
        help_text=_('The JSON representation of the object after the changes '
                    'were made and saved to the database. This provides a '
                    'snapshot of the object state post-change for auditing '
                    'and rollback purposes.'),
        null=True,
        blank=True,
    )
