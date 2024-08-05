# Python - regex import:
import re

# Python - json import:
import json

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - validators import:
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


# Name validator:
@deconstructible
class NameValueValidator(RegexValidator):
    """ Validate if specified value is a valid name field. """

    regex = r'^[0-9,A-Z,a-z,-_. ]{4,64}$'
    message = _('The object hostname must contain 4 to 64 digits, '\
        'letters and special characters -, _, . or spaces.')
    flags = 0


# Description validator:
@deconstructible
class DescriptionValueValidator(RegexValidator):
    """ Validate if specified value is a valid description field. """

    regex = r'^[0-9,A-Z,a-z,-_." ]{8,256}$'
    message = _('Description must contain 8 to 256 digits, letters '\
        'and special characters -, _, . or spaces.')
    flags = 0


# Code validator:
@deconstructible
class CodeValueValidator(RegexValidator):
    """ Validate if specified value is a valid code field. """

    regex = r'^[A-Z,a-z]{2,8}$'
    message = _('The object code must contain 2 to 8 letters.')
    flags = 0


@deconstructible
class UrlWithVariablesValidator(RegexValidator):
    """
    Validate if the given value is a standard URL or a URL containing
    template-style variables.
    """
    regex = r'^[a-zA-Z0-9_\/]*(?:\{\{[^{}]*\}\}[a-zA-Z0-9_\/]*)*\/?$'
    message = _('Enter a valid URL or a URL with template '\
        'variables like {{value}}.')
    flags = 0


# Regex validator:
def regex_validator(value):
    """ Validate if specified value is a valid regex expression. """

    pattern = rf'{value}'
    try: # Try to compile given value to regex:
        re.compile(pattern)
    except Exception as exception:
        raise ValidationError(
            _(f'Regex validation error: {exception}'))
