# WanderSwiss - notification import:
from notification.api.serializers.notification_serializer import notificationSerializer

# WanderSwiss - notification filter import:
from notification.api.filters.notification_filter import NotificationFilter

# WanderSwiss - notification model import:
from notification.models.notification_model import NotificationModel

# WanderSwiss - base view set import:
from wanderswiss.base.api.base_model_viewset import ReadDeleteViewSet

# WanderSwiss - base pagination import:
from wanderswiss.base.api.base_pagination import BaseSmallPaginator


# Notification view class:
class NotificationView(ReadDeleteViewSet):
    """
    Notification Read and write view.
    """

    # Notification changes:
    Notification_changes = True
    # Basic API view parameters:
    queryset = NotificationModel.objects.all().order_by('timestamp')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = notificationSerializer
    # Django rest framework filters:
    filterset_class = NotificationFilter
    ordering_fields = '__all__'
    search_fields = '__all__'
