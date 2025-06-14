from .currency.currency_parser import CurrencyParser
from .datetime_util.datetime_util import DateTimeUtil
from .enum_toolkit import EnumToolkit 
from .region.region_matcher import RegionMatcher
from .regex.regex import RegexTool
from .contact.contact import ContactSniffer
from .text_toolkit import TextToolkit
from .types import TypeTransformer


class ScrapingToolkit:
    
    def __init__(self):
        self.contact = ContactSniffer(self)
        self.currency = CurrencyParser(self)
        self.date = DateTimeUtil(self)
        self.enum = EnumToolkit(self)
        self.regex = RegexTool(self)
        self.region = RegionMatcher(self)
        self.text = TextToolkit(self)
        self.types = TypeTransformer(self)
