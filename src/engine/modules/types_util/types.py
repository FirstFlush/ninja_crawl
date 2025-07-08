from ...base import BaseEngine
from decimal import Decimal

class TypeTransformer(BaseEngine):
    
    TRUE_VALUES = {"true", "yes", "y",}
    FALSE_VALUES = {"false", "no", "n",}

    def to_bool(self, text: str) -> bool | None:
        """
        Strictly parses a boolean value from a single data field.
        """
        cleaned = text.lower().strip()
        if cleaned in self.TRUE_VALUES:
            return True
        if cleaned in self.FALSE_VALUES:
            return False
        return None
        
    def infer_bool(self, text: str) -> bool | None:
        """
        Infers a boolean value from a sentence or messy input.
        """
        cleaned = text.lower().strip()
        if any(val in cleaned for val in self.engine.types.TRUE_VALUES if len(val) > 1):
            return True
        if any(val in cleaned for val in self.engine.types.FALSE_VALUES if len(val) > 1):
            return False
        return None

    def to_decimal(self, text: str) -> Decimal | None:
        num = self.to_float(text)
        return Decimal(num) if num is not None else None

    def to_float(self, text: str) -> float | None:
        cleaned = text.lower().strip()
        pattern = self.engine.regex.common_patterns.TO_FLOAT
        float_text = self.engine.regex.search(pattern=pattern, text=cleaned)
        if float_text is not None:
            return float(float_text)
        return None
    
    def to_int(self, text: str) -> int | None:
        value = self.to_float(text)
        if value is not None and value.is_integer():
            return int(value)
        return None