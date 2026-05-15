import os
import shutil
from typing import List, Optional
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_core.embeddings import Embeddings
from src.config.settings import settings
from src.utils.logger import get_logger

logger = get_logger(__name__)

def get_vectorstore_path() -> str:
    return str(settings.VECTOR_STORE_DIR / "faiss_index")

def create_and_save_vectorstore(chunks: List[Document], embeddings: Embeddings) -> FAISS:
    """Create a new FAISS vector store from chunks and save it to disk."""
    try:
        logger.info("Creating FAISS vector store...")
        vectorstore = FAISS.from_documents(chunks, embeddings)
        
        save_path = get_vectorstore_path()
        logger.info(f"Saving vector store to {save_path}")
        vectorstore.save_local(save_path)
        
        return vectorstore
    except Exception as e:
        logger.error(f"Error creating vector store: {str(e)}")
        raise e

def load_vectorstore(embeddings: Embeddings) -> Optional[FAISS]:
    """Load an existing FAISS vector store from disk."""
    save_path = get_vectorstore_path()
    
    if os.path.exists(save_path) and os.path.isdir(save_path) and os.path.exists(os.path.join(save_path, "index.faiss")):
        try:
            logger.info(f"Loading existing vector store from {save_path}")
            # Ensure dangerous deserialization is enabled if needed for FAISS load_local
            vectorstore = FAISS.load_local(save_path, embeddings, allow_dangerous_deserialization=True)
            return vectorstore
        except Exception as e:
            logger.error(f"Error loading vector store: {str(e)}")
            return None
    
    logger.info("No existing vector store found.")
    return None

def clear_vectorstore() -> None:
    """Delete the existing vector store from disk."""
    save_path = get_vectorstore_path()
    if os.path.exists(save_path):
        try:
            shutil.rmtree(save_path)
            logger.info("Cleared existing vector store.")
        except Exception as e:
            logger.error(f"Error clearing vector store: {str(e)}")
