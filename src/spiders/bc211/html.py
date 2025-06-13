from typing import Any
from ..base_spider import HtmlSpider, CssSelectors
from ...enums.spider_keys import SpiderKeys


class BC211CssSelectors(CssSelectors):
    
    result = "article.resultCard"
    

class BC211SearchSpider(HtmlSpider):
    
    KEYS = [SpiderKeys.BC211_HTML]
    css = BC211CssSelectors
    
    def scrape(self, raw_data: str, key: str) -> dict[str, Any]:
        
        soup = self.parse_data(raw_data)
        results = soup.select(self.css.result)
        print(results)
        
        
        return {
            "resultCount": len(results),
        }