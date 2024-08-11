# Django - models import:
from django.db import models

# WanderSwiss - base model import:
from wanderswiss.base.models.identification_model import IdentificationBaseModel


class CardModel(IdentificationBaseModel):

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

    pass