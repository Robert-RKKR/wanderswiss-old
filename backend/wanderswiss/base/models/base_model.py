# Python - base import:
import uuid

# Django - models import:
from django.db import models


# Base models class:
class BaseModel(models.Model):

    class Meta:
        
        # Model name values:
        verbose_name = 'Base model'
        verbose_name_plural = 'Base models'

        # Abstract class value:
        abstract = True

    # Define main show variable:
    dashboard_model_data = {}

    # Primary Key value:
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text='Unique identifier for this object. It is automatically '\
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
    
    def save(self, *args, **kwargs):
        # Run dedicated operation before clean:
        self.run_before_save()
        # Run original save method:
        super().save(*args, **kwargs)

    def clean(self):
        # Run dedicated operation before clean:
        self.run_before_clean()
        # Run original clean method:
        super().clean()

    def full_clean(self, *args, **kwargs):
        # Ensure the slug is set before running full_clean
        self.clean()
        # Run original full_clean method:
        super().full_clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not hasattr(self, '_dedicated_operation_ran') or not self._dedicated_operation_ran:
            self.dedicated_operation()
            self._dedicated_operation_ran = True
        self.run_before_save()
        super().save(*args, **kwargs)
        self._dedicated_operation_ran = False  # Reset the flag after save

    def clean(self):
        if not hasattr(self, '_dedicated_operation_ran') or not self._dedicated_operation_ran:
            self.dedicated_operation()
            self._dedicated_operation_ran = True
        self.run_before_clean()
        super().clean()
        self._dedicated_operation_ran = False  # Reset the flag after clean

    def full_clean(self, *args, **kwargs):
        if not hasattr(self, '_dedicated_operation_ran') or not self._dedicated_operation_ran:
            self.dedicated_operation()
            self._dedicated_operation_ran = True
        self.clean()
        # Run original full_clean method:
        super().full_clean(*args, **kwargs)
        self._dedicated_operation_ran = False  # Reset the flag after full_clean

    def as_dictionary(self):
        """
        Return all attributes of the instance as a dictionary.
        """
        # Return dictionary representation:
        return {
            field.name: getattr(self, field.name) for field in self._meta.fields}
