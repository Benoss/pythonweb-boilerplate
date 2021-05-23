from pathlib import Path
from typing import Any, Optional

from django.conf import settings
from django.http import HttpRequest
from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment, FileSystemBytecodeCache


def page_url(page_slug: str) -> Optional[str]:
    return reverse("home:page", args=[page_slug])


def is_current(url: str, request: HttpRequest) -> bool:
    return url == request.path


def environment(**options: Any) -> Environment:
    cache_path = Path("./cache/")
    cache_path.mkdir(exist_ok=True)
    fsbc = FileSystemBytecodeCache(str(cache_path))
    options["trim_blocks"] = True
    options["lstrip_blocks"] = True
    options["bytecode_cache"] = fsbc
    env = Environment(**options)
    env.globals.update(
        {"static": static, "url": reverse, "DEBUG": settings.DEBUG, "page_url": page_url, "is_current": is_current}
    )
    env.globals.update(settings.TEMPLATE_ENVS)
    return env
