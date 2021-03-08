from django.conf import settings
from django.conf.urls import include

# from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from boilerplate_backend.apps.home.views import async_home, async_page

urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + [
    path(r"", async_home),
    path(r"p/<slug:page>/", async_page, name="page"),
    # path('admin/', admin.site.urls),
]

if settings.DEBUG and getattr(settings, "USE_DEBUG_TOOLBAR", settings.DEBUG):  # pragma: no cover
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
