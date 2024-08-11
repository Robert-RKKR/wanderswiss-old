# Rest framework - serializer import:
from rest_framework.serializers import HyperlinkedIdentityField

# WanderSwiss - base serializer import:
from wanderswiss.base.api.base_serializers import BaseSerializer

# WanderSwiss - notification model import:
from notification.models.notification_model import NotificationModel

# Serializer details:
model = NotificationModel
depth = 0
fields = [
    'pk',
    'url',
    'timestamp',
    'severity',
    'task_id',
    'message',
    'url',
]
read_only_fields = [
    'pk',
    'url',
    'timestamp',
    'severity',
    'task_id',
    'message',
    'url',
]


# Notification serializer class:
class notificationSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-notification:notification_model-detail',
        help_text='URL to provided object.',
        read_only=False,
    )

    class Meta:

        model = model
        depth = depth
        fields = fields
        read_only_fields = read_only_fields
