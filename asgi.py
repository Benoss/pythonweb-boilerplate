from django.apps import apps
from django.conf import settings
from django.core.asgi import get_asgi_application as django_get_asgi_application
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

apps.populate(settings.INSTALLED_APPS)


def get_application() -> FastAPI:
    from boilerplate_backend.api.urls import router as api_router

    app = FastAPI(debug=settings.DEBUG)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(api_router, prefix="/api")

    if not settings.DEBUG:
        app.mount(
            settings.STATIC_URL.rstrip("/"),
            StaticFiles(directory=settings.STATIC_ROOT),
            name="static",
        )
    app.mount("/", django_get_asgi_application())

    return app


app = get_application()
