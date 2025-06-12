from pydantic import BaseModel


class ScrapeRequest(BaseModel):
    spider_key: str
    raw_data: str | bytes

