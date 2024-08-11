# Django - models import:
from django.http import JsonResponse

# Rest framework - view import:
from rest_framework.viewsets import ViewSet

# Rest framework - authentication & permissions import:
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions

# Django - http import:
from django.http import HttpResponse


# Base celery views classes:
class BaseListViewSet(ViewSet):
    """
    Base viewset class.
    """
    
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    error_message = None
    error_code = None

    def collect_data(self):
        raise NotImplementedError

    def list(self, request, format=None):
        """
        Description.
        """

        # Collect data:
        collected_data = self.collect_data()
        # Prepare response:
        if collected_data:
            response = {
                'page_response': collected_data
            }
        else:
            response = {
                'page_response': None,
                'page_error': {
                    'code': self.error_code,
                    'message': self.error_message
                }
            }
        # Prepare API response:
        return JsonResponse(response, status=200)


class BaseRetrieveViewSet(ViewSet):
    """
    Base viewset class.
    """
    
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    error_message = None
    error_code = None

    def collect_data(self, pk):
        raise NotImplementedError
    
    def retrieve(self, request, pk=None):
        """
        Description.
        """

        # Collect data:
        collected_data = self.collect_data(pk)
        # Prepare response:
        if collected_data:
            response = {
                'page_response': collected_data
            }
        else:
            response = {
                'page_response': None,
                'page_error': {
                    'code': self.error_code,
                    'message': self.error_message
                }
            }
        # Prepare API response:
        return JsonResponse(response, status=200)


class DownloadFileViewSet(ViewSet):
    """
    Base viewset class.
    """
    
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    error_message = None
    error_code = None

    def collect_data(self):
        raise NotImplementedError

    def list(self, request, format=None):
        """
        Description.
        """

        # Collect data:
        collected_file, collected_file_name = self.collect_data()
        # Prepare results:
        response = HttpResponse(collected_file, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{collected_file_name}"'
        # Download response:
        # response['Content-Disposition'] = f'attachment; filename="{collected_file_name}"'

        return response
