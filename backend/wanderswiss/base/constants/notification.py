# WanderSwiss - choices model import:
from wanderswiss.base.constants.base.base_choices import BaseIntegerChoices

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class SeverityChoices(BaseIntegerChoices):

    # Choices values:
    CRITICAL = 1, _('Critical')
    ERROR = 2, _('Error')
    WARNING = 3, _('Warning')
    INFO = 4, _('Info')
    DEBUG = 5, _('Debug')


class ExclusionInclusionChoices(BaseIntegerChoices):

    # Choices values:
    NONE = 0, _('None')
    EXCLUDE = 1, _('Exclude')
    INCLUDE = 2, _('Include')


class ApplicationChoices(BaseIntegerChoices):

    # Choices values:
    NONE = 0, _('None')
    WANDERSWISS = 1, _('Wander Swiss')
    ARTICLE = 2, _('Article')
    CARD = 3, _('Card')
    HIKING = 4, _('Hiking')
