from fastapi import APIRouter, Response, status
from .models.io import ScrapeRequest
from .exc import NinjaCrawlError, SpiderRegistryError
from .scrape.scraping_service import ScrapingService
from .scrape.registry import SpiderRegistry
from .scrape.scrape_io import ScrapeIO
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/ping")
def ping():
    logger.debug("pinged!")
    return {"ping": "PONG"}


@router.post("/scrape")
def scrape(req: ScrapeRequest):
    
    scrape_io = ScrapeIO(request=req)
    scrape_io.start_timer()
    error = None
    try:
        spider = SpiderRegistry.get_spider(
            key=req.spider_key, 
            metadata=req.metadata,
        )
        service = ScrapingService(
            key=req.spider_key, 
            spider=spider
        )
    except NinjaCrawlError as e:
        scraped_data = None
        error = e
    except Exception as e:
        scraped_data = None
        logger.error(f"Unhandled `{e.__class__.__name__ }` in scrape route. scraped_data=None", exc_info=True)
        error = e
    else:
        scraped_data = service.run_scrape(req.raw_data)

    elapsed_ms = scrape_io.stop_timer()
    response =  scrape_io.build_response(
        scraped_data=scraped_data,
        elapsed_ms=elapsed_ms,
        error=error,
    )
    return scrape_io.http_response(response)
