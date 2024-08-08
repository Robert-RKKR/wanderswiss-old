# WanderSwiss - choices model import:
from wanderswiss.base.constants.base.base_choices import BaseIntegerChoices

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class UserRoleChoices(BaseIntegerChoices):

    # Choices values:
    ADMINISTRATOR = 1, _('Administrator')
    AUTHOR = 2, _('Author')
    USER = 3, _('User')
