# Rest framework - serializer import:
from rest_framework.serializers import HyperlinkedIdentityField

# WanderSwiss - base serializer import:
from wanderswiss.base.api.base_serializers import BaseSerializer

# WanderSwiss - notification model import:
from notification.models.log_model import LogModel

# Serializer details:
model = LogModel
depth = 0
fields = [
    'pk',
    'url',
    'app_name',
    'model_name',
    'object_id',
    'object_representation',
    'timestamp',
    'severity',
    'task_id',
    'application',
    'message',
    'execution_time',
    'additional_data',
]
read_only_fields = [
    'pk',
    'url',
    'app_name',
    'model_name',
    'object_id',
    'object_representation',
    'timestamp',
    'severity',
    'task_id',
    'application',
    'message',
    'execution_time',
    'additional_data',
]


# Log serializer class:
class LogSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-notification:log_model-detail',
        help_text='URL to provided object.',
        read_only=False,
    )

    class Meta:

        model = model
        depth = depth
        fields = fields
        read_only_fields = read_only_fields
