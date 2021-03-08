from typing import Dict, List

from pydantic import BaseModel


class SwapiResponseList(BaseModel):
    message: str
    total_records: int
    total_pages: int
    previous: str
    next: str
    results: List[Dict]
