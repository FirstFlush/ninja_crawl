import dateparser
from datetime import datetime
from ..base import BaseTool
from .time_mapping import TimeMapping


class DateTimeUtil(BaseTool):
    
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
        normalized = self.tools.text.normalize(text)
        return self.dt_from_context(normalized)
        
    def dt_from_context(self, text: str) -> datetime | None:
        time_str_tuple = self._check_mapping(text)
        if time_str_tuple:
            meridian = self.get_meridian(text, time_str=time_str_tuple[1])
            if meridian:
                time_str = time_str_tuple[0] + meridian
        else:
            normalized_whitespace = self.tools.text.normalize(text, keep_whitespace=True)
            time_str = self._check_keywords(normalized_whitespace)        
        if time_str:
            return self.get_dt(time_str)
        return None

    def get_meridian(self, text: str, time_str: str) -> str | None:
        meridian = self._check_merdian_suffix(text, time_str)
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
    
    def _check_merdian_suffix(self, text: str, time_str: str) -> str | None:
        first_char_index = text.find(time_str) + len(time_str)
        third_char_index = first_char_index + 2
        meridian = text[first_char_index:third_char_index].lower()
        if meridian == "am":
            return "am"
        elif meridian == "pm":
            return "pm"
        else: return None

    def _infer_meridian_from_context(self, text: str) -> str | None:
        return self.time_mapping.get_key(
            text=text,
            mapping=self.time_mapping.TIME_CONTEXTS
        )