# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# WanderSwiss - choices model import:
from wanderswiss.base.constants.base.base_choices import BaseStringChoices


# Choices class:
class IconChoices(BaseStringChoices):

    # Choices values:
    ADMINISTRATOR = 'fa-regular fa-user', _('Administrator')
    CIRCLE = 'bi bi-1-circle', _('Circle')
