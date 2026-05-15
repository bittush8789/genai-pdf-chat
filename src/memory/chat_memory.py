import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

def init_chat_memory():
    """Initialize chat memory in Streamlit session state."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
def get_chat_history_for_chain(limit: int = 5):
    """
    Convert session state messages to LangChain message objects for the RAG chain.
    """
    history = []
    recent_messages = st.session_state.messages[-(limit*2):]
    
    for msg in recent_messages:
        if msg["role"] == "user":
            history.append(HumanMessage(content=msg["content"]))
        else:
            history.append(AIMessage(content=msg["content"]))
    return history

def get_chat_messages_for_ui():
    """Return the raw list of dictionaries for UI rendering."""
    return st.session_state.messages

def add_message_to_history(role: str, content: str, sources: list = None):
    """Add a message to the session state."""
    msg = {"role": role, "content": content}
    if sources:
        msg["sources"] = sources
    st.session_state.messages.append(msg)

def clear_memory():
    """Clear the chat memory."""
    st.session_state.messages = []
