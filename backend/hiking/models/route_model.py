# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - base model import:
from wanderswiss.base.models.identification_model import IdentificationBaseModel
from wanderswiss.base.models.localization_model import LocalizationBaseModel
from wanderswiss.base.models.status_model import StatusBasedModel

# WanderSwiss - choices import:
from wanderswiss.base.constants.choices import ChoicesChoices

# WanderSwiss - models import:
from infopedia.models.choice_model import ChoiceModel
from achievement.models.card_model import CardModel


# WanderSwiss dedicated model:
class RouteModel(
    StatusBasedModel,
    IdentificationBaseModel,
    LocalizationBaseModel):

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
    start_point = models.ForeignKey(
        ChoiceModel, 
        verbose_name = _('Start point'),
        related_name='route_start_point',
        help_text = _('Starting point of the route.'),
        limit_choices_to={'type': ChoicesChoices.POI},
        on_delete = models.PROTECT, 
    )
    middle_points = models.ManyToManyField(
        ChoiceModel, 
        verbose_name = _('Middle points'),
        related_name='route_middle_points',
        help_text = _('All middle points of the route.'),
        limit_choices_to={'type': ChoicesChoices.POI},
        null=True,
        blank=True
    )
    end_point = models.ForeignKey(
        ChoiceModel, 
        verbose_name = _('End point'),
        related_name='route_end_point',
        help_text = _('Ending point of the route.'),
        limit_choices_to={'type': ChoicesChoices.POI},
        on_delete = models.PROTECT,
    )
    route_type = models.ForeignKey(
        ChoiceModel, 
        verbose_name = _('Route type'),
        related_name='route_route_type',
        help_text = _('Ending point of the route.'),
        limit_choices_to={'type': ChoicesChoices.HIKING_DIFFICULTY},
        on_delete = models.PROTECT,
    )

    # Model based values:
    gps_data = models.TextField(
        verbose_name = _('GPS Data'),
        help_text = _('GPS data in XML format.'),
        null=True,
        blank=True
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
        help_text = _('Minimum elevation in meters.'),
        null=True,
        blank=True
    )
    max_elevation = models.FloatField(
        verbose_name = _('Maximum Elevation (m)'), 
        help_text = _('Maximum elevation in meters.')
    )
