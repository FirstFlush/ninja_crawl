from .modules.currency.currency_parser import CurrencyParser
from .modules.datetime_util.datetime_util import DateTimeUtil
from .modules.enums.enum_toolkit import EnumToolkit 
from .modules.html.html_toolkit import HtmlToolkit
from .modules.pdf.pdf_toolkit import PdfToolkit
from .modules.region.region_matcher import RegionMatcher
from .modules.regex.regex import RegexTool
from .modules.contact.contact import ContactSniffer
from .modules.text.text_toolkit import TextToolkit
from .modules.types_util.types import TypeTransformer


class ScrapingEngine:
    
    def __init__(self):
        self.contact = ContactSniffer(self)
        self.currency = CurrencyParser(self)
        self.date = DateTimeUtil(self)
        self.enum = EnumToolkit(self)
        self.html = HtmlToolkit(self)
        self.pdf = PdfToolkit(self)
        self.regex = RegexTool(self)
        self.region = RegionMatcher(self)
        self.text = TextToolkit(self)
        self.types = TypeTransformer(self)
