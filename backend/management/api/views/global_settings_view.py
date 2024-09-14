# WanderSwiss - base classes import:
from wanderswiss.base.api.base_viewset import BaseRetrieveViewSet

# WanderSwiss - global settings import:
from management.models.global_settings_model import GlobalSettingsModel

# Policy Execution view class:
class GlobalSettingsView(BaseRetrieveViewSet):
    
    def collect_data(self):
        """
        Return WanderSwiss global settings.
        """

        # Collect global settings if they exist:
        global_settings = GlobalSettingsModel.objects.get_or_create(
            is_current=True)
        global_settings_dict = global_settings.__dict__
        # Return all global settings:
        return global_settings_dict

