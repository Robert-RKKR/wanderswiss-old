# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - base model import:
from wanderswiss.base.models.identification_model import IdentificationBaseModel
from wanderswiss.base.models.language_model import LanguageBaseModel
from wanderswiss.base.models.status_model import StatusBasedModel


# WanderSwiss dedicated model:
class CategoryModel(
    StatusBasedModel,
    IdentificationBaseModel,
    LanguageBaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

        # Default ordering:
        ordering = ['-created']

        # Overwrite default permissions:
        default_permissions = ()
        permissions = (
            ('read_write', 'Read and write access.'),
            ('read_only', 'Read only access')
        )
        
    pass
