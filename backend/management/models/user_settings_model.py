# Python -import:
import copy

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - models import:
from django.db import models

# WanderSwiss - choices import:
from wanderswiss.base.constants.measurement import MeasurementSystemChoices

# WanderSwiss - base model import:
from wanderswiss.base.models.base_model import BaseModel

# WanderSwiss - model import:
from management.models.user_model import UserModel

# User settings dictionary:
user_settings = {}


# User setting model class:
class UserSettingsModel(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('User settings')
        verbose_name_plural = _('User settings')

        # Overwrite default permissions:
        default_permissions = ()
        permissions = (
            ('read_write', 'Read and write access.'),
            ('read_only', 'Read only access')
        )

    
    # Relation with other models:
    user = models.ForeignKey(
        UserModel, 
        on_delete = models.SET_NULL, 
        null = True, 
        blank = True, 
        verbose_name = _('Author')
    )

    # Model data time information:
    created = models.DateTimeField(
        verbose_name=_('Created'),
        help_text=_('The date and time when the user settings was created. This '\
                    'timestamp is automatically set when the object is created.'),
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name=_('Updated'),
        help_text=_('The date and time when these user settings were last '
                    'updated. This helps in tracking changes to settings over '
                    'time.'),
        auto_now=True,
    )

    # User settings:
    measurement_system = models.IntegerField(
        choices = MeasurementSystemChoices.choices, 
        verbose_name = _('Measurement systems'), 
        help_text = _('Xxx.'),
        default=MeasurementSystemChoices.INTERNATIONAL
    )

    # object representation:
    def __repr__(self) -> str:
        return str(self.pk)

    def __str__(self) -> str:
        return str(self.pk)

    @property
    def __dict__(self):
        return {
            'created': self.created,
            'updated': self.updated,
            'measurement_system': self.measurement_system,
        }

    # Natural key representation:
    def natural_key(self):
        return str(self.pk)

    # Overwrite default save method:
    def save(self, *args, **kwargs):
        # Call the original save method to perform the actual save:
        super().save(*args, **kwargs)
        # Check if saved settings are current:
        if self.is_current:
            # Collect and save user settings object content:
            self.update_user_settings_dictionary()

    def update_user_settings_dictionary(self):
        # Collect user settings object content:
        data = self.__dict__
        # Collect user pk:
        user_pk = self.user.pk
        # Collect user settings:
        collected_user_settings = user_settings.get(user_pk)
        # Update user settings dictionary:
        collected_user_settings.update(data)

# Collect user settings helper function:
def collect_user_settings(
        key: str,
        user_pk: str):
    """ Collect user settings. """

    def collect_user_settings():
        # Collect user settings from dictionary:
        collected_user_settings = user_settings.get(user_pk)
        # Check if user settings are available:
        if collected_user_settings:
            # Collect data from user settings dictionary:
            value = collected_user_settings.get(key)
        # Check if user settings value is available:
        if value: # Return collected settings value:
            return copy.deepcopy(value) if isinstance(value, dict) else value
        else: # Return false response:
            return False
    
    if user_settings:
        # Collect user settings:
        return collect_user_settings()
    else: # Try to collect all user settings from database:
        all_collect_settings = UserSettingsModel.objects.all()
        # Iterate thru all user settings:
        for user_settings in all_collect_settings:
            # Update user settings:
            user_settings.update_user_settings_dictionary()
        # Collect user settings:
        return collect_user_settings()
