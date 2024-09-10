# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - base models import:
from wanderswiss.base.models.base_m2m_model import BaseM2mModel

# WanderSwiss - user model import:
from management.models.user_model import UserModel


# User models class:
class UserM2mModel(BaseM2mModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('BaseM2mModel')
        verbose_name_plural = _('BaseM2mModels')
        
        # Abstract class value:
        abstract = True

        # Default ordering:
        ordering = ['id']
        
    # Relation with other models:
    user = models.ForeignKey(
        UserModel, 
        on_delete=models.CASCADE, 
        verbose_name=_('Event Participant'),
        help_text=_('The participant (user) associated with this event. If '
                    'the user is deleted, this record will also be removed.')
    )
