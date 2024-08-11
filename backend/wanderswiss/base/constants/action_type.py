# WanderSwiss - base integer model import:
from wanderswiss.base.constants.base.base_choices import BaseIntegerChoices

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class ActionTypeChoices(BaseIntegerChoices):

    # Choices values:
    EMPTY = 0, _('Empty')
    CREATE = 1, _('Create')
    UPDATE = 2, _('Update')
    DELETE = 3, _('Delete')
