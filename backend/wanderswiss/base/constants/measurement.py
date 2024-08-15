# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# WanderSwiss - choices model import:
from wanderswiss.base.constants.base.base_choices import BaseIntegerChoices


# Choices class:
class MeasurementSystemChoices(BaseIntegerChoices):

    # Choices values:
    INTERNATIONAL = 1, _('International System')
    IMPERIAL = 2, _('imperial system')
