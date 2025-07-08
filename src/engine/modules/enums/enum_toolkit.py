from enum import Enum
from typing import Type, TypeVar
from ...base import BaseEngine


E = TypeVar("E", bound=Enum)


class EnumToolkit(BaseEngine):
    
    def match_by_normalized_value(
            self,
            enum_cls: Type[E],
            text: str
    ) -> E | None:
        normalized = self.engine.text.normalize(text)
        for member in enum_cls:
            if self.engine.text.normalize(member.value) == normalized:
                return member
            
        return None