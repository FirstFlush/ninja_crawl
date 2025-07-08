import logging
from typing import Any
from ..exc import TransformerError
# from ..transformers.base_spider import BaseSpider
from ..transformers.base_transformer import BaseTransformer
from ..common.types.types import JsonType

logger = logging.getLogger(__name__)


class ScrapingService:
    
    def __init__(self, key: str, transformer: BaseTransformer):
        self.key = key
        self.transformer = transformer

    def run_scrape(self, raw_data: bytes | JsonType) -> dict[str, Any] | None:
        try:
            logger.debug(f"{self.transformer.__class__.__name__} starting scrape...")
            scraped_data = self._scrape(raw_data)
        except TransformerError:
            scraped_data = None
            msg = f"{self.transformer.__class__.__name__} scrape failed due to a SpiderError"
            logger.error(msg)
        except Exception as e:
            scraped_data = None
            msg = f"{self.transformer.__class__.__name__} scrape failed due to an unexpected `{e.__class__.__name__}` with spider key `{self.key}`"
            logger.error(msg, exc_info=True)
        else:
            logger.debug(f"{self.transformer.__class__.__name__} scrape successful.")
            
        return scraped_data
        
    def _scrape(self, raw_data: bytes | JsonType) -> dict[str, Any]:
        try:
            return self.transformer.scrape(raw_data=raw_data, key=self.key)
        finally:
            self.transformer.clean_up()
