from abc import ABC
from ...common.types import JsonData
from ..tools.scraping_toolkit import ScrapingToolkit


class BaseEngine(ABC):
    
    tools = ScrapingToolkit()


class JsonEngine(BaseEngine):

    def __init__(self, data: JsonData):
        self.data = data