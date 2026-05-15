from langchain_huggingface import HuggingFaceEmbeddings
from src.config.settings import settings
from src.utils.logger import get_logger

logger = get_logger(__name__)

def get_embeddings() -> HuggingFaceEmbeddings:
    """
    Initialize and return the HuggingFace embeddings model.
    """
    try:
        logger.info(f"Initializing embeddings model: {settings.EMBEDDING_MODEL}")
        embeddings = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL,
            model_kwargs={'device': 'cpu'}, # Configured for CPU-friendly setup
            encode_kwargs={'normalize_embeddings': True}
        )
        return embeddings
    except Exception as e:
        logger.error(f"Failed to initialize embeddings model: {str(e)}")
        raise e
