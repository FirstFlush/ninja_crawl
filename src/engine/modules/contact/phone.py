import phonenumbers
from phonenumbers import PhoneNumberFormat, PhoneNumberMatcher
from ...base import BaseEngine


class PhoneSniffer(BaseEngine):

    def extract_number(self, text: str, region: str = "CA") -> str | None:
        _matches = PhoneNumberMatcher(text, region)
        for _match in _matches:
            number = _match.number
            if phonenumbers.is_valid_number(number):
                return phonenumbers.format_number(number, PhoneNumberFormat.E164)
        return None

    def extract_numbers(self, text: str, region: str = "CA") -> list[str]:
        results = []
        _matches = PhoneNumberMatcher(text, region)
        for _match in _matches:
            number = _match.number
            if phonenumbers.is_valid_number(number):
                formatted = phonenumbers.format_number(number, PhoneNumberFormat.E164)
                results.append(formatted)

        return results
    
