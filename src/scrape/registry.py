from ..transformers.base_transformer import BaseTransformer
from ..transformers.bc211 import BC211PdfTransformer, BC211SearchTransformer
import logging
from ..exc import TransformerRegistryError
from typing import Any, Type


logger = logging.getLogger(__name__)


class TransformerRegistry:

    ACTIVE_TRANSFORMERS: list[Type[BaseTransformer]] = [
        BC211PdfTransformer,
        BC211SearchTransformer,
    ]

    @classmethod
    def get_transformer(
            cls, 
            key: str, 
            metadata: dict[str, Any] | None = None
    ) -> BaseTransformer:
        try:
            spider = cls._get_transformer(key=key, metadata=metadata)
        except RuntimeError as e:
            msg = f"Could not get Spider class with key `{key}` due to the following errors: "
            logger.error(msg, exc_info=True)
            raise TransformerRegistryError(msg) from e
        else:
            logger.debug(f"Instantiated spider: {spider.__class__.__name__}")
            return spider
    
    
    @classmethod
    def _get_transformer(cls, key: str, metadata: dict[str, Any] | None = None) -> BaseTransformer:
        matches = [spider_cls for spider_cls in cls.ACTIVE_TRANSFORMERS if spider_cls.check_keys(key)]
        if not matches:
            raise RuntimeError(f"No spider found for key: {key}")
        if len(matches) > 1:
            names = ', '.join(spider_cls.__name__ for spider_cls in matches)
            raise RuntimeError(f"Multiple spiders matched key `{key}`: {names}")
        
        return matches[0](metadata=metadata)