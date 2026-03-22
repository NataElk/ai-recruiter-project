from app.rag.vector_store import build_vector_store


def test_build_vector_store():
    vector_store, split_docs = build_vector_store(
        persist_directory="chroma_db",
        collection_name="job_description_collection",
    )

    count = vector_store._collection.count()

    print(f"\nSplit docs: {len(split_docs)}")
    print(f"Stored chunks in Chroma: {count}")

    assert len(split_docs) > 0
    assert count > 0