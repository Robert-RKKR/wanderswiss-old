# python - import:
import time

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - slugify import:
from django.template.defaultfilters import slugify

# Django - models import:
from django.db import models

# WanderSwiss - base validators Import:
from wanderswiss.base.validators.base_validator import DescriptionValueValidator
from wanderswiss.base.validators.base_validator import NameValueValidator

# WanderSwiss - base models import:
from wanderswiss.base.models.base_model import BaseModel

# WanderSwiss - choice import:
from wanderswiss.base.constants.icon import IconChoices


# Identification models class:
class IdentificationBaseModel(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('IdentificationModel')
        verbose_name_plural = _('IdentificationModels')

        # Abstract class value:
        abstract = True

        # Default ordering:
        ordering = ['name']

    # Model validators:
    name_validator = NameValueValidator()
    description_validator = DescriptionValueValidator()

    # Identification values:
    name = models.CharField(
        verbose_name=_('Name'),
        help_text=_('Unique name for the object. Must be between 3 and 64 '\
                    'characters long, and can include letters, digits, '\
                    'spaces, or special characters such as -, _.'),
        max_length=64,
        validators=[name_validator],
        error_messages={
            'invalid': _('Enter a valid name. It must contain 3 to 64 digits, '\
                        'letters, or special characters -, _ or spaces.'),
        },
    )
    slug = models.CharField(
        verbose_name=_('Slug'),
        help_text=_('Unique slug representation of the object. Generated '\
                    'automatically from the name.'),
        max_length=128,
    )
    description = models.CharField(
        verbose_name=_('Description'),
        help_text=_('Detailed description of the object. Must be between 8 '\
                    'and 256 characters long and can include letters, '\
                    'digits, spaces, and special characters -, _, .'),
        max_length=256,
        validators=[description_validator],
        error_messages={
            'invalid': _('Enter a valid description. It must contain 8 to '\
                        '256 digits, letters, and special characters -, _, . '\
                        'or spaces.'),
        },
        null=True,
        blank=True,
    )
    ico = models.CharField(
        choices=IconChoices.choices,
        verbose_name=_('Object ico'),
        help_text=_('Graphical representation of the object. Default value '\
                    'is Administrator icon.'),
        default=IconChoices.ADMINISTRATOR,
        max_length=64,
    )
    is_dynamic = models.BooleanField(
        verbose_name=_('Is dynamic'),
        help_text=_('Indicates if this device was dynamically created. '\
                    'Dynamic devices are often generated based on specific '\
                    'conditions or user input at runtime.'),
        default=False,
    )

    def __init__(self, *args, **kwargs):
        """
        Base init method.
        """
        
        super().__init__(*args, **kwargs)
        if not self.description:
            self.description = f'{self.model_representation()} '\
                'default description.'

    # object representation:
    def __repr__(self) -> str:
        """
        WanderSwiss model representation:
        """

        # Collect model representation name:
        model_rep = self.model_representation()
        # Return object representation:
        return f'<{model_rep}: {self.name}>'

    def __str__(self) -> str:
        """
        WanderSwiss model representation:
        """

        # Collect model representation name:
        model_rep = self.model_representation()
        # Return object representation:
        return f'<{model_rep}: {self.name}>'

    def natural_key(self) -> str:
        """
        WanderSwiss model representation:
        """

        # Collect model representation name:
        model_rep = self.model_representation()
        # Return object representation:
        return f'<{model_rep}: {self.name}>'
    
    # Additional model methods:
    def dedicated_operation(self):
        # Call the original dedicated_operation method:
        super().dedicated_operation()
        # Generate a new name is object is dynamic:
        self._generate_name()
        # Set the slug field before validation:
        self.slug = slugify(self.name)

    def _generate_name(self):
        """
        Generate name for dynamic objects.
        """
        if self.is_dynamic:
            date = time.perf_counter()
            name = f'Dynamic object {date}'
            self.name = name
