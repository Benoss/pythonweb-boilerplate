from typing import Dict, List, Optional

from pydantic import BaseModel


class SwapiResponseList(BaseModel):
    message: str
    total_records: int
    total_pages: int
    previous: Optional[str]
    next: str
    results: List[Dict]
