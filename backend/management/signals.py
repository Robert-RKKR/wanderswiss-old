# management/signals.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from management.models.global_settings_model import GlobalSettingsModel

@receiver(pre_save, sender=GlobalSettingsModel)
def current_settings(sender, instance, **kwargs):
    """
    If a new or changed settings object has the current value set to True,
    all other settings objects should have the current value set to False.
    """
    if instance.is_current:
        # Set other instances to not be current
        GlobalSettingsModel.objects.exclude(pk=instance.pk).filter(is_current=True).update(is_current=False)
