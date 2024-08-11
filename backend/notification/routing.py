# Django - url import:
from django.urls import path

# WanderSwiss - notification consumers import:
from notification.consumers import NotificationConsumer

ws_urlpatterns = [
    path('ws/notification/', NotificationConsumer.as_asgi()),
]
