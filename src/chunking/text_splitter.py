from typing import List
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.utils.logger import get_logger

logger = get_logger(__name__)

def split_documents(documents: List[Document], chunk_size: int = 1000, chunk_overlap: int = 200) -> List[Document]:
    """
    Split a list of documents into smaller chunks using RecursiveCharacterTextSplitter.
    """
    if not documents:
        logger.warning("No documents provided for splitting.")
        return []
        
    try:
        logger.info(f"Splitting {len(documents)} documents. (chunk_size={chunk_size}, chunk_overlap={chunk_overlap})")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            add_start_index=True,
        )
        
        chunks = text_splitter.split_documents(documents)
        logger.info(f"Successfully split into {len(chunks)} chunks.")
        return chunks
        
    except Exception as e:
        logger.error(f"Error during document splitting: {str(e)}")
        raise e
