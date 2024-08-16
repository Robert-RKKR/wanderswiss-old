# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# WanderSwiss - base models import:
from wanderswiss.base.models.gps_localization_model import GpsLocalizationBaseModel
from wanderswiss.base.models.identification_model import IdentificationBaseModel
from wanderswiss.base.models.status_model import StatusBasedModel

# WanderSwiss - choices import:
from wanderswiss.base.constants.choices import ChoicesChoices


# WanderSwiss dedicated model:
class ChoiceModel(
    StatusBasedModel,
    IdentificationBaseModel,
    GpsLocalizationBaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Choice')
        verbose_name_plural = _('Choices')

        # Overwrite default permissions:
        default_permissions = ()
        permissions = (
            ('read_write', 'Read and write access.'),
            ('read_only', 'Read only access')
        )

    # Type related values:
    type = models.IntegerField(
        choices=ChoicesChoices.choices,
        verbose_name = _('Choice type'),
        help_text = _('Xxx.'),
        default=ChoicesChoices.POI
    )
    content = models.TextField(
        verbose_name = _('Content'),
        help_text = _('Xxx.'),
    )
