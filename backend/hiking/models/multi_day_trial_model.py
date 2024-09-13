# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - base model import:
from wanderswiss.base.models.identification_model import IdentificationBaseModel
from wanderswiss.base.models.status_model import StatusBasedModel
from wanderswiss.base.models.base_m2m_model import BaseM2mModel

# WanderSwiss - models import:
from hiking.models.trial_model import TrialModel


# WanderSwiss dedicated model:
class MultiDayTrialModel(
    StatusBasedModel,
    IdentificationBaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Multi day trial'
        verbose_name_plural = 'Multi day trials'

        # Default ordering:
        ordering = ['-created']

        # Overwrite default permissions:
        default_permissions = ()
        permissions = (
            ('read_write', 'Read and write access.'),
            ('read_only', 'Read only access')
        )

    # Relation with other models:
    trials = models.ManyToManyField(
        TrialModel, 
        through = 'MultiDayTrialTrialModel',
        verbose_name = _('Trials'), 
        help_text = _('Trials that are part of the multi day trial.')
    )

    # Model based values:
    days = models.IntegerField(
        verbose_name = _('Days'), 
        help_text = _('Number of days for the multi day trial.')
    )


# Many to many relation model:
class MultiDayTrialTrialModel(BaseM2mModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Multi day trial & Trial relation'
        verbose_name_plural = 'Multi day trial & Trial relations'

    # Relation with other models:
    trial = models.ForeignKey(
        TrialModel, 
        on_delete = models.CASCADE, 
        verbose_name = _('Trial'), 
        help_text = _('Trial included in the multi day trial.')
    )
    multi_day_trial = models.ForeignKey(
        MultiDayTrialModel, 
        on_delete = models.CASCADE, 
        verbose_name = _('Multi day Trial'), 
        help_text = _('Multi day trial that includes this trial.')
    )

    # Additional M2M values:
    order = models.IntegerField(
        verbose_name = _('Order'), 
        help_text = _('Order of the trial within the multi day trial.')
    )
