import streamlit as st
import time
from src.chains.rag_chain import create_rag_chain
from src.llm.groq_client import get_llm
from src.embeddings.embedding_model import get_embeddings
from src.vectorstore.faiss_store import load_vectorstore
from src.memory.chat_memory import get_chat_messages_for_ui, get_chat_history_for_chain, add_message_to_history
from src.ui.components import render_source_card
from src.utils.logger import get_logger

logger = get_logger(__name__)

def render_chat_ui():
    """Render a premium, centered AI research interface."""
    
    # 1. CENTERED CONTAINER START
    st.markdown('<div class="centered-container">', unsafe_allow_html=True)
    
    # 2. BRAND HEADER
    st.markdown('<h1 class="main-header">Aristotle<span style="color:#6366F1;">.</span>Pro</h1>', unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center; margin-top: -30px; margin-bottom: 50px; color: #64748B; font-weight: 500; font-size: 1.1rem; letter-spacing: 0.5px;">
            Advanced Document Intelligence & Neural Research Engine
        </div>
    """, unsafe_allow_html=True)
    
    # 3. CHAT HISTORY
    chat_messages = get_chat_messages_for_ui()
    if not chat_messages:
        render_welcome_screen()
    else:
        for message in chat_messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # 4. FIXED INPUT AREA
    prompt = st.chat_input("Enter your research query...")
    
    if prompt:
        handle_chat_interaction(prompt)
        
    st.markdown('</div>', unsafe_allow_html=True)

def render_welcome_screen():
    """Render a premium welcome screen for empty states."""
    st.markdown("""
        <div style="text-align: center; padding: 60px 20px; background: rgba(30, 41, 59, 0.2); border: 1px dashed #334155; border-radius: 30px; margin-top: 20px;">
            <div style="font-size: 3rem; margin-bottom: 20px;">💠</div>
            <h3 style="color: #F8FAFC; font-weight: 700; margin-bottom: 10px;">Ready to Analyze?</h3>
            <p style="color: #94A3B8; font-size: 0.95rem; max-width: 450px; margin: 0 auto;">
                Upload your research papers in the sidebar and synchronize the index to start an immersive AI-driven investigation.
            </p>
            <div style="margin-top: 30px; display: flex; justify-content: center; gap: 15px;">
                <span style="background: rgba(99, 102, 241, 0.1); color: #818CF8; padding: 6px 15px; border-radius: 10px; font-size: 0.75rem; font-weight: 700;">PDF Support</span>
                <span style="background: rgba(99, 102, 241, 0.1); color: #818CF8; padding: 6px 15px; border-radius: 10px; font-size: 0.75rem; font-weight: 700;">Neural OCR</span>
                <span style="background: rgba(99, 102, 241, 0.1); color: #818CF8; padding: 6px 15px; border-radius: 10px; font-size: 0.75rem; font-weight: 700;">Bilingual</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

def handle_chat_interaction(prompt):
    """Handle core chat logic with premium status feedback."""
    lang_map = {"en": "English", "hi": "Hindi"}
    selected_lang = lang_map.get(st.session_state.get("language", "en"), "English")
    
    with st.chat_message("user"):
        st.markdown(prompt)
    add_message_to_history("user", prompt)
    
    with st.chat_message("assistant"):
        status_label = "◈ रिसर्च इंटेलिजेंस" if selected_lang == "Hindi" else "◈ Research Intelligence"
        with st.status(status_label, expanded=True) as status:
            try:
                # Visualization feedback
                st.write("🔍 " + ("दस्तावेज़ों का विश्लेषण..." if selected_lang == "Hindi" else "Analyzing Knowledge Base..."))
                
                embeddings = get_embeddings()
                vectorstore = load_vectorstore(embeddings)
                
                if not vectorstore:
                    status.update(label="Index Required", state="error", expanded=False)
                    st.warning("Please synchronize documents in the sidebar.")
                    return
                
                st.write("📂 " + ("प्रासंगिक संदर्भ निकाला जा रहा है..." if selected_lang == "Hindi" else "Extracting semantic context..."))
                llm = get_llm(st.session_state.selected_model)
                retriever = vectorstore.as_retriever(search_kwargs={"k": 6})
                rag_chain = create_rag_chain(llm, retriever)
                
                st.write("🧠 " + ("उत्तर तैयार किया जा रहा है..." if selected_lang == "Hindi" else "Synthesizing response..."))
                response = rag_chain.invoke({
                    "input": prompt,
                    "chat_history": get_chat_history_for_chain(),
                    "language": selected_lang
                })
                
                answer = response["answer"]
                status.update(label="Complete", state="complete", expanded=False)
                
                # Render Answer
                st.markdown(answer)
                add_message_to_history("assistant", answer)
                
                # Source Cards
                if "context" in response:
                    source_title = "◈ Verified Sources" if selected_lang == "English" else "◈ प्रमाणित स्रोत"
                    with st.expander(source_title, expanded=False):
                        for doc in response["context"]:
                            render_source_card(
                                filename=doc.metadata.get("source_file", "Research Note"),
                                page=doc.metadata.get("page", 1),
                                snippet=doc.page_content
                            )
                            
            except Exception as e:
                logger.error(f"Chat Fault: {str(e)}")
                status.update(label="Fault Detected", state="error", expanded=False)
                st.error("Intelligence service interrupted. Please retry.")
