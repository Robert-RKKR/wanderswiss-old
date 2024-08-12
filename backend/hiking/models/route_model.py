# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - base model import:
from wanderswiss.base.models.identification_model import IdentificationBaseModel
from wanderswiss.base.models.status_model import StatusBasedModel

# WanderSwiss - choices import:
from wanderswiss.base.constants.choices import ChoicesChoices
from wanderswiss.base.constants.road import RoadTypeChoices

# WanderSwiss - models import:
from infopedia.models.choice_model import ChoiceModel
from achievement.models.card_model import CardModel


# WanderSwiss dedicated model:
class RouteModel(
    StatusBasedModel,
    IdentificationBaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'

        # Default ordering:
        ordering = ['-created']

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

    # Choice relation:
    regions = models.ManyToManyField(
        ChoiceModel,
        verbose_name = _('Regions'),
        related_name='route_regions',
        help_text = _('Region(s) through which the route passes.'),
        limit_choices_to={'type': ChoicesChoices.REGION}
    )
    start_point = models.ForeignKey(
        ChoiceModel, 
        verbose_name = _('Start Point'),
        related_name='route_start_point',
        help_text = _('Starting point of the route.'),
        limit_choices_to={'type': ChoicesChoices.POI},
        on_delete = models.PROTECT, 
    )
    end_point = models.ForeignKey(
        ChoiceModel, 
        verbose_name = _('End Point'),
        related_name='route_end_point',
        help_text = _('Ending point of the route.'),
        limit_choices_to={'type': ChoicesChoices.POI},
        on_delete = models.PROTECT,
    )

    # Model based values:
    gps_data = models.TextField(
        verbose_name = _('GPS Data'),
        help_text = _('GPS data in XML format.')
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
