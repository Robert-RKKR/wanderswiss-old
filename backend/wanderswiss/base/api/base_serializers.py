# Rest framework - imports:
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.exceptions import ValidationError
from rest_framework import serializers

# Drf spectacular - import:
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

# Django - exceptions import:
from django.core.exceptions import MultipleObjectsReturned
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import FieldError

# WanderSwiss - helper function import:
from wanderswiss.base.helper.filters import dict_to_filter_params


# Base serializer class:
class BaseSerializer(serializers.ModelSerializer):
    """
    Base serializer class providing additional functionality.
    """

    @extend_schema_field(OpenApiTypes.STR)
    def get_display(self, obj):
        """
        Get the display representation of an object.
        
        Args:
            obj: The object to get the display representation for.
            
        Returns:
            str: The display representation of the object.
        """
        return str(obj)


# Base nested serializer class:
class WritableNestedSerializer(BaseSerializer):
    """
    Serializer for handling nested objects.
    """

    def to_internal_value(self, data):
        """
        Convert external data representation to internal value.
        
        Args:
            data: The data to be converted.
            
        Returns:
            object: The converted data.
            
        Raises:
            ValidationError: If conversion fails or multiple objects are returned.
        """

        # Check if data (PK) has been provided:
        if data is None:
            # If not return empty response:
            return None

        # Check if provided data is dictionary:
        if isinstance(data, dict):
            # If yes, collect filter parameters:
            params = dict_to_filter_params(data)
            # Collect Django query set:
            queryset = self.Meta.model.objects
            try: # Try to collect object based on provided filters parameters:
                return queryset.get(**params)
            # Return Exceptions:
            except ObjectDoesNotExist:
                # Raise validation error:
                raise ValidationError('Related object not found using '\
                    f'the provided attributes: {params}')
            except MultipleObjectsReturned:
                # Raise Multiple objects returned Error:
                raise ValidationError('Multiple objects match the '\
                    f'provided attributes: {params}')
            except FieldError as error:
                # Raise field error:
                raise ValidationError(error)

        try: # Try to retrieve integer PK value:
            pk = data
        except (TypeError, ValueError):
            # Raise validation error if provided PK is not a number:
            raise ValidationError('Related objects must be referenced by '\
                'numeric ID or by dictionary of attributes. Received an '\
                f'unrecognized value: {data}')

        try: # Try to collect object using PK value:
            return self.Meta.model.objects.get(pk=pk)
        except ObjectDoesNotExist:
            # Raise object does not exist error:
            raise ValidationError('Related object not found using '\
                f'the provided numeric ID: {pk}')


# Field serializer for PrimaryKeyRelatedField:
class SerializedPKRelatedField(PrimaryKeyRelatedField):
    """
    Extends PrimaryKeyRelatedField to return a serialized object on read.
    """

    def __init__(self, serializer, **kwargs):
        self.serializer = serializer
        self.pk_field = kwargs.pop('pk_field', None)
        super().__init__(**kwargs)

    def to_representation(self, value):
        return self.serializer(value, context={
            'request': self.context['request']}).data
