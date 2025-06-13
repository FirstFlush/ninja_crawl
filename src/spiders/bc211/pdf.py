from ..base_spider import PdfSpider
from ...enums.spider_keys import SpiderKeys

class BC211PdfSpider(PdfSpider):
    
    KEYS = [SpiderKeys.BC211_PDF]
    
    def scrape(self, raw_data: bytes, key: str):
        engine = self.get_engine(raw_data)