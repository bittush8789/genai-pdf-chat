# Translation dictionary for multilingual support
# Easy to extend with Spanish, French, etc.

TRANSLATIONS = {
    "en": {
        "app_title": "ARISTOTLE PRO",
        "app_subtitle": "Neural Research AI",
        "intelligence": "Intelligence",
        "neural_engine": "Neural Engine",
        "knowledge_base": "Knowledge Base",
        "upload_assets": "Upload Research Assets",
        "sync_index": "◈ SYNCHRONIZE INDEX",
        "system": "System",
        "reset_memory": "↺ RESET CORE MEMORY",
        "about_dev": "👤 About Developer",
        "sys_status": "SYSTEM STATUS: OPERATIONAL",
        "ask_placeholder": "Ask anything...",
        "thinking": "Neural Engine Processing...",
        "no_index_warning": "No assets detected for synchronization.",
        "index_success": "Neural Index Synced",
        "index_fail": "Index failure: No extractable data found.",
        "clear_chat": "Chat memory cleared.",
        "dev_role": "AI & LLMOps Engineer",
        "dev_bio": "Passionate AI Engineer focused on building scalable GenAI, RAG, and LLMOps systems using LangChain, Groq, and Cloud-Native tech.",
        "source_ref": "DOCUMENT RETRIEVAL",
        "page": "PAGE",
        "citation": "CITATION",
        "not_found": "I could not find this information in the uploaded PDF documents.",
        "lang_name": "English 🇺🇸"
    },
    "hi": {
        "app_title": "अरस्तू प्रो",
        "app_subtitle": "न्यूरल रिसर्च एआई",
        "intelligence": "इंटेलिजेंस",
        "neural_engine": "न्यूरल इंजन",
        "knowledge_base": "नॉलेज बेस",
        "upload_assets": "रिसर्च एसेट्स अपलोड करें",
        "sync_index": "◈ इंडेक्स सिंक्रोनाइज़ करें",
        "system": "सिस्टम",
        "reset_memory": "↺ कोर मेमोरी रीसेट करें",
        "about_dev": "👤 डेवलपर के बारे में",
        "sys_status": "सिस्टम स्थिति: परिचालन",
        "ask_placeholder": "कुछ भी पूछें...",
        "thinking": "न्यूरल इंजन प्रोसेसिंग...",
        "no_index_warning": "सिंक्रोनाइज़ेशन के लिए कोई फ़ाइल नहीं मिली।",
        "index_success": "न्यूरल इंडेक्स सिंक हो गया",
        "index_fail": "इंडेक्स विफलता: कोई डेटा नहीं मिला।",
        "clear_chat": "चैट मेमोरी साफ़ कर दी गई।",
        "dev_role": "AI और LLMOps इंजीनियर",
        "dev_bio": "स्केलेबल GenAI, RAG और LLMOps सिस्टम बनाने पर केंद्रित भावुक AI इंजीनियर।",
        "source_ref": "दस्तावेज़ पुनर्प्राप्ति",
        "page": "पेज",
        "citation": "प्रशस्ति पत्र",
        "not_found": "मुझे अपलोड किए गए पीडीएफ दस्तावेजों में यह जानकारी नहीं मिली।",
        "lang_name": "हिंदी 🇮🇳"
    }
}

def get_text(key, lang="en"):
    """Get translated text for a given key and language."""
    return TRANSLATIONS.get(lang, TRANSLATIONS["en"]).get(key, TRANSLATIONS["en"][key])
