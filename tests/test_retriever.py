import shutil
from pathlib import Path

from app.rag.vector_store import build_vector_store
from app.rag.retriever import get_retriever


def test_retriever():
    test_db_path = Path("test_chroma_db")

    if test_db_path.exists():
        shutil.rmtree(test_db_path)

    build_vector_store(
        persist_directory=str(test_db_path),
        collection_name="test_job_description_collection",
    )

    retriever = get_retriever(
        persist_directory=str(test_db_path),
        collection_name="test_job_description_collection",
        k=3,
    )

    question = "What are the main responsibilities of this role?"
    docs = retriever.invoke(question)

    assert docs is not None
    assert len(docs) > 0

    print("\nQuestion:", question)
    print("\nNumber of retrieved docs:", len(docs))

    for i, doc in enumerate(docs, start=1):
        print(f"\n--- Retrieved doc #{i} ---")
        print(doc.page_content[:700])