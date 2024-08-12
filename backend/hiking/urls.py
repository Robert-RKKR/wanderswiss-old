# Django - path import:
from django.urls import path

# Capybara - view import:
from .views import test

# App name registration:
app_name = 'test'

# URLs registration:
urlpatterns = [
    path('test/', test, name='test'),
]
