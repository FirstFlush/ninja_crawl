from ..base_transformer import BaseTransformer
from ...common.enums.spider_keys import SpiderKeys



class BC211PdfTransformer(BaseTransformer):
    
    KEYS = [SpiderKeys.BC211_PDF]
    
    def scrape(self, raw_data: str, key: str):
                
        print(type(raw_data))
        
        return {
            "hi":"bye"
        }