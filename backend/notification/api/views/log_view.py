# WanderSwiss - notification import:
from notification.api.serializers.log_serializer import LogSerializer

# WanderSwiss - base view set import:
from wanderswiss.base.api.base_model_viewset import ReadDeleteViewSet

# WanderSwiss - base pagination import:
from wanderswiss.base.api.base_pagination import BaseSmallPaginator

# WanderSwiss - notification filter import:
from notification.api.filters.log_filter import LogFilter

# WanderSwiss - notification model import:
from notification.models.log_model import LogModel


# Policy Execution view class:
class LogView(ReadDeleteViewSet):
    """
    Policy Execution Read and write view.
    """

    # Basic API view parameters:
    queryset = LogModel.objects.all().order_by('timestamp')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = LogSerializer
    # Django rest framework filters:
    filterset_class = LogFilter
    ordering_fields = '__all__'
    search_fields = '__all__'
