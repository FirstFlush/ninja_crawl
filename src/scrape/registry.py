from ..spiders.base_spider import BaseSpider
from ..spiders.bc211 import BC211PdfSpider, BC211SearchSpider
import logging
from ..exc import SpiderRegistryError
from typing import Any, Type


logger = logging.getLogger(__name__)


class SpiderRegistry:

    ACTIVE_SPIDERS: list[Type[BaseSpider]] = [
        BC211PdfSpider,
        BC211SearchSpider,
    ]

    @classmethod
    def get_spider(
            cls, 
            key: str, 
            metadata: dict[str, Any] | None = None
    ) -> BaseSpider:
        try:
            spider = cls._get_spider(key=key, metadata=metadata)
        except RuntimeError as e:
            msg = f"Could not get Spider class with key `{key}` due to the following errors: "
            logger.error(msg, exc_info=True)
            raise SpiderRegistryError(msg) from e
        else:
            logger.debug(f"Instantiated spider: {spider.__class__.__name__}")
            return spider
    
    
    @classmethod
    def _get_spider(cls, key: str, metadata: dict[str, Any] | None = None) -> BaseSpider:
        matches = [spider_cls for spider_cls in cls.ACTIVE_SPIDERS if spider_cls.check_keys(key)]
        if not matches:
            raise RuntimeError(f"No spider found for key: {key}")
        if len(matches) > 1:
            names = ', '.join(spider_cls.__name__ for spider_cls in matches)
            raise RuntimeError(f"Multiple spiders matched key `{key}`: {names}")
        
        return matches[0](metadata=metadata)