from ..base_spider import HtmlSpider
from ...enums.spider_keys import SpiderKeys

class BC211SearchSpider(HtmlSpider):
    
    KEYS = [SpiderKeys.BC211_HTML]