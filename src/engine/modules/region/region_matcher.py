
from ...base import BaseEngine
from .municipalities import MunicipalityBC
from .provinces import ProvinceAbbreviation, ProvinceName


class RegionMatcher(BaseEngine):
    
    municipalities = MunicipalityBC
    provinces = ProvinceName
    provinces_abbreviated = ProvinceAbbreviation
    
    def get_municipality(self, text: str) -> MunicipalityBC | None:
        normalized = self.engine.text.normalize(text)
        return self.engine.enum.match_by_normalized_value(
            enum_cls=self.municipalities,
            text=normalized,
        )
    
    def get_province(self, text: str, abbreviation: bool = False) -> ProvinceName | ProvinceAbbreviation | None:
        normalized = self.engine.text.normalize(text)
        enum_cls = ProvinceAbbreviation if abbreviation else ProvinceName
        return self.engine.enum.match_by_normalized_value(
            enum_cls=enum_cls,
            text=normalized,
        )