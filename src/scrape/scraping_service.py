import logging
from typing import Any
from ..exc import SpiderError
from ..spiders.base_spider import BaseSpider
from ..common.types import JsonData

logger = logging.getLogger(__name__)


class ScrapingService:
    
    def __init__(self, key: str, spider: BaseSpider):
        self.key = key
        self.spider = spider

    def run_scrape(self, raw_data: str | bytes | JsonData) -> dict[str, Any] | None:
        try:
            logger.debug(f"{self.spider.__class__.__name__} starting scrape...")
            scraped_data = self._scrape(raw_data)
        except SpiderError:
            scraped_data = None
            msg = f"{self.spider.__class__.__name__} scrape failed due to a SpiderError"
            logger.error(msg)
        except Exception as e:
            scraped_data = None
            msg = f"{self.spider.__class__.__name__} scrape failed due to an unexpected `{e.__class__.__name__}` with spider key `{self.key}`"
            logger.error(msg, exc_info=True)
        else:
            logger.debug(f"{self.spider.__class__.__name__} scrape successful.")
            
        return scraped_data
        
    def _scrape(self, raw_data: str | bytes | JsonData) -> dict[str, Any]:
        try:
            return self.spider.scrape(raw_data=raw_data, key=self.key)
        finally:
            self.spider.clean_up()
