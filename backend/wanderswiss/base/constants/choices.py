# WanderSwiss - choices model import:
from wanderswiss.base.constants.base.base_choices import BaseIntegerChoices

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class ChoicesChoices(BaseIntegerChoices):

    # Choices values:
    ACHIEVEMENT_DIFFICULTY = 1, _('Achievement difficulty')
    CARD_DIFFICULTY = 2, _('Card difficulty')
    POI = 3, _('Point of Interest')
    CARD_TYPE = 4, _('Cart type')
    COUNTRY = 5, _('Country')
    REGION = 6, _('Region')
