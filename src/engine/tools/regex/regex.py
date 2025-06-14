import re
from typing import Iterator
from ..base import BaseTool
from .regex_patterns import CommonPatterns


class RegexTool(BaseTool):

    common_patterns = CommonPatterns

    def find_all(self, pattern: str, text: str, flags: int = 0) -> list[str]:
        return re.findall(pattern, text, flags)

    def search(self, pattern: str, text: str, flags: int = 0) -> str | None:
        match = re.search(pattern, text, flags)
        return match.group(0) if match else None

    def sub(self, pattern: str, repl: str, text: str, flags: int = 0) -> str:
        return re.sub(pattern=pattern, repl=repl, string=text, flags=flags)


    def extract_groups(self, pattern: str, text: str, groups: list[int], flags: int = 0) -> list[str] | None:
        match = re.search(pattern, text, flags)
        if not match:
            return None
        return [match.group(i) for i in groups]

    def iter_matches(self, pattern: str, text: str, group: int = 0, flags: int = 0) -> Iterator[str]:
        for match in re.finditer(pattern, text, flags):
            yield match.group(group)

    def replace(self, pattern: str, repl: str, text: str, flags: int = 0) -> str:
        return re.sub(pattern, repl, text, flags)
    
    def has_match(self, pattern: str, text: str, flags: int = 0) -> bool:
        return re.search(pattern, text, flags) is not None