from typing import Any
from ..base_spider import JsonSpider
from ...enums.spider_keys import SpiderKeys


class BC211SearchSpider(JsonSpider):
    
    KEYS = [SpiderKeys.BC211_JSON]
    
    def scrape(self, raw_data: Any, key: str) -> dict[str, Any]:
        
        engine = self.get_engine(raw_data)
        print(raw_data[0])
        return {
            "rawData": raw_data,
        }