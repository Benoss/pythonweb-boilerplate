from django.apps import apps
from django.conf import settings
from django.core.asgi import get_asgi_application as django_get_asgi_application

apps.populate(settings.INSTALLED_APPS)
app = django_get_asgi_application()
