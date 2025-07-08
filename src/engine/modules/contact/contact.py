from typing import TYPE_CHECKING
from ...base import BaseEngine
from .address import AddressSniffer
from.email import EmailSniffer
from.phone import PhoneSniffer

if TYPE_CHECKING:
    from ...scraping_engine import ScrapingEngine


class ContactSniffer(BaseEngine):
    
    def __init__(self, engine: "ScrapingEngine"):
        super().__init__(engine=engine)
        self.address = AddressSniffer(self.engine)
        self.email = EmailSniffer(self.engine)
        self.phone = PhoneSniffer(self.engine)