# WanderSwiss - base filter import:
from wanderswiss.base.filters.base_filter import BaseFilter

# WanderSwiss - notification model import:
from notification.models.log_model import LogModel


# Filters:
class LogFilter(BaseFilter):

    class Meta:

        model = LogModel
        fields = {
            'app_name': ['exact', 'icontains'],
            'model_name': ['exact', 'icontains'],
            'object_id': ['exact'],
            'object_representation': ['exact', 'icontains'],
            'timestamp': ['exact', 'icontains', 'lt', 'gt'],
            'severity': ['exact', 'icontains', 'lt', 'gt'],
            'task_id': ['exact'],
            'application': ['exact', 'icontains'],
            'execution_time': ['exact', 'icontains', 'lt', 'gt'],
        }
