from ..base import BaseTool
from bs4 import BeautifulSoup


class HtmlToolkit(BaseTool):

    def _get_soup(self, markup: str, features: str = "lxml", **kwargs) -> BeautifulSoup:
        return BeautifulSoup(markup, features, **kwargs)
