# WanderSwiss - base filter import:
from wanderswiss.base.filters.base_filter import BaseFilter

# WanderSwiss - notification model import:
from notification.models.notification_model import NotificationModel


# Filters:
class NotificationFilter(BaseFilter):

    class Meta:

        model = NotificationModel
        fields = {
            'timestamp': ['exact', 'icontains', 'lt', 'gt'],
            'severity': ['exact', 'icontains', 'lt', 'gt'],
            'task_id': ['exact', 'icontains'],
        }
