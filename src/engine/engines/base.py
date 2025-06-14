from abc import ABC
from typing import Any
from ..tools.scraping_toolkit import ScrapingToolkit


class BaseEngine(ABC):
    
    tools = ScrapingToolkit()


class DefaultEngine(BaseEngine):

    def __init__(self, data: dict[str, Any]):
        self.data = data