import sys
from loguru import logger
from src.config.settings import settings

# Configure logger
logger.remove()
logger.add(sys.stdout, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>")

# Ensure log directory exists before adding file logger
log_dir = settings.BASE_DIR / "logs"
try:
    log_dir.mkdir(parents=True, exist_ok=True)
    logger.add(log_dir / "app.log", rotation="10 MB", retention="10 days", level="INFO")
except Exception as e:
    # Fallback if filesystem is read-only
    print(f"Warning: Could not initialize file logging: {e}")

def get_logger(name):
    return logger.bind(name=name)
