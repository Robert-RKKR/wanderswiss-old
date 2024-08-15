# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - choices import:
from wanderswiss.base.constants.language import LanguageChoices

# WanderSwiss - base models import:
from wanderswiss.base.models.base_model import BaseModel


# Language models class:
class LanguageBaseModel(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('LanguageBaseModel')
        verbose_name_plural = _('LanguageBaseModels')
        
        # Abstract class value:
        abstract = True

        # Default ordering:
        ordering = ['created']

    # Language information:
    language = models.CharField(
        choices=LanguageChoices.choices,
        verbose_name = _('Language'),
        help_text = _('Xxx.'),
        default=LanguageChoices.EN,
        max_length=2
    )
