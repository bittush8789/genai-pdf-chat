import os
import shutil
from pathlib import Path
from typing import List, Optional
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from PIL import Image
import pytesseract
import pdfplumber
from src.utils.logger import get_logger
from src.config.settings import settings

logger = get_logger(__name__)

def load_documents(file_paths: List[str]) -> List[Document]:
    """Load and parse PDFs and Images into LangChain Documents."""
    all_documents = []
    for path in file_paths:
        try:
            ext = Path(path).suffix.lower()
            filename = Path(path).name
            
            if ext == ".pdf":
                logger.info(f"Loading PDF: {path}")
                docs = []
                try:
                    # Try standard PyPDFLoader first
                    loader = PyPDFLoader(path)
                    docs = loader.load()
                except Exception as pypdf_err:
                    logger.warning(f"PyPDFLoader failed, falling back to pdfplumber: {str(pypdf_err)}")
                    # Fallback to pdfplumber for better extraction
                    with pdfplumber.open(path) as pdf:
                        for i, page in enumerate(pdf.pages):
                            text = page.extract_text()
                            if text:
                                docs.append(Document(
                                    page_content=text,
                                    metadata={"source_file": filename, "page": i+1}
                                ))
                
                if docs:
                    for doc in docs:
                        doc.metadata['source_file'] = filename
                    all_documents.extend(docs)
                    logger.info(f"Successfully loaded {len(docs)} pages from PDF: {filename}")
                else:
                    logger.error(f"No text extracted from PDF: {filename}")
                
            elif ext in [".png", ".jpg", ".jpeg", ".bmp", ".tiff"]:
                logger.info(f"Processing Image for OCR: {path}")
                text = pytesseract.image_to_string(Image.open(path))
                if text.strip():
                    doc = Document(
                        page_content=text,
                        metadata={"source_file": filename, "page": 1, "type": "image"}
                    )
                    all_documents.append(doc)
                    logger.info(f"Successfully extracted text from Image: {filename}")
                else:
                    logger.warning(f"No text found in image: {filename}")
            
            else:
                logger.warning(f"Unsupported file format: {ext} for file {filename}")
                
        except Exception as e:
            logger.error(f"Error loading document {path}: {str(e)}")
            
    return all_documents

def save_uploaded_files(uploaded_files) -> List[str]:
    """Save Streamlit UploadedFile objects to disk."""
    saved_paths = []
    for uploaded_file in uploaded_files:
        try:
            file_path = settings.RAW_DATA_DIR / uploaded_file.name
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            saved_paths.append(str(file_path))
            logger.info(f"Saved uploaded file to {file_path}")
        except Exception as e:
            logger.error(f"Error saving {uploaded_file.name}: {str(e)}")
    return saved_paths

def clean_raw_data() -> None:
    """Clean up raw data directory."""
    try:
        for file in settings.RAW_DATA_DIR.iterdir():
            if file.is_file():
                file.unlink()
        logger.info("Cleaned up raw data directory.")
    except Exception as e:
        logger.error(f"Error cleaning raw data: {str(e)}")
