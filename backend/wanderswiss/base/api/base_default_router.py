# Rest framework - routers import:
from rest_framework.routers import DefaultRouter


# Base default router class:
class BaseDefaultRouter(DefaultRouter):
    """
    Customized version of DRF's DefaultRouter with additional functionality.
    """

    def get_api_root_view(self, api_urls=None):
        """
        Returns an alphabetically sorted dictionary of API endpoints.

        Parameters:
        - api_urls (list): Optional list of API URLs.

        Returns:
        - APIRootView: Alphabetically sorted view of API endpoints.
        """
        # Dictionary to hold the API endpoints:
        api_root_dict = {}
        
        # Name of the endpoint list:
        list_name = self.routes[0].name
        
        # Sorting the registry alphabetically by prefix:
        for prefix, viewset, basename in sorted(self.registry, key=lambda x: x[0]):
            api_root_dict[prefix] = list_name.format(basename=basename)

        # Returning the APIRootView with the sorted dictionary:
        return self.APIRootView.as_view(api_root_dict=api_root_dict)
