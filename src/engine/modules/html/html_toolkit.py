from ...base import BaseEngine
from bs4 import BeautifulSoup


class HtmlToolkit(BaseEngine):

    def _get_soup(self, markup: str, features: str = "lxml", **kwargs) -> BeautifulSoup:
        return BeautifulSoup(markup, features, **kwargs)
