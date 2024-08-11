# WanderSwiss - notification import:
from notification.api.serializers.change_log_serializer import ChangeLogSerializer

# WanderSwiss - notification filter import:
from notification.api.filters.change_log_filter import ChangeLogFilter

# WanderSwiss - base view set import:
from wanderswiss.base.api.base_model_viewset import ReadOnlyViewSet

# WanderSwiss - base pagination import:
from wanderswiss.base.api.base_pagination import BaseSmallPaginator

# WanderSwiss - notification model import:
from notification.models.change_log_model import ChangeLogModel


# Policy Execution view class:
class ChangeLogView(ReadOnlyViewSet):
    """
    Policy Execution Read and write view.
    """

    # ChangeLog changes:
    log_changes = True
    # Basic API view parameters:
    queryset = ChangeLogModel.objects.all().order_by('timestamp')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = ChangeLogSerializer
    # Django rest framework filters:
    filterset_class = ChangeLogFilter
    ordering_fields = '__all__'
    search_fields = '__all__'
