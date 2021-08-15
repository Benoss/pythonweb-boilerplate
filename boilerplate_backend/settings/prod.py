from .base_settings import *  # noqa

DEBUG = False
ALLOWED_HOSTS = ["www.boilerplatebackend.com"]
STATIC_ROOT = BASE_DIR / ".static"  # noqa
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
COMPILE_JINJA = True

TEMPLATE_ENVS = {}
