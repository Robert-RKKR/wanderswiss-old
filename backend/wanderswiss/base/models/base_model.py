# Python - base import:
import uuid
import re

# Django - models import:
from django.db import models

# WanderSwiss - base manager import:
from wanderswiss.base.managers.base_manager import BaseManager


# Base models class:
class BaseModel(models.Model):

    class Meta:
        
        # Model name values:
        verbose_name = 'Base model'
        verbose_name_plural = 'Base models'

        # Abstract class value:
        abstract = True

    # Model objects manager:
    objects = BaseManager()

    # Define main show variable:
    dashboard_model_data = {}

    # Primary Key value:
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text='Unique identifier for this object. It is automatically '
                    'generated and cannot be modified.'
    )

    @classmethod
    def show_count_all(cls):
        """ Return number of existing objects. """
        return cls.objects.count()

    @classmethod
    def dashboard(cls):
        """ Return all collected dashboard data. """

        # Collect all dashboard data:
        cls.dashboard_model_data['count_all'] = cls.show_count_all()
        # Return all collected dashboard data:
        return cls.dashboard_model_data

    # object representation:
    def __repr__(self) -> str:
        """
        WanderSwiss model representation:
        """

        # Collect model representation name:
        model_rep = self.model_representation()
        # Return object representation:
        return f'<WanderSwiss {model_rep}, object: {self.pk}>'

    def __str__(self) -> str:
        """
        WanderSwiss model representation:
        """

        # Collect model representation name:
        model_rep = self.model_representation()
        # Return object representation:
        return f'<WanderSwiss {model_rep}, object: {self.pk}>'

    def natural_key(self) -> str:
        """
        WanderSwiss model representation:
        """

        # Collect model representation name:
        model_rep = self.model_representation()
        # Return object representation:
        return f'<WanderSwiss {model_rep}, object: {self.pk}>'

    # Enriched original Django methods:
    def save(self, *args, **kwargs):
        """
        Enriched original Django save method.
        """

        if not hasattr(self, '_dedicated_operation_ran') or\
            not self._dedicated_operation_ran:
            self.dedicated_operation()
            self._dedicated_operation_ran = True
        # Run before save method:
        self.run_before_save()
        # Run original save method:
        super().save(*args, **kwargs)
        # Reset the flag after save:
        self._dedicated_operation_ran = False

    def clean(self):
        """
        Enriched original Django clean method.
        """

        if not hasattr(self, '_dedicated_operation_ran') or\
            not self._dedicated_operation_ran:
            self.dedicated_operation()
            self._dedicated_operation_ran = True
        # Run before clean method:
        self.run_before_clean()
        # Run original clean method:
        super().clean()
        # Reset the flag after clean:
        self._dedicated_operation_ran = False

    def full_clean(self, *args, **kwargs):
        """
        Enriched original Django full_clean method.
        """

        if not hasattr(self, '_dedicated_operation_ran') or\
            not self._dedicated_operation_ran:
            self.dedicated_operation()
            self._dedicated_operation_ran = True
        self.clean()
        # Run original full_clean method:
        super().full_clean(*args, **kwargs)
        # Reset the flag after full_clean:
        self._dedicated_operation_ran = False

    def as_dictionary(self):
        """
        Return all attributes of the instance as a dictionary.
        """

        # Return dictionary representation:
        return {
            field.name: getattr(self, field.name) for field in self._meta.fields}
    
    # Additional model methods:
    def camel_case_to_spaces(self, name):
        """
        Convert camel case to space-separated words.
        """

        return re.sub(r'(?<!^)(?=[A-Z])', ' ', name).replace('_', ' ')
    
    def model_representation(self):
        """
        Return model string representation.
        """

        return self.camel_case_to_spaces(self.__class__.__name__)
    
    def dedicated_operation(self):
        return None
    
    def run_before_save(self):
        """
        Custom logic to be executed before saving the model.
        """

        pass

    def run_before_clean(self):
        """
        Custom logic to be executed before cleaning the model.
        """

        pass
