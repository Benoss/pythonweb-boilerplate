import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from typing import Dict, List

BASE_DIR = Path(__file__).resolve().parent.parent.parent
from django_jinja.builtins import DEFAULT_EXTENSIONS

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS: List[str] = []


# Application definition

INSTALLED_APPS: List[str] = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "boilerplate_backend.apps.core",
    "boilerplate_backend.apps.home",
]

MIDDLEWARE: List[str] = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "boilerplate_backend.urls"

TEMPLATES = [
    {
        # Django backends are used for django admin and debug toolbar
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
        },
    },
    {
        "NAME": "jinja2",
        "BACKEND": "django_jinja.backend.Jinja2",
        "DIRS": ["templates/"],
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".html",
            "match_regex": r"^(?!debug_toolbar/|admin/).*",
            # "environment": "webui.django.jinja2.environment",
            "extensions": DEFAULT_EXTENSIONS + ["boilerplate_backend.jinja2.CustomExtension"],
        },
    },
]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
WSGI_APPLICATION = "boilerplate_backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model
AUTH_USER_MODEL = "core.User"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# https://docs.djangoproject.com/en/3.2/releases/3.2/#customizing-type-of-auto-created-primary-keys
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"

USE_I18N = False
USE_L10N = False
USE_TZ = True

SERVER_PORT = os.environ.get("SERVER_PORT", 8080)
SERVER_HOST = "127.0.0.1"

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

TEMPLATE_ENVS: Dict = {}
RUN_GULP = False
