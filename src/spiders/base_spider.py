from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import io
import logging
import pdfplumber
from typing import Any
from ..enums.spider_keys import SpiderKeys
from ..exc import SpiderError


logger = logging.getLogger(__file__)


class CssSelectors:
    body = "body"
    html = "html"


class BaseSpider(ABC):
    
    KEYS: list[SpiderKeys] | None = None

    def __init__(self, metadata: dict[str, Any] | None = None):
        self.metadata = metadata 

    @classmethod
    def check_keys(cls, key: str) -> bool:
        if not cls.KEYS or not isinstance(cls.KEYS, list):
            msg = f"{cls.__name__} has invalid KEYS attribute: `{cls.KEYS}`. Please set at least one valid key."
            logger.error(msg)
            raise SpiderError(msg)
        return key.strip() in [k.value for k in cls.KEYS]

    @abstractmethod
    def scrape(self, raw_data: str | bytes, key: str) -> dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def parse_data(self, data: str | bytes):
        raise NotImplementedError

    @abstractmethod
    def clean_up(self):
        raise NotImplementedError


class HtmlSpider(BaseSpider):
    
    css = CssSelectors
    
    def parse_data(self, data: str) -> BeautifulSoup:
        if not isinstance(data, str):
            msg = f"{self.__class__.__name__} expected HTML data as a string, but received type `{type(data)}`"
            logger.error(msg)
            raise SpiderError(msg)
        try:
            return BeautifulSoup(data, "lxml")
        except Exception as e:
            msg = f"{self.__class__.__name__} failed to create BeautifulSoup object"
            logger.error(msg, exc_info=True)
            raise SpiderError(msg) from e

    def clean_up(self):
        logger.debug(f"{self.__class__.__name__} has nothing to clean up")


class PdfSpider(BaseSpider):
    
    def __init__(self, metadata: dict[str, Any] | None = None):
        super().__init__(metadata=metadata)
        self._open_pdfs: list[pdfplumber.pdf.PDF] = []
    
    def parse_data(self, data: bytes) -> pdfplumber.pdf.PDF:
        try:
            pdf = pdfplumber.open(io.BytesIO(data))
        except Exception as e:
            msg = f"{self.__class__.__name__} received invalid PDF data of type `{type(data)}`"
            logger.error(msg, exc_info=True)
            raise SpiderError(msg) from e
        else:
            self._open_pdfs.append(pdf)
            return pdf

    def clean_up(self):
        for pdf in self._open_pdfs:
            logger.debug(f"{self.__class__.__name__}: closing open pdf")
            pdf.close()
        self._open_pdfs.clear()