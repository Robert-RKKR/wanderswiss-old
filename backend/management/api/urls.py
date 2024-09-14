# WanderSwiss - base route import:
from management.api.views.global_settings_view import GlobalSettingsView

# WanderSwiss - view set import:
from wanderswiss.base.api.base_default_router import BaseDefaultRouter

# Register router:
router = BaseDefaultRouter()

# App name registration:
app_name = 'api-management'

# Standard view route registration:
router.register(r'management-global-settings', GlobalSettingsView, basename='management_global_setting')

# Add urlpatterns:
urlpatterns = router.urls
