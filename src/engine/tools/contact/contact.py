from typing import TYPE_CHECKING
from ..base import BaseTool
from .address import AddressSniffer
from.email import EmailSniffer
from.phone import PhoneSniffer

if TYPE_CHECKING:
    from ..scraping_tools import ScrapingTools


class ContactSniffer(BaseTool):
    
    def __init__(self, tools: "ScrapingTools"):
        self.tools = tools
        self.address = AddressSniffer(self.tools)
        self.email = EmailSniffer(self.tools)
        self.phone = PhoneSniffer(self.tools)