from typing import Any
from ..base_spider import JsonSpider
from ...common.enums.spider_keys import SpiderKeys
from ...common.types import JsonData

class BC211SearchSpider(JsonSpider):
    
    KEYS = [SpiderKeys.BC211_SEARCH_HOMELESSNESS]
    
    def scrape(self, raw_data: JsonData, key: str) -> dict[str, Any]:
        
        transformed_results = []
        engine = self.get_engine(raw_data)
        for result in raw_data:
            transformed_results.append(self.transform_result(result))
        
        return {
            "rawData": raw_data,
        }
        
    def transform_result(self, result):
        ...
    