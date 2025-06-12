from dotenv import load_dotenv
import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path
from termcolor import colored
from typing import Optional

load_dotenv()

# Directories & Files
# =====================================
ROOT_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = ROOT_DIR / "log"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "ninja_crawl.log"


# Env vars
# =====================================
ENV = os.getenv("ENV", "dev").lower()

# Logging
# =====================================
def setup_logging(env: Optional[str] = "prod"):
    """
    Setup logging configuration for the FastAPI application.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()
    
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=1024*1024*5,
        backupCount=3
    )
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    
    # Console handler - using colored formatter
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if env == "dev" else logging.INFO)
    
    class ColoredLevelFormatter(logging.Formatter):
        COLORS = {
            'DEBUG': 'blue',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red'
        }
        
        def format(self, record):
            levelname = f"{record.levelname}:".ljust(10)
            if record.levelname in self.COLORS:
                levelname = colored(levelname, self.COLORS[record.levelname])
            return levelname + record.getMessage()
    
    console_handler.setFormatter(ColoredLevelFormatter('%(levelname)-10s%(message)s'))
    logger.addHandler(console_handler)
    
    # UVICORN loggers
    for log in ["uvicorn", "uvicorn.access", "uvicorn.error"]:
        logging.getLogger(log).handlers = [h for h in logger.handlers if not isinstance(h, RotatingFileHandler)]