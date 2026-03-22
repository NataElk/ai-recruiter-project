from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from app.utils.config import OPENAI_API_KEY


def test_chroma_contents():
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=OPENAI_API_KEY,
    )

    vector_store = Chroma(
        persist_directory="chroma_db",
        collection_name="job_description_collection",
        embedding_function=embeddings,
    )

    collection = vector_store._collection
    count = collection.count()

    print("\nDocument count in collection:", count)

    assert count > 0