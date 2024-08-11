# Django filters - rest framework filters import:
from django_filters.rest_framework import DjangoFilterBackend

# Rest framework - authentication & permissions import:
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions

# Rest framework - exceptions import:
from rest_framework.exceptions import MethodNotAllowed

# Rest framework - viewsets import:
from rest_framework import viewsets

# Rest framework - filters import:
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter

# Capybara - base model mixin import:
from capybara.base.api.base_model_mixin import BaseRetrieveModelMixin
from capybara.base.api.base_model_mixin import BaseDestroyModelMixin
from capybara.base.api.base_model_mixin import BaseUpdateModelMixin
from capybara.base.api.base_model_mixin import BaseCreateModelMixin
from capybara.base.api.base_model_mixin import BaseListModelMixin


# Base ModelViewSet model:
class BaseViewSet(viewsets.GenericViewSet):
    """
    Base ModelViewSet model.
    """

    # Initiate empty QuerySet:
    queryset = None

    # Authentication and permissions:
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [DjangoModelPermissions]

    # Django rest framework filters:
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Log changes:
    log_changes = False
    
    metadata = {
        'my_custom_option': 'Some custom option',
        'my_other_option': 'Another custom option',
    }

    def metadata(self, request):
        metadata = super().metadata(request)
        metadata['my_custom_option'] = 'Modified custom option'
        return metadata


# All Capybara ModelViewSet models:
class ReadWriteViewSet(
    BaseViewSet,
    BaseCreateModelMixin,
    BaseRetrieveModelMixin,
    BaseUpdateModelMixin,
    BaseDestroyModelMixin,
    BaseListModelMixin):
    """
    Base ModelViewSet model.
    """

    pass
    

class ReadOnlyViewSet(
    BaseViewSet,
    BaseRetrieveModelMixin,
    BaseListModelMixin):
    """
    Base ModelViewSet model.
    """

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)


class ReadDeleteViewSet(
    BaseViewSet,
    BaseRetrieveModelMixin,
    BaseListModelMixin,
    BaseDestroyModelMixin):
    """
    Base ModelViewSet model.
    """

    pass


class RetrieveOnlyViewSet(
    BaseViewSet,
    BaseRetrieveModelMixin):
    """
    Base ModelViewSet model.
    """

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)
    

class ReadEditViewSet(
    BaseViewSet,
    BaseRetrieveModelMixin,
    BaseUpdateModelMixin,
    BaseListModelMixin):
    """
    Base ModelViewSet model.
    """

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)
