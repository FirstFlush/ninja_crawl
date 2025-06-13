from ..base_spider import PdfSpider
from ...enums.spider_keys import SpiderKeys

class BC211PdfSpider(PdfSpider):
    
    KEYS = [SpiderKeys.BC211_PDF]
    
    def scrape(self, raw_data: bytes, key: str):
        self.parse_data(raw_data)