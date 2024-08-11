# WanderSwiss - base filter import:
from wanderswiss.base.filters.base_filter import BaseFilter

# WanderSwiss - notification model import:
from notification.models.change_log_model import ChangeLogModel


# Filters:
class ChangeLogFilter(BaseFilter):

    class Meta:

        model = ChangeLogModel
        fields = {
            'app_name': ['exact', 'icontains'],
            'model_name': ['exact', 'icontains'],
            'object_id': ['exact'],
            'object_representation': ['exact', 'icontains'],
            'timestamp': ['exact', 'icontains', 'lt', 'gt'],
            'administrator': ['exact'],
            'action_type': ['exact'],
        }
