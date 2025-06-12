from .base_spider import BaseSpider
from .bc211 import BC211PdfSpider, BC211SearchSpider
from typing import Type


class SpiderRegistry:

    ACTIVE_SPIDERS: list[Type[BaseSpider]] = [
        BC211PdfSpider,
        BC211SearchSpider,
    ]
    
    def get_spider(self, key: str) -> BaseSpider:
        matches = [cls for cls in self.ACTIVE_SPIDERS if cls.check_keys(key)]
        if not matches:
            raise RuntimeError(f"No spider found for key: {key}")
        if len(matches) > 1:
            names = ', '.join(cls.__name__ for cls in matches)
            raise RuntimeError(f"Multiple spiders matched key `{key}`: {names}")
        
        return matches[0]()