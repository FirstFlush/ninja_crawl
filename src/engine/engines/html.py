from .base import BaseEngine
from bs4 import BeautifulSoup


class HtmlEngine(BaseEngine):
    
    def __init__(self, soup: BeautifulSoup):
        self.soup = soup