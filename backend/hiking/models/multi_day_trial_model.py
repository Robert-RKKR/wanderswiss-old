# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - base model import:
from wanderswiss.base.models.identification_model import IdentificationBaseModel

# WanderSwiss - models import:
from hiking.models.trial_model import TrialModel


class MultiDayTrialModel(IdentificationBaseModel):

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


class MultiDayTrialTrialModel(models.Model):

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

    # Model based values:
    order = models.IntegerField(
        verbose_name = _('Order'), 
        help_text = _('Order of the trial within the multi day trial.')
    )

    def __str__(self):
        return f'{self.multi_day_trial.name} includes {self.trial.name} in order {self.order}'
