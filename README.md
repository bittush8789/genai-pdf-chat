# 💠 Aristotle Pro | Advanced Multilingual AI Research Assistant

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

**Aristotle Pro** is a production-grade, enterprise-ready AI Research Assistant designed to transform complex PDF documents into actionable intelligence. Built with an "Aether" premium dark interface, it leverages Advanced RAG (Retrieval-Augmented Generation) with strict anti-hallucination protocols.

---

## 📸 Platform Preview

<p align="center">
  <img src="../apps-photo/image.png" width="800" alt="Aristotle Pro UI Preview">
</p>

*The Aristotle Pro interface featuring the Aether V2 Design System, centered chat area, and premium research sidebar.*

---

## 🚀 Key Features

- **🎯 Ultra-Strict RAG Architecture**: Zero-hallucination logic ensures answers are derived exclusively from uploaded documents.
- **🌍 Bilingual Intelligence**: Seamlessly switch between professional English and academic Hindi research modes.
- **🔍 Source Transparency**: Perplexity-style citations including PDF filenames, page numbers, and italicized semantic snippets.
- **💠 Aether Pro UI/UX**: A startup-grade, glassmorphism-inspired dark theme with centered content layouts and smooth animations.
- **⚡ Neural Engine Support**: Compatible with state-of-the-art LLMs (Llama 3.3, Groq, etc.) via a persistent vector storage layer.
- **🛡️ Hardened Security**: Production-ready error handling that suppresses technical stack traces and implementation leaks.

---

## 🛠️ Technology Stack

- **Core**: Python 3.10+
- **Frontend**: Streamlit (Hardened Stealth Mode)
- **LLM Orchestration**: LangChain, LangGraph
- **Vector Database**: FAISS (High-Performance Semantic Indexing)
- **Inference**: Groq (Llama-3.1/3.3 Series)
- **Document Processing**: PyPDF, PDFPlumber, Pydantic
- **Styling**: Vanilla CSS, Glassmorphism Design System

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/aristotle-pro.git
cd aristotle-pro
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🏗️ Project Architecture

```text
ai-pdf-chatbot/
├── app.py                # Application Entry Point
├── src/
│   ├── chains/           # RAG Orchestration Logic
│   ├── ui/               # Aether Pro Design Components
│   ├── vectorstore/      # FAISS Index Management
│   ├── prompts/          # Anti-Hallucination Prompt Engineering
│   ├── memory/           # Persistent Chat History
│   └── utils/            # Multilingual Translation & Logging
└── requirements.txt      # Dependency Manifest
```

---

## 👤 Developer

**Bittu Sharma**  
*AI Research Lead & Engineer*  
Dedicated to building the future of Document Intelligence.

---

<p align="center">
  Built with 💠 by the Aristotle Pro Team
</p>
