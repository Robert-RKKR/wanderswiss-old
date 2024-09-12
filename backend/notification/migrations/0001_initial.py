# Generated by Django 5.0.7 on 2024-09-12 12:41

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LogModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier for this object. It is automatically generated and cannot be modified.', primary_key=True, serialize=False)),
                ('app_name', models.CharField(blank=True, help_text='The name of the application that this object belongs to. This helps in identifying the application context of the object.', max_length=64, null=True, verbose_name='Object application name')),
                ('model_name', models.CharField(blank=True, help_text='The name of the model that this object is an instance of. This helps in identifying the type of the object.', max_length=64, null=True, verbose_name='Object model name')),
                ('object_id', models.CharField(blank=True, help_text='The primary key (PK) number of the correlated object. This is a unique identifier for the object within its model.', max_length=64, null=True, verbose_name='Object PK number')),
                ('object_representation', models.CharField(blank=True, help_text='A string representation of the object. This provides a human-readable description or identifier of the object.', max_length=128, null=True, verbose_name='Object representation')),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text='The date and time when the log entry was created. This field is automatically populated when the log is created, providing an accurate record of the log event.', verbose_name='Timestamp')),
                ('severity', models.IntegerField(choices=[(1, 'Critical'), (2, 'Error'), (3, 'Warning'), (4, 'Info'), (5, 'Debug')], default=5, help_text='The level of severity associated with the log entry. This indicates the importance or urgency of the logged event, such as information, warning, or error.', verbose_name='Severity level')),
                ('task_id', models.CharField(blank=True, help_text='The unique identifier of the task associated with this log entry. This helps in tracking and correlating logs to specific tasks or operations within the application.', max_length=64, null=True, verbose_name='Task ID')),
                ('application', models.IntegerField(choices=[(0, 'None'), (1, 'Wander Swiss'), (2, 'Article'), (3, 'Card'), (4, 'Hiking')], default=0, help_text='The name of the application that generated this log entry. This helps in identifying which part of the system is responsible for the logged event.', verbose_name='Application')),
                ('message', models.CharField(error_messages={'invalid': 'Enter a valid notification message. It must contain 1 to 1024 digits.'}, help_text='The log message describing the event. This message provides detailed information about the event, which is useful for debugging and tracking purposes. The message must be between 1 and 1024 characters long.', max_length=1024, verbose_name='Message')),
                ('execution_time', models.FloatField(blank=True, help_text='The time taken to execute the logged event. This value is useful for performance monitoring and optimization.', null=True, verbose_name='Execution time')),
                ('additional_data', models.JSONField(blank=True, help_text='Any additional data related to the log entry. This can include context-specific information that provides more insight into the logged event.', null=True, verbose_name='Additional data')),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
                'ordering': ['-timestamp'],
                'permissions': (('read_write', 'Read and write access.'), ('read_only', 'Read only access')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='NotificationModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier for this object. It is automatically generated and cannot be modified.', primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text='The date and time when the notification was created. This field is automatically populated when the notification is created.', verbose_name='Timestamp')),
                ('severity', models.IntegerField(choices=[(1, 'Critical'), (2, 'Error'), (3, 'Warning'), (4, 'Info'), (5, 'Debug')], default=0, help_text='The severity level of the notification. Indicates the importance or urgency of the notification.', verbose_name='Severity level')),
                ('task_id', models.CharField(blank=True, help_text='The unique identifier of the task associated with this notification. Helps in tracking and correlating notifications to specific tasks.', max_length=64, null=True, verbose_name='Task ID')),
                ('message', models.CharField(error_messages={'invalid': 'Enter a valid notification message. It must contain 1 to 1024 digits.'}, help_text='The notification message detailing the event or action. This message provides information about the notification. The message must be between 1 and 1024 characters long.', max_length=1024, verbose_name='Message')),
                ('url', models.CharField(blank=True, help_text='The URL to the object related to this notification. This can be used to provide a direct link to the relevant object or page within the application.', max_length=256, null=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
                'ordering': ['-timestamp'],
                'permissions': (('read_write', 'Read and write access.'), ('read_only', 'Read only access')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ChangeLogModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier for this object. It is automatically generated and cannot be modified.', primary_key=True, serialize=False)),
                ('app_name', models.CharField(blank=True, help_text='The name of the application that this object belongs to. This helps in identifying the application context of the object.', max_length=64, null=True, verbose_name='Object application name')),
                ('model_name', models.CharField(blank=True, help_text='The name of the model that this object is an instance of. This helps in identifying the type of the object.', max_length=64, null=True, verbose_name='Object model name')),
                ('object_id', models.CharField(blank=True, help_text='The primary key (PK) number of the correlated object. This is a unique identifier for the object within its model.', max_length=64, null=True, verbose_name='Object PK number')),
                ('object_representation', models.CharField(blank=True, help_text='A string representation of the object. This provides a human-readable description or identifier of the object.', max_length=128, null=True, verbose_name='Object representation')),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text='The date and time when the change was created. This field automatically records the exact moment when the change entry is added to the log.', verbose_name='Timestamp')),
                ('action_type', models.IntegerField(choices=[(0, 'Empty'), (1, 'Create'), (2, 'Update'), (3, 'Delete')], default=0, help_text='The type of action that was performed on the object. This could include actions such as creation, modification, or deletion of records. The choices are defined in the ActionTypeChoices constant.', verbose_name='Type of action')),
                ('after', models.JSONField(blank=True, help_text='The JSON representation of the object after the changes were made and saved to the database. This provides a snapshot of the object state post-change for auditing and rollback purposes.', null=True, verbose_name='JSON object representation after change')),
                ('user', models.ForeignKey(blank=True, help_text='The user responsible for the change. This field links to the user who performed the action, providing accountability and traceability.', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Change',
                'verbose_name_plural': 'Changes',
                'ordering': ['-timestamp'],
                'permissions': (('read_write', 'Read and write access.'), ('read_only', 'Read only access')),
                'default_permissions': (),
            },
        ),
    ]
