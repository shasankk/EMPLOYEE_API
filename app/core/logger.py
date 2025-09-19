# app/core/logger.py
import logging
from .config import settings
def setup_logger():
    logging.basicConfig(
        level=getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO),
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    return logging.getLogger("employee_api")
logger = setup_logger()
