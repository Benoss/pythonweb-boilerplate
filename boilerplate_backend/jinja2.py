from typing import Optional
from uuid import uuid4

from django.conf import settings
from django.http import HttpRequest
from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment
from jinja2.ext import Extension


def is_current(url: str, request: HttpRequest) -> bool:
    return url == request.path


def page_url(page_slug: str) -> Optional[str]:
    return reverse("home:page", args=[page_slug])


class CustomExtension(Extension):
    def __init__(self, environment: Environment) -> None:
        super(CustomExtension, self).__init__(environment)
        environment.globals.update(
            {
                "page_url": page_url,
                "static": static,
                "url": reverse,
                "is_current": is_current,
                "DEBUG": settings.DEBUG,
            }
        )

        environment.filters["uuid4"] = lambda any_str: uuid4()
