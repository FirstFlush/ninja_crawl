from fastapi import Response, status
import logging
import time
from typing import Any
from ..models.io import ScrapeRequest, ScrapeResponse

logger = logging.getLogger(__name__)


class ScrapeIO:
    """
    Adapter layer between FastAPI route logic and the scraping service.

    ScrapeIO exists to decouple HTTP request/response formatting from the core scraping logic.
    It handles timing, error formatting, and response structuring without knowing anything about
    the internals of the spider or scraping service.

    This separation allows the route handler to remain thin and declarative, while ensuring all
    outgoing responses are consistent, time-stamped, and optionally include useful debug metadata.

    ScrapeIO does not invoke the scraping logic itself — it simply prepares for it and cleans up after.
    """
    def __init__(self, request: ScrapeRequest):
        self.request = request
        self._start: float | None = None

    def start_timer(self):
        self._start = time.monotonic()
        logger.debug("Scraping timer started")

    def stop_timer(self) -> int:
        if self._start is None:
            logger.error(f"{self.__class__.__name__}._start is None. elapsed_ms defaulting to 0")
            return 0
        else:
            elapsed_ms = int((time.monotonic() - self._start) * 1000)
            logger.debug(f"Scraping completed in {elapsed_ms}ms")
            return elapsed_ms

    def _error_to_str(self, e: Exception) -> str:
        return f"{e.__class__.__name__}: {str(e)}"

    def build_response(
            self, 
            scraped_data: dict[str, Any] | None,
            elapsed_ms: int,
            error: Exception | None = None,
    ) -> ScrapeResponse:
        logger.debug("Building ScrapeResponse object")
        success = bool(scraped_data)
        if not success:
            logger.error("No scraped data to build ScrapeResponse object with!")

        return ScrapeResponse(
            success=success,
            spider_key=self.request.spider_key,
            data=scraped_data,
            elapsed_ms=elapsed_ms,
            error=self._error_to_str(error) if error else None,
        )

    def http_response(self, response: ScrapeResponse) -> Response:
        return Response(
            content=response.model_dump_json(),
            status_code=status.HTTP_200_OK if response.success else status.HTTP_400_BAD_REQUEST,
        )