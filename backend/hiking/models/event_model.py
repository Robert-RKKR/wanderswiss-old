# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - base model import:
from wanderswiss.base.models.identification_model import IdentificationBaseModel
from wanderswiss.base.models.localization_model import LocalizationBaseModel
from wanderswiss.base.models.status_model import StatusBasedModel
from wanderswiss.base.models.user_m2m_model import UserM2mModel

# WanderSwiss - user model import:
from management.models.user_model import UserModel

# WanderSwiss - hiking model import:
from hiking.models.route_model import RouteModel


# WanderSwiss dedicated model:
class EventModel(
    StatusBasedModel,
    IdentificationBaseModel,
    LocalizationBaseModel):


    class Meta:
        
        # Model name values:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

        # Default ordering:
        ordering = ['-created']

        # Overwrite default permissions:
        default_permissions = ()
        permissions = (
            ('read_write', 'Read and write access.'),
            ('read_only', 'Read only access')
        )

    # Relation with other models:
    users = models.ManyToManyField(
        UserModel, 
        through='UserEventModel',
        verbose_name=_('Event Participants'), 
        help_text=_('Users who are participating in this event, '
                    'through multi-day trials or individual trials '
                    'linked to this event.')
    )
    route = models.ForeignKey(
        RouteModel,
        on_delete=models.PROTECT,
        verbose_name=_('Hiking Route'),
        help_text=_('The route that will be taken during this event.'),
        null=True,
        blank=True
    )


class UserEventModel(UserM2mModel):


    class Meta:
        
        # Model name values:
        verbose_name = 'User Event relation'
        verbose_name_plural = 'User Event relations'

    # Relation with other models:
    event = models.ForeignKey(
        EventModel, 
        on_delete=models.CASCADE, 
        verbose_name=_('Related Event'),
        help_text=_('The specific event this user is participating in. If'
                    'the event is deleted, this record will also be removed.')
    )

    # Additional M2M values:
    participant_id = models.CharField(
        verbose_name=_('Event Participant Identification Number'),
        help_text=_('Unique ID assigned to the participant by the event '
                    'organizer. This ID is specific to the walk event, '
                    'used for tracking, communication, and identification. '
                    'It ensures proper registration and identification of each '
                    'participant throughout the event.'),
        max_length=64
    )
