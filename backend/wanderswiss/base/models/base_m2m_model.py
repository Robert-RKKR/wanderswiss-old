# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models


# WanderSwiss - base models import:
from wanderswiss.base.models.base_model import BaseModel


# Base models class:
class BaseM2mModel(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('BaseM2mModel')
        verbose_name_plural = _('BaseM2mModels')
        
        # Abstract class value:
        abstract = True

        # Default ordering:
        ordering = ['id']
        
    pass
