# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - base model import:
from wanderswiss.base.models.identification_model import IdentificationBaseModel
from wanderswiss.base.models.status_model import StatusBasedModel
from wanderswiss.base.models.user_model import UserBaseModel


# WanderSwiss dedicated model:
class ProfileModel(
    StatusBasedModel,
    IdentificationBaseModel,
    UserBaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

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
