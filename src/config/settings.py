import os
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App Settings
    APP_NAME: str = "Aristotle AI | Research Assistant"
    APP_VERSION: str = "1.2.1"
    
    # Paths
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
    DATA_DIR: Path = BASE_DIR / "data"
    RAW_DATA_DIR: Path = DATA_DIR / "raw"
    VECTOR_STORE_DIR: Path = DATA_DIR / "vector_store"
    ASSETS_DIR: Path = BASE_DIR / "assets"
    
    # LLM Settings
    GROQ_API_KEY: str = Field(default=os.getenv("GROQ_API_KEY", ""))
    DEFAULT_MODEL: str = "llama-3.1-8b-instant"
    
    # Expanded Model List from user request
    SUPPORTED_MODELS: list[str] = [
        "llama-3.1-8b-instant",
        "llama-3.3-70b-versatile",
        "llama3-70b-8192",
        "mixtral-8x7b-32768",
        "gemma2-9b-it",
        "groq/compound",
        "groq/compound-mini",
        "canopylabs/orpheus-v1-english",
        "openai/gpt-oss-120b",
        "openai/gpt-oss-20b",
        "whisper-large-v3-turbo"
    ]
    
    # Embedding Settings
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    
    # Chunking Settings
    CHUNK_SIZE: int = 1000 
    CHUNK_OVERLAP: int = 200
    
    # Retrieval Settings
    SEARCH_TYPE: str = "similarity"
    TOP_K: int = 6

    class Config:
        env_file = ".env"

# Initialize settings
settings = Settings()

# Ensure directories exist
settings.RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
settings.VECTOR_STORE_DIR.mkdir(parents=True, exist_ok=True)
settings.ASSETS_DIR.mkdir(parents=True, exist_ok=True)
