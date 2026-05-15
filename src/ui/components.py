import streamlit as st

def set_page_config():
    """Configure the Streamlit page with professional AI SaaS defaults."""
    st.set_page_config(
        page_title="Aristotle Pro | Premium Research AI",
        page_icon="💠",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def inject_custom_css():
    """
    Inject the 'Aether V2' ultra-premium design system.
    Focuses on glassmorphism, depth, and startup-grade aesthetics.
    """
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
        
        /* 1. CORE DESIGN TOKENS */
        :root {
            --bg-main: #020817;
            --bg-sidebar: #0F172A;
            --bg-card: #111827;
            --bg-glass: rgba(17, 24, 39, 0.75);
            --border-main: #334155;
            --accent-primary: #4F46E5;
            --accent-secondary: #8B5CF6;
            --text-primary: #F8FAFC;
            --text-secondary: #CBD5E1;
            --glow-blue: rgba(79, 70, 229, 0.4);
        }

        /* 2. LAYOUT & FRAMEWORK OVERRIDES */
        html, body, [data-testid="stAppViewContainer"] {
            background-color: var(--bg-main) !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: var(--text-primary) !important;
        }

        [data-testid="stHeader"], footer, #MainMenu { visibility: hidden !important; height: 0 !important; }
        .stDeployButton { display: none !important; }

        /* Centered Research Area */
        [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
            max-width: 900px !important;
            margin: 0 auto !important;
        }

        /* 3. SIDEBAR REDESIGN */
        [data-testid="stSidebar"] {
            background-color: var(--bg-sidebar) !important;
            border-right: 1px solid var(--border-main) !important;
            width: 320px !important;
        }
        
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
            padding: 2rem 1.2rem !important;
        }

        .sidebar-card {
            background: rgba(30, 41, 59, 0.4);
            border: 1px solid var(--border-main);
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            transition: all 0.3s ease;
        }
        .sidebar-card:hover {
            border-color: var(--accent-primary);
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }

        /* 4. PREMIUM CHAT INTERFACE */
        .stChatMessage {
            background: var(--bg-glass) !important;
            border: 1px solid var(--border-main) !important;
            border-radius: 24px !important;
            padding: 1.5rem !important;
            margin-bottom: 2rem !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4) !important;
            backdrop-filter: blur(10px) !important;
            animation: fadeIn 0.5s ease-out;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* 5. MODERN INPUT AREA */
        div[data-testid="stChatInput"] {
            background: var(--bg-card) !important;
            border: 1px solid var(--border-main) !important;
            border-radius: 20px !important;
            padding: 10px !important;
            box-shadow: 0 0 40px rgba(0,0,0,0.5) !important;
            transition: all 0.3s ease;
        }
        
        div[data-testid="stChatInput"]:focus-within {
            border-color: var(--accent-primary) !important;
            box-shadow: 0 0 20px var(--glow-blue) !important;
        }

        /* 6. TYPOGRAPHY & HEADERS */
        .main-header {
            font-family: 'Space Grotesk', sans-serif !important;
            background: linear-gradient(135deg, #F8FAFC 0%, #4F46E5 50%, #8B5CF6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 4rem;
            font-weight: 800;
            text-align: center;
            letter-spacing: -3px;
            margin-bottom: 3rem;
            filter: drop-shadow(0 0 10px rgba(79, 70, 229, 0.2));
        }

        /* 7. CUSTOM SOURCE CARD */
        .source-container {
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid var(--border-main);
            border-radius: 18px;
            padding: 1.2rem;
            margin-top: 1rem;
            border-left: 4px solid var(--accent-primary);
            transition: transform 0.2s ease;
        }
        .source-container:hover {
            transform: scale(1.01);
            border-color: var(--accent-secondary);
        }

        /* 8. BUTTON STYLING */
        .stButton > button {
            background: linear-gradient(90deg, var(--accent-primary), var(--accent-secondary)) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            padding: 0.6rem 1.2rem !important;
            transition: all 0.3s ease !important;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-size: 0.8rem !important;
        }
        .stButton > button:hover {
            opacity: 0.9 !important;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px var(--glow-blue) !important;
        }

        </style>
    """, unsafe_allow_html=True)

def render_source_card(filename: str, page: int, snippet: str):
    """Render a premium, Perplexity-style research source card."""
    st.markdown(f"""
        <div class="source-container">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="color: var(--accent-primary); font-weight: 800; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px;">
                    ◈ DOCUMENT: {filename.upper()}
                </span>
                <span style="background: rgba(79, 70, 229, 0.15); color: #818CF8; padding: 4px 10px; border-radius: 8px; font-size: 0.7rem; font-weight: 700;">
                    PAGE {page}
                </span>
            </div>
            <div style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.7; font-style: italic;">
                "{snippet[:400]}..."
            </div>
            <div style="margin-top: 12px; display: flex; align-items: center; gap: 8px;">
                <div style="width: 6px; height: 6px; background: #22C55E; border-radius: 50%;"></div>
                <span style="color: #475569; font-size: 0.65rem; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">Verified Research Node</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
