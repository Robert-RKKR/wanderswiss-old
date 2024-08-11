# Python - copy import:
import copy

# Django - exceptions import:
from django.core.exceptions import ValidationError
from django.db.models import ProtectedError

# Django - admin import:
from django.contrib import admin

# Rest framework - exceptions import:
from rest_framework.exceptions import PermissionDenied
from rest_framework.exceptions import NotAcceptable

# Rest framework - mixins import:
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import DestroyModelMixin
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.mixins import ListModelMixin

# Rest framework - other imports:
from rest_framework.response import Response
from rest_framework import status

# Capybara - constance import:
from capybara.base.constants.action_type import ActionTypeChoices

# Capybara - collect object information import:
from notification.object_collector import collect_object_data

# Capybara - notification import:
from notification.notification import Notification

# Capybara - log change import:
from notification.changer import log_change

# Init API notification:
notification = Notification('API', channel_name='objects_notifications')

# Helper function to check if an instance is not a root object:
def is_not_root(instance: object) -> bool:
    """
    Check if an instance is not a root object.

    Args:
        instance (object): The instance to check.

    Returns:
        bool: True if instance is not a root, False otherwise.
    """
    
    try: # Try to collect is_root attribute:
        is_root = instance.is_root
    except: # If object doesn't have is_root attribute, return True:
        return True
    else: # If root object attribute is True return API error:
        if is_root: # Prepare Root error message:
            message = f"{instance._meta.object_name} object can't "\
                "be changed, because it's a root object"
            # Prepare error response:
            exception = {
                'page_status': False,
                'PermissionDenied': {
                    'type': 'RootProtectedError',
                    'message': message}}
            # Raise API error:
            raise PermissionDenied(exception)
        else: # If root object attribute is False, return True:
            return True

# Function to create notifications for object changes:
def create_notification(
    instance: object,
    action: ActionTypeChoices,
    user: admin,
    serializer = False,
    log_changes = False) -> None:
    """
    Create a notification for object changes.

    Args:
        instance (object):
            The instance on which the notification will be created.
        action (ActionTypeChoices):
            Notification action (Create, Update, Delete).
        user (admin):
            Django user who performed the action.
        serializer (bool):
            Serializer data (default: False).
    """

    if log_changes:
        # Create a new change notification:
        log_change(instance, user, action)
        # Collect object data:
        object_related_data = collect_object_data(instance)
        model_name = object_related_data.get('model_name', False)
        instance_representation = object_related_data.get(
            'object_representation', False)
        try: # Try to collect url:
            url = serializer.data['url']
        except: # If url not available return None:
            url = None
        # Send notification:
        notification.info(f'{model_name} "{instance_representation}" '\
            f'has been {ActionTypeChoices.value_from_int(action)}d.',
            url=url)  


# Base mixins custom classes:
class BaseCreateModelMixin(CreateModelMixin):
    """
    Mixin class to create a model instance.
    """

    def create(self, request, *args, **kwargs):
        # Collect serializer:
        serializer = self.get_serializer(data=request.data)
        # Validate serializer:
        serializer.is_valid(raise_exception=True)
        # Save serializer:
        instance = serializer.save()
        # Create change notifications:
        create_notification(
            instance, ActionTypeChoices.CREATE, request.user,
            serializer, self.log_changes)
        # Prepare headers:
        headers = self.get_success_headers(serializer.data)
        # Prepare response:
        response = {
            'page_status': True,
            'page_results': serializer.data}
        # Return HTTP response 201, object was created:
        return Response(
            response, status=status.HTTP_201_CREATED, headers=headers)


class BaseUpdateModelMixin(UpdateModelMixin):
    """
    Mixin class to update a model instance.
    """
    
    def update(self, request, *args, **kwargs):
        # Update method:
        partial = kwargs.pop('partial', False)
        # Collect instance:
        instance = self.get_object()
        # Check if instance is root object:
        if is_not_root(instance):
            # Collect serializer:
            serializer = self.get_serializer(
                instance, data=request.data, partial=partial)
            # Validate serializer:
            serializer.is_valid(raise_exception=True)
            try: # Try to update object:
                serializer.save()
            except ValidationError as exception:
                # Collect error data:
                error_response = {
                    'page_status': False,
                    'NotAcceptable': {
                        'type': 'ValidationError',
                        'message': exception.message}}
                # Raise API error:
                raise NotAcceptable(error_response)
            else: # Create change notifications:
                create_notification(
                    instance, ActionTypeChoices.UPDATE, request.user,
                    serializer, self.log_changes)
                # getattr update action:
                if getattr(instance, '_prefetched_objects_cache', None):
                    # If 'prefetch_related' has been applied to a queryset, 
                    # we need to forcibly invalidate the prefetch cache
                    # on the instance.
                    instance._prefetched_objects_cache = {}
                # Prepare response:
                response = {
                    'page_status': True,
                    'page_results': serializer.data}
                # Return HTTP response 200, object was updated:
                return Response(response, status=status.HTTP_200_OK)


# Base mixins classes:
class BaseDestroyModelMixin(DestroyModelMixin):
    """
    Mixin class to destroy a model instance.
    """

    def destroy(self, request, *args, **kwargs):
        # Collect object instance:
        instance = self.get_object()
        # Copy instance:
        copy_instance = copy.copy(instance)
        # Check if instance is not a root:
        if is_not_root(instance):
            try: # Try to delete provided instance:
                self.perform_destroy(instance)
            except ProtectedError as exception:
                object_list = []
                # Iterate thru all related objects:
                for row in exception.protected_objects:
                    # Collect object data:
                    object_related_data = collect_object_data(row)
                    # Add collected object data into list:
                    object_list.append(object_related_data)
                # Prepare error response:
                error_response = {
                    'page_status': False,
                    'NotAcceptable': {
                        'type': 'ProtectedError',
                        'message': str(exception.args),
                        'related_objects': object_list}}
                # Raise API error:
                raise NotAcceptable(error_response)
            else: # Create change notifications:
                create_notification(
                    copy_instance, ActionTypeChoices.DELETE,
                    request.user, self.log_changes)
                # Return 204 HTTP response if object was deleted:
                return Response(status=status.HTTP_204_NO_CONTENT)   


class BaseRetrieveModelMixin(RetrieveModelMixin):
    """
    Mixin class to retrieve a model instance.
    """
    
    def retrieve(self, request, *args, **kwargs):
        # Collect instance:
        instance = self.get_object()
        # Collect serializer:
        serializer = self.get_serializer(instance)
        # Prepare response:
        response = {
            'page_status': True,
            'page_results': serializer.data}
        # Return HTTP response 200.
        return Response(response, status=status.HTTP_200_OK)


class BaseListModelMixin(ListModelMixin):
    """
    List a queryset.
    """

    pass
