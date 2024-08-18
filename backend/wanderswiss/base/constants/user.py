# WanderSwiss - choices model import:
from wanderswiss.base.constants.base.base_choices import BaseIntegerChoices

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class UserRoleChoices(BaseIntegerChoices):

    # Choices values:

    # Full access:
    ADMINISTRATOR = 1, _('Administrator')
    # RW access to their content across all apps:
    AUTHOR = 2, _('Author')
    # RW access only to Hiking app content they created:
    GUEST = 3, _('Guest')
