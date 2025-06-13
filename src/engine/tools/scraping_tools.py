from .currency import CurrencyParser
from .date import DateUtil
from .types import TypeTransformer


class ScrapingTools:
    currency = CurrencyParser()
    date = DateUtil()
    types = TypeTransformer()