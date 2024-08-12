# WanderSwiss - choices model import:
from wanderswiss.base.constants.base.base_choices import BaseIntegerChoices

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class StatusChoices(BaseIntegerChoices):

    # Choices values:
    PUBLISHED = 1, _('Published')
    DRAFT = 2, _('Draft')
