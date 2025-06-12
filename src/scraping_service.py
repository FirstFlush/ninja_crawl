import logging
from typing import Any
from .exc import ScrapingServiceError, SpiderError
from .enums.spider_keys import SpiderKeys
from .spiders.registry import SpiderRegistry
from .spiders.base_spider import BaseSpider

logger = logging.getLogger(__name__)


class ScrapingService:
    
    def __init__(
            self,
            key: str,
            registry: SpiderRegistry = SpiderRegistry(),
    ):
        self.key = key
        self.registry = registry
        self.spider = self._spider()

    def _spider(self) -> BaseSpider:
        try:
            spider = self.registry.get_spider(self.key)
        except RuntimeError as e:
            msg = f"Could not get Spider class with key `{self.key}` due to the following errors: "
            logger.error(msg, exc_info=True)
            raise ScrapingServiceError(msg) from e
        else:
            logger.debug(f"Instantiated spider: {spider.__class__.__name__}")
            return spider

    def scrape(self, data: str | bytes) -> dict[str, Any]:
        try:
            scraped_data = self.spider.scrape(data)
        except SpiderError:
            raise
        except Exception as e:
            msg = f"Unexpected `{e.__class__.__name__}` when scraping with spider `{self.spider.__class__.__name__}`"
            logger.error(msg, exc_info=True)
            raise ScrapingServiceError(msg) from e
        else:
            logger.debug(f"{self.spider.__class__.__name__} scrape successful.")
        finally:
            self.spider.clean_up()
        
        return scraped_data