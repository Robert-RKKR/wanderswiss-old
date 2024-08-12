# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - base model import:
from wanderswiss.base.models.identification_model import IdentificationBaseModel
from wanderswiss.base.models.status_model import StatusBasedModel

# WanderSwiss - choices import:
from wanderswiss.base.constants.choices import ChoicesChoices

# WanderSwiss - models import:
from infopedia.models.choice_model import ChoiceModel


class AchievementModel(
    StatusBasedModel,
    IdentificationBaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'

        # Default ordering:
        ordering = ['-created']

        # Overwrite default permissions:
        default_permissions = ()
        permissions = (
            ('read_write', 'Read and write access.'),
            ('read_only', 'Read only access')
        )

    # Choice One to One relation:
    difficulty = models.ForeignKey(
        ChoiceModel,
        verbose_name=_('Difficulty'),
        related_name='achievement_difficulty',
        help_text=_('Difficulty level of the achievement.'),
        limit_choices_to={'type': ChoicesChoices.ACHIEVEMENT_DIFFICULTY},
        on_delete=models.PROTECT,
    )

    # Base information:
    points = models.IntegerField(
        verbose_name=_('Points'),
        help_text=_('Points awarded for this achievement.')
    )
    conditions = models.JSONField(
        verbose_name=_('Conditions'),
        help_text=_('Xxx.'),
        # validators=[json_list_validator]
    )
