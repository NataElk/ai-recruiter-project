from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from app.utils.config import OPENAI_API_KEY


def get_retriever(
    persist_directory: str = "chroma_db",
    collection_name: str = "job_description_collection",
    k: int = 3,
):
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=OPENAI_API_KEY,
    )

    vector_store = Chroma(
        persist_directory=persist_directory,
        collection_name=collection_name,
        embedding_function=embeddings,
    )

    retriever = vector_store.as_retriever(search_kwargs={"k": k})
    return retriever