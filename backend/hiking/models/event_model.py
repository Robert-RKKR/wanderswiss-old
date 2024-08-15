# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - base model import:
from wanderswiss.base.models.identification_model import IdentificationBaseModel
from wanderswiss.base.models.localization_model import LocalizationBaseModel
from wanderswiss.base.models.status_model import StatusBasedModel


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

    #
    participant_id = models.CharField(
        verbose_name = _('Participant identification number'),
        help_text = _('Xxx.'),
        max_length=64
    )
