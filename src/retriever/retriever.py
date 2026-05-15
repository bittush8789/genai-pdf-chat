from langchain_community.vectorstores import FAISS
from langchain_core.vectorstores import VectorStoreRetriever
from src.config.settings import settings
from src.utils.logger import get_logger

logger = get_logger(__name__)

def get_retriever(vectorstore: FAISS) -> VectorStoreRetriever:
    """
    Get a retriever interface from the FAISS vector store.
    """
    try:
        logger.info(f"Configuring retriever (type={settings.SEARCH_TYPE}, k={settings.TOP_K})")
        retriever = vectorstore.as_retriever(
            search_type=settings.SEARCH_TYPE,
            search_kwargs={"k": settings.TOP_K}
        )
        return retriever
    except Exception as e:
        logger.error(f"Failed to configure retriever: {str(e)}")
        raise e
