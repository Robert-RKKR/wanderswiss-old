# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# WanderSwiss - base model import:
from wanderswiss.base.models.base_model import BaseModel


# Object representation model class:
class ObjectRepresentationModel(BaseModel):

    class Meta:

        # Abstract class value:
        abstract = True

        # Overwrite default permissions:
        default_permissions = ()
        permissions = (
            ('read_write', 'Read and write access.'),
            ('read_only', 'Read only access')
        )

    # Information about correlated object:
    app_name = models.CharField(
        verbose_name=_('Object application name'),
        help_text=_('The name of the application that this object belongs to. '
                    'This helps in identifying the application context of the object.'),
        max_length=64,
        null=True,
        blank=True,
    )
    model_name = models.CharField(
        verbose_name=_('Object model name'),
        help_text=_('The name of the model that this object is an instance of. '
                    'This helps in identifying the type of the object.'),
        max_length=64,
        null=True,
        blank=True,
    )
    object_id = models.CharField(
        verbose_name=_('Object PK number'),
        help_text=_('The primary key (PK) number of the correlated object. '
                    'This is a unique identifier for the object within its model.'),
        max_length=64,
        null=True,
        blank=True,
    )
    object_representation = models.CharField(
        verbose_name=_('Object representation'),
        help_text=_('A string representation of the object. This provides a '
                    'human-readable description or identifier of the object.'),
        max_length=128,
        null=True,
        blank=True,
    )

    # Object representation:
    def __repr__(self) -> str:
        return f'{self.pk}: {self.object_representation}'

    def __str__(self) -> str:
        return  f'{self.pk}: {self.object_representation}'

    # Natural key representation:
    def natural_key(self):
        return str(self.object_representation)
