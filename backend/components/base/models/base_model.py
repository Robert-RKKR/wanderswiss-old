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
        raise NotImplementedError(
            'Dedicated operation has not been yet implemented.')
    
    def save(self, *args, **kwargs):
        # Run dedicated operation before clean:
        self.dedicated_operation()
        # Run original save method:
        super().save(*args, **kwargs)

    def clean(self):
        # Run dedicated operation before clean:
        self.dedicated_operation()
        # Run original clean method:
        super().clean()

    def full_clean(self, *args, **kwargs):
        # Ensure the slug is set before running full_clean
        self.clean()
        # Run original full_clean method:
        super().full_clean(*args, **kwargs)

    def as_dictionary(self):
        """
        Return all attributes of the instance as a dictionary.
        """
        # Return dictionary representation:
        return {
            field.name: getattr(self, field.name) for field in self._meta.fields}
