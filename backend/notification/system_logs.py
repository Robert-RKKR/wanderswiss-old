# Python import:
import uuid

# WanderSwiss - constance import:
from wanderswiss.base.constants.notification import ApplicationChoices

# WanderSwiss - notification import:
from notification.logger import Logger

# Generate random task ID:
task_id = str(uuid.uuid4())

# Register main application logger:
application_logger = Logger(
    ApplicationChoices.WANDERSWISS, task_id)
