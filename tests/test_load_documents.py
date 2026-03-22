from app.rag.load_documents import load_job_documents


def test_load_job_documents():
    documents = load_job_documents()

    assert documents is not None
    assert len(documents) > 0

    print("\nNumber of loaded documents:", len(documents))
    print("\nFirst document preview:\n")
    print(documents[0].page_content[:1000])