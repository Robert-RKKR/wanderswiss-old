# Django - integer model import:
from django.db.models import IntegerChoices
from django.db.models import TextChoices

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Base integer choices class:
class BaseIntegerChoices(IntegerChoices):

    @classmethod
    def value_from_int(cls, int_to_search):
        """
        Returns a xxx.
        """

        # Iterate thru all chaises:
        for choice in cls.choices:
            if choice[0] == int_to_search:
                return choice[1]
        # If not found return False value:
        return False

    @classmethod
    def value_from_str(cls, str_to_search):
        """
        Returns a xxx.
        """

        # Iterate thru all chaises:
        for choice in cls.choices:
            if choice[1] == str_to_search:
                return choice[0]
        # If not found return False value:
        return False

    @classmethod
    def standard_value(cls):
        """
        Returns a xxx.
        """

        list_of_values = []
        # Iterate thru all chaises:
        for choice in cls.choices:
            list_of_values.append((choice[0], choice[1]))
        # Return all collected values:
        return list_of_values

    @classmethod
    def tuple_from_first_values(cls):
        """
        Returns a list of all choices as (value, display name) tuples.
        """

        return tuple(choice[0] for choice in cls.choices)

    @classmethod
    def tuple_from_second_values(cls):
        """
        Returns a list of all choices as (value, display name) tuples.
        """

        return tuple(choice[1] for choice in cls.choices)


# Base string choices class:
class BaseStringChoices(TextChoices):

    @classmethod
    def value_from_str(cls, str_to_search):
        """
        Returns a xxx.
        """

        # Iterate thru all chaises:
        for choice in cls.choices:
            if choice[0] == str_to_search:
                return choice[1]
        # If not found return False value:
        return False

    @classmethod
    def value_from_int(cls, int_to_search):
        """
        Returns a xxx.
        """

        # Iterate thru all chaises:
        for choice in cls.choices:
            if choice[1] == int_to_search:
                return choice[0]
        # If not found return False value:
        return False

    @classmethod
    def standard_value(cls):
        """
        Returns a xxx.
        """

        list_of_values = []
        # Iterate thru all chaises:
        for choice in cls.choices:
            list_of_values.append((choice[0], choice[1]))
        # Return all collected values:
        return list_of_values

    @classmethod
    def tuple_from_first_values(cls):
        """
        Returns a list of all choices as (value, display name) tuples.
        """

        return tuple(choice[0] for choice in cls.choices)

    @classmethod
    def tuple_from_second_values(cls):
        """
        Returns a list of all choices as (value, display name) tuples.
        """

        return tuple(choice[1] for choice in cls.choices)
