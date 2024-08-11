# Python - library import:
import os

# Django - wsgi import:
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wanderswiss.settings')
application = get_wsgi_application()
