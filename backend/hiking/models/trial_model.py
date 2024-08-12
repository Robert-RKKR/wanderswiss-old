# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - base model import:
from wanderswiss.base.models.identification_model import IdentificationBaseModel
from wanderswiss.base.models.status_model import StatusBasedModel

# WanderSwiss - models import:
from hiking.models.route_model import RouteModel


# WanderSwiss dedicated model:
class TrialModel(
    StatusBasedModel,
    IdentificationBaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Trial'
        verbose_name_plural = 'Trials'

        # Default ordering:
        ordering = ['-created']

        # Overwrite default permissions:
        default_permissions = ()
        permissions = (
            ('read_write', 'Read and write access.'),
            ('read_only', 'Read only access')
        )

    # Relation with other models:
    routes = models.ManyToManyField(
        RouteModel, 
        through = 'TrialRouteModel', 
        verbose_name = _('Routes'), 
        help_text = _('Routes that are part of the trial.')
    )


class TrialRouteModel(models.Model):

    # Relation with other models:
    trial = models.ForeignKey(
        TrialModel, 
        on_delete = models.CASCADE, 
        verbose_name = _('Trial'), 
        help_text = _('Trial that includes this route.')
    )
    route = models.ForeignKey(
        RouteModel, 
        on_delete = models.CASCADE, 
        verbose_name = _('Route'), 
        help_text = _('Route included in the trial.')
    )

    # Model based values:

    def __str__(self):
        return f'{self.trial.name} includes {self.route.name}'
