# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - validators import:
from django.core.exceptions import ValidationError

# Schema values:
DICT_SCHEMA = {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'Key': {'type': 'string'},
            'Value': {'type': 'string'},
        },
    }
}
LIST_SCHEMA = {
    'type': 'array',
    'items': {
        'type': 'string'
    }
}

# Helper factions:
def is_valid_type(value):
    """
    Checks if the given value is of a valid type.
    """
    return isinstance(value, (int, bool, str, type(None)))

def validate_dict(d):
    """
    Validates if the given dictionary has keys and values of valid types.
    """
    if not isinstance(d, dict):
        return False
    return all(is_valid_type(k) and is_valid_type(v) for k, v in d.items())

# JSON list validator:
def json_list_validator(value):
    """
    Validate if specified value is a valid list.
    """

    # Check if provided value is a valid dictionary:
    if not isinstance(value, list):
        # If not raise validation error:
        raise ValidationError(_('Only a list value is allowed.'))

# JSON dictionary validator:
def json_dictionary_validator(value):
    """
    Validate if specified value is a valid dictionary.
    """

    # Check if provided value is a valid dictionary:
    if not isinstance(value, dict):
        # If not raise validation error:
        raise ValidationError(_('Only a dictionary value is allowed.'))
    
def json_dictionary_str_int_bool_validator(value):
    return NotImplementedError

# JSON dictionary validator:
def json_list_dict_validator(value):
    """
    Validate if specified value is a valid dictionary.
    Dictionary can only contains strings, integers, or bools
    values as keys and key values.
    """

    def validate_value(value):
        if value is None:
            return True
        elif isinstance(value, dict):
            return validate_dict(value)
        return False
    
    status = None
    # Check if provided value is a valid list:
    if isinstance(value, list):
        # Check if all list values are dictionary's:
        for x in value:
            if not validate_value(x):
                status = False
    if status is False:
        raise ValidationError(_('Only a list of dictionaries that contains '\
            'key and key values that are strings are allowed.'))
