# Python - many import:
import datetime
import pytest
import random

# Mock - import:
from unittest.mock import MagicMock
from unittest.mock import patch

# WanderSwiss - settings import:
from management.models.global_settings_model import collect_global_settings

# WanderSwiss - management model import:
from management.models.global_settings_model import GlobalSettingsModel

# WanderSwiss - constance import:
from wanderswiss.base.constants.notification import SeverityChoices

# WanderSwiss - notifications import:
from notification.notification import Notification

# Channels - import:
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Channels registration:
channel_layer = get_channel_layer()

# Declare global settings levels:
@pytest.fixture(scope='function', params=[2, 3, 4])
def notification_level(request):
    return request.param

# Create global settings instance:
@pytest.fixture(scope='function')
def settings(notification_level):
    return GlobalSettingsModel.objects.create(
        notification_level=notification_level)

# Create notification instance:
@pytest.fixture(scope='function')
def notification():
    task_id = random.randint(385473959353496, 999999999999999)
    return Notification(
        task_id=task_id,
        channel_name='Test notification channel')

# Declare logs variance:
@pytest.mark.parametrize('severity, message',
    [(2, 'Error message'),
    (3, 'Warning message'),
    (4, 'Info message')])

# Test creation of new notifications:
@pytest.mark.django_db
def test_notification_creation(settings, notification, severity, message):

    notification_method = getattr(notification,
        str(SeverityChoices.value_from_int(severity)).lower())
    notification_instance = notification_method(message)

    # Verify if notification level allows for notification creation:
    if severity > collect_global_settings('logger_level'):
        assert notification_instance is None
    else: # Checks of log data:
        assert isinstance(notification_instance.timestamp, datetime.datetime), (
            f'Timestamp is not a datetime object. '
            f'Expected: type datetime.datetime, Got: "{type(notification_instance.timestamp)}"')
        assert notification_instance.message == message, (
            f'Message mismatch. '
            f'Expected: "{message}", Got: "{notification_instance.message}"')

        # Check if the notification is sent to the correct channel
        mock_group_send = MagicMock()
        with patch('notification.notification.async_to_sync') as mock_async_to_sync:
            mock_async_to_sync.return_value = mock_group_send
            notification_instance.send_to_channel()
            mock_async_to_sync.assert_called_once_with(channel_layer.group_send)
            mock_group_send.assert_called_once_with('Test notification channel', {
                'task_id': notification.task_id,
                'message': message,
                'severity': severity,
                'url': None,
                'type': 'send_collect',
                'id': str(notification_instance.pk)
            })
