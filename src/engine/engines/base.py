from abc import ABC
from typing import Any
from ..tools.scraping_tools import ScrapingTools


class BaseEngine(ABC):
    
    tools = ScrapingTools()


class DefaultEngine(BaseEngine):

    def __init__(self, data: dict[str, Any]):
        self.data = data