import httpx as request
from fastapi import APIRouter

from .models import SwapiResponseList

router = APIRouter()


@router.get("/people/", tags=["people"])
async def get_users() -> SwapiResponseList:
    resp = await request.get("https://www.swapi.tech/api/people/").json()
    response_list = SwapiResponseList.parse_obj(resp)
    return response_list
