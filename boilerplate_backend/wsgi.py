from django.apps import apps
from django.conf import settings
from django.core.wsgi import get_wsgi_application

apps.populate(settings.INSTALLED_APPS)
application = get_wsgi_application()
