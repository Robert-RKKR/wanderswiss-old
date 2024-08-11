# WanderSwiss - settings import:
from management.models.global_settings_model import collect_global_settings

# WanderSwiss - notification model import:
from notification.models.notification_model import NotificationModel

# WanderSwiss - constance import:
from wanderswiss.base.constants.notification import SeverityChoices

# Channels - layers import:
from channels.layers import get_channel_layer

# Channels - async import:
from asgiref.sync import async_to_sync

# Channels registration:
channel_layer = get_channel_layer()


# Notification class:
class Notification:
    """
    Notification class.

    Methods:
    --------
    error:
        Create error severity notification.
    warning:
        Create warning severity notification.
    info:
        Create info severity notification.
    """

    def __init__(self,
        task_id: str = 'None',
        channel_name: str = 'notification') -> None:
        """
        Notification class.
        Provided the ability to notify users of events via
        Django channels and database.

        Parameters:
        -----------------
        channel_name: string
            Channel name used to send notifications to users.
        task_id: string
            Task ID related with celery task.
        """

        # Declare instance parameter:
        self._check_parameters(task_id, channel_name)

        # Notification instance parameters - logger data:
        self.severity = None
        self.message = None
        self.url = None

    def __repr__(self) -> str:
        """ Notification class representation. """
        return f'<Class Notification ({self.channel_name}:{self.task_id})>'

    def error(self,
        message: str,
        url: str = None) -> NotificationModel:
        """
        Create a new error notification based on the following data:

        Args:
            message (str):
                Notification message string value.

        Returns:
            Notification: Notification class object.
        """

        # Verify that the logger global settings allow the log to be created:
        if SeverityChoices.ERROR > collect_global_settings('logger_level'):
            # Return empty response:
            return None
        else: # Verify provided data:
            self._check_notification_data(message, url)
            # Create a new log:
            return self._create_notification(
                message, SeverityChoices.ERROR, url)

    def warning(self,
        message: str,
        url: str = None) -> NotificationModel:
        """
        Create a new warning notification based on the following data:

        Args:
            message (str):
                Notification message string value.

        Returns:
            Notification: Notification class object.
        """

        # Verify that the logger global settings allow the log to be created:
        if SeverityChoices.WARNING > collect_global_settings('logger_level'):
            # Return empty response:
            return None
        else: # Verify provided data:
            self._check_notification_data(message, url)
            # Create a new log:
            return self._create_notification(
                message, SeverityChoices.WARNING, url)

    def info(self,
        message: str,
        url: str = None) -> NotificationModel:
        """
        Create a new info notification based on the following data:

        Args:
            message (str):
                Notification message string value.

        Returns:
            Notification: Notification class object.
        """

        # Verify that the logger global settings allow the log to be created:
        if SeverityChoices.INFO > collect_global_settings('logger_level'):
            # Return empty response:
            return None
        else: # Verify provided data:
            self._check_notification_data(message, url)
            # Create a new log:
            return self._create_notification(
                message, SeverityChoices.INFO, url)
        
    def _create_notification(self,
        message, severity, url) -> NotificationModel:

        # Clean previous notification data:
        self._notification_cleanup()
        
        # Collect data to object attributes:
        self.severity = severity
        self.message = message
        self.url = url

        # Collect notification data:
        notification_data = {
            'task_id': self.task_id,
            'message': self.message,
            'severity': self.severity,
            'url': self.url}

        try: # Try to create a new notification:
            notification = NotificationModel.objects.create(**notification_data)
        except Exception as exception:
            # Print notification creation error:
            print(f'NOTIFICATION ERROR: {exception}\n'\
                f'Notification data: {notification_data}')
            # Return False value:
            return False
        else: # Send notification to channel:
            # Prepare notification data:
            notification_data['type'] = 'send_collect'
            notification_data['id'] = str(notification.pk)
            # Send channel notification:
            async_to_sync(channel_layer.group_send)(self.channel_name, 
                notification_data)
            # Return created log:
            return notification
        
    def _check_notification_data(self, message, url) -> None:
        
        # Verify that the message variable is an string type:
        if not isinstance(message, str):
            raise TypeError('The provided notification message variable '\
                f'must be a string.\nProvided: "{type(message)}"')
        if len(message) > 1024:
            self.message = message[:1020] + ' ...'
        
        # Verify that the URL variable is an string type:
        if not (isinstance(url, str) or url is None):
            # Raise error if URL variable is not a string:
            raise TypeError('The provided notification URL variable '\
                f'must be a string.\nProvided: "{type(url)}"')

    def _notification_cleanup(self) -> None:
        """ Reset all notification parameters. """

        # Notification instance parameters - logger data:
        self.severity = None
        self.message = None
        self.url = None

    def _check_parameters(self, task_id, channel_name) -> None:
        
        # Verify that the Task ID variable is an string type:
        if isinstance(task_id, int):
            task_id = str(task_id)
        elif not isinstance(task_id, str):
            # Raise error if task ID variable is not a sting or integer:
            raise TypeError('The provided task ID variable must be a string '\
                f'or integer.\nProvided: "{type(task_id)}"')
        # Limit task_id length:
        self.task_id = task_id[:64]

        # Verify that the channel name variable is an string type:
        if not isinstance(channel_name, str):  
            raise TypeError('The provided channel name variable must be a '\
                f'string.\nProvided: "{type(channel_name)}"')
        # If yes save channel name:
        self.channel_name = channel_name
    
    @property
    def __dict__(self):
        return {
            'task_id': self.task_id,
            'message': self.message,
            'severity': self.severity
        }
