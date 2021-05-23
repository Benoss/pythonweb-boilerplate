import httpx as requests
from django.http import HttpRequest
from ninja import NinjaAPI

from .models import SwapiResponseList

api = NinjaAPI()


@api.get("/people/", tags=["people"])
async def get_users(request: HttpRequest) -> SwapiResponseList:
    client = requests.AsyncClient()
    resp = await client.get("https://www.swapi.tech/api/people/")
    await client.aclose()
    response_list = SwapiResponseList.parse_obj(resp.json())
    return response_list
