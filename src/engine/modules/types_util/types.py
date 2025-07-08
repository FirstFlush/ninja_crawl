from ...base import BaseEngine


class TypeTransformer(BaseEngine):
    
    TRUE_VALUES = {"true", "yes", "y",}
    FALSE_VALUES = {"false", "no", "n",}

    def to_bool(self, text: str) -> bool | None:
        cleaned = text.lower().strip()
            
        if cleaned in self.TRUE_VALUES:
            return True
        if cleaned in self.FALSE_VALUES:
            return False
        for val in self.TRUE_VALUES:
            if val in cleaned and len(val) > 1:
                return True
        for val in self.FALSE_VALUES:
            if val in cleaned and len(val) > 1:
                return False
        return None

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