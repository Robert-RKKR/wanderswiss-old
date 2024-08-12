# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - base models import:
from wanderswiss.base.models.base_model import BaseModel


# Localization models class:
class LocalizationBaseModel(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('LocalizationModel')
        verbose_name_plural = _('LocalizationModels')
        
        # Abstract class value:
        abstract = True

        # Default ordering:
        ordering = ['created']

    # Localization information:
    latitude = models.FloatField(
        verbose_name=_('Latitude'),
        help_text=_('Latitude of the location.')
    )
    longitude = models.FloatField(
        verbose_name=_('Longitude'),
        help_text=_('Longitude of the location.')
    )

    # Localization range information:
    range = models.IntegerField(
        verbose_name=_('Localization range'),
        help_text=_('Xxx.'),
        null=True,
        blank=True
    )
