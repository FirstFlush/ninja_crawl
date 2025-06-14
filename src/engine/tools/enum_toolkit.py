from enum import Enum
from typing import Type, TypeVar
from .base import BaseTool


E = TypeVar("E", bound=Enum)


class EnumToolkit(BaseTool):
    
    def match_by_normalized_value(
            self,
            enum_cls: Type[E],
            text: str
    ) -> E | None:
        normalized = self.tools.text.normalize(text)
        for member in enum_cls:
            if self.tools.text.normalize(member.value) == normalized:
                return member
            
        return None