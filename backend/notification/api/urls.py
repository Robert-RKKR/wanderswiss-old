# WanderSwiss - base route import:
from wanderswiss.base.api.base_default_router import BaseDefaultRouter

# WanderSwiss - view set import:
from notification.api.views.notification_view import NotificationView
from notification.api.views.change_log_view import ChangeLogView
from notification.api.views.log_view import LogView

# Register router:
router = BaseDefaultRouter()

# App name registration:
app_name = 'api-notification'

# Standard view route registration:
router.register(r'notification', NotificationView, basename='notification_model')
router.register(r'change_log', ChangeLogView, basename='change_log_model')
router.register(r'log', LogView, basename='log_model')

# Add urlpatterns:
urlpatterns = router.urls
