from ..base_spider import PdfSpider
from ...enums.spider_keys import SpiderKeys

class BC211PdfSpider(PdfSpider):
    
    KEY = [SpiderKeys.BC211_PDF]
    
    def scrape(self, data: bytes):
        self.parse_data(data)