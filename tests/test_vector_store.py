import shutil
from pathlib import Path

from app.rag.vector_store import build_vector_store


def test_build_vector_store():
    test_db_path = Path("test_chroma_db")

    if test_db_path.exists():
        shutil.rmtree(test_db_path)

    vector_store, split_docs = build_vector_store(
        persist_directory=str(test_db_path),
        collection_name="test_job_description_collection",
    )

    assert vector_store is not None
    assert len(split_docs) > 0

    print("\nNumber of chunks created:", len(split_docs))
    print("\nFirst chunk preview:\n")
    print(split_docs[0].page_content[:700])