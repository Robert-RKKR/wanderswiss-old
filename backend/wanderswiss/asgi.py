# Python - library import:
import os

# Django - asgi import:
from django.core.asgi import get_asgi_application

# Channels - import:
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# Capybara - routing import:
from notification.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wanderswiss.settings')
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns)),
})
