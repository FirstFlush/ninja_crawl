from fastapi import APIRouter
from .models import ScrapeRequest
from .exc import NinjaCrawlError
from .scraping_service import ScrapingService
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/ping")
def ping():
    logger.debug("pinged!")
    return {"ping": "PONG"}


@router.post("/scrape")
def scrape(req: ScrapeRequest):
    
    try:
        ss = ScrapingService(key=req.spider_key)
        ss.scrape(req.raw_data)
    except NinjaCrawlError as e:
        ...
    except Exception as e:
        msg = f"Unexpected `{e.__class__.__name__}` while attempting to scrape with key `{ss.key}` and spider `{ss.spider}`"
        logger.critical(msg, exc_info=True)
        
    return {"message": f"Scraping with {req.spider_key}"}