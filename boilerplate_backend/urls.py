from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from boilerplate_backend.api.urls import api
from boilerplate_backend.apps.home.urls import home_urls

urlpatterns = [
    path(r"", include(home_urls.urls)),
    path("api/", api.urls),
]
urlpatterns += [
    path("admin/", admin.site.urls),
]


if settings.DEBUG and getattr(settings, "USE_DEBUG_TOOLBAR", settings.DEBUG):  # pragma: no cover
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
