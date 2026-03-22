from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from app.rag.load_documents import load_job_documents
from app.utils.config import OPENAI_API_KEY


def build_vector_store(
    persist_directory: str = "chroma_db",
    collection_name: str = "job_description_collection",
):
    """
    Load the PDF, split it into chunks, embed the chunks,
    and store them in Chroma.
    Returns the vector store and the split documents.
    """

    documents = load_job_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )

    split_docs = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=OPENAI_API_KEY,
    )

    vector_store = Chroma.from_documents(
        documents=split_docs,
        embedding=embeddings,
        persist_directory=persist_directory,
        collection_name=collection_name,
    )

    return vector_store, split_docs