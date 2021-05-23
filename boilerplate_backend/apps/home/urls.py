from typing import Tuple

from django.urls import path

from .views import AboutView, async_home, async_page


class HomeApp:
    name = "home"

    def get_urls(self) -> list:
        urlpatterns = [
            path("", async_home, name="home"),
            path("about/", AboutView.as_view(), name="about"),
            path("p/<str:page>/", async_page, name="page"),
        ]
        return urlpatterns

    @property
    def urls(self) -> Tuple[list, str]:
        return self.get_urls(), self.name


home_urls = HomeApp()
