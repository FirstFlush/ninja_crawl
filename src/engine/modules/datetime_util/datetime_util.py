import dateparser
from datetime import datetime
from ...base import BaseEngine
from .time_mapping import TimeMapping


class DateTimeUtil(BaseEngine):
    
    time_mapping = TimeMapping
    
    def get_dt(self, text: str) -> datetime | None:
        dt = dateparser.parse(text)
        if dt:
            return dt
        return None
    
    def parse(self, text: str) -> datetime | None:
        dt = self.get_dt(text)
        if dt:
            return dt
        normalized = self.engine.text.normalize(text)
        return self.dt_from_context(normalized)
        
    def dt_from_context(self, text: str) -> datetime | None:
        
        time_str = None
        _match = self._check_mapping(text)
        
        if _match:
            base_time, match_string = _match
            meridian = self.resolve_meridian(text, match_string)
            time_str = f"{base_time} {meridian}" if meridian else base_time
        else:
            normalized = self.engine.text.normalize(text, keep_whitespace=True)
            time_str = self._check_keywords(normalized)
        
        return self.get_dt(time_str) if time_str else None

    def resolve_meridian(self, text: str, time_str: str) -> str | None:
        meridian = self._check_meridian_suffix(text, time_str)
        if not meridian:
            meridian = self._infer_meridian_from_context(text)
        return meridian

    def _check_mapping(self, text: str) -> tuple[str, str] | None:
        return self.time_mapping.get_key_with_match(
            text=text,
            mapping=self.time_mapping.CLOCK_TIMES,
        )

    def _check_keywords(self, text: str) -> str | None:
        return self.time_mapping.get_key(
            text=text,
            mapping=self.time_mapping.KEYWORDS
        )

    def _check_meridian_suffix(self, text: str, time_str: str) -> str | None:
        idx = text.find(time_str)
        if idx == -1:
            return None
        suffix = text[idx + len(time_str):].strip().lower()
        if suffix.startswith("am"):
            return "am"
        if suffix.startswith("pm"):
            return "pm"
        return None

    def _infer_meridian_from_context(self, text: str) -> str | None:
        return self.time_mapping.get_key(
            text=text,
            mapping=self.time_mapping.TIME_CONTEXTS
        )