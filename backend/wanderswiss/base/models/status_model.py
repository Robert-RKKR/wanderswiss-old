# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - base models import:
from wanderswiss.base.models.base_model import BaseModel


# Status models class:
class StatusBasedModel(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Status model')
        verbose_name_plural = _('Status models')

        # Abstract class value:
        abstract = True

        # Default ordering:
        ordering = ['created']

    # Model status values:
    is_deleted = models.BooleanField(
        verbose_name=_('Deleted'),
        help_text=_('Indicates if the object is marked as deleted. Deleted '\
                    'objects are not removed from the database.'),
        default=False,
    )
    is_root = models.BooleanField(
        verbose_name=_('Root'),
        help_text=_('Indicates if the object is a root object. Root objects '\
                    'cannot be deleted or modified.'),
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name=_('Active'),
        help_text=_('Indicates if the object is active. Inactive objects have '\
                    'limited functionality and may not appear in queries.'),
        default=True,
    )

    # Model data time information:
    created = models.DateTimeField(
        verbose_name=_('Created'),
        help_text=_('The date and time when the object was created. This '\
                    'timestamp is automatically set when the object is created.'),
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name=_('Updated'),
        help_text=_('The date and time when the object was last updated. '\
                    'This timestamp is automatically updated whenever the '\
                    'object is modified.'),
        auto_now=True,
    )

    # object representation:
    def __repr__(self) -> str:
        return f'PK: {self.pk}'

    def __str__(self) -> str:
        return  f'PK: {self.pk}'

    # Natural key representation:
    def natural_key(self):
        return f'PK: {self.pk}'

    @classmethod
    def show_count_inactive(cls):
        """ Return number of active objects. """
        return cls.objects.filter(is_active=False).count()

    @classmethod
    def show_count_active(cls):
        """ Return number of active objects. """
        return cls.objects.filter(is_active=True).count()

    @classmethod
    def show_creation_dates(cls):
        """ Return number of active objects. """
        # Declare response data value:
        response_data = []
        # Collect query set:
        queryset = cls.objects.values_list(
            'created', flat=True).order_by('created')
        try: # Try to convert collected queryset data:
            data = list(queryset)
            # Iterate thru list:
            for row in data:
                response_data.append(row.strftime("%Y-%m-%d %H:%M:%S %Z"))
        except: # Ignore any errors:
            return False
        # Return collected / converted data:
        return response_data

    @classmethod
    def dashboard(cls):
        """ Return all collected dashboard data. """

        # Collect data from parent class:
        super().dashboard()
        # Collect all dashboard data:
        cls.dashboard_model_data['creation_dates'] = cls.show_creation_dates()
        cls.dashboard_model_data['count_inactive'] = cls.show_count_inactive()
        cls.dashboard_model_data['count_active'] = cls.show_count_active()
        # Return all collected dashboard data:
        return cls.dashboard_model_data
