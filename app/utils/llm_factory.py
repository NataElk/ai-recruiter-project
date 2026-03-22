from langchain_openai import ChatOpenAI
from .config import OPENAI_API_KEY


def get_llm():
    llm = ChatOpenAI(
        model="gpt-4o-2024-11-20",
        temperature=0,
        api_key=OPENAI_API_KEY
    )
    return llm