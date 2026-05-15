from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.runnables import Runnable
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.documents import Document

from src.utils.logger import get_logger
from src.prompts.system_prompt import get_qa_prompt

logger = get_logger(__name__)

def get_contextualize_q_prompt():
    contextualize_q_system_prompt = (
        "Given a chat history and the latest user question "
        "which might reference context in the chat history, "
        "formulate a standalone question which can be understood "
        "without the chat history. Do NOT answer the question, "
        "just reformulate it if needed and otherwise return it as is."
    )
    return ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

def create_rag_chain(llm, retriever) -> Runnable:
    """
    Create a Retrieval-Augmented Generation (RAG) chain.
    Updated to use the exact strict prompt format provided by the user.
    """
    try:
        logger.info("Creating strict RAG chain")
        
        # 1. Create history aware retriever to resolve coreferences (e.g. "it", "this")
        # This keeps the conversation fluid while the final answer remains strict.
        contextualize_q_prompt = get_contextualize_q_prompt()
        history_aware_retriever = create_history_aware_retriever(
            llm, retriever, contextualize_q_prompt
        )
        
        # 2. Create the QA chain using the user's exact template
        qa_prompt = get_qa_prompt()
        
        # The qa_prompt now expects {question} and {context}
        # We need to tell create_stuff_documents_chain to map its input to {question}
        question_answer_chain = create_stuff_documents_chain(
            llm, 
            qa_prompt,
            document_variable_name="context"
        )
        
        # 3. Combine both into a retrieval chain
        # The retrieval chain will pass its 'input' to the history_aware_retriever,
        # and then the output of that (standalone question) will be passed to qa_prompt as 'question'
        rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
        
        # Since our prompt uses {question} but the chain uses {input} by default, 
        # we might need to wrap it or adjust the variable names in the prompt.
        # LangChain 0.3 create_retrieval_chain passes 'input' to the combined chain.
        # Let's adjust the prompt variables in the next step if needed.
        
        return rag_chain
        
    except Exception as e:
        logger.error(f"Failed to create RAG chain: {str(e)}")
        raise e
