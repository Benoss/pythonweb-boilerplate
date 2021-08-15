from .base_settings import *  # noqa
from boilerplate_backend.settings.base_settings import INSTALLED_APPS, MIDDLEWARE

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
# This is required for Django debug toolbar
INTERNAL_IPS = ["127.0.0.1", "localhost"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
MIDDLEWARE[:0] = ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa
INSTALLED_APPS += ["debug_toolbar"]

try:
    from .local import *  # noqa
except ImportError:  # pragma: no cover
    import logging
    import random
    from pathlib import Path

    local_settings = Path(__file__).resolve().parent / "local.py"
    random_string = "".join((random.choice("abcdefghijklmnopqrstuvwxyz")) for x in range(48))
    local_settings.write_text(f"SECRET_KEY = '{random_string}'\n")
    # Here you can write more to the local settings if needed

    logging.error(f"Could not find the local settings file{local_settings}, creating one with a new SECRET_KEY ...")
    from .local import *  # noqa
