from typing import Any, Dict

from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import TemplateDoesNotExist


async def async_home(request: HttpRequest) -> HttpResponse:
    context: Dict[str, Any] = {}
    return render(request, "index.html", context)


async def async_page(request: HttpRequest, page: str) -> HttpResponse:
    context: Dict[str, Any] = {}
    template_path = f"pages/{page.replace('-', '_')}.html"

    try:
        return render(request, template_path, context)
    except TemplateDoesNotExist:
        raise Http404(f"Template: {template_path} does not exist")
