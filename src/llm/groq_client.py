from langchain_groq import ChatGroq
from src.config.settings import settings
from src.utils.logger import get_logger

logger = get_logger(__name__)

def get_llm(model_name: str = None) -> ChatGroq:
    """
    Initialize the Groq Chat Model.
    """
    model = model_name or settings.DEFAULT_MODEL
    
    if not settings.GROQ_API_KEY:
        logger.error("GROQ_API_KEY is not set.")
        raise ValueError("GROQ_API_KEY is required to initialize the LLM.")
        
    try:
        logger.info(f"Initializing Groq LLM: {model}")
        llm = ChatGroq(
            temperature=0.0, # Low temperature for more grounded answers
            groq_api_key=settings.GROQ_API_KEY,
            model_name=model,
            streaming=True
        )
        return llm
    except Exception as e:
        logger.error(f"Failed to initialize Groq LLM: {str(e)}")
        raise e
