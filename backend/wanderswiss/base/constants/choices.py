# WanderSwiss - choices model import:
from wanderswiss.base.constants.base.base_choices import BaseIntegerChoices

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class ChoicesChoices(BaseIntegerChoices):

    # Choices values:
    REGION = 1, _('Region')
    POI = 2, _('Point of Interest')
