# Django - models import:
from django.db import models

# WanderSwiss - base model import:
from components.base.models.identification_model import IdentificationBaseModel


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

    gps_data = models.TextField(
        verbose_name='GPS Data',
        help_text='GPS data in XML format.'
    )
    cantons = models.IntegerField(
        choices=CantonChoices.choices,
        verbose_name='Cantons',
        help_text='Canton(s) through which the route passes.'
    )
    distance = models.FloatField(
        verbose_name='Distance (km)', 
        help_text='Distance of the route in kilometers.'
    )
    ascents = models.FloatField(
        verbose_name='Ascents (m)',
        help_text='Total ascents in meters.'
    )
    descents = models.FloatField(
        verbose_name='Descents (m)', 
        help_text='Total descents in meters.'
    )
    min_elevation = models.FloatField(
        verbose_name='Minimum Elevation (m)', 
        help_text='Minimum elevation in meters.'
    )
    max_elevation = models.FloatField(
        verbose_name='Maximum Elevation (m)', 
        help_text='Maximum elevation in meters.'
    )
    roads_type = models.IntegerField(
        choices=RoadTypeChoices.choices, 
        verbose_name='Roads Type', 
        help_text='Type of roads on the route.'
    )
    start_point = models.ForeignKey(
        'self', 
        related_name='route_start', 
        on_delete=models.CASCADE, 
        verbose_name='Start Point', 
        help_text='Starting point of the route.'
    )
    end_point = models.ForeignKey(
        'self', 
        related_name='route_end', 
        on_delete=models.CASCADE, 
        verbose_name='End Point', 
        help_text='Ending point of the route.'
    )
    cards = models.ManyToManyField(
        CardModel, 
        verbose_name='Cards', 
        help_text='Cards related to the route.'
    )
