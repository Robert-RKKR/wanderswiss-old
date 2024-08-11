# Python - json import:
import json

# WanderSwiss - base models import:
from wanderswiss.base.models.base_model import BaseModel

# WanderSwiss - notification model import:
from notification.models.log_model import LogModel

# WanderSwiss - constance import:
from wanderswiss.base.constants.notification import ApplicationChoices
from wanderswiss.base.constants.notification import SeverityChoices

# WanderSwiss - object data collector import:
from notification.object_collector import collect_object_data

# WanderSwiss - settings import:
from management.models.global_settings_model import collect_global_settings

# WanderSwiss - cli messages:
from notification.cli_logger import cli_message


# Logger class:
class Logger:
    """
    Logger class.

    Methods:
    --------
    critical:
        Create critical severity log.
    error:
        Create error severity log.
    warning:
        Create warning severity log.
    info:
        Create info severity log.
    debug:
        Create debug severity log.
    """

    def __init__(self,
        application: ApplicationChoices = ApplicationChoices.NONE,
        task_id: str = 'None') -> None:
        """
        Logger class.
        Provided the ability to log events in database.

        Parameters:
        -----------------
        application: string
            Name of the application that triggers notifications.
        task_id: string
            Task ID related with celery task.
        """

        # Declare instance parameter:
        self._check_parameters(application, task_id)

        # Logger instance parameters - logger data:
        self.severity = None
        self.message = None

        # Logger instance parameters - related object:
        self.object_representation = None
        self.correlated_object = None
        self.model_name = None
        self.object_id = None
        self.app_name = None

        # Logger instance parameters - additional data:
        self.json_additional_data = None
        self.additional_data = None

    def __repr__(self) -> str:
        """ Logger class representation. """
        return f'<Class Logger ({self.application}:{self.task_id})>'

    def critical(self,
        message: str,
        correlated_object: BaseModel = None,
        execution_time: float = 0.0,
        additional_data: dict = None) -> LogModel:
        """
        Create a new critical log based on the following data:

        Args:
            message (str):
                Log message string value.
            correlated_object (BaseModel, optional):
                Correlated object. Defaults to None.
            execution_time (float, optional):
                Time of script / task / connection execution.
                Defaults to 0.

        Returns:
            Log: Logger class object.
        """

        # Create a new log:
        return self._log(
            message, correlated_object,
            SeverityChoices.CRITICAL,
            execution_time,
            additional_data)

    def error(self,
        message: str,
        correlated_object: BaseModel = None,
        execution_time: float = 0.0,
        additional_data: dict = None) -> LogModel:
        """
        Create a new error log based on the following data:

        Args:
            message (str):
                Log message string value.
            correlated_object (BaseModel, optional):
                Correlated object. Defaults to None.
            execution_time (float, optional):
                Time of script / task / connection execution.
                Defaults to 0.

        Returns:
            Log: Logger class object.
        """

        # Create a new log:
        return self._log(
            message, correlated_object,
            SeverityChoices.ERROR,
            execution_time,
            additional_data)

    def warning(self,
        message: str,
        correlated_object: BaseModel = None,
        execution_time: float = 0.0,
        additional_data: dict = None) -> LogModel:
        """
        Create a new warning log based on the following data:

        Args:
            message (str):
                Log message string value.
            correlated_object (BaseModel, optional):
                Correlated object. Defaults to None.
            execution_time (float, optional):
                Time of script / task / connection execution.
                Defaults to 0.

        Returns:
            Log: Logger class object.
        """

        # Create a new log:
        return self._log(
            message, correlated_object,
            SeverityChoices.WARNING,
            execution_time,
            additional_data)

    def info(self,
        message: str,
        correlated_object: BaseModel = None,
        execution_time: float = 0.0,
        additional_data: dict = None) -> LogModel:
        """
        Create a new info log based on the following data:

        Args:
            message (str):
                Log message string value.
            correlated_object (BaseModel, optional):
                Correlated object. Defaults to None.
            execution_time (float, optional):
                Time of script / task / connection execution.
                Defaults to 0.

        Returns:
            Log: Logger class object.
        """

        # Create a new log:
        return self._log(
            message, correlated_object,
            SeverityChoices.INFO,
            execution_time,
            additional_data)

    def debug(self,
        message: str,
        correlated_object: BaseModel = None,
        execution_time: float = 0.0,
        additional_data: dict = None) -> LogModel:
        """
        Create a new debug log based on the following data:

        Args:
            message (str):
                Log message string value.
            correlated_object (BaseModel, optional):
                Correlated object. Defaults to None.
            execution_time (float, optional):
                Time of script / task / connection execution.
                Defaults to 0.

        Returns:
            Log: Logger class object.
        """

        # Create a new log:
        return self._log(
            message, correlated_object,
            SeverityChoices.DEBUG,
            execution_time,
            additional_data)

    def _log(self,
        message: str,
        correlated_object: BaseModel,
        severity: SeverityChoices,
        execution_time: float,
        additional_data: dict) -> LogModel:

        # Cache global settings to avoid repeated function calls
        global_settings = {
            'logger_cli': collect_global_settings('logger_cli'),
            'logger_level': collect_global_settings('logger_level'),
            'logger_db': collect_global_settings('logger_db')
        }

        # Check if log should be printed in CLI console:
        if (global_settings['logger_cli'] and 
                severity <= global_settings['logger_level']):
            # Verify provided data and create a new console log
            self._check_log_data(message, correlated_object, execution_time, 
                        additional_data)
            cli_message(severity, message)

        # Verify that the logger global settings allow the log to be created:
        if (global_settings['logger_db'] and 
                severity <= global_settings['logger_level']):
            # Verify provided data and create a new database log:
            self._check_log_data(message, correlated_object,
                execution_time, additional_data)
            return self._create_log(message, correlated_object,
                severity, execution_time, additional_data)

        # Return empty response:
        return None

    def _create_log(self,
        message,
        correlated_object,
        severity,
        execution_time,
        additional_data) -> LogModel:

        # Clean previous log data:
        self._log_cleanup()
        
        # Collect data to object attributes:
        self.additional_data = self._convert_additional_data(additional_data)
        self.correlated_object = correlated_object
        self.execution_time = execution_time
        self.severity = severity
        self.message = message

        # Check if object was provided:
        if self.correlated_object:
            # Collect information about provided object:
            related_object_data = collect_object_data(correlated_object)
            # Collect app and model name based on object information:
            self.app_name = related_object_data.get('app_name', None)
            self.model_name = related_object_data.get('model_name', None)
            # Collect object ID:
            self.object_id = related_object_data.get('object_id', None)
            # Collect object representation:
            self.object_representation = related_object_data.get(
                'object_representation', None)

        # Collect log data:
        log_data = {
            'object_representation': self.object_representation,
            'additional_data': self.additional_data,
            'execution_time': self.execution_time,
            'application': self.application,
            'model_name': self.model_name,
            'object_id': self.object_id,
            'app_name': self.app_name,
            'severity': self.severity,
            'task_id': self.task_id,
            'message': self.message}
        try: # Try to create a new log:
            log = LogModel.objects.create(**log_data)
        except Exception as exception:
            # Print logger log creation error:
            cli_message(SeverityChoices.ERROR,
                f'{exception}.\nLOG DATA: {log_data}')
            # Return False value:
            return False
        else: # Return created log:
            return log

    def _convert_additional_data(self, additional_data: dict) -> dict:
        try: # Check if additional data can be converted into JSON format:
            json.dumps(additional_data, ensure_ascii=False)
            # If yes return additional data intact:
            return additional_data
        except Exception:
            # If the dictionary cannot be serialized, handle non-serializable values:
            converted_data = {}
            for key, value in additional_data.items():
                try: # Try to convert key into string:
                    string_key = str(key)
                except Exception:
                    pass
                else: # Convert value to string if conversion to JSON will fail.
                    try: # Attempt to convert each value to JSON
                        json.dumps(value, ensure_ascii=False)
                        # If successful, keep the original value
                        converted_data[string_key] = value
                    except Exception:
                        try: # If the value cannot be serialized,
                            # try to convert it to a string:
                            converted_data[string_key] = str(value)
                        except Exception:
                            # Overwrite data if can't be converted into string:
                            converted_data[string_key] = '...'
            # Return converted data:
            return converted_data

    def _check_log_data(self,
        message,
        correlated_object,
        execution_time,
        additional_data) -> None:
        
        # Verify that the message variable is an string type:
        if not isinstance(message, str):
            raise TypeError('The provided notification message variable '\
                f'must be a string.\nProvided: "{type(message)}"')
        if len(message) > 1024:
            self.message = message[:1020] + ' ...'

        # Verify that the correlated object variable is an BaseModel class:
        if not (isinstance(correlated_object, BaseModel)\
            or correlated_object is None):
            raise TypeError('The provided correlated object variable must '\
                f'be a WanderSwiss model object.\nProvided: '\
                f'"{type(correlated_object)}"')

        # Verify that the execution time variable is an float type:   
        if not isinstance(execution_time, float):
            raise TypeError('The provided execution time variable must be '\
                f'float.\nProvided: "{type(execution_time)}"')

        # Verify that the additional data variable is an dict type:   
        if not (isinstance(additional_data, dict) or additional_data is None):
            # Raise error if additional data variable is not a dict:
            raise TypeError('The provided additional data variable must be '\
                f'dictionary.\nProvided: "{type(additional_data)}"')

    def _log_cleanup(self) -> None:
        """ Reset all log parameters. """

        # Logger instance parameters - logger data:
        self.severity = None
        self.message = None

        # Logger instance parameters - related object:
        self.object_representation = None
        self.correlated_object = None
        self.model_name = None
        self.object_id = None
        self.app_name = None

        # Logger instance parameters - additional data:
        self.json_additional_data = None
        self.additional_data = None

    def _check_parameters(self, application, task_id) -> None:

        # Verify that the application variable is an string type:
        if not isinstance(application, ApplicationChoices):
            raise TypeError('The provided application variable must be a '\
                f'ApplicationChoices object.\nProvided: "{type(application)}"')
        # Assign application value:
        self.application = application

        # Verify that the Task ID variable is an string type:
        if isinstance(task_id, int):
            task_id = str(task_id)
        elif not isinstance(task_id, str):
            # Raise error if task ID variable is not a sting or integer:
            raise TypeError('The provided task ID variable must be a string '\
                f'or integer.\nProvided: "{type(task_id)}"')
        # Limit task_id length:
        self.task_id = task_id[:64]

    @property
    def __dict__(self):
        return {
            'application': self._application,
            'task_id': self._task_id,
            'message': self.message,
            'severity': self.severity,
            'correlated_object': self.correlated_object,
            'app_name': self.app_name,
            'model_name': self.model_name,
            'object_id': self.object_id,
            'object_representation': self.object_representation,
            'json_additional_data': self.json_additional_data,
            'additional_data': self.additional_data
        }
