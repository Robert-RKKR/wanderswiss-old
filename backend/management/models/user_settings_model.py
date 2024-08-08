# Python -import:
import copy

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - html template import:
from management.templates.html_templates import base_html_template

# WanderSwiss - base model import:
from wanderswiss.base.models.base_model import BaseModel

# WanderSwiss - model import:
from management.models.user_model import UserModel


# User setting model class:
class UserSettingsModel(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('User settings')
        verbose_name_plural = _('User settings')

        # Overwrite default permissions:
        default_permissions = ()
        permissions = (
            ('read_write', 'Read and write access.'),
            ('read_only', 'Read only access')
        )

    
    # Relation with other models:
    author = models.ForeignKey(
        UserModel, 
        on_delete = models.SET_NULL, 
        null = True, 
        blank = True, 
        verbose_name = _('Author')
    )

    # Model data time information:
    updated = models.DateTimeField(
        verbose_name=_('Updated'),
        help_text=_('The date and time when these user settings were last '
                    'updated. This helps in tracking changes to settings over '
                    'time.'),
        auto_now=True,
    )

    # User settings:

    # object representation:
    def __repr__(self) -> str:
        return str(self.pk)

    def __str__(self) -> str:
        return str(self.pk)

    @property
    def __dict__(self):
        return {
            'updated': self.updated,
        }
