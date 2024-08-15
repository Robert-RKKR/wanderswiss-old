# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db.models import Max
from django.db import models

# WanderSwiss - base model import:
from wanderswiss.base.models.gps_localization_model import GpsLocalizationBaseModel
from wanderswiss.base.models.identification_model import IdentificationBaseModel
from wanderswiss.base.models.localization_model import LocalizationBaseModel
from wanderswiss.base.models.status_model import StatusBasedModel

# WanderSwiss - choices import:
from wanderswiss.base.constants.choices import ChoicesChoices

# WanderSwiss - models import:
from infopedia.models.choice_model import ChoiceModel


# WanderSwiss dedicated model:
class CardModel(
    StatusBasedModel,
    IdentificationBaseModel,
    GpsLocalizationBaseModel,
    LocalizationBaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

        # Default ordering:
        ordering = ['-created']

        # Overwrite default permissions:
        default_permissions = ()
        permissions = (
            ('read_write', 'Read and write access.'),
            ('read_only', 'Read only access')
        )

    # Dedicated value:
    identification_number = models.CharField(
        verbose_name=_('Identification Number'),
        help_text=_('Unique identification number in the format 0000.'),
        max_length=4,
        editable=False,
        unique=True,
    )

    # Choice One to One relation:
    type = models.ForeignKey(
        ChoiceModel,
        verbose_name = _('Type'),
        related_name='card_type',
        help_text = _('Xxx.'),
        limit_choices_to={'type': ChoicesChoices.CARD_TYPE},
        on_delete = models.PROTECT,
    )

    # Choice One to Many relations:
    difficulties = models.ManyToManyField(
        ChoiceModel,
        verbose_name = _('Difficulties'),
        related_name='card_difficulties',
        help_text = _('Xxx.'),
        limit_choices_to={'type': ChoicesChoices.HIKING_DIFFICULTY}
    )

    # Card details:
    altitude = models.TextField(
        verbose_name = _('Altitude'),
        help_text = _('Xxx.')
    )
    
    def dedicated_operation(self):
        # Call the original dedicated_operation method:
        super().dedicated_operation()
        # Generate a new identification number:
        self._generate_identification_number()

    def _generate_identification_number(self):
        """
        Generate a new identification number.
        """

        if not self.identification_number:
            max_id = CardModel.objects.aggregate(
                max_id=Max('identification_number'))['max_id']
            if max_id:
                max_id = int(max_id)
            else:
                max_id = 0
            self.identification_number = f'{max_id + 1:04d}'
