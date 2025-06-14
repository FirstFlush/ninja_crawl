
from ..base import BaseTool
from .municipalities import MunicipalityBC
from .provinces import ProvinceAbbreviation, ProvinceName


class RegionMatcher(BaseTool):
    
    municipalities = MunicipalityBC
    provinces = ProvinceName
    provinces_abbreviated = ProvinceAbbreviation
    
    def get_municipality(self, text: str) -> MunicipalityBC | None:
        normalized = self.tools.text.normalize(text)
        return self.tools.enum.match_by_normalized_value(
            enum_cls=self.municipalities,
            text=normalized,
        )
    
    def get_province(self, text: str, abbreviation: bool = False) -> ProvinceName | ProvinceAbbreviation | None:
        normalized = self.tools.text.normalize(text)
        enum_cls = ProvinceAbbreviation if abbreviation else ProvinceName
        return self.tools.enum.match_by_normalized_value(
            enum_cls=enum_cls,
            text=normalized,
        )