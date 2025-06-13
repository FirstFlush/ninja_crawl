from pydantic import BaseModel
from typing import Any, Optional


class ScrapeRequest(BaseModel):
    
    spider_key: str
    raw_data: str | bytes
    metadata: Optional[dict[str, Any]] = None


class ScrapeResponse(BaseModel):
    
    success: bool
    spider_key: str
    data: Optional[dict[str, Any]] = None
    error: Optional[str] = None
    elapsed_ms: Optional[int]