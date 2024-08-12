# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# WanderSwiss - constance import:
from wanderswiss.base.constants.color import ColorChoices

# WanderSwiss - base models import:
from wanderswiss.base.models.identification_model import IdentificationBaseModel


class TagModel(IdentificationBaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

        # Overwrite default permissions:
        default_permissions = ()
        permissions = (
            ('read_write', 'Read and write access.'),
            ('read_only', 'Read only access')
        )

    # Tag color:
    color = models.CharField(
        verbose_name=_('Color'),
        help_text=_('The color associated with this tag. This color helps in '
                    'visually distinguishing tags from each other in the '
                    'interface. Select from the predefined color choices '
                    'available. For example, "blue" might represent information, '
                    '"red" for important or critical items, and "green" for '
                    'success or positive statuses.'),
        max_length=6,
        choices=ColorChoices.choices,
        default=ColorChoices.BLUE,
    )
