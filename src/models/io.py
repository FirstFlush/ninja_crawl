from pydantic import BaseModel
from typing import Any, Optional
from ..common.types.types import JsonType


class ScrapeRequest(BaseModel):
    
    spider_key: str
    raw_data: bytes | JsonType
    metadata: Optional[dict[str, Any]] = None


class ScrapeResponse(BaseModel):
    
    success: bool
    spider_key: str
    data: Optional[dict[str, Any]] = None
    error: Optional[str] = None
    elapsed_ms: Optional[int]