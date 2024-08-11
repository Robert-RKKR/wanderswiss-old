# Rest framework - serializer import:
from rest_framework.serializers import HyperlinkedIdentityField

# WanderSwiss - base serializer import:
from wanderswiss.base.api.base_serializers import BaseSerializer

# WanderSwiss - notification model import:
from notification.models.change_log_model import ChangeLogModel

# Serializer details:
model = ChangeLogModel
depth = 0
fields = [
    'pk',
    'url',
    'app_name',
    'model_name',
    'object_id',
    'object_representation',
    'timestamp',
    'administrator',
    'action_type',
    'after',
]
read_only_fields = [
    'pk',
    'url',
    'app_name',
    'model_name',
    'object_id',
    'object_representation',
    'timestamp',
    'administrator',
    'action_type',
    'after',
]


# ChangeLog serializer class:
class ChangeLogSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-notification:change_log_model-detail',
        help_text='URL to provided object.',
        read_only=False,
    )

    class Meta:

        model = model
        depth = depth
        fields = fields
        read_only_fields = read_only_fields
