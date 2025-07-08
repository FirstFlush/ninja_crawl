from typing import Any
from ..base_transformer import BaseTransformer
from ...common.enums.spider_keys import SpiderKeys
from ...common.types.types import JsonType


class BC211SearchTransformer(BaseTransformer):
    
    KEYS = [SpiderKeys.BC211_SEARCH_HOMELESSNESS]
    
    def scrape(self, raw_data: JsonType, key: str) -> dict[str, Any]:
        
        return {
            "rawData": raw_data,
        }
    