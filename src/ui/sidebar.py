import streamlit as st
import os
import base64
from src.config.settings import settings
from src.loaders.document_loader import save_uploaded_files, load_documents
from src.chunking.text_splitter import split_documents
from src.embeddings.embedding_model import get_embeddings
from src.vectorstore.faiss_store import create_and_save_vectorstore, load_vectorstore
from src.memory.chat_memory import clear_memory
from src.utils.logger import get_logger

logger = get_logger(__name__)

def get_base64_image(image_path):
    """Convert an image to base64 string for HTML embedding."""
    try:
        if os.path.exists(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
        return None
    except Exception as e:
        logger.error(f"Error encoding image: {str(e)}")
        return None

def render_sidebar():
    """Render a clean, high-end sidebar without extra empty boxes."""
    if "language" not in st.session_state:
        st.session_state.language = "en"
        
    with st.sidebar:
        # 1. PREMIUM BRANDING
        st.markdown("""
            <div style="text-align: center; padding: 10px 0; margin-bottom: 20px;">
                <svg width="55" height="55" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <defs>
                        <linearGradient id="sidebar-grad" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" style="stop-color:#4F46E5;stop-opacity:1" />
                            <stop offset="100%" style="stop-color:#8B5CF6;stop-opacity:1" />
                        </linearGradient>
                    </defs>
                    <rect x="25" y="25" width="50" height="50" rx="12" stroke="url(#sidebar-grad)" stroke-width="4"/>
                    <path d="M40 50L47 57L60 43" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <h2 style="font-family: 'Space Grotesk', sans-serif; font-weight: 800; color: #F8FAFC; margin-top: 10px; letter-spacing: -1.5px; font-size: 1.6rem; margin-bottom: 0;">
                    Aristotle<span style="color:#6366F1;">.</span>
                </h2>
                <div style="color: #6366F1; font-size: 0.6rem; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase;">
                    PRO ENGINE V2
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<hr style='margin: 10px 0; opacity: 0.1;'>", unsafe_allow_html=True)

        # 2. CONFIGURATION SECTIONS (Clean Layout)
        st.markdown("#### 🌍 Output Language")
        lang_options = {"en": "English 🇺🇸", "hi": "Hindi 🇮🇳"}
        st.session_state.language = st.selectbox(
            "Select Response Language",
            options=list(lang_options.keys()),
            format_func=lambda x: lang_options[x],
            index=0 if st.session_state.language == "en" else 1,
            label_visibility="collapsed"
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("#### 💠 Intelligence")
        st.session_state.selected_model = st.selectbox(
            "Neural Engine",
            options=settings.SUPPORTED_MODELS,
            index=0,
            label_visibility="collapsed"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)

        # 3. KNOWLEDGE ASSETS
        st.markdown("#### 📂 Research Assets")
        uploaded_files = st.file_uploader(
            "Upload Files",
            type=["pdf", "png", "jpg", "jpeg"],
            accept_multiple_files=True,
            label_visibility="collapsed"
        )
        if st.button("SYNCHRONIZE", use_container_width=True, type="primary"):
            if uploaded_files:
                process_files(uploaded_files)
            else:
                st.warning("Upload files first")

        st.markdown("<hr style='margin: 20px 0; opacity: 0.1;'>", unsafe_allow_html=True)

        # 4. DEVELOPER PROFILE
        photo_path = os.path.join("phto", "Profile (1).jpg")
        img_base64 = get_base64_image(photo_path)
        
        with st.expander("◈ RESEARCHER PROFILE", expanded=False):
            if img_base64:
                st.markdown(f"""
                    <div style="text-align: center; padding: 5px;">
                        <img src="data:image/jpeg;base64,{img_base64}" style="width: 80px; height: 80px; border-radius: 15px; border: 2px solid #6366F1; object-fit: cover; margin-bottom: 8px;">
                        <div style="font-weight: 800; color: #F8FAFC; font-size: 1rem;">Bittu Sharma</div>
                        <div style="font-size: 0.7rem; color: #6366F1; font-weight: 700; text-transform: uppercase;">AI Lead</div>
                    </div>
                """, unsafe_allow_html=True)

        # 5. PURGE CONTROL
        if st.button("PURGE MEMORY", use_container_width=True):
            clear_memory()
            st.rerun()

def process_files(uploaded_files):
    """Secure document processing pipeline."""
    with st.spinner("Decoding Knowledge Base..."):
        try:
            saved_paths = save_uploaded_files(uploaded_files)
            documents = load_documents(saved_paths)
            if not documents:
                st.error("Processing failed.")
                return
                
            chunks = split_documents(documents)
            embeddings = get_embeddings()
            create_and_save_vectorstore(chunks, embeddings)
                
            st.session_state.vectorstore_ready = True
            st.toast("Intelligence Synced", icon="💠")
        except Exception as e:
            logger.error(f"Sync Fault: {str(e)}")
            st.error("Synchronization failed.")
