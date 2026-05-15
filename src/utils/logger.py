import sys
from loguru import logger
from src.config.settings import settings

# Configure logger
logger.remove()
logger.add(sys.stdout, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>")
logger.add(settings.BASE_DIR / "logs" / "app.log", rotation="10 MB", retention="10 days", level="INFO")

def get_logger(name):
    return logger.bind(name=name)
