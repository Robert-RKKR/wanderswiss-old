# Rest framework - views import:
from rest_framework.authtoken.views import obtain_auth_token

# Django - import:
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views

# Drf spectacular - view import:
from drf_spectacular.views import SpectacularSwaggerView
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularAPIView

# Django - url import:
from django.contrib import admin
from django.urls import include
from django.urls import path


# URLs registration:
urlpatterns = [
    # Add the path for language switching:
    path('i18n/', include('django.conf.urls.i18n')),

    # API - token generator registration:
    path('api-admin/token-generate/', obtain_auth_token, name='token_generate'),

    # API - schema registration:
    path('api-schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api-docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api_docs'),
    path('api-rdocs/',
        SpectacularRedocView.as_view(url_name='api-schema'),
        name='api_rdocs'),

    # API views registration:
    path('api-notification/', include('notification.api.urls')),
]

urlpatterns += i18n_patterns(

    # Django - admin registration:
    path('admin/', admin.site.urls),

    # Test server registration:
    path('test/', include('hiking.urls'))
)
