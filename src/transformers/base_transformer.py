from abc import ABC, abstractmethod
import logging
from typing import Any
from ..common.enums.spider_keys import SpiderKeys
from ..exc import TransformerError
from ..common.types.types import JsonType


from ..engine.scraping_toolkit import ScrapingEngine

logger = logging.getLogger(__file__)
logging.getLogger("pdfminer").setLevel(logging.WARNING)


class BaseTransformer(ABC):
    
    KEYS: list[SpiderKeys] | None = None

    def __init__(self, metadata: dict[str, Any] | None = None):
        self.metadata = metadata 
        self.engine = ScrapingEngine()

    @classmethod
    def check_keys(cls, key: str) -> bool:
        if not cls.KEYS or not isinstance(cls.KEYS, list):
            msg = f"{cls.__name__} has invalid KEYS attribute: `{cls.KEYS}`. Please set at least one valid key."
            logger.error(msg)
            raise TransformerError(msg)
        return key.strip() in [k.value for k in cls.KEYS]

    def clean_up(self):
        if self.engine.pdf._open_pdfs:
            logger.debug(f"Closing {len(self.engine.pdf._open_pdfs)} open PDF streams...")
            self.engine.pdf.clean_up()
            logger.debug("All PDFs cleared from memory")

    @abstractmethod
    def scrape(self, raw_data: bytes | JsonType, key: str) -> dict[str, Any]:
        raise NotImplementedError
