# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - base model import:
from wanderswiss.base.models.identification_model import IdentificationBaseModel

# WanderSwiss - choices import:
from wanderswiss.base.constants.regions import RegionChoices

# WanderSwiss - models import:
from cards.models.card_model import CardModel


class RouteModel(IdentificationBaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'

        # Default ordering:
        ordering = ['-timestamp']

        # Overwrite default permissions:
        default_permissions = ()
        permissions = (
            ('read_write', 'Read and write access.'),
            ('read_only', 'Read only access')
        )

    # Relation with other models:
    cards = models.ManyToManyField(
        CardModel, 
        verbose_name = _('Cards'), 
        help_text = _('Cards related to the route.')
    )

    # Model based values:
    gps_data = models.TextField(
        verbose_name = _('GPS Data'),
        help_text = _('GPS data in XML format.')
    )
    regions = models.IntegerField(
        choices = RegionChoices.choices,
        verbose_name = _('Regions'),
        help_text = _('Region(s) through which the route passes.')
    )
    distance = models.FloatField(
        verbose_name = _('Distance (km)'), 
        help_text = _('Distance of the route in kilometers.')
    )
    ascents = models.FloatField(
        verbose_name = _('Ascents (m)'),
        help_text = _('Total ascents in meters.')
    )
    descents = models.FloatField(
        verbose_name = _('Descents (m)'), 
        help_text = _('Total descents in meters.')
    )
    min_elevation = models.FloatField(
        verbose_name = _('Minimum Elevation (m)'), 
        help_text = _('Minimum elevation in meters.')
    )
    max_elevation = models.FloatField(
        verbose_name = _('Maximum Elevation (m)'), 
        help_text = _('Maximum elevation in meters.')
    )
    roads_type = models.IntegerField(
        choices = RoadTypeChoices.choices, 
        verbose_name = _('Roads Type'), 
        help_text = _('Type of roads on the route.')
    )
    start_point = models.ForeignKey(
        'self', 
        related_name = _('route_start'), 
        on_delete = models.CASCADE, 
        verbose_name = _('Start Point'), 
        help_text = _('Starting point of the route.')
    )
    end_point = models.ForeignKey(
        'self', 
        related_name = _('route_end'), 
        on_delete = models.CASCADE, 
        verbose_name = _('End Point'), 
        help_text = _('Ending point of the route.')
    )
