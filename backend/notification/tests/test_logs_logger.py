# Python - import:
from unittest.mock import patch
from io import StringIO
import datetime
import pytest
import random

# WanderSwiss - settings import:
from management.models.global_settings_model import collect_global_settings

# WanderSwiss - management model import:
from management.models.global_settings_model import GlobalSettingsModel

# WanderSwiss - constance import:
from wanderswiss.base.constants.notification import SeverityChoices

# WanderSwiss - logger import:
from notification.system_logs import application_logger

# Declare global settings levels:
@pytest.fixture(scope='function', params=[(level, db, cli)
    for level in range(1, 6) 
    for db in [True, False]
    for cli in [True, False]])
def logger_settings(request):
    return request.param

# Create global settings instance:
@pytest.fixture(scope='function')
def settings(logger_settings):
    logger_level, logger_db, logger_cli = logger_settings
    return GlobalSettingsModel.objects.create(
        logger_level=logger_level,
        logger_db=logger_db,
        logger_cli=logger_cli)

# Create logger instance:
@pytest.fixture(scope='function')
def logger():
    return application_logger

# Declare logs variance:
@pytest.mark.parametrize('severity, message', [
    (1, 'Critical message'),
    (2, 'Error message'),
    (3, 'Warning message'),
    (4, 'Info message'),
    (5, 'Debug message')
])

# Test all log creation variations:
@pytest.mark.django_db
def test_log_creation(logger, settings, severity, message):

    # Example log data:
    additional_data = {'test': 'value'}
    execution_time = 23.43

    # Redirect stdout to a StringIO object
    with patch('sys.stdout', new=StringIO()) as fake_stdout:
        # Create a new test log:
        log_method = getattr(logger, str(SeverityChoices.value_from_int(severity)).lower())
        log = log_method(message, settings, execution_time, additional_data)
        # Get the printed output from StringIO:
        printed_output = fake_stdout.getvalue().strip()
        # Check if the logger CLI value is True:
        if collect_global_settings('logger_cli'):
            # If the logger CLI value is True, check if logger level allows for log creation:
            if severity > collect_global_settings('logger_level'):
                # Check that there is no log that has not been created:
                assert log == None
            else: # Check if CLI message has been generated:
                assert message in printed_output, (
                    'Printed message mismatch. Expected: '\
                    f'"{message}", Got: "{printed_output}"')
        else: # If the logger CLI value is False, no data should be printed to the console:
            assert printed_output == ''
            
    # Verify if logger level allows for log creation:
    if severity > collect_global_settings('logger_level'):
        assert log == None
    else: # Checks of log data:
        if collect_global_settings('logger_db'):
            assert isinstance(log.timestamp, datetime.datetime), (
                f'Timestamp is not a datetime object. '
                f'Expected: type datetime.datetime, Got: "{type(log.timestamp)}"')
            assert isinstance(log.task_id, str), (
                f'Task ID is not a string. '
                f'Expected: type str, Got: "{type(log.task_id)}"')
            assert log.object_representation == settings.pk, (
                f'Object representation mismatch. '
                f'Expected: "{settings.pk}", Got: "{log.object_representation}"')
            assert log.additional_data == additional_data, (
                f'Additional data mismatch. '
                f'Expected: "{additional_data}", Got: "{log.additional_data}"')
            assert log.execution_time == execution_time, (
                f'Execution time mismatch. '
                f'Expected: "{execution_time}", Got: "{log.execution_time}"')
            assert log.app_name == 'management', (
                f'Application name mismatch. '
                f'Expected: "management", Got: "{log.app_name}"')
            assert log.model_name == 'GlobalSettingsModel', (
                f'Model name mismatch. '
                f'Expected: "GlobalSettingsModel", Got: "{log.model_name}"')
            assert log.severity == severity, (
                f'Severity mismatch. '
                f'Expected: "{severity}", Got: "{log.severity}"')
            assert log.message == message, (
                f'Message mismatch. '
                f'Expected: "{message}", Got: "{log.message}"')
            assert log.object_id == settings.pk, (
                f'Object ID mismatch. '
                f'Expected: "{settings.pk}", Got: "{log.object_id}"')
        else:
            assert log is None
