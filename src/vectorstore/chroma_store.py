import os
import shutil
from typing import List, Optional
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_core.embeddings import Embeddings
from src.config.settings import settings
from src.utils.logger import get_logger

logger = get_logger(__name__)

def get_chroma_path() -> str:
    """Return the persistent directory for ChromaDB."""
    return str(settings.VECTOR_STORE_DIR / "chroma_db")

def create_and_save_vectorstore(chunks: List[Document], embeddings: Embeddings) -> Chroma:
    """Create a new Chroma vector store and persist it to disk."""
    try:
        save_path = get_chroma_path()
        logger.info(f"Creating ChromaDB at {save_path}...")
        
        # If directory exists, clear it for a fresh index
        if os.path.exists(save_path):
            shutil.rmtree(save_path)
            
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=save_path
        )
        # In newer LangChain/Chroma, persistence is automatic, 
        # but we call it for compatibility if available.
        return vectorstore
    except Exception as e:
        logger.error(f"Error creating ChromaDB: {str(e)}")
        raise e

def load_vectorstore(embeddings: Embeddings) -> Optional[Chroma]:
    """Load an existing Chroma vector store from disk."""
    save_path = get_chroma_path()
    
    if os.path.exists(save_path) and os.path.isdir(save_path):
        try:
            logger.info(f"Loading ChromaDB from {save_path}")
            vectorstore = Chroma(
                persist_directory=save_path,
                embedding_function=embeddings
            )
            return vectorstore
        except Exception as e:
            logger.error(f"Error loading ChromaDB: {str(e)}")
            return None
    
    logger.info("No existing ChromaDB found.")
    return None

def clear_vectorstore() -> None:
    """Delete the existing ChromaDB from disk."""
    save_path = get_chroma_path()
    if os.path.exists(save_path):
        try:
            shutil.rmtree(save_path)
            logger.info("Cleared existing ChromaDB.")
        except Exception as e:
            logger.error(f"Error clearing ChromaDB: {str(e)}")
