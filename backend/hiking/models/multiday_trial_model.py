# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - base model import:
from wanderswiss.base.models.identification_model import IdentificationBaseModel

# WanderSwiss - models import:
from hiking.models.trial_model import TrialModel


class MultidayTrialModel(IdentificationBaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Multiday trial'
        verbose_name_plural = 'Multiday trials'

        # Default ordering:
        ordering = ['-timestamp']

        # Overwrite default permissions:
        default_permissions = ()
        permissions = (
            ('read_write', 'Read and write access.'),
            ('read_only', 'Read only access')
        )

    # Relation with other models:
    trials = models.ManyToManyField(
        TrialModel, 
        through = _('MultidayTrialTrialModel'),
        verbose_name = _('Trials'), 
        help_text = _('Trials that are part of the multiday trial.')
    )

    # Model based values:
    days = models.IntegerField(
        verbose_name = _('Days'), 
        help_text = _('Number of days for the multiday trial.')
    )


class MultidayTrialTrialModel(models.Model):

    # Relation with other models:
    trial = models.ForeignKey(
        TrialModel, 
        on_delete = models.CASCADE, 
        verbose_name = _('Trial'), 
        help_text = _('Trial included in the multiday trial.')
    )
    multiday_trial = models.ForeignKey(
        MultidayTrialModel, 
        on_delete = models.CASCADE, 
        verbose_name = _('Multiday Trial'), 
        help_text = _('Multiday trial that includes this trial.')
    )

    # Model based values:
    order = models.IntegerField(
        verbose_name = _('Order'), 
        help_text = _('Order of the trial within the multiday trial.')
    )

    def __str__(self):
        return f'{self.multiday_trial.name} includes {self.trial.name} in order {self.order}'
