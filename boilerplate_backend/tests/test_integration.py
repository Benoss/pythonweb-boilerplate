from django.http import HttpResponse
from django.test import TestCase


class MyTests(TestCase):
    def get_url_response(self, url: str, response_code: int = 200) -> HttpResponse:
        res: HttpResponse = self.client.get(url)
        self.assertEqual(res.status_code, response_code)
        return res

    def test_api_docs(self) -> None:
        self.get_url_response("/api/docs")

    def test_api_people(self) -> None:
        self.get_url_response("/api/people/")

    def test_pages(self) -> None:
        self.get_url_response("/")
        self.get_url_response("/about/")
        self.get_url_response("/p/login/")
        self.get_url_response("/p/pricing", 301)
        self.get_url_response("/p/pricing/")
