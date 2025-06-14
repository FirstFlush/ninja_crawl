from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .scraping_tools import ScrapingTools


class BaseTool(ABC):

    def __init__(self, tools: "ScrapingTools"):
        self.tools = tools