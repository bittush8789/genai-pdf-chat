import os
import sys
from dotenv import load_dotenv
import streamlit as st

# Ensure the current directory is in sys.path for local imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables
load_dotenv()

from src.ui.components import set_page_config, inject_custom_css
from src.ui.sidebar import render_sidebar
from src.ui.chat_ui import render_chat_ui
from src.memory.chat_memory import init_chat_memory
from src.config.settings import settings
from src.embeddings.embedding_model import get_embeddings
# Reverted to faiss_store
from src.vectorstore.faiss_store import load_vectorstore

def check_env_vars():
    """Ensure required environment variables are set."""
    if not settings.GROQ_API_KEY or settings.GROQ_API_KEY == "your_key_here":
        st.error("⚠️ GROQ_API_KEY is missing. Please set it in your .env file.")
        st.stop()

def initialize_app_state():
    """Initialize session state variables with FAISS check."""
    init_chat_memory()
    if "vectorstore_ready" not in st.session_state:
        try:
            embeddings = get_embeddings()
            vectorstore = load_vectorstore(embeddings)
            st.session_state.vectorstore_ready = vectorstore is not None
        except:
            st.session_state.vectorstore_ready = False

def main():
    """Main application entry point."""
    set_page_config()
    inject_custom_css()
    check_env_vars()
    initialize_app_state()
    
    render_sidebar()
    render_chat_ui()

if __name__ == "__main__":
    main()
