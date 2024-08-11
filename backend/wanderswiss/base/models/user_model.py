# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - base models import:
from wanderswiss.base.models.identification_model import IdentificationBaseModel

# WanderSwiss - management model import:
from management.models.user_model import UserModel


# User models class:
class UserBaseModel(IdentificationBaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('UserModel')
        verbose_name_plural = _('UserModels')
        
        # Abstract class value:
        abstract = True

        # Default ordering:
        ordering = ['created']

    # User information:
    user = models.ForeignKey(
        UserModel,
        verbose_name=_('User'),
        help_text=_('User responsible for the provided object. This field '\
                    'links to the user who created or is managing this object.'),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
