from ...base import BaseEngine
from .mapping import CurrencyMapping

class CurrencyParser(BaseEngine):
    
    currency_mapping = CurrencyMapping
    
    def resolve_free(self, text: str) -> float | None:
        normalized = self.engine.text.normalize(text)
        amount = self.currency_mapping.get_key(
            text=normalized,
            mapping=self.currency_mapping.FREE_WORDS,
        )
        return float(amount) if amount else None
    
    def resolve_currency_type(self, text: str) -> str | None:
        
        normalized = self.engine.text.normalize(text)
        currency_type = self.currency_mapping.get_key(
            text=normalized,
            mapping=self.currency_mapping.CURRENCY_TYPES
        )
        return currency_type if currency_type else None