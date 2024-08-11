# Python - math import:
import math

# Rest framework - import:
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


# All paginator classes:
class BasePaginator(PageNumberPagination):
    """
    Base paginator class providing common pagination
    settings and response structure.
    """
    # Pagination page query name:
    page_query_param = 'page_number'
    page_query_description = 'A page number within the paginated result set.'
    # Pagination size query name:
    page_size_query_param = 'page_size'
    page_size_query_description = 'Number of results to return per page.'
    # Pagination size:
    page_size = 10
    # Pagination max size:
    max_page_size = 1000
    # Pagination last page query name:
    last_page_strings = ('last_page',)

    # Pagination response schema:
    def get_paginated_response(self, data):
        """
        Get the paginated response with metadata including the paginated data,
        total number of objects, page count, and links to next and previous pages.
        """

        return Response({
            'page_results': data,
            'page_objects': self.page.paginator.count,
            'page_count': math.ceil(self.page.paginator.count/self.get_page_sizes()),
            'page_links': {
                'page_next': self.get_next_link(),
                'page_previous': self.get_previous_link()
            }
        })

    def get_page_sizes(self):
        """
        Get the page size dynamically from the request query parameters.
        """
        
        page_size = self.request.query_params.get(self.page_size_query_param)
        if page_size:
            try:
                page_size = int(page_size)
                return min(page_size, self.max_page_size)
            except ValueError:
                pass
        return self.page_size


class BaseSmallPaginator(BasePaginator):
    """
    Paginator class for smaller pagination.
    """

    # Pagination page size:
    page_size = 10


class BaseMediumPaginator(BasePaginator):
    """
    Paginator class for medium-sized pagination.
    """

    # Pagination page size:
    page_size = 50


class BaseLargePaginator(BasePaginator):
    """
    Paginator class for larger pagination.
    """

    # Pagination page size:
    page_size = 100
