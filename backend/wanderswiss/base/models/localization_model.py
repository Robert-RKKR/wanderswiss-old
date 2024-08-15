# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - choices import:
from wanderswiss.base.constants.choices import ChoicesChoices

# WanderSwiss - base models import:
from wanderswiss.base.models.base_model import BaseModel

# WanderSwiss - models import:
from infopedia.models.choice_model import ChoiceModel


# Localization models class:
class LocalizationBaseModel(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('LocalizationModel')
        verbose_name_plural = _('LocalizationModels')
        
        # Abstract class value:
        abstract = True

        # Default ordering:
        ordering = ['created']

    # Localization information:
    regions = models.ManyToManyField(
        ChoiceModel,
        verbose_name = _('Regions'),
        related_name='%(class)s_regions',
        help_text = _('Regions through which the route passes.'),
        limit_choices_to={'type': ChoicesChoices.REGION}
    )
    countries = models.ManyToManyField(
        ChoiceModel,
        verbose_name = _('Countries'),
        related_name='%(class)s_countries',
        help_text = _('Countries through which the route passes.'),
        limit_choices_to={'type': ChoicesChoices.COUNTRY}
    )

    def __init_subclass__(cls, **kwargs):
        # Run original __init_subclass__ method:
        super().__init_subclass__(**kwargs)
        # Add suffix to the relation related name:
        cls.add_related_name_suffix()

    @classmethod
    def add_related_name_suffix(cls):
        # Check if not _meta:
        if not hasattr(cls, '_meta'):
            return
        # Iterate thru model fields:
        for field in cls._meta.fields:
            if isinstance(field, models.ManyToManyField):
                if field.name == 'regions':
                    field.rel.related_name = f'{cls.__name__.lower()}_regions'
                elif field.name == 'countries':
                    field.rel.related_name = f'{cls.__name__.lower()}_countries'
